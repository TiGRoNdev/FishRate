#! /bin/bash

sudo /etc/init.d/gunicorn restart
sudo gunicorn -c /home/tigron/projects/fishrate/etc/gunicorn-django.conf fish.wsgi:application
