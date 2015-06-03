# web-l1

Для начала надо поставить LAMP сервер:
sudo apt-get install tasksel
sudo tasksel install lamp-server

Потом правим /etc/apache2/apache2.conf, для того чтобы можно было запускать cgi скрипты. Дописываем туда:
ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
<Directory "/usr/lib/cgi-bin">
  AllowOverride None
  Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
  Require all granted
</Directory>

Дальше качаем репозиторий:
git clone https://github.com/yagitag/web-l1 l1-alimov
cd alimov-l1
sudo ./install.sh #можно почитать его сначала :)

Открываем бразуер, вбиваем localhost, и все...
