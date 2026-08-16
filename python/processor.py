from validator import validar_job
from json_generator import gerar_json


def processar_jobs(folders):

    total = 0
    validos = 0
    invalidos = 0
    houve_erros = False

    # ALTERAÇÃO 1 - calcular o total de jobs
    for folder in folders:
        total += len(folder.jobs)

    # ALTERAÇÃO 2 - agora percorremos todas as folders
    for folder in folders:

        # e depois todos os jobs daquela folder
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

    # ALTERAÇÃO 3 - gerar um JSON para cada folder
    if not houve_erros:

        for folder in folders:
            gerar_json(folder)

    return total, validos, invalidos