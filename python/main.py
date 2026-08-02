from excel_reader import ler_jobs
from json_generator import gerar_json


def main():
    print("=" * 50)
    print("Control-M Automation Factory")
    print("=" * 50)

    jobs = ler_jobs()

    print("\nJobs encontrados:\n")

    for job in jobs:
        gerar_json(job)


if __name__ == "__main__":
    main()