from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError
from app.models.base import db

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


manager.add_command('db', MigrateCommand)


@app.errorhandler(Exception)
def framework_error(e):
    """
        捕捉所有异常(flask 1.0才有)
        e：APIException/HTTPException/Exception
    """
    if isinstance(e, APIException):
        return e

    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)

    else:
        # 可以做 log 日志记录
        # 调试模式
        if app.config['DEBUG']:
            raise e

        return ServerError()


if __name__ == '__main__':
    manager.run()
