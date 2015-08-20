install:
	pip install -r www/deploy/requirements.txt --use-mirrors
	www/manage.py syncdb --noinput
	www/manage.py migrate
	www/manage.py loaddata www/fixtures/auth.json

.PHONY: install

