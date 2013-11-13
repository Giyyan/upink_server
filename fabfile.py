from fabric.api import *
from fabtools import require
import fabtools


@task
def setup(env_path="/home/giyyan/.envs/erp61", project_path="/home/giyyan/projects/upink_deploy"):
    fabtools.deb.install([
        'python-dev',
        'libmysqlclient-dev',
        'postgresql-server',
        'postgresql-server-dev-all',
        'libsasl2-dev',
        'libldap2-dev',
        'libxml2-dev',
        'libxslt1-dev',
    ])

    with fabtools.python.virtualenv(env_path):
        pass
        #fabtools.python.install_requirements('{}/requiresents/local.txt'.format(project_path,))s