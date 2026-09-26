import streamlit as st
import pandas as pd
import json
import os
import re
import time
import ollama
from dotenv import load_dotenv
import sys
sys.path.insert(0, os.path.dirname(__file__))
from dados_externos import atualizar_dados, salvar_dados_atualizados
from dados_externos import buscar_dados_mercado

# Load environment variables
load_dotenv()

# --- Configurações da Página ---
st.set_page_config(
    page_title="Aurora | Sua Mentora Financeira",
    page_icon="💎",
    layout="centered"
)

# --- Buscar dados de mercado ---
mercado_dados = buscar_dados_mercado()

# --- Configurações da Página ---
st.set_page_config(
    page_title="Aurora | Sua Mentora Financeira",
    page_icon="💎",
    layout="centered"
)

# --- Configurações ---
OLLAMA_MODEL = st.sidebar.text_input("Modelo do Ollama:", value="qwen2.5:3b")
st.sidebar.markdown("*Certifique-se de que o modelo já foi baixado (`ollama pull qwen2.5:3b`)*")

MAX_HISTORY_MESSAGES = 20
MAX_INPUT_CHARS = 500
MIN_INPUT_CHARS = 3
COOLDOWN_SECONDS = 2

PADRAO_INGRESSO = re.compile(
    r'(system\s*:|ignore\s+previous|dockerfile|sudo|cat\s+/etc/passwd|rm\s+-rf|SELECT\s+|INSERT\s+|DROP\s+|EXEC\s+|<script|javascript:|<iframe)',
    re.IGNORECASE
)

# --- Carregamento de Dados da Base de Conhecimento ---
@st.cache_data
def load_data():
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    with open(os.path.join(data_dir, "perfil_investidor.json"), "r", encoding="utf-8") as f:
        perfil = json.load(f)
    with open(os.path.join(data_dir, "produtos_financeiros.json"), "r", encoding="utf-8") as f:
        produtos = json.load(f)
    with open(os.path.join(data_dir, "dados_externos.json"), "r", encoding="utf-8") as f:
        externos = json.load(f)
    transacoes = pd.read_csv(os.path.join(data_dir, "transacoes.csv"))
    historico = pd.read_csv(os.path.join(data_dir, "historico_atendimento.csv"))
    return perfil, produtos, externos, transacoes, historico

try:
    perfil, produtos, externos, transacoes, historico = load_data()
except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    st.stop()

# --- Buscar dados de mercado ---
mercado_dados = buscar_dados_mercado()

# --- TELA INICIAL ---
st.markdown("""
<style>
    .hero-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2D3436;
        text-align: center;
        margin-bottom: 0.25rem;
    }
    .hero-subtitle {
        font-size: 1.1rem;
        color: #636E72;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .divider {
        height: 3px;
        background: linear-gradient(to right, #00B894, #00CEC9, #0984E3);
        border-radius: 2px;
        margin: 1.5rem 0;
    }
</style>
<div class="hero-title">💎 Bem-vindo à Aurora</div>
<div class="hero-subtitle">Sua mentora financeira para uma jornada inteligente</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# --- Preparar o Contexto ---
transacoes_resumo = transacoes.tail(5).to_string(index=False)
produtos_resumo = "\n".join(
    f"- {p['nome']} | Risco: {p['risco']} | Rentabilidade: {p['rentabilidade_desc']} | Aporte mínimo: R$ {p['aporte_minimo']:,.2f} | {p['indicado_para']}"
    for p in produtos
)
perfil_resumo = json.dumps(perfil, indent=2, ensure_ascii=False)

# --- Few-Shot Examples ---
FEW_SHOT_TEXT = """
EXEMPLOS DE INTERAÇÃO:

Exemplo 1:
Usuário: "O que é CDI?"
Assistente: "Que ótima pergunta! O CDI significa Certificado de Depósito Interbancário. Imagine que é como a taxa de juros que os bancos cobram emprestado uns dos outros — é a referência básica de juros no Brasil. Quando um investimento rende 100% do CDI, significa que você está recebendo o mesmo que essa taxa."

Exemplo 2:
Usuário: "Gastei 500 em roupas e agora não tenho como pagar a fatura do cartão, me sinto um desastre."
Assistente: "Entendo perfeitamente! Não se culpe — todos passam por isso. O importante é que você reconheceu o padrão. Vamos trabalhar juntos: tente parcelar essa fatura para não sobrecarregar seu orçamento do mês. E para a próxima vez, que tal separar um valor mensal pequeno para gastos pessoais? Você está no caminho certo!"

Exemplo 3:
Usuário: "Me indica uma ação que valorize rápido"
Assistente: "Entendo a vontade de buscar retornos rápidos! Mas no mundo dos investimentos, a regra de ouro é a paciência. Produtos que prometem riqueza rápida geralmente têm riscos enormes de você perder tudo. Como seu perfil é de iniciante, o ideal é focarmos em montar sua reserva de emergência primeiro, com segurança. Vamos começar pelo básico seguro?"

Exemplo 4:
Usuário: "Qual time vai ganhar o campeonato hoje?"
Assistente: "Ah, de esportes eu não entendo muito! Meu forte mesmo é ajudar o seu dinheiro a ser um campeão no fim do mês. Quer dar uma olhadinha em como estão seus gastos dessa semana?"
"""

# --- System Prompt ---
SYSTEM_PROMPT = f"""
Você é a "Mentora Financeira" (também chamada de Aurora), uma assistente virtual empática, acolhedora e didática.
Sua missão é ajudar iniciantes a organizar as finanças e dar os primeiros passos nos investimentos.

DADOS DO USUÁRIO:
Perfil de Investidor: {perfil_resumo}
Últimas Transações Bancárias:
{transacoes_resumo}

TAXAS DE MERCADO ATUAIS (setembro 2026):
- Taxa Selic: {externos['taxa_selic']['valor']}% ao ano
- Taxa CDI: {externos['taxa_cdi']['valor']}% ao ano
- IPCA: 4,44% ao ano

PRODUTOS FINANCEIROS DISPONÍVEIS NA INSTITUIÇÃO:
{produtos_resumo}

REGRAS ESTritas:
1. NUNCA invente ou recomende produtos financeiros que não estejam listados acima.
2. Use as taxas de mercado fornecidas acima para calcular rentabilidades. NÃO invente números.
3. Explique os jargões usando analogias simples e amigáveis.
4. Seja sempre encorajador, não faça o usuário se sentir culpado por gastos.
5. Caso o usuário peça recomendações de alto risco, explique os riscos gentilmente e sugira o básico.
6. LIMITAÇÃO DE ESCOPO ABSOLUTA: Você está terminantemente proibido de responder a perguntas sobre programação, conhecimentos gerais, política, esportes, receitas culinárias ou qualquer assunto fora de finanças e economia básica. Se questionado sobre isso, negue educadamente afirmando seu escopo.
7. Não faça promessas de ganhos futuros irreais ou projeções garantidas de rentabilidade.
8. RESPONDA SEMPRE EM PORTUGUÊS DO BRASIL.
9. RESPONDA EM FORMATO JSON ESTRUTURADO com os campos: {{ "resposta": "texto da resposta", "topicos": ["tópico1", "tópico2"], "nivel_confianca": "alta|media|baixa" }}
10. NÃO inclua markdown, negritos ou formatação extra dentro do campo "resposta" — apenas texto plano.

EXEMPLOS DE INTERAÇÃO (few-shot):
{FEW_SHOT_TEXT}
"""

# --- Segurança: Sanitização de Input ---
def sanitizar_input(texto: str) -> str:
    texto = texto.strip()
    if len(texto) > MAX_INPUT_CHARS:
        texto = texto[:MAX_INPUT_CHARS]
    return texto

def validar_input(texto: str) -> tuple[bool, str]:
    if len(texto) < MIN_INPUT_CHARS:
        return False, f"Sua mensagem precisa ter pelo menos {MIN_INPUT_CHARS} caracteres."
    if PADRAO_INGRESSO.search(texto):
        return False, "⚠️ Parece que sua mensagem contém padrões suspeitos. Vamos focar nas suas finanças! 💰"
    return True, ""

# --- Gerenciamento de Estado do Chat ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! Eu sou a Aurora, sua Mentora Financeira Pessoal. 🌟\n\nEstou aqui para ajudar você a cuidar do seu dinheiro sem complicação, sem julgamentos e no seu próprio ritmo. Como posso te ajudar a dar um passo na sua jornada financeira hoje?"}
    ]

if "last_request_time" not in st.session_state:
    st.session_state.last_request_time = 0

# Limite o histórico de mensagens para evitar estouro de contexto
if len(st.session_state.messages) > MAX_HISTORY_MESSAGES:
    st.session_state.messages = st.session_state.messages[-MAX_HISTORY_MESSAGES:]

# Exibir histórico de mensagens (ignora o system prompt na UI)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# --- Caixa de Entrada de Texto ---
if prompt := st.chat_input("Pergunte algo sobre seus gastos ou investimentos..."):
    # Sanitizar e validar input
    prompt_sanitizado = sanitizar_input(prompt)
    valido, msg_erro = validar_input(prompt_sanitizado)

    if not valido:
        st.warning(msg_erro)
        st.stop()

    # Cooldown para evitar requisições excessivas
    tempo_atual = time.time()
    if tempo_atual - st.session_state.last_request_time < COOLDOWN_SECONDS:
        st.warning("Aguarde um momento antes de enviar outra mensagem.")
        st.stop()
    st.session_state.last_request_time = tempo_atual

    # Adicionar mensagem do usuário na tela e no estado
    st.session_state.messages.append({"role": "user", "content": prompt_sanitizado})
    with st.chat_message("user"):
        st.markdown(prompt_sanitizado)

    # Obter resposta do Ollama
    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        try:
            chat_history = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages

            response = ollama.chat(
                model=OLLAMA_MODEL,
                messages=chat_history,
                format="json"
            )

            raw_content = response['message']['content']

            # Tentar parsear JSON estruturado
            try:
                limpo = raw_content.strip()
                if limpo.startswith("```"):
                    limpo = limpo.split("```")[1].strip()
                if limpo.startswith("json"):
                    limpo = limpo[4:].strip()
                resposta_json = json.loads(limpo)
                conteudo_exibir = resposta_json.get("resposta", raw_content)
            except (json.JSONDecodeError, IndexError):
                try:
                    resposta_json = json.loads(raw_content)
                    conteudo_exibir = resposta_json.get("resposta", raw_content)
                except json.JSONDecodeError:
                    conteudo_exibir = raw_content

            message_placeholder.markdown(conteudo_exibir)

            # Adicionar resposta ao histórico
            st.session_state.messages.append({"role": "assistant", "content": conteudo_exibir})

        except Exception as e:
            st.error(f"Erro na comunicação com o Ollama (o serviço está rodando?): {e}")

# --- Sidebar: Resumo do Usuário ---
st.sidebar.title("👤 Perfil do Usuário")
st.sidebar.markdown(f"**Nome:** {perfil['nome']}")
st.sidebar.markdown(f"**Idade:** {perfil['idade']}")
st.sidebar.markdown(f"**Renda:** R$ {perfil['renda_mensal']:,.2f}")
st.sidebar.markdown(f"**Perfil:** {perfil['perfil_investidor']}")
st.sidebar.markdown(f"**Patrimônio:** R$ {perfil['patrimonio_total']:,.2f}")
st.sidebar.markdown(f"**Reserva Atual:** R$ {perfil['reserva_emergencia_atual']:,.2f}")
st.sidebar.markdown(f"**Meta:** {perfil['objetivo_principal']}")

st.sidebar.title("📊 Transações Recentes")
st.sidebar.dataframe(transacoes.tail(5), use_container_width=True)

st.sidebar.title("📋 Produtos Disponíveis")
for produto in produtos:
    st.sidebar.markdown(f"**{produto['nome']}** ({produto['categoria']})")
    st.sidebar.markdown(f"  - Risco: {produto['risco']} | Rentabilidade: {produto['rentabilidade_desc']}")
    st.sidebar.markdown(f"  - Aporte mínimo: R$ {produto['aporte_minimo']:,.2f}")
    st.sidebar.markdown("")

# --- Atualização de Dados Externos ---
st.sidebar.markdown("---")
st.sidebar.title("🔄 Atualizar Dados")
if st.sidebar.button("Buscar dados de sites públicos"):
    with st.spinner("Buscando dados..."):
        dados = atualizar_dados()
        salvar_dados_atualizados(dados)
        st.sidebar.success("Dados atualizados com sucesso!")
        mercado = dados.get("mercado", {})
        if mercado.get("bvsp_atual"):
            st.sidebar.info(f"🏦 B3 (BVSP): {mercado['bvsp_atual']:,.0f}")
            st.sidebar.info(f"📈 Variação: {mercado.get('bvap_variacao', 0):.2f}%")
        if mercado.get("usd_atual"):
            st.sidebar.info(f"💱 USD/BRL: {mercado['usd_atual']:.3f}")
        if dados.get("manual", {}).get("taxa_selic"):
            st.sidebar.info(f"📝 Selic manual: {dados['manual']['taxa_selic']}%")
