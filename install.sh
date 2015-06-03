#!/usr/bin/env bash
 
set -o errexit 
cd $( dirname $0 )

SERVER_DIR=/var/www/html
CGI_DIR=/usr/lib/cgi-bin

Backup() {
  local path=$1
  if [[ -n $( ls $path ) ]] ; then
    [[ ! -d $path/.backup ]] && mkdir $path/.backup
    mv $path/* $path/.backup
  fi
}

Backup $SERVER_DIR
#Backup /usr/lib/cgi-bin

cp main.php $SERVER_DIR/index.php
cp handler.py $CGI_DIR
