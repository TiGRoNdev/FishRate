#! /bin/bash

sudo /etc/init.d/gunicorn restart
sudo gunicorn -c /home/tigron/fishrate/etc/gunicorn-django.conf fish.wsgi:application
