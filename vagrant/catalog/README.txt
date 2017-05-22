This is for catalog CRUD project. And with social login for authentication.

Pre-install Package

	Please check the package with pg_config.sh

Pre-setup catalog.db

	1. run application_database_setup.py
	2. run application_lotsofitem.py

Get Social Credential And Save to JSON
	1. Google
		1) visit https://console.developers.google.com
		2) make OAuth 2.0 client ID, download and rename to g_client_secrets.json
	2. Fackebook
		1) visit https://developers.facebook.com
		2) make a web app, get a app id & secret code, save to fb_client_secrets.json

Access to Local Web Server

	1. run application.py
	2. Open browser and access to http://localhost:8000
