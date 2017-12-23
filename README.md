# Tools for Python-Phabricator

### Requirements

Install python-phabricator as such:

```
cd ~
git clone https://github.com/helgemathee/python-phabricator
cd python-phabricator
python setup.py install
```

### Usage

Refer to the documentation at https://github.com/helgemathee/python-phabricator

For automatic authentification you need to setup a file in you home folder called

`~/.arcrc`

with content similar to this: 

```
{

    "hosts": 
    {
        "https://MYDOMAIN/api/":
        {
            "user": "MYBOTUSER",
            "token": "MYAPITOKEN"
        }
    }
}
```

The accessible API can be inspected on your phabricator site - in the conduit application. (https://MYDOMAIN/conduit)