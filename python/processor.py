from validator import validar_job
from json_generator import gerar_json


def processar_jobs(jobs):

    total = len(jobs)
    validos = 0
    invalidos = 0
    houve_erros = False

    for job in jobs:

        erros = validar_job(job, jobs)

        if erros:
            houve_erros = True
            invalidos += 1

            print("\nErros encontrados:")

            for erro in erros:
                print(" -", erro)

        else:
            validos += 1

    if not houve_erros:
        gerar_json(jobs)

    return total, validos, invalidos