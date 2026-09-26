import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import json
import os

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
with open(os.path.join(data_dir, 'produtos_financeiros.json')) as f:
    produtos = json.load(f)

with open(os.path.join(data_dir, 'dados_externos.json')) as f:
    externos = json.load(f)

fig, ax = plt.subplots(figsize=(14, 7))

names = []
rates = []
colors = []

for p in produtos:
    names.append(p['nome'])
    rate = p['rentabilidade_num'] if p['rentabilidade_num'] is not None else 0
    rates.append(rate)
    color = '#e94560' if p['categoria'] == 'renda_fixa' else '#0984e3'
    colors.append(color)

bars = ax.barh(range(len(names)), rates, color=colors, edgecolor='white', linewidth=0.5)
ax.set_yticks(range(len(names)))
ax.set_yticklabels(names, fontsize=10)
ax.set_xlabel('Rentabilidade (% a.a.)', fontsize=11)
ax.set_title('Produtos Financeiros Disponíveis - Setembro 2026', fontsize=14, fontweight='bold', pad=15)

for i, (bar, rate) in enumerate(zip(bars, rates)):
    original_rate = produtos[i]['rentabilidade_num']
    if original_rate is not None:
        ax.text(rate + 0.2, bar.get_y() + bar.get_height()/2,
                f'{rate:.2f}%', va='center', fontsize=9, color='#ffffff')
    else:
        ax.text(0.2, bar.get_y() + bar.get_height()/2,
                'Variavel', va='center', fontsize=9, color='#ffffff')

# Linha CDI
cdi = externos['taxa_cdi']['valor']
ax.axvline(x=cdi, color='#00b894', linestyle='--', linewidth=2, label=f'CDI ({cdi}%)')
ax.axvline(x=externos['taxa_selic']['valor'], color='#e94560', linestyle='--',
           linewidth=2, label=f'Selic ({externos["taxa_selic"]["valor"]}%)')

# Linha Selic
selic = externos['taxa_selic']['valor']

ax.legend(fontsize=10, loc='lower right')
ax.set_xlim(0, 20)
ax.invert_yaxis()

# Fundo
ax.set_facecolor('#1a1a2e')
fig.patch.set_facecolor('#1a1a2e')
ax.spines['bottom'].set_color('#333')
ax.spines['left'].set_color('#333')
ax.tick_params(colors='#fff')
ax.xaxis.label.set_color('#fff')
ax.title.set_color('#e94560')

plt.tight_layout()
plt.savefig('assets/img/produtos.png', dpi=150, bbox_inches='tight',
            facecolor='#1a1a2e', edgecolor='none')
print("OK: produtos.png")
