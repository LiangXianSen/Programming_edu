# Install Mysql

```
$ apt-get install mysql-server
$ mysql -u root
mysql> GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' IDENTIFIED BY 'admin@programming' WITH GRANT OPTION;
mysql> FLUSH PRIVILEGES;
mysql> CREATE DATABASE programming_edu;
```



# Init Environment

```
python3 -m django --version (2.1.2)
python3 manage.py startproject web
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver 8000
```



# Prepare

`setting.py`

```
import pymysql
pymysql.install_as_MySQLdb()
```

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'programming_edu',
        'USER': 'admin',
        'PASSWORD': 'admin@programming',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

```
TIME_ZONE = 'Asia/Shanghai'
```

