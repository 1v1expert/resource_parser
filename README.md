# resource_parser

Parser take a data from мobile.de

Install:
```bash
$ sudo apt-get install python3-dev libmysqlclient-dev build-essential
$ pip install mysqlclient
```
>> create dump data
```bash
$ python manage.py dumpdata --indent=2 --exclude=contenttypes > datadump.json
```
