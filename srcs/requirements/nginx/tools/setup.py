#encoding: UTF-8
#  **************************************************************************  #
#                                                                              #
#                                                          :::      ::::::::   #
#    setup.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahabachi <ahabachi@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/04 01:43:12 by ahabachi          #+#    #+#              #
#    Updated: 2023/05/04 23:38:48 by ahabachi         ###   ########.fr        #
#                                                                              #
#  **************************************************************************  #
#                                                                              #
#   █████████            ██████████         ██████████         ██████████      #
#   ██     ██                    ██                 ██         ██      ██      #
#          ██                    ██                 ██         ██      ██      #
#          ██                    ██                 ██                 ██      #
#          ██            ██████████         ██████████                 ██      #
#          ██                    ██                 ██                 ██      #
#          ██                    ██                 ██                 ██      #
#          ██                    ██                 ██                 ██      #
#       ████████         ██████████         ██████████                 ██      #
#                                                                              #
#  **************************************************************************  #

import os

__dirname__ = __file__[:-len(__file__.split('/')[-1])]

def create_certificates():
	os.system("mkdir -p /etc/nginx/certificates/")
	os.system('''openssl req -newkey rsa:2048 -nodes '''
		'''-keyout /etc/nginx/certificates/ahabachi.42.fr.key -x509 '''
		'''-days 365 -out /etc/nginx/certificates/ahabachi.42.fr.crt '''
		'''-subj "/CN=ahabachi.42.fr"''')

def nginx_config():
	conf = open(__dirname__ + 'nginx-ahabachi.conf').read()
	with open(__dirname__ + 'sites-enabled/default', 'w') as fp:
		fp.write(conf)

def create_default_page():
	if (not os.path.exists('/var/www/html/index.html')):
		os.system("mkdir -p /var/www/html/")
		with open('/var/www/html/index.html', 'w') as fp:
			fp.write("<h1>Hello World!</h1>")
	if (not os.path.exists('/var/www/wordpress/index.php')):
		os.system("mkdir -p /var/www/wordpress/")
		with open('/var/www/wordpress/index.html', 'w') as fp:
			fp.write("<h1>Error Wordpress Not Found!</h1>")
create_certificates()
nginx_config()
create_default_page()
