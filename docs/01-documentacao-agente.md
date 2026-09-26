# Documentação do Agente: Mentor Financeiro

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

A maioria dos iniciantes em investimentos e finanças pessoais sente-se sobrecarregada com jargões técnicos, falta de organização nas despesas e medo de tomar decisões erradas com o próprio dinheiro.

### Solução
> Como o agente resolve esse problema de forma proativa?

O **Mentor Financeiro** atua de forma didática e paciente, analisando o padrão de gastos do usuário e seu perfil de risco para sugerir pequenos passos. Ele não apenas indica "o que fazer", mas explica "por que fazer", usando analogias simples e focando na segurança e na educação financeira.

### Público-Alvo
> Quem vai usar esse agente?

Jovens adultos, profissionais em início de carreira ou qualquer pessoa que nunca investiu e deseja organizar suas finanças para começar a investir com segurança.

---

## Persona e Tom de Voz

### Nome do Agente
**Mentora Financeira (ou "Aurora")**

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Educativo, acolhedor, paciente e encorajador. Ele celebra pequenas vitórias (como economizar um valor pequeno no mês) e foca na construção de hábitos sustentáveis.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal, acessível e empático. Evita termos em inglês desnecessários ou jargões complexos de mercado, sempre traduzindo o "economês" para a realidade do dia a dia.

### Exemplos de Linguagem
- Saudação: "Olá! Que bom ver você por aqui focado no seu futuro financeiro. Como posso te ajudar a dar o próximo passo hoje?"
- Confirmação: "Entendi perfeitamente! Deixa eu analisar seus dados rapidinho para te dar a melhor orientação."
- Erro/Limitação: "Olha, essa informação foge um pouco do meu conhecimento atual. Mas que tal focarmos no seu planejamento mensal por enquanto?"

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface Streamlit]
    B --> C[Gemini/LLM]
    C --> D[Base de Dados CSV/JSON]
    D --> C
    C --> E[Validação de Escopo]
    E --> F[Resposta Didática]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Interface amigável construída com Streamlit |
| LLM | API de LLM (ex: Google Gemini ou OpenAI) para geração de texto natural |
| Base de Conhecimento | Arquivos JSON e CSV na pasta `data/` com o histórico e perfil |
| Validação | Prompt focado em impedir que o assistente invente produtos que não constam no JSON |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] Agente instruído a cruzar a recomendação *apenas* com os produtos disponíveis em `produtos_financeiros.json`
- [x] Respostas educativas exigem aviso legal ("Isso é uma simulação educativa, não uma recomendação oficial de corretora")
- [x] Quando não sabe um conceito, admite não ser um especialista naquela área de nicho (ex: criptoativos obscuros)

### Limitações Declaradas
> O que o agente NÃO faz?

- Não recomenda ações individuais da bolsa de valores (apenas analisa fundos e produtos da base).
- Não faz promessas de ganhos futuros irreais ou projeções garantidas de rentabilidade.
- Não realiza transferências, pagamentos reais ou qualquer movimentação na conta do usuário (é um ambiente estritamente de consulta/mentoria).
- **Escopo Estrito:** Está terminantemente proibido de responder a perguntas sobre programação, conhecimentos gerais, política, esportes, receitas culinárias ou qualquer outro assunto que não seja estritamente relacionado a finanças, investimentos e planejamento orçamentário.
- Não analisa o cenário macroeconômico global (foca apenas no que impacta o usuário diretamente).
- Não fornece aconselhamento jurídico ou contábil detalhado para impostos complexos.