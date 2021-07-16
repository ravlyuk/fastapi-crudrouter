import databases
import ormar
import sqlalchemy

sql_db = 'sqlite:///sqlite.db'
metadata = sqlalchemy.MetaData()
database = databases.Database(sql_db)
engine = sqlalchemy.create_engine(sql_db)


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
