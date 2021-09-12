
from app import App
from flask_script import Manager,Server

# Creating app instance
app = App('development')

manager = Manager(app)
manager.add_command('server',Server)

if __name__ == '__main__':
    manager.run(debug = True)