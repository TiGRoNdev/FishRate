#! /bin/bash

sudo unlink /etc/nginx/sites-enabled/default
sudo unlink /etc/nginx/sites-available/default

sudo ln -s /home/tigron/fishrate/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -s /home/tigron/fishrate/etc/nginx.conf  /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
sudo gunicorn -c /home/tigron/fishrate/etc/gunicorn-django.conf fish.wsgi:application
