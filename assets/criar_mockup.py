from PIL import Image, ImageDraw

img = Image.new('RGB', (512, 512), '#1a1a2e')
draw = ImageDraw.Draw(img)

center = (256, 256)
for r in range(250, 100, -10):
    color_val = int(233 * (r / 250))
    draw.ellipse([center[0]-r, center[1]-r, center[0]+r, center[1]+r],
                 fill=(color_val, 69, 96))

draw.ellipse([200, 200, 312, 312], fill='#16213e', outline='#e94560', width=3)

draw.text((210, 235), 'A', fill='#e94560', font_size=40)
draw.text((290, 235), 'U', fill='#00b894', font_size=40)
draw.text((370, 235), 'R', fill='#e94560', font_size=40)
draw.text((450, 235), 'O', fill='#00b894', font_size=40)

img.save('assets/img/logo.png')
print("OK: logo.png")

mockup = Image.new('RGB', (1200, 800), '#0f0f23')
draw2 = ImageDraw.Draw(mockup)

draw2.rectangle([0, 0, 1200, 80], fill='#16213e')
draw2.text((40, 20), 'Mentor Financeiro', fill='#e94560', font_size=24)
draw2.text((800, 20), 'Aurora', fill='#00b894', font_size=16)

draw2.rectangle([20, 100, 1180, 600], fill='#1a1a2e', outline='#0f3460')

draw2.text((40, 120), 'Olá! Eu sou a Aurora, sua Mentora Financeira', fill='#00b894', font_size=14)
draw2.text((40, 150), 'Como posso te ajudar com suas financas?', fill='#ffffff', font_size=14)
draw2.text((800, 120), 'Oi! Tenho 1000 reais, onde investir?', fill='#e94560', font_size=14)
draw2.text((40, 250), 'O melhor para seu perfil conservador e o Tesouro Selic.', fill='#ffffff', font_size=14)
draw2.text((40, 275), 'Rende 100% da Selic (13.75% a.a.)', fill='#00b894', font_size=14)
draw2.text((800, 350), 'Poupanca: R$98/ano', fill='#ffffff', font_size=14)
draw2.text((800, 375), 'CDB 100% CDI: R$139/ano', fill='#00b894', font_size=14)

draw2.rectangle([1100, 100, 1180, 600], fill='#16213e')
draw2.text((1110, 110), '[ SIDEBAR ]', fill='#0984e3', font_size=10)

draw2.rectangle([0, 600, 1200, 800], fill='#0f0f23')
draw2.text((40, 650), 'Campo de entrada: Pergunte sobre seus gastos...', fill='#333', font_size=12)

mockup.save('assets/img/screenshot.png')
print("OK: screenshot.png")
print("Todos assets criados!")
