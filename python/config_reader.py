import json
from pathlib import Path


def carregar_config():

    arquivo = Path("config.json")

    with arquivo.open("r", encoding="utf-8") as f:
        return json.load(f)
