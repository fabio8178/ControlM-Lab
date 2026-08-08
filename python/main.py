from excel_reader import ler_jobs
from processor import processar_jobs


def main():

    print("=" * 50)
    print("Control-M Automation Factory")
    print("=" * 50)

    jobs = ler_jobs()

    total, validos, invalidos = processar_jobs(jobs)

    print("\n" + "=" * 50)
    print("Resumo")
    print("=" * 50)

    print(f"Jobs lidos      : {total}")
    print(f"Jobs válidos    : {validos}")
    print(f"Jobs inválidos  : {invalidos}")


if __name__ == "__main__":
    main()