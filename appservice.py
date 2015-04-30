#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

msj = ''

def is_integer(x):
    try:
        int(x)
        return False
    except ValueError:
        print('Please enter an integer above 2')
        return True

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[93m'
    WARNING = '\033[31m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

if os.geteuid() != 0:
    print 'Debes tener privilegios root para este script.'
    sys.exit(1)
else:

    option = 100

    while option:

        os.system('clear')
        print msj
        msj = ''

        try:
            subprocess.check_output("sudo service apache2 status", shell=True)
            apache = bcolors.OKGREEN + 'INICIADO' + bcolors.ENDC
        except subprocess.CalledProcessError, e:
            apache = bcolors.WARNING + 'APAGADO' + bcolors.ENDC


        mysql = subprocess.check_output("sudo service mysql status", shell=True)
        if 'stop' in mysql:
            mysql = bcolors.WARNING + 'APAGADO' + bcolors.ENDC
        else:
            mysql = bcolors.OKGREEN + 'INICIADO' + bcolors.ENDC


        try:
            postgresql = subprocess.check_output("sudo service postgresql status", shell=True)
            postgresql = bcolors.OKGREEN + 'INICIADO' + bcolors.ENDC
        except subprocess.CalledProcessError, e:
            postgresql = bcolors.WARNING + 'APAGADO' + bcolors.ENDC


        ssh = subprocess.check_output("sudo service ssh status", shell=True)
        if 'stop' in ssh:
            ssh = bcolors.WARNING + 'APAGADO' + bcolors.ENDC
        else:
            ssh = bcolors.OKGREEN + 'INICIADO' + bcolors.ENDC

        
        cups = subprocess.check_output("sudo service cups status", shell=True)
        if 'stop' in cups:
            cups = bcolors.WARNING + 'APAGADO' + bcolors.ENDC
        else:
            cups = bcolors.OKGREEN + 'INICIADO' + bcolors.ENDC


        iptables = subprocess.check_output("sudo iptables -L -n", shell=True)
        if "DROP" in iptables:
            iptables = bcolors.OKGREEN + 'INICIADO' + bcolors.ENDC
        else:
            iptables = bcolors.WARNING + 'APAGADO' + bcolors.ENDC

        print '='*40
        print 'Item \t Service \t Estado'
        print '-'*40
        print '1 \t Apache \t%s' %apache
        print '2 \t MySQL  \t%s' %mysql
        print '3 \t PostgreSQL  \t%s' %postgresql
        print '4 \t SSH    \t%s' %ssh
        print '5 \t Cups   \t%s' %cups
        print '6 \t IPTables   \t%s' %iptables
        print '7 \t eth0: Clonar mac   \t'
        print '-'*40
        print '0 \t SALIR  '
        print '='*40

        
        try:
            option = int(input('Seleccione el Service: '))
        except (SyntaxError, NameError):
            msj = bcolors.OKBLUE + 'Opcion ingresada NO ES VALIDA!!! \nIngrese nuevamente la Opcion' + bcolors.ENDC

        
        if option != 100:

            if option == 1:
                if 'APAGADO' in apache:
                    os.system('sudo service apache2 start')
                else:
                    os.system('sudo service apache2 stop')

            elif option == 2:
                if 'APAGADO' in mysql:
                    os.system('sudo service mysql start')
                else:
                    os.system('sudo service mysql stop')

            elif option == 3:
                if 'APAGADO' in postgresql:
                    os.system('sudo service postgresql start')
                else:
                    os.system('sudo service postgresql stop')

            elif option == 4:
                if 'APAGADO' in ssh:
                    os.system('sudo service ssh start')
                else:
                    os.system('sudo service ssh stop')

            elif option == 5:
                if 'APAGADO' in cups:
                    os.system('sudo service cups start')
                else:
                    os.system('sudo service cups stop')

            elif option == 6:
                if 'APAGADO' in iptables:
                    os.system('sudo /home/scasas/exe/./firewall ')
                else:
                    os.system('sudo iptables -F ')
            
            elif option == 7:
                os.system('sudo ifconfig eth0 hw ether 00:11:22:33:aa:bb')

            else:

                msj = bcolors.OKBLUE + 'Opcion ingresada NO ES VALIDA!!! \nIngrese nuevamente la Opcion' + bcolors.ENDC

    