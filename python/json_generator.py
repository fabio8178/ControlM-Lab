import json
from pathlib import Path


def gerar_json(jobs):

    dados = {
        "Application": jobs[0].application,
        "Jobs": {}
    }

    for job in jobs:

        dados["Jobs"][job.nome] = {
            "Type": "Job:Command",
            "SubApplication": job.subapplication,
            "Host": job.host,
            "RunAs": job.runas,
            "Command": job.command,
            "Description": job.description
        }

        if job.depends_on:

           dados["Jobs"][job.nome]["DependsOn"] = job.depends_on

    pasta = Path("../output/jobs")
    pasta.mkdir(parents=True, exist_ok=True)

    arquivo = pasta / "Financeiro.json"

    with arquivo.open("w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)

    print(f"Arquivo criado: {arquivo.name}")