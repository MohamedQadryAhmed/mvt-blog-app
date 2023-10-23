

class Config:
    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog-app.sqlite"


class ProdactionConfig(Config):
    DEBUG = False
      # postgresql://username:password@localhost:portnumber/dbname
    SQLALCHEMY_DATABASE_URI = "postgresql://flask:iti@localhost:5432/blogdb"


projectConfig={
    "dev": DevelopmentConfig,
    'prd': ProductionConfig
}