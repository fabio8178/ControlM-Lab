import json
from pathlib import Path
from config_reader import carregar_config
from logger import logger


def gerar_json(folder):

    config = carregar_config()
    dados = {
        folder.nome: {
        "Type": "Folder",        
        "Application": folder.application,
        "Jobs": {}
        }
    }
    for job in folder.jobs:

        dados[folder.nome]["Jobs"][job.nome] = {
            "Type": "Job:Command",
            "SubApplication": job.subapplication,
            "Host": job.host,
            "RunAs": job.runas,
            "Command": job.command,
            "Description": job.description
        }

        if job.depends_on:

           dados[folder.nome]["Jobs"][job.nome]["DependsOn"] = job.depends_on

    pasta = Path(config["output_folder"])
    pasta.mkdir(parents=True, exist_ok=True)

    arquivo = pasta / f"{folder.nome}.json"

    with arquivo.open("w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)

    logger.info(f"Arquivo criado: {arquivo.name}")