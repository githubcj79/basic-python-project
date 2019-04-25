# file:~/Documents/Python/Lab/basicp-git/Readme.py

April 25, 2019.

	Previo a cualquier ejecución de la aplicación:
	$ pipenv shell

	Ejecución de basicp como módulo:
	(basicp-git)$ python -m basicp

April 24, 2019.

	Debo:
		- revisar el mejor modo de incorporar logging
		- agregar la línea siguiente a los *.py, que creo:
			from __future__ import print_function, with_statement

	Logging
	Me baso en: https://realpython.com/python-logging/



April 23, 2019.

Me baso en https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6

	Creo este esqueleto de proyecto (basicp: basic project), con la finalidad
	de usarlo como template en futuros desarrollos.

		carlos@carlos-Latitude-E6440:~/Documents/Python/Lab$ mkdir -p basicp-git/basicp
		carlos@carlos-Latitude-E6440:~/Documents/Python/Lab$ tree
		.
		└── basicp-git
		    └── basicp

		2 directories, 0 files

Uso pipenv
	https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv

	carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ pipenv --python 2.7

Instalo pytest
	https://www.linuxjournal.com/content/testing-your-code-pythons-pytest

	carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ pipenv install pytest

	Note:

		To activate this project's virtualenv, run pipenv shell.
		Alternatively, run a command inside the virtualenv with pipenv run.

Usaré git

	carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ git init

Launching subshell in virtual environment…

	~/Documents/Python/Lab/basicp-git$ pipenv shell
	(basicp-git) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$

Verificando versión de python
(basicp-git) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ python --version
Python 2.7.15rc1

Creando estructura básica:

(basicp-git) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ touch basicp/__init__.py
(basicp-git) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ touch basicp/__main__.py
(basicp-git) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ touch basicp/app.py
(basicp-git) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ mkdir -p basicp/common
(basicp-git) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ mkdir -p basicp/data
(basicp-git) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ mkdir -p basicp/resources
(basicp-git) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ mkdir -p basicp/tests
(basicp-git) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ touch basicp/common/__init__.py
(basicp-git) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ touch basicp/data/__init__.py
(basicp-git) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ touch basicp/tests/__init__.py

Ejecución de basicp como módulo:
(basicp-git) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ python -m basicp
	--> basicp/__main__.py --> basicp/app.run() --> print('Hello world !!!')

Ejecución de tests:
(basicp-git) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/basicp-git$ pytest

-----------------
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file: basicp/data/settings.py

import logging

from datetime import datetime

# LOG_FILE = './log_dir/cmocp.log'
_now = datetime.now()
LOG_FILE = _now.strftime('./log_dir/%Y%m%d_cmocp.log')

# Definiciones para el nivel de log.
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )
-----------------

carlos@carlos-Latitude-E6440:~/Documents/Python/Lab$ mkdir -p basicp-git/basicp
carlos@carlos-Latitude-E6440:~/Documents/Python/Lab$ tree
.
└── basicp-git
    └── basicp

2 directories, 0 files



La idea es crear el ambiente básico Python2, para hacer un desarrollo.
Este debe considerar el uso de:

Cómo estructurar el proyecto
	https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6
	
- git
- pipenv
	Referencias
		https://pipenv.readthedocs.io/en/latest/basics/
		https://www.linode.com/docs/development/python/manage-python-environments-pipenv/
		https://pipenv.readthedocs.io/en/latest/
		https://www.ioannispoulakas.com/2018/01/28/manage-your-python-dependencies-with-pipenv/

- looging
- modulos
- referencias entre módulos
- archivo de configuración
- testpy

Primeros comandos
	$ mkdir myproject && cd myproject
	$ pipenv --python 2.7
	$ pipenv install pytest
	$ pipenv run python --version
	$ git init
	$ pipenv shell
	(myproject) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/Lab0/myproject$
	(myproject) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/Lab0/myproject$ python --version
	Python 2.7.15rc1
	(myproject) carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/Lab0/myproject$ exit
	exit
	carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/Lab0/myproject$
	carlos@carlos-Latitude-E6440:~/Documents/Python/Lab/Lab0/myproject$ pipenv run which python
	/home/carlos/.local/share/virtualenvs/myproject-TNKDvw5J/bin/python