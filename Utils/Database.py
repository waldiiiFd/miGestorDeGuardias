import psycopg2


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.host = "localhost"
        self.database = "GestionGuardias"
        self.user = "postgres"
        self.password = "cocoloco02"

    def connect(self):
        try:
            conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            return conn
        except psycopg2.Error as e:
            print("Error al conectar a la base de datos:", e)
            return None
