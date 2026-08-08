from job import Job


job = Job(
    "ReceberArquivo",
    "FINANCEIRO",
    "IMPORTACAO",
    "LINUX01",
    "batch01",
    "receber.sh",
    "Recebe arquivos bancários"
)

print(job.nome)
print(job.host)
print(job.command)
