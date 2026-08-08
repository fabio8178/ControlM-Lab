from validator import validar_job
from json_generator import gerar_json


def processar_jobs(folder):

    total = len(folder.jobs)
    validos = 0
    invalidos = 0
    houve_erros = False

    for job in folder.jobs:

        print(job.nome, "->", job.depends_on)
        
        erros = validar_job(job, folder.jobs)

        if erros:
            houve_erros = True
            invalidos += 1

            print("\nErros encontrados:")

            for erro in erros:
                print(" -", erro)

        else:
            validos += 1

    if not houve_erros:
        gerar_json(folder)

    return total, validos, invalidos