from flask_script import Manager

from App import createApp

app = createApp('default')
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
