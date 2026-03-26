# 🔍 DATA-SEARCH-AI

## Sistema de Busca Inteligente com RAG (Retrieval-Augmented Generation)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29+-red.svg)](https://streamlit.io/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-0.5+-green.svg)](https://www.trychroma.com/)
[![Groq](https://img.shields.io/badge/Groq-Llama%203.3-orange.svg)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Arquitetura](#arquitetura)
- [Funcionalidades](#funcionalidades)
- [Stack Tecnológica](#stack-tecnológica)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar](#como-executar)
- [Exemplos de Uso](#exemplos-de-uso)
- [Resultados](#resultados)
- [Próximos Passos](#próximos-passos)
- [Autor](#autor)
- [Licença](#licença)

---

## 🎯 Sobre o Projeto

**DATA-SEARCH-AI** é um sistema de busca inteligente que combina **Retrieval-Augmented Generation (RAG)** com banco vetorial e modelos de linguagem de última geração.

O sistema permite fazer perguntas em linguagem natural e obtém respostas precisas baseadas em documentos indexados, com citação automática das fontes utilizadas.

### 📊 Dataset Processado

| Dataset | Quantidade | Descrição |
|---------|------------|-----------|
| **IMDB Reviews** | 50.000 críticas | Críticas de filmes com sentimentos (positivo/negativo) |
| **Documentos Técnicos** | 2 documentos | Conteúdo sobre Inteligência Artificial e RAG |

---

## 🏗️ Arquitetura

## Interface do Sistema

![Interface do DATA-SEARCH-AI](https://github.com/Jonny23Parker/DATA-SEARCH-AI/blob/main/img/Arquitetura%20img.jpg)

---

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|----------------|-----------|
| 🔍 **Busca Semântica** | Encontra documentos relevantes usando similaridade vetorial |
| 🤖 **RAG (Retrieval-Augmented Generation)** | Combina busca com geração de respostas por IA |
| 🌐 **Tradução Automática** | Perguntas em português são traduzidas para inglês automaticamente |
| 📚 **Múltiplas Bases** | Documentos técnicos + 50.000 críticas de filmes IMDB |
| 🎨 **Interface Web** | Chat interativo com Streamlit |
| 📖 **Citação de Fontes** | Mostra quais documentos foram usados na resposta |
| ⚡ **Alta Performance** | Busca em <2 segundos |

---

## 🛠️ Stack Tecnológica

### Core
| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| Python | 3.10+ | Linguagem principal |
| ChromaDB | 0.5+ | Banco de dados vetorial |
| Groq API | - | Inferência de LLM (Llama 3.3 70B) |

### Interface e Visualização
| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| Streamlit | 1.29+ | Framework para interface web |
| Pandas | 2.2+ | Processamento de dados |

### Utilitários
| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| python-dotenv | 1.0+ | Gerenciamento de variáveis de ambiente |
| deep-translator | 1.11+ | Tradução automática |

---

## 📁 Estrutura do Projeto

## Interface do Sistema

![Interface do DATA-SEARCH-AI](https://github.com/Jonny23Parker/DATA-SEARCH-AI/blob/main/img/Estrutura%20img.jpg)

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash

git clone https://github.com/Jonny23Parker/data-search-ai.git
cd data-search-ai

```

## 2. Download manual
```bash

O download automático precisa de criar conta e autenticação de token no Kaggle, manualmente neste caso foi mais rapido:

Acesse: https://www.kaggle.com/datasets/waseemalastal/imdb-dataset

Baixe o arquivo IMDB Dataset.csv

Coloque na pasta data/ do projeto

```

## 3. Crie e ative o ambiente virtual

```bash

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

```

## 4. Instale as dependências
```bash

pip install -r requirements.txt

```

## 5. Configure as variáveis de ambiente
```bash

GROQ_API_KEY=sua_chave_aqui

🔑 Obtenha sua chave gratuitamente em: console.groq.com/keys

```

## 6. Carregue os dados no ChromaDB
```bash

python reload_imdb.py

⏱️ Atenção: Esta etapa pode levar de 10 a 20 minutos na primeira execução (processa 50.000 críticas).

```


## 7. Inicie a interface

```

streamlit run app/main.py

Acesse: http://localhost:8501

```


## ✅ Verificação rápida
Após iniciar, você deve ver:

* ✅ Conexão com ChromaDB estabelecida

* ✅ Mensagem "Motor RAG inicializado"

* ✅ Interface aberta no navegador



## 8. Iniciar via START.bat

Voce pode criar um arquivo de texto e inserir os comanddos abaixo, para ser executado diretemente da área de trabalho em sua maquina.
nasta criar o arquivo e renomear a extensão para nomeescolhido.bat

```
@echo off
cd /d "F:\Curriculos Jonatas\PORTFOLIO DADOS\data-search-ai"
call .\venv\Scripts\activate
streamlit run app/main.py
pause

```































