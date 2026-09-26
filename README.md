# 💎 Agente Inteligente (Aurora)

## 📌 Sobre o Projeto

O **Mentor Financeiro (Aurora)** é um assistente virtual de educação financeira desenvolvido como protótipo para ajudar **iniciantes** a organizar suas finanças e dar os primeiros passos nos investimentos.

Diferente de assistentes tradicionais que oferecem apenas recomendações frias, a Aurora atua com **acolhimento, empatia e didática**, analisando o padrão de gastos do usuário, traduzindo jargões do mercado para linguagem simples, e propondo pequenas mudanças de hábito baseadas em dados reais.

---

## 🎯 Objetivo

Resolver o problema de milhões de brasileiros que têm dinheiro parado na poupança perdendo para a inflação, simplesmente porque têm medo de investir ou acham o mercado financeiro "complicado demais".

**Aurora não vende produtos — ela educa.**

---

## ✨ Funcionalidades

### 💬 Chat Inteligente
- Interface de chat em tempo real via **Streamlit**
- Respostas empáticas e didáticas em português brasileiro
- Análise de padrão de gastos usando dados reais do usuário
- Identificação de "ralos invisíveis" no orçamento mensal

### 📊 Análise Financeira Automática
- Carregamento de perfil de investidor (risco, renda, metas)
- Análise das últimas transações bancárias
- Cálculo de progresso em relação às metas financeiras
- Barra de progresso visual da reserva de emergência

### 🛡️ Segurança e Anti-Alucinação
- **Só recomenda produtos existentes** no catálogo (nunca inventa)
- Limitação de escopo rigorosa (não responde sobre programação, política, esportes, etc.)
- Avisos legais de simulação educativa
- Respostas estruturadas em JSON com nível de confiança

### 📈 Dados de Mercado em Tempo Real
- Taxas atualizadas: Selic (13,75%), CDI (13,65%), IPCA (4,44%)
- Dados do B3 e câmbio USD/BRL via `yfinance`
- Scraping de sites públicos para CDBs e Tesouro Direto
- 11 produtos disponíveis incluindo bancos digitais

### 🤖 IA Generativa Local
- Modelo **Ollama** rodando localmente (`qwen2.5:3b`)
- Sem necessidade de chave de API
- System Prompt personalizado com few-shot examples
- Respostas em formato JSON estruturado

### 📋 Interface Amigável
- Sidebar com resumo do perfil, transações e produtos
- Card de boas-vindas com métricas do usuário
- Destaques visuais (Educação, Segurança, Empatia)
- Logo, diagrama de arquitetura e mockup da interface

---

## 🏗️ Arquitetura do Sistema

```
[USUÁRIO]
    │
    ▼
[STREAMLIT] ◄── Interface Web (Frontend)
    │
    ▼
[SYSTEM PROMPT] ◄── Regras, Few-shot, Taxas de mercado
    │
    ▼
[OLLAMA / LLM] ◄── Processa prompt, gera resposta
    │
    ▼
[BASE DE DADOS] ◄── JSON + CSV (perfil, transações, produtos)
    │
    ▼
[RESPOSTA] ◄── Texto didático, empático, em PT-BR
```

**Fluxo:** Usuário pergunta → Streamlit monta o contexto → Ollama processa → Resposta didática é exibida

---

## 🧠 Persona — Aurora

| Atributo | Detalhe |
|----------|---------|
| **Nome** | Mentora Financeira (Aurora) |
| **Personality** | Educativa, acolhedora, paciente e encorajadora |
| **Tom** | Informal, acessível, empático |
| **Missão** | Traduzir o "economês" para linguagem do dia a dia |
| **Limitação** | Não julga gastos, não promete ganhos, não sai do escopo |
| **Exemplo de saudação** | "Olá! Que bom ver você por aqui focado no seu futuro financeiro." |
| **Exemplo de erro** | "Olha, essa informação foge um pouco do meu conhecimento atual." |

---

## 📦 Base de Conhecimento

### Dados Mockados (JSON + CSV)

| Arquivo | Conteúdo |
|---------|----------|
| `perfil_investidor.json` | João Silva, 32 anos, analista de sistemas, perfil moderado |
| `produtos_financeiros.json` | 11 produtos com taxa, risco, aporte mínimo |
| `transacoes.csv` | 10 transações de outubro/2025 |
| `historico_atendimento.csv` | 5 atendimentos passados |
| `dados_externos.json` | Dados de mercado atualizados |

### Produtos Disponíveis

Catálogo com **11 produtos de investimento** divididos em categorias:

| Categoria | Produtos |
|-----------|----------|
| **Renda Fixa** | Tesouro Selic, CDBs de liquidez diária, LCI/LCA, CDBs de bancos digitais |
| **Fundos** | Fundo Multimercado, Fundo de Ações |

