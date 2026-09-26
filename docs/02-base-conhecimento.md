# Base de Conhecimento

## Dados Utilizados

A base de conhecimento foca em fornecer um contexto realista para a mentoria financeira. Usamos os seguintes arquivos da pasta `data/`:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Lembrar de dúvidas passadas e evolução do aprendizado do cliente |
| `perfil_investidor.json` | JSON | Adequar o tom da explicação ao nível de risco (ex: explicar por que renda fixa é importante para perfis conservadores) |
| `produtos_financeiros.json` | JSON | Ofertar apenas produtos reais e seguros, traduzindo as características técnicas de cada um para linguagem simples |
| `transacoes.csv` | CSV | Diagnosticar o padrão de despesas, encontrar "ralos de dinheiro" e sugerir economias práticas |

---

## Estratégia de Integração

### Como os dados são carregados?
Os dados em CSV (pandas DataFrame) e JSON (dicionários) são carregados na memória ao iniciar a aplicação Streamlit e convertidos em um formato de texto/resumo.

### Como os dados são usados no prompt?
Os dados são concatenados no System Prompt como "Contexto Atual do Usuário". Assim, o LLM já começa a conversa sabendo o saldo, o perfil de risco e os últimos gastos do usuário sem precisar perguntar.

---

## Exemplo de Contexto Montado

```text
Você está falando com o usuário.
Perfil de Investidor: Conservador

Resumo Financeiro:
- Renda: R$ 4.500
- Despesas recentes: Muitas transações em aplicativos de delivery.

Produtos Disponíveis na Plataforma:
- CDB Liquidez Diária (Rende 100% do CDI)
- Tesouro Selic

Histórico: O usuário perguntou recentemente o que é "CDI".
```
