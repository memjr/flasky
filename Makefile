update-deps:
	pip-compile --upgrade
	pip-compile --upgrade --output-file dev-requirements.txt dev-requirements.in
	pip install --upgrade -r requirements.txt -r dev-requirements.txt

install:
	pip install --editable .

install_dev:
	pip install --editable .[dev]

init:
	pip install --upgrade pip setuptools wheel
	pip install pip-tools
	rm -rf .tox
	echo '{"extends": "stylelint-config-standard"}' > ./.stylelintrc.json

update:  init update-deps install_dev

remove_venv:
	@if [ -d "./venv" ]; then rm -rf venv; fi

create_venv:
	python3.8 -m venv venv
	clear
	@echo "\n\n ***** Now execute 'source ./venv/bin/activate && make update' *****\n\n"

setup: remove_venv create_venv

.PHONY: update-deps init update install_dev


INVENV=$(python -c 'import sys; print ("1" if hasattr(sys, "real_prefix") else "0")')