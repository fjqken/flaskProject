from flask import Flask
from flask_cors import CORS
from apis.user import app_user
from apis.interface_debugging import interface_debugging
from apis.project_api import project_api
import config.configs as configs
from common.database import db
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(app_user)
app.register_blueprint(interface_debugging)
app.register_blueprint(project_api)

app.config.from_object(configs)
db.init_app(app)
migrate = Migrate(app, db)


# ORM模型欧射成表的三步
# 1.fLask db init:这步只需要执行一次
# 2.fLask db migrate: 识ORM模型的改变，生成迁移脚本#
# 3.fLask db upgrade: 运行还移脚本，同步到数据库中


# app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
# db = SQLAlchemy(app)
#
# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute("select 1")
#         print(rs.fetchone())

# with app.app_context():
#     db.create_all()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    # run(host, port, debug, **options)
    # host要监听的主机名。 默认为127.0.0.1（localhost）。设置为“0.0.0.0”以使服务器在外部可用
    # port 端口号 默认5000
    # debug 提供调试信息 TRUE 为提供
