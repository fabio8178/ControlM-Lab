import json
from pathlib import Path


def gerar_json(job):

    dados = {
        job["Job"]: {
            "Type": "Job:Command",
            "Host": job["Host"],
            "RunAs": "controlm",
            "Command": job["Command"]
        }
    }

    pasta = Path("../output/jobs")
    pasta.mkdir(parents=True, exist_ok=True)

    arquivo = pasta / f"{job['Job']}.json"

    with arquivo.open("w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)

    print(f"Arquivo criado: {arquivo.name}")
