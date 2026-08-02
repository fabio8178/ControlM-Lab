from openpyxl import load_workbook
from pathlib import Path


def ler_jobs():
    arquivo = Path("../input/jobs.xlsx")

    if not arquivo.exists():
        print("Arquivo Excel não encontrado!")
        return []

    workbook = load_workbook(arquivo)
    planilha = workbook.active

    jobs = []

    for linha in planilha.iter_rows(min_row=2, values_only=True):
        job = {
            "Job": linha[0],
            "Host": linha[1],
            "Command": linha[2]
        }
        jobs.append(job)

    return jobs