import sys

def metros_para_centimetros(metros):
    centimetros = metros * 100
    return centimetros

def centimetros_para_metros(centimetros):
    metros = centimetros / 100
    return metros

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Por favor, forneça um valor em metros para converter para centímetros/metros ou a unidade de medida para conversão.")
    else:
        try:
            if(("centímetros" in sys.argv[2] or "centimetros" in sys.argv[2]) and int(sys.argv[1]) >= 0):
                metros = float(sys.argv[1])
                centimetros = metros_para_centimetros(metros)
                print(f"{sys.argv[1]} metros é igual a {centimetros} centímetros.")
            elif("metros" in sys.argv[2] and int(sys.argv[1]) >= 0):
                centimetros = float(sys.argv[1])
                metros = centimetros_para_metros(centimetros)
                print(f"{sys.argv[1]} centimetros é igual a {metros} metros.")
            else:
                print("Unidade não encontrada,só são aceitas as medidas metros e centímetros e valores positivos.")
                print("Entrada válida: python3 conversion_medida.py 100 metros")
        except ValueError:
            print("Por favor, forneça um valor válido em metros.")
