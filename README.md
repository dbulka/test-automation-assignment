### Instalation:
Software Requirements: Python 3.7 or later

##### Linux
    $ git clone https://github.com/echoprotocol/pytests.git
    $ virtualenv <ENVIRONMENT_NAME> -p python3.7
    $ source <ENVIRONMENT_NAME>/bin/activate
    $ pip3 install -r requirements.txt

### To run tests you can use following commands in console:
Filter                           | lcc commands
---------------------------------|----------------------
Run all tests                    | $ py.test
Run GUI tests                    | $ py.test -m guitests
Run API tests                    | $ py.test -m apitests
