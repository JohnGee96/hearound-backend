# Database Migration Management

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from server import app
from server.models import db

app.config.from_object('server.config.DevelopmentConfig')
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()