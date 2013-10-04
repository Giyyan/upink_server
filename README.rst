========================
UpSale and Inksystem OpenERP deploy
========================

Модули для OpenERP v. 6.1

Установка OpenERP:
===================

Ubuntu
===================

#. Создаем виртуальное окружение для работы (virtualenv/virtualenvwrapper) - дальше работаем зайдя в окружение
#. Ставим PostgreSQL 9.2
    #. Создаем /etc/apt/sources.list.d/pgdg.list
    #. Добавляем в него::
    
        $ deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main
        
    #. Добавляем ключ для репозитория::
    
        $ wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -
    
    #. Обновляем и ставим::
    
        $ sudo apt-get update
        $ sudo apt-get install postgresql-common -t raring
        $ sudo apt-get install postgresql-9.2  
        
#. Ставим пакеты::

    $ sudo apt-get install python-dev libmysqlclient-dev postgresql-server-dev-all libsasl2-dev libldap2-dev libxml2-dev libxslt1-dev
          
#. Ставим недостающие пакеты::

    $ pip install -r requirements/local.txt
    
#. Ставим aeroolib (в папке libs/aeroolib) $ python setup.py install
#. Ставим openerp (в папке libs/server) $ python setup.py install
#. Настраиваем PostgreSQL (http://www.if-not-true-then-false.com/2012/install-postgresql-on-fedora-centos-red-hat-rhel/)::

    $ sudo passwd postgres
    $ /etc/postgresql/*/main/pg_hba.conf - trust всем
    $ можно поставить webmin, будет удобно создать пользователя и смотреть за бд.

CentOS
===================

Все тоже самое что с убунтой, только ставим другие пакеты::

    $ sudo yum install python-dateutil python-docutils python-feedparser python-gdata \
        python-jinja2 python-ldap libxslt-python python-lxml python-mako python-mock python-openid \
        python-psycopg2 python-psutil python-babel pychart pydot python3-pyparsing \
        python-reportlab python-simplejson python-dateutil python-unittest2 python-vatnumber python-vobject \
        python-webdav-library python-werkzeug python-xlwt python-yaml python-ZSI freetype-devel

Запуск OpenERP:
===================

Developing:
===================

Из-под рабочего окружения запускаем сервер(примеры settings_file лежат в папке settings - .openerp_serverrc) можно просто скопировать в домашную папку и тогда запускать без параметра -с::

    $ openerp-server -c /path/to/settings_file
    
Production:
===================

На продакшне запускаем сервер с помощью gunicorn

#. Заходим в рабочее окружение
#. Устанавливаем gunicorn (http://gunicorn.org/)::
    
    $ pip install gunicorn
    
#. Запускаем сервер::

    $ gunicorn openerp:core.wsgi.application -c /path/to/gunicorn.conf.py

#. Устанавливаем supervisord (http://supervisord.org/) для контроля процесса openerp::

    $ pip install supervisord
    
