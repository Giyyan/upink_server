# coding=utf-8
import os
from fabric.api import *

env.hosts = ['46.28.67.221']


def production_env():
    """Окружение для продакшена"""
    env.user = 'andrey'
    env.password = "{djcn0atb"
    env.project_root = '/home/andrey/upink_server'
    env.python = '/home/andrey/.venvs/erp61/bin/python'


def demo_env():
    """Окружение для демо"""
    env.user = 'andrey'
    env.password = "edge0city"
    env.project_root = '/home/andrey/upink'
    env.python = '/home/andrey/.venvs/ue/bin/python'


def iptables_check(ip):
    if sudo('iptables --list-rules | grep %s' % ip, quiet=True):
        return True
    else:
        return False


@hosts('46.28.67.221')
def iptables_add(ip, port=8080):
    production_env()
    with cd(env.project_root):
        if iptables_check(ip):
            print 'Уже существует такая запись'
        else:
            print 'Сейчас добавим'
            if not sudo('iptables -A INPUT -p tcp -m state -m tcp -s %s --dport %s --state NEW -j ACCEPT' % (ip, port), quiet=True):
                print 'Добавили'
            else:
                print 'Что-то пошло не так'


@hosts('46.28.67.221')
def iptables_del(ip, port=8080):
    production_env()
    with cd(env.project_root):
        if iptables_check(ip) and not sudo('iptables -D INPUT -p tcp -m state -m tcp -s %s --dport %s --state NEW -j ACCEPT' % (ip, port), quiet=True):
            print 'Удалили'
        else:
            print 'Что-то пошло не так'


def deploy():
    pass