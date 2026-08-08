from openpyxl import load_workbook
from pathlib import Path
from job import Job


def ler_jobs():
    arquivo = Path("../input/jobs.xlsx")

    if not arquivo.exists():
        print("Arquivo Excel não encontrado!")
        return []

    workbook = load_workbook(arquivo)
    planilha = workbook.active

    jobs = []

    for linha in planilha.iter_rows(min_row=2, values_only=True):
        job = Job(
            linha[0],
            linha[1],
            linha[2],
            linha[3],
            linha[4],
            linha[5],
            linha[6],
            linha[7]
        )
        jobs.append(job)

    return jobs