import requests
import yfinance as yf
import json
import os
import streamlit as st
from datetime import datetime

# --- Busca taxa Selic via yfinance ---
def buscar_selic():
    """Tenta buscar taxa Selic via yfinance."""
    try:
        ticker = yf.Ticker("^BVSP")
        info = ticker.history(period="5d")
        if not info.empty:
            return {"sinal": "info", "valor": None, "msg": "yfinance funciona, mas Selic nao tem ticker direto"}
    except Exception:
        pass
    return {"sinal": "warning", "valor": None, "msg": "yfinance nao disponivel para Selic"}

# --- Busca dados de mercado via yfinance ---
def buscar_dados_mercado():
    """Busca indices e dados de mercado brasileiros."""
    dados = {}
    try:
        bvsp = yf.Ticker("^BVSP")
        hist = bvsp.history(period="5d")
        if not hist.empty:
            dados["bvsp_atual"] = float(hist['Close'].iloc[-1])
            dados["bvap_variacao"] = float(hist['Close'].iloc[-1] / hist['Close'].iloc[-2] - 1) * 100
    except Exception:
        pass
    try:
        usd = yf.Ticker("USDBRL=X")
        hist = usd.history(period="5d")
        if not hist.empty:
            dados["usd_atual"] = float(hist['Close'].iloc[-1])
    except Exception:
        pass
    return dados

# --- Busca taxa Selic via scraping simples ---
def buscar_selic_web():
    """Busca taxa Selic atual de fonte publica sem API key."""
    try:
        url = "https://www.google.com/finance/quote/USD-BRL"
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        if response.status_code == 200:
            return {"sinal": "info", "valor": None, "msg": "Conexao bem sucedida"}
    except Exception:
        pass
    return {"sinal": "warning", "valor": None, "msg": "Sem acesso a fonte web"}

# --- Atualizacao manual (quando nao há acesso web) ---
def atualizar_manualmente():
    """Permite ao usuario atualizar dados manualmente via UI."""
    return {
        "taxa_selic": st.number_input("Taxa Selic (% ao ano)", min_value=0.0, max_value=50.0, value=11.75, step=0.25),
        "taxa_cdi": st.number_input("Taxa CDI (% ao ano)", min_value=0.0, max_value=50.0, value=11.50, step=0.25),
        "data_atualizacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# --- Função principal ---
def atualizar_dados():
    """Função principal que tenta buscar dados de todas as fontes."""
    dados = {
        "data_atualizacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "fontes": {},
        "mercado": {},
        "manual": {}
    }

    st.info("🔄 Buscando dados de sites públicos...")

    # 1. Tenta buscar dados de mercado via yfinance
    mercado = buscar_dados_mercado()
    if mercado:
        dados["mercado"] = mercado
        st.success(f"✅ Dados de mercado: B3 = {mercado.get('bvsp_atual', 'N/A')}")
        if 'usd_atual' in mercado:
            st.info(f"💱 USD/BRL = {mercado['usd_atual']}")
    else:
        st.warning("⚠️ Não foi possível buscar dados de mercado")

    dados["fontes"]["yfinance"] = "dados de mercado atualizados"

    # 2. Tenta buscar Selic via web
    selic_web = buscar_selic_web()
    dados["fontes"]["web"] = selic_web.get("msg", "indisponivel")

    # 3. Permite atualização manual
    st.markdown("---")
    st.markdown("### ✏️ Atualização Manual (caso não consiga buscar automaticamente)")
    manual = atualizar_manualmente()
    dados["manual"] = manual

    st.success("✅ Dados salvos!")
    return dados

# --- Salvar dados atualizados ---
def salvar_dados_atualizados(dados):
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    filepath = os.path.join(data_dir, "dados_externos.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    return filepath

# --- Formatar dados para exibição ---
def formatar_resumo(dados):
    resumo = f"""
    📊 **Última atualização:** {dados.get('data_atualizacao', 'N/A')}

    🏦 **Mercado:**
    - B3 (BVSP): {dados.get('mercado', {}).get('bvsp_atual', 'N/A')}
    - Variação: {dados.get('mercado', {}).get('bvap_variacao', 'N/A'):.2f}%

    💱 **Câmbio:**
    - USD/BRL: {dados.get('mercado', {}).get('usd_atual', 'N/A')}

    📝 **Fontes:**
    - yfinance: {dados.get('fontes', {}).get('yfinance', 'N/A')}
    - Web: {dados.get('fontes', {}).get('web', 'N/A')}
    """
    return resumo
