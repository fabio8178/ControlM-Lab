from excel_reader import ler_jobs
from processor import processar_jobs
import time


def main():

    inicio = time.perf_counter()
    print("=" * 50)
    print("Control-M Automation Factory")
    print("=" * 50)

    folders = ler_jobs()

    total, validos, invalidos = processar_jobs(folders)

    print("\n" + "=" * 50)
    print("RESUMO DA EXECUCAO")
    print("=" * 50)

    print(f"Jobs lidos      : {total}")
    print(f"Jobs válidos    : {validos}")
    print(f"Jobs inválidos  : {invalidos}")

    fim = time.perf_counter()
    tempo = fim - inicio

    print(f"Tempo execução  : {tempo:.2f} segundos")

if __name__ == "__main__":
    main()