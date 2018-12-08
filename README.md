# Install Mysql

```
$ apt-get install mysql-server
$ mysql -u root
mysql> GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' IDENTIFIED BY 'admin@programming' WITH GRANT OPTION;
mysql> FLUSH PRIVILEGES;
mysql> CREATE DATABASE programming_edu CHARACTER SET utf8;;
```


# Install Django Runtime

```
pip install -r requirement.txt
```


# Init Environment

```
python -m django --version (2.1.2)
python manage.py startapp web
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
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

