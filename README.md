# 💎 Mentor Financeiro - Agente Inteligente (Aurora)

## Contexto

Este projeto é um protótipo de assistente virtual focado em **educação financeira**, desenvolvido para iniciantes que desejam organizar suas finanças e dar os primeiros passos nos investimentos.

A **Aurora** utiliza IA Generativa (Ollama + LLM local) para analisar o comportamento do usuário, oferecer orientação empática e traduzir jargões financeiros para linguagem simples.

---

## Estrutura do Repositório

```text
📁 PROJETO ASSISTENTE VIRTUAL/
│
├── 📄 README.md                      # Este arquivo
├── 📄 requirements.txt               # Dependências do projeto
├── 📄 .gitignore                     # Arquivos ignorados pelo Git
├── 📄 .env.example                   # Template de variáveis de ambiente
│
├── 📁 data/                          # Base de Conhecimento
│   ├── perfil_investidor.json        # Perfil do cliente (João Silva)
│   ├── produtos_financeiros.json     # Catálogo de investimentos (11 produtos)
│   ├── dados_externos.json           # Taxas de mercado atualizadas
│   ├── transacoes.csv                # Extrato bancário
│   └── historico_atendimento.csv     # Histórico de atendimentos
│
├── 📁 docs/                          # Documentação detalhada
│   ├── 01-documentacao-agente.md     # Persona e arquitetura
│   ├── 02-base-conhecimento.md       # Uso dos dados
│   ├── 03-prompts.md                 # System Prompt e exemplos
│   ├── 04-metricas.md                # Como avaliar o assistente
│   └── 05-pitch.md                   # Roteiro de apresentação
│
├── 📁 src/                           # Código-fonte
│   ├── app.py                        # Aplicação principal (Streamlit)
│   └── dados_externos.py             # Módulo de scraping e dados de mercado
│
└── 📁 assets/                        # Recursos visuais
```

---

## Como Executar

### 1. Pré-requisitos
- Python 3.8+
- Ollama instalado e rodando (modelo `qwen2.5:3b`)

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Configurar ambiente
```bash
# Copiar o template de ambiente
copy .env.example .env
# Editar o arquivo .env se necessário
```

### 4. Rodar o Assistente
```bash
streamlit run src/app.py
```
Acesse `http://localhost:8501`.

---

## Tecnologias Utilizadas

| Tecnologia | Uso |
|-----------|-----|
| **Streamlit** | Interface web |
| **Ollama** | LLM local (qwen2.5:3b) |
| **Python** | Linguagem principal |
| **pandas** | Manipulação de dados |
| **requests / beautifulsoup4** | Scraping de sites públicos |
| **yfinance** | Dados de mercado (B3, câmbio) |
| **python-dotenv** | Variáveis de ambiente |

---

## Dados de Mercado (Setembro 2026)

| Indicador | Valor |
|-----------|-------|
| **Selic** | 13,75% a.a. |
| **CDI** | 13,65% a.a. |
| **IPCA** | 4,44% a.a. |
| **B3 (BVSP)** | ~183.477 |

### Produtos Disponíveis (11)
- Tesouro Selic
- CDB Liquidez Diária
- LCI/LCA
- Fundo Multimercado
- Fundo de Ações
- **CDB Nubank** (100% CDI)
- **CDB Banco Inter** (100% CDI)
- **CDB PicPay** (102% CDI)
- **CDB Banco C6** (118% CDI)
- **Mercado Pago Conta** (100% CDI)
- **Mercado Pago Cofrinhos** (120% CDI)

---

## Documentação Completa

- [Persona e Arquitetura](./docs/01-documentacao-agente.md)
- [Base de Conhecimento](./docs/02-base-conhecimento.md)
- [Prompts e Exemplos](./docs/03-prompts.md)
- [Métricas e Avaliação](./docs/04-metricas.md)
- [Pitch de Apresentação](./docs/05-pitch.md)

---

## Configuração para GitHub

### Se o Git já está instalado:
```bash
git init
git add .
git commit -m "feat: assistente financeiro com dados de setembro 2026"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
git push -u origin main
```

### Se o Git NÃO está instalado:
1. Baixe e instale o Git: https://git-scm.com/downloads
2. Reinicie o terminal/PowerShell
3. Execute os comandos acima
```
