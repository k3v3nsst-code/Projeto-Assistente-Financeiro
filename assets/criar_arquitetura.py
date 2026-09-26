import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

cor_fundo = '#1a1a2e'
cor_card = '#16213e'
cor_accent = '#0f3460'
cor_bright = '#e94560'
cor_green = '#00b894'
cor_blue = '#0984e3'
cor_yellow = '#fdcb6e'
cor_text = '#ffffff'

ax.add_patch(plt.Rectangle((0, 0), 14, 10, color=cor_fundo, zorder=0))

# Título
ax.text(7, 9.5, 'MENTOR FINANCEIRO (AURORA)', ha='center', fontsize=16,
        color=cor_bright, fontweight='bold', zorder=5)
ax.text(7, 9.0, 'Arquitetura do Sistema', ha='center', fontsize=12,
        color=cor_text, alpha=0.8, zorder=5)

# Card: Usuário
ax.add_patch(FancyBboxPatch((1, 7), 3, 1.5, boxstyle="round,pad=0.1",
    facecolor=cor_card, edgecolor=cor_bright, linewidth=2, zorder=2))
ax.text(2.5, 7.75, '[ USUARIO ]', ha='center', fontsize=11, color=cor_bright, fontweight='bold', zorder=3)
ax.text(2.5, 7.3, 'Pergunta sobre\nfinancas', ha='center', fontsize=8, color=cor_text, zorder=3)

# Card: Streamlit
ax.add_patch(FancyBboxPatch((5, 7), 3, 1.5, boxstyle="round,pad=0.1",
    facecolor=cor_card, edgecolor=cor_blue, linewidth=2, zorder=2))
ax.text(6.5, 7.75, '[ STREAMLIT ]', ha='center', fontsize=11, color=cor_blue, fontweight='bold', zorder=3)
ax.text(6.5, 7.3, 'Interface Web\nFrontend', ha='center', fontsize=8, color=cor_text, zorder=3)

# Card: LLM
ax.add_patch(FancyBboxPatch((9, 7), 3, 1.5, boxstyle="round,pad=0.1",
    facecolor=cor_card, edgecolor=cor_green, linewidth=2, zorder=2))
ax.text(10.5, 7.75, '[ OLLAMA ]', ha='center', fontsize=11, color=cor_green, fontweight='bold', zorder=3)
ax.text(10.5, 7.3, 'qwen2.5:3b\nProcessa prompt', ha='center', fontsize=8, color=cor_text, zorder=3)

# Setas
ax.add_patch(FancyArrowPatch((2.5, 7), (5, 7), arrowstyle='->', color=cor_text, lw=2, zorder=4))
ax.add_patch(FancyArrowPatch((8, 7), (9, 7), arrowstyle='->', color=cor_text, lw=2, zorder=4))
ax.add_patch(FancyArrowPatch((6.5, 8.5), (10.5, 8.5), arrowstyle='->', color=cor_text, lw=2, zorder=4,
    connectionstyle='arc3,rad=-0.3'))
ax.add_patch(FancyArrowPatch((10.5, 6.5), (6.5, 6.5), arrowstyle='->', color=cor_text, lw=2, zorder=4,
    connectionstyle='arc3,rad=0.3'))

# Card: System Prompt
ax.add_patch(FancyBboxPatch((5, 4), 3, 1.5, boxstyle="round,pad=0.1",
    facecolor=cor_card, edgecolor=cor_yellow, linewidth=2, zorder=2))
ax.text(6.5, 5.25, '[ SYSTEM PROMPT ]', ha='center', fontsize=10, color=cor_yellow, fontweight='bold', zorder=3)
ax.text(6.5, 4.75, 'Regras, Few-shot,\nTaxas de mercado', ha='center', fontsize=8, color=cor_text, zorder=3)

# Card: Dados
ax.add_patch(FancyBboxPatch((9, 4), 3, 1.5, boxstyle="round,pad=0.1",
    facecolor=cor_card, edgecolor=cor_green, linewidth=2, zorder=2))
ax.text(10.5, 5.25, '[ DADOS ]', ha='center', fontsize=10, color=cor_green, fontweight='bold', zorder=3)
ax.text(10.5, 4.75, 'JSON + CSV\nperfil, transacoes,\nprodutos', ha='center', fontsize=8, color=cor_text, zorder=3)

ax.add_patch(FancyArrowPatch((10.5, 5.5), (6.5, 5.5), arrowstyle='->', color=cor_text, lw=2, zorder=4))
ax.add_patch(FancyArrowPatch((6.5, 4.5), (6.5, 5), arrowstyle='->', color=cor_text, lw=2, zorder=4))

# Card: Resposta
ax.add_patch(FancyBboxPatch((5, 1.5), 3, 1.5, boxstyle="round,pad=0.1",
    facecolor=cor_card, edgecolor=cor_bright, linewidth=2, zorder=2))
ax.text(6.5, 2.75, '[ RESPOSTA ]', ha='center', fontsize=10, color=cor_bright, fontweight='bold', zorder=3)
ax.text(6.5, 2.25, 'Texto didatico,\nempatico, PT-BR', ha='center', fontsize=8, color=cor_text, zorder=3)

ax.add_patch(FancyArrowPatch((6.5, 4), (6.5, 3), arrowstyle='->', color=cor_text, lw=2, zorder=4))
ax.add_patch(FancyArrowPatch((6.5, 2.5), (2.5, 2.5), arrowstyle='->', color=cor_text, lw=2, zorder=4))

# Card: Sidebar
ax.add_patch(FancyBboxPatch((11.5, 1.5), 2, 1.5, boxstyle="round,pad=0.1",
    facecolor=cor_card, edgecolor=cor_blue, linewidth=2, zorder=2))
ax.text(12.5, 2.75, '[ SIDEBAR ]', ha='center', fontsize=9, color=cor_blue, fontweight='bold', zorder=3)
ax.text(12.5, 2.25, 'Perfil,\nTransacoes,\nProdutos', ha='center', fontsize=7, color=cor_text, zorder=3)

ax.add_patch(FancyArrowPatch((8, 7), (12, 4.5), arrowstyle='->', color=cor_text, lw=1.5,
    connectionstyle='arc3,rad=0.2', zorder=4, alpha=0.6))

# Legenda
ax.text(7, 0.5, 'Fluxo: Usuario -> Streamlit -> LLM -> Resposta',
        ha='center', fontsize=9, color=cor_text, alpha=0.6, style='italic', zorder=5)
ax.text(7, 0.2, 'Dados em cache | System Prompt montado dinamicamente | Ollama local',
        ha='center', fontsize=7, color=cor_text, alpha=0.4, zorder=5)

plt.tight_layout()
plt.savefig('assets/img/arquitetura.png', dpi=150, bbox_inches='tight',
            facecolor=cor_fundo, edgecolor='none')
print("OK: arquitetura.png")
