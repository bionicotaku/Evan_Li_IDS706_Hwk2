install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py 

lint:
	ruff check *.py mylib/*.py

run:
	python main.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile
	
push:
	git config --global user.email "action@github.com" &&\
		git config --global user.name "GitHub Action" &&\
		git add . &&\
		git commit -m "Update" &&\
		git push

all: install test lint format run push
