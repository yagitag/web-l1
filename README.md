# web-l1

Для начала надо поставить LAMP сервер:

<code>
  sudo apt-get install tasksel
  sudo tasksel install lamp-server
</code>

Потом правим /etc/apache2/apache2.conf, для того чтобы можно было запускать cgi скрипты. Дописываем туда:

<code>
  ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
  <Directory "/usr/lib/cgi-bin">
    AllowOverride None
    Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
    Require all granted
  </Directory>
</code>

Дальше качаем репозиторий:

<code>
  git clone https://github.com/yagitag/web-l1 l1-alimov
  cd alimov-l1
  sudo ./install.sh #можно почитать его сначала :)
</code>

Открываем бразуер, вбиваем localhost, и все...
