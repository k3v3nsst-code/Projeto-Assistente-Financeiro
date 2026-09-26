# Assets — Recursos Visuais do Mentor Financeiro

## Imagens

| Arquivo | Descrição |
|---------|-----------|
| `img/logo.png` | Logo do Aurora (512x512) |
| `img/arquitetura.png` | Diagrama de arquitetura do sistema |
| `img/produtos.png` | Gráfico comparativo dos produtos financeiros |
| `img/screenshot.png` | Mockup da interface da aplicação |

## Scripts de Geração

- `criar_arquitetura.py` — Gera `arquitetura.png` (matplotlib)
- `criar_produtos.py` — Gera `produtos.png` (matplotlib)
- `criar_mockup.py` — Gera `logo.png` e `screenshot.png` (PIL)

## Uso

Para regenerar as imagens:
```bash
python assets/criar_arquitetura.py
python assets/criar_produtos.py
python assets/criar_mockup.py
```

## Estrutura

```
assets/
├── README.md
├── RoteiroLab.md
├── .gitignore
└── img/
    ├── logo.png
    ├── arquitetura.png
    ├── produtos.png
    └── screenshot.png
```

## Git Ignore

Arquivos `.py` de geração estão na `.gitignore` para não serem enviados ao GitHub.
As imagens `.png` são rastreadas.
