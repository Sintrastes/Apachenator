#!/bin/sh

sudo apt-get install apache2 python

sudo mkdir /opt/apachenator
sudo cp ./Apachenator.desktop ~/.local/share/applications/Apachenator.desktop
sudo cp -R ./ /opt/apachenator/
sudo cp -R ./ /opt/apachenator/

sudo chmod -R 777 /opt/apachenator
