# Allow Django to use PyMySQL when DATABASE_URL points to MySQL.
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
