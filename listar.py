from pathlib import Path
from PIL import Image

PASTA_ENTRADA = Path("entrada")
EXTENSOES = {".jpg", ".jpeg", ".png"}

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

    print(f"{imagem.name} - {largura}x{altura} - {tamanho_mb:.2f} MB")