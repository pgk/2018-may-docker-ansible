

env:
	python3 -m venv env
	env/bin/pip install --upgrade pip
	env/bin/pip install -r requirements.txt

provision: env
	env/bin/ansible-playbook -i hosts docker_provision.yml

.PHONY: provision
