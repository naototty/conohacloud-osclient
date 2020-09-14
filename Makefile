
py37:
	pip3.7 install -r pip-freeze-centos7-py36.txt --use-feature=2020-resolver

wsl1-py37:
	pip3.7 install -r pip-freeze-ubuntu16-py37.txt --use-feature=2020-resolver

novassh:
	curl -sL https://github.com/hironobu-s/novassh/releases/download/current/novassh-linux.amd64.gz | zcat > novassh && chmod +x ./novassh
