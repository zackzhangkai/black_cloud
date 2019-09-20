#!/usr/bin/env bash
source ./env_boxes/web_py36/bin/activate
uwsgi --ini ./netstore/conf/netstore_uwsgi.ini