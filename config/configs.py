# 用于保存系统的配置信息
HOST = 'localhost'
PORT = '3306'
DATABASE = 'tpmstore'
USERNAME = 'root'
PASSWORD = '951212'
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
