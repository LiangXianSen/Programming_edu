# Install Mysql

```
$ apt-get install mysql-server
$ mysql -u root
mysql> GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' IDENTIFIED BY 'admin@programming' WITH GRANT OPTION;
mysql> FLUSH PRIVILEGES;
mysql> CREATE DATABASE programming_edu CHARACTER SET utf8;
```


# Install Django Runtime

```
pip install -r requirements.txt
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



# Special Effect

### Preloader

This part of the documentation will help you to customize preloader

Underneath the `<body>` tag you can find preloader mark-up. You can apply any custom styles of preloader as you want by customizing css in `style.css`. You can also use gif images. 
Follow the steps below to apply preloader

**Step-1:** Add preloader markup.

```html
`<``body` `id``=``"body"` `class``=``""``>``  ``<``div` `id``=``"preloader"` `class``=``"loader-wrapper"``>` `    ``<!-- Put any preloader markup you can also use gif images -->` `  ``</``div``>`
```

**Step-2:** Copy the following javascript code in `custom.js`

```javascript
`setTimeout(``function``(){``  ``$(``'body'``).addClass(``'loaded'``);``}, 3000);`
```

This will add a class **loaded** in the `<body>` element after the loader finishes loading. By default loader time is set for 3 seconds, you can increase or decrease it in the function above.

**Step-3:** `body` containes some style properties until the preloader loads. You need to overwrite the properties when the loaded class added. Copy the following css and paste it in `style.css`

```css
`#preloader {``  ``/* Apply any css style properties for loader. */``}` `/* Hide the preloader when finishes loading */``.loaded {``  ``#preloader {``    ``opacity: ``0``;``    ``visibility``: ``hidden``;``    ``@include transition(``all` `0.7``s ease-out);``  ``}``}`
```