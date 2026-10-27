from pathlib import Path
from PIL import Image

PASTA_ENTRADA = Path("entrada")
EXTENSOES = {".jpg", ".jpeg", ".png"}
LARGURA_MAXIMA = 1920

imagens = [
    arquivo
    for arquivo in PASTA_ENTRADA.iterdir()
    if arquivo.suffix.lower() in EXTENSOES
]

print(f"Encontradas {len(imagens)} imagens:\n")

for imagem in imagens:
    tamanho_mb = imagem.stat().st_size / (1024 * 1024)

    with Image.open(imagem) as img:
        largura, altura = img.size
        
        if largura > LARGURA_MAXIMA: # compara largura da foto com a largura maxima
            proporcao = LARGURA_MAXIMA / largura #estabelece a proporção da largura máxima dividindo a largura da imagem
            nova_largura = LARGURA_MAXIMA #faz com que o resultado da linha de cima seja a (nova largura)
            nova_altura = round(altura * proporcao) # após usando o round para obter um resultado preciso do calculo da altura da imagem com a proporção calculada
        else:
            nova_largura = largura
            nova_altura = altura

    print(f"{imagem.name} - {largura}x{altura} -> {nova_largura}x{nova_altura} - {tamanho_mb:.2f} MB")