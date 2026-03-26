import sys
import pandas as pd
from pathlib import Path

sys.path.append('src')
from database.vector_db import VectorDatabase

print("=" * 60)
print("🚀 DATA-SEARCH-AI - Carregando críticas do IMDB")
print("=" * 60)

# Conectar à coleção de filmes
movies_db = VectorDatabase(collection_name="movies_imdb")

# Verificar se já existem documentos
info = movies_db.get_collection_info()
existing_count = info['count']

if existing_count > 0:
    print(f"\n✅ Coleção 'movies_imdb' já possui {existing_count} documentos!")
    print("   Pulando carga...")
    print("\n📊 Status atual:")
    print(f"   Nome: {info['name']}")
    print(f"   Total de documentos: {info['count']}")
    
    # Testar busca rápida
    print("\n🔍 Testando busca por 'action movie':")
    results = movies_db.search("action movie", n_results=3)
    if results['documents'] and results['documents'][0]:
        print("   Resultados encontrados:")
        for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
            print(f"   📄 {meta.get('sentiment', 'N/A')}: {doc[:120]}...")
    else:
        print("   ⚠️ Nenhum resultado encontrado")
    
    print("\n✅ Tudo pronto! Pode iniciar o Streamlit: streamlit run app/main.py")
    sys.exit(0)

print("\n📦 Coleção vazia. Iniciando carga dos dados...")
print("   ⏱️  Isso pode levar de 10 a 20 minutos para 50.000 críticas...")

# Carregar o CSV
data_folder = Path("data")
csv_file = data_folder / "IMDB Dataset.csv"

if not csv_file.exists():
    print(f"\n❌ Arquivo não encontrado: {csv_file}")
    print("   Certifique-se que o arquivo 'IMDB Dataset.csv' está na pasta 'data/'")
    sys.exit(1)

print(f"\n📁 Lendo arquivo: {csv_file.name}")
df = pd.read_csv(csv_file, encoding='utf-8')
total_criticas = len(df)
print(f"   ✅ {total_criticas} críticas encontradas")
print(f"   🔧 Processando todas as críticas...")

all_chunks = []
sentiment_counts = {'positive': 0, 'negative': 0}

for idx, row in df.iterrows():
    review = row['review']
    sentiment = row['sentiment']
    
    # Contar sentimentos
    sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1
    
    # Limpar texto (remover tags HTML)
    review = review.replace('<br /><br />', ' ').replace('<br />', ' ')
    
    # Criar um único chunk por crítica
    chunk_id = f"imdb_{idx}"
    
    all_chunks.append({
        'id': chunk_id,
        'text': review,
        'metadata': {
            'filename': 'IMDB Dataset.csv',
            'source': 'imdb',
            'sentiment': sentiment,
            'review_id': idx,
            'type': 'movie_review'
        }
    })
    
    # Progresso a cada 5000 críticas
    if (idx + 1) % 5000 == 0:
        percent = (idx + 1) / total_criticas * 100
        print(f"   📄 Processadas {idx + 1}/{total_criticas} críticas ({percent:.1f}%)")

print(f"\n📊 Estatísticas do dataset:")
print(f"   ✅ Críticas positivas: {sentiment_counts['positive']}")
print(f"   ❌ Críticas negativas: {sentiment_counts['negative']}")
print(f"   📦 Total de chunks gerados: {len(all_chunks)}")

# Carregar em lotes
if all_chunks:
    ids = [c['id'] for c in all_chunks]
    docs = [c['text'] for c in all_chunks]
    metas = [c['metadata'] for c in all_chunks]
    
    print(f"\n💾 Carregando {len(all_chunks)} chunks no ChromaDB...")
    print("   ⏱️  Esta é a parte mais demorada. Aguarde...")
    
    # Carregar em lotes de 1000 para melhor performance
    movies_db.add_documents(ids, docs, metas, batch_size=1000)
    
    print("\n" + "=" * 60)
    print("✅ CRIAÇÃO DA BASE CONCLUÍDA COM SUCESSO!")
    print("=" * 60)
    
    # Verificar resultado final
    info = movies_db.get_collection_info()
    print(f"\n📊 Status final da coleção 'movies_imdb':")
    print(f"   Nome: {info['name']}")
    print(f"   Total de documentos: {info['count']}")
    print(f"   Metadados: {info['metadata']}")
    
    # Testar busca com diferentes termos
    print("\n🔍 Testando buscas na coleção:")
    
    test_queries = [
        ("action movie", "Busca por 'action movie'"),
        ("good film", "Busca por 'good film'"),
        ("bad acting", "Busca por 'bad acting'"),
        ("comedy", "Busca por 'comedy'")
    ]
    
    for query, desc in test_queries:
        print(f"\n   {desc}:")
        results = movies_db.search(query, n_results=2)
        if results['documents'] and results['documents'][0]:
            for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
                print(f"      📄 {meta.get('sentiment', 'N/A')}: {doc[:100]}...")
        else:
            print("      ⚠️ Nenhum resultado encontrado")
    
    print("\n" + "=" * 60)
    print("🎉 TUDO PRONTO! Agora você pode iniciar a interface:")
    print("   streamlit run app/main.py")
    print("=" * 60)

else:
    print("❌ Nenhum chunk gerado. Verifique o arquivo CSV.")