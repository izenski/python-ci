# python-ci
This is a DevOps Best Practices Repo

## Create a virtual environment
* run `virtualenv ~/.venv`
* run `source ~/.venv/bin/activate`

### optional update ~/.bashrc
/# at the end of the file:
echo "sourcing VENV"
source  ~/.venv/bin/activate

## Create a scaffold 
* `requirements.txt`
* `Makefile`: Cookbook that runs commands
* `hello/py`: Code
* `test_hello.py`: Test Code

Also include build server YAML files:
* GitHub Actions Config files

## running the program
$ ./app.py

## running tests
$ make test

## lint the program
$ make lint