Todos os produtos são verificados e listados no arquivo `data/produtos_financeiros.json`. Rentabilidades são calculadas automaticamente com base na taxa CDI do mercado.

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- [Ollama](https://ollama.com) instalado com modelo `qwen2.5:3b`
- Comandos: `ollama pull qwen2.5:3b`

### Instalação
```bash
# 1. Clone o repositório
git clone https://github.com/SEU-USUARIO/Projeto-Assistente-Financeiro.git
cd Projeto-Assistente-Financeiro

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure o ambiente
copy .env.example .env
# Edite .env se necessário

# 4. Execute o assistente
streamlit run src/app.py
```

Acesse: **http://localhost:8501**

---

## 📚 Documentação Completa

| Documento | Conteúdo |
|-----------|----------|
| [Persona e Arquitetura](./docs/01-documentacao-agente.md) | Persona, arquitetura, limitações, anti-alucinação |
| [Base de Conhecimento](./docs/02-base-conhecimento.md) | Estratégia de integração de dados, exemplos de contexto |
| [Prompts e Exemplos](./docs/03-prompts.md) | System Prompt, few-shot examples, edge cases |
| [Métricas e Avaliação](./docs/04-metricas.md) | Critérios de qualidade, cenários de teste |
| [Pitch de Apresentação](./docs/05-pitch.md) | Roteiro de 3 minutos para apresentação |

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|-----------|-----|
| **Streamlit** | Interface web responsiva |
| **Ollama** | LLM local (qwen2.5:3b) — sem necessidade de API |
| **Python** | Linguagem principal |
| **pandas** | Manipulação de CSV e dados |
| **requests / beautifulsoup4** | Scraping de sites públicos |
| **yfinance** | Dados de mercado (B3, câmbio) em tempo real |
| **python-dotenv** | Variáveis de ambiente |
| **PIL (Pillow)** | Geração de logo e mockups |
| **matplotlib** | Diagramas e gráficos |

---

## 📁 Estrutura do Repositório

```
📁 PROJETO ASSISTENTE VIRTUAL/
│
├── 📄 README.md                      # Este arquivo
├── 📄 requirements.txt               # Dependências do projeto
├── 📄 .gitignore                     # Arquivos ignorados pelo Git
├── 📄 .env.example                   # Template de variáveis de ambiente
├── 📄 setup_github.sh                # Script de inicialização git
│
├── 📁 assets/                        # Recursos visuais
│   ├── img/
│   │   ├── logo.png                  # Logo do Aurora
│   │   ├── arquitetura.png           # Diagrama de arquitetura
│   │   ├── produtos.png              # Gráfico comparativo de produtos
│   │   └── screenshot.png            # Mockup da interface
│   ├── README.md                     # Documentação dos assets
│   └── RoteiroLab.md                 # Script de vídeos do desafio
│
├── 📁 data/                          # Base de Conhecimento
│   ├── perfil_investidor.json        # Perfil do cliente (João Silva)
│   ├── produtos_financeiros.json     # Catálogo de 11 produtos
│   ├── dados_externos.json           # Taxas de mercado atualizadas
│   ├── transacoes.csv                # Extrato bancário
│   └── historico_atendimento.csv     # Histórico de atendimentos
│
├── 📁 docs/                          # Documentação detalhada
│   ├── 01-documentacao-agente.md     # Persona e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # System Prompt e exemplos
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Pitch de apresentação
│
├── 📁 src/                           # Código-fonte
│   ├── app.py                        # Aplicação principal (Streamlit)
│   └── dados_externos.py             # Módulo de dados de mercado
│
├── 📁 examples/                      # Exemplos e referências
│   └── README.md
│
└── 📄 .gitignore
```

---

## 🔒 Segurança

| Estratégia | Detalhe |
|-----------|---------|
| **Anti-alucinação** | Só recomenda produtos do JSON — nunca inventa |
| **Escopo estrito** | Bloqueia perguntas sobre programação, política, esportes, etc. |
| **Sanitização de input** | Regex bloqueia padrões suspeitos (SQL, prompt injection) |
| **Cooldown** | Limite de 2 segundos entre mensagens |
| **Limite de histórico** | Máximo de 20 mensagens para evitar estouro de contexto |
| **Aviso legal** | Toda resposta é simulação educativa, não recomendação oficial |

---

## 📝 Dependências

Ver `requirements.txt`:
```
streamlit
ollama
pandas
python-dotenv
requests
beautifulsoup4
yfinance
```

---

## 🧪 Testes

O projeto inclui cenários de teste documentados em `docs/04-metricas.md`:

1. **Explicação de jargão** — "O que é CDI?"
2. **Gatilho de culpa financeira** — "Gastei demais, sou um desastre"
3. **Fora do escopo com pressão** — "Compra essa cripto para mim"
4. **Recomendação agressiva** — "Me indica uma ação para ficar rico rápido"

---

## 🎤 Pitch de 3 Minutos

Ver `docs/05-pitch.md` para o roteiro completo de apresentação do projeto.

---

## 🤝 Contribuindo

1. Abra uma issue descrevendo a melhoria
2. Crie uma branch para sua feature
3. Faça commit com mensagem descritiva
4. Abra um Pull Request

---

## 📄 Licença

Este projeto é um protótipo educacional desenvolvido como parte de um desafio de IA Generativa.

---

## 📄 Agradecimentos

- **DIO** pelo desafio que motivou este projeto

