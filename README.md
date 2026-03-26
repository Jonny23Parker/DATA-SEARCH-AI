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

[img]


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


[img]



---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/Jonny23Parker/data-search-ai.git
cd data-search-ai

---




2. Crie e ative o ambiente virtual

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate




3. Instale as dependências

pip install -r requirements.txt
