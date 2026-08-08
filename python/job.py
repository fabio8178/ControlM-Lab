class Job:

    def __init__(
        self,
        nome,
        application,
        subapplication,
        host,
        runas,
        command,
        description,
        depends_on
    ):

        self.nome = nome
        self.application = application
        self.subapplication = subapplication
        self.host = host
        self.runas = runas
        self.command = command
        self.description = description
        self.depends_on = depends_on