from news import create_app
from flask_script import Manager,Server

import news

# Creating app instance
app = create_app('development')

manage = Manager(news)
manage.add_command('server',Server)

if __name__ == '__main__':
    manage.run()
    