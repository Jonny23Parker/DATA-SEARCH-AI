import streamlit as st
import sys
import os
from pathlib import Path

# Adicionar o diretório raiz ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rag.rag_engine import RAGEngine
from src.database.vector_db import VectorDatabase

# Configuração da página
st.set_page_config(
    page_title="DATA-SEARCH-AI",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("🔍 DATA-SEARCH-AI")
st.subheader("Sistema de Busca Inteligente com RAG (Retrieval-Augmented Generation)")

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)
    st.markdown("## ⚙️ Configurações")
    
    # Seleção da coleção
    collection_option = st.selectbox(
        "📚 Escolha a base de conhecimento:",
        ["📘 Documentos Técnicos (IA e RAG)", "🎬 Críticas de Filmes (IMDB)"],
        help="Selecione qual base de dados deseja consultar"
    )
    
    # Mapear opção para nome da coleção
    collection_map = {
        "📘 Documentos Técnicos (IA e RAG)": "technical_docs",
        "🎬 Críticas de Filmes (IMDB)": "movies_imdb"
    }
    collection_name = collection_map[collection_option]
    
    # Configurações avançadas
    with st.expander("🔧 Configurações Avançadas"):
        top_k = st.slider(
            "Número de documentos a recuperar (Top K):",
            min_value=1,
            max_value=20,
            value=5,
            help="Quantos documentos serão buscados para gerar a resposta"
        )
        
        temperature = st.slider(
            "Temperatura da IA (criatividade):",
            min_value=0.0,
            max_value=1.0,
            value=0.3,
            step=0.1,
            help="Valores mais baixos = respostas mais precisas; mais altas = mais criativas"
        )
    
    st.markdown("---")
    st.markdown("### 📊 Status do Sistema")
    
    # Verificar status da coleção
    try:
        tech_db = VectorDatabase(collection_name=collection_name)
        info = tech_db.get_collection_info()
        st.success(f"✅ Conectado à coleção: **{collection_name}**")
        st.info(f"📄 Documentos disponíveis: **{info['count']}**")
    except Exception as e:
        st.error(f"❌ Erro ao conectar: {e}")

# Área principal
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 💬 Faça sua pergunta")
    
    # Inicializar histórico de conversa
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Inicializar o RAG Engine uma única vez (cache)
    @st.cache_resource
    def get_rag_engine(collection, k):
        return RAGEngine(collection_name=collection, top_k=k)
    
    # Exibir histórico de mensagens
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Input do usuário
    if prompt := st.chat_input("Digite sua pergunta sobre IA, RAG ou filmes..."):
        # Adicionar mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Gerar resposta
        with st.chat_message("assistant"):
            with st.spinner("🔍 Buscando documentos e gerando resposta..."):
                try:
                    # Obter o RAG Engine (cacheado)
                    rag = get_rag_engine(collection_name, top_k)
                    
                    # Obter resposta
                    result = rag.query(prompt)
                    response = result["answer"]
                    sources = result["sources"]
                    
                    # Exibir resposta
                    st.markdown(response)
                    
                    # Exibir fontes
                    if sources:
                        st.markdown("---")
                        st.markdown("**📚 Fontes utilizadas:**")
                        for source in set(sources):
                            st.markdown(f"- `{source}`")
                    
                    # Adicionar ao histórico
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": f"{response}\n\n---\n📚 **Fontes:** {', '.join(set(sources))}"
                    })
                    
                except Exception as e:
                    error_msg = f"❌ Erro ao gerar resposta: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})

with col2:
    st.markdown("### ℹ️ Sobre o Projeto")
    st.markdown("""
    **DATA-SEARCH-AI** é um sistema de busca inteligente que combina:
    
    - 🔍 **ChromaDB** - Banco vetorial para busca semântica
    - 🧠 **Groq (Llama 3)** - Modelo de linguagem para geração de respostas
    - 📚 **RAG** - Retrieval-Augmented Generation
    - 🌐 **Tradução automática** - Perguntas em português são traduzidas para inglês
    
    **Bases de conhecimento disponíveis:**
    
    📘 **Documentos Técnicos**
    - Inteligência Artificial
    - RAG (Retrieval-Augmented Generation)
    
    🎬 **Críticas de Filmes (IMDB)**
    - 50.000 críticas
    - Sentimentos positivo/negativo
    - **Nota:** As críticas estão em inglês, mas você pode perguntar em português que o sistema traduz automaticamente!
    
    ---
    
    **💡 Exemplos de perguntas:**
    
    *Sobre IA:*
    - O que é Inteligência Artificial?
    - Como funciona o RAG?
    - Quais as vantagens do RAG?
    
    *Sobre filmes:*
    - O que as pessoas dizem sobre filmes de ação?
    - Quais as melhores críticas positivas?
    - Me fale sobre filmes de suspense
    - What do people say about action movies?
    """)
    
    st.markdown("---")
    st.markdown("### 🛠️ Stack Tecnológica")
    st.markdown("""
    - Python 🐍
    - ChromaDB
    - Groq API (Llama 3)
    - Streamlit
    - Pandas
    - Deep Translator
    """)

# Footer
st.markdown("---")
st.markdown(
    "<center>🚀 Desenvolvido com ❤️ usando RAG + ChromaDB + Groq</center>",
    unsafe_allow_html=True
)
