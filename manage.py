from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

app.config.from_pyfile("../config.py")
print(app.config.get("SQLALCHEMY_DATABASE_URI"))

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
