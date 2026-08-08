from openpyxl import load_workbook
from pathlib import Path
from job import Job
from folder import Folder


def ler_jobs():
    arquivo = Path("../input/jobs.xlsx")

    if not arquivo.exists():
        print("Arquivo Excel não encontrado!")
        return []

    workbook = load_workbook(arquivo)
    planilha = workbook.active

    folder = None

    for linha in planilha.iter_rows(min_row=2, values_only=True):
        if folder is None:
           folder = Folder(
           linha[0],
           linha[2]
        )
        job = Job(
            linha[1],
            linha[2],
            linha[3],
            linha[4],
            linha[5],
            linha[6],
            linha[7],
            linha[8]
        )
        folder.jobs.append(job)

    return folder