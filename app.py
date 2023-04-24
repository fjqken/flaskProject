from flask import Flask
from flask_cors import CORS
from apis.user import app_user
import config.configs as configs
from flask_sqlalchemy import SQLAlchemy
from common.database import db

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(app_user)
app.config.from_object(configs)
db.init_app(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
# db = SQLAlchemy(app)
#
# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute("select 1")
#         print(rs.fetchone())

with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    # run(host, port, debug, **options)
    # host要监听的主机名。 默认为127.0.0.1（localhost）。设置为“0.0.0.0”以使服务器在外部可用
    # port 端口号 默认5000
    # debug 提供调试信息 TRUE 为提供
