from pathlib import Path

PASTA_ENTRADA = Path("entrada")
EXTENSOES = {".jpg," ".jpeg", ".png"}

imagens = [
    arquivo
    for arquivo in PASTA_ENTRADA.iterdir()
    if arquivo.suffix.lower() in EXTENSOES
]

print(f"Encontradas {len(imagens)} imagens:\n")

for imagem in imagens:
    tamanho_mb = imagens.stat().st_size / (1024 * 1024)
    print (f"{imagem.name} - {tamanho_mb:.2f} MB")