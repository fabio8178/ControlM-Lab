def validar_job(job, jobs):

    erros = []
    nomes_jobs = []

    for j in jobs:
        nomes_jobs.append(j.nome)

    if not job.nome:
        erros.append("Campo Job não informado.")

    if not job.host:
        erros.append(f"Job {job.nome}: Host não informado.")

    if not job.command:
        erros.append(f"Job {job.nome}: Command não informado.")

    if not job.runas:
        erros.append(f"Job {job.nome}: RunAs não informado.")

    if job.depends_on:

       if job.depends_on not in nomes_jobs:
          erros.append(
              f"Job {job.nome}: DependsOn '{job.depends_on}' não existe."
          )    

    return erros