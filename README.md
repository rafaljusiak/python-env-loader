# python-env-loader
[![PyPI version](https://badge.fury.io/py/python-env-loader.svg)](https://badge.fury.io/py/python-env-loader)
[![Coverage Status](https://coveralls.io/repos/github/rafaljusiak/python-env-loader/badge.svg?branch=master)](https://coveralls.io/github/rafaljusiak/python-env-loader?branch=master)
[![Build Status](https://travis-ci.com/rafaljusiak/python-env-loader.svg?branch=master)](https://travis-ci.com/rafaljusiak/python-env-loader)

Reads the variables from `.env` files in similar way that is used in 
[React.js](https://create-react-app.dev/docs/adding-custom-environment-variables/#what-other-env-files-can-be-used) 
and adds them to environment variables, automatically guessing and parsing to correct types in 
Python. It is great for managing app settings during development, tests and in production 
without writing additional configuration, and to hold settings separated by 
environment type clearly in a one place. 


## Usage

Call `load_env` on the application start, and it will load environment variables from a 
certain set of `.env` files in the selected directory and return and `EnvFile` object.
After that, you can get values by using `get` method of `EnvFile` object, or by reading it
directly from the environment variables (by using `os.environ`).

Example `.env` file looks like this:

```shell script
SECRET_KEY=test-secret-key.123
EXTERNAL_API_URL=api.example.com
EXTERNAL_API_KEY=this-is-external-api-key
DEBUG=true
ALLOWED_HOSTS=127.0.0.1:8000,0.0.0.0:8000,localhost:8000
```

## Getting started

### Installation

Install the latest version with:

```shell script
pip install -U python-env-loader
```


### First steps
Assuming you have created the `.env` and `.env.local` files inside your project root directory:

    .
    ├── .env
    └── .env.local
    
And they have the following content:
```shell script 
# .env
DEBUG=false  # maps to False in python
ALLOWED_HOSTS=,  # maps to empty list []
```

```shell script 
# .env.local
DEBUG=true  # maps to True in python
ALLOWED_HOSTS=127.0.0.1:8000,0.0.0.0:8000,localhost:8000  # maps to list [127.0.0.1:8000, 0.0.0.0:8000, localhost:8000]
```

Add the following code to your settings module - for example `settings.py` in Django:

```python
# settings.py
from env_loader import load_env
env = load_env()  # if env files are in your root directory of the project
```

or:
```python
# settings.py
from env_loader import load_env
env = load_env("/app")  # if your env file is stored in /app directory
```

Parsed key/value pairs from the `.env` and `.env.local` files are now accessible in `env` object:
```python
# settings.py
env.get("DEBUG")  # returns True, because .env.local file has higher priority
env.get("IS_TEST_ENV", False)  # returns False, because this key is not present in any env file
```

or you can use them as system environment variable and they can be conveniently accessed 
via `os.getenv()`, but then every value is received as a string:

```python
# settings.py
import os
DEBUG = os.getenv("DEBUG")  # returns "true" AS A STRING
```

### Automatic parsing
`python-env-loader` automatically guesses the Python type of the environment variable. If a variable consists 
only of digits, it assumes that it's an integer. If a value consists only of a digits and has a one dot, then
it's treated as a float.

More custom parsing:

|Python value|.env value|
|------------|----------|
|True | true, True, y, yes |
|False | false, False, n, no |
|None | null, None |

Empty string is mapped to `None`.

You can disable automatic parsing by passing `auto_parse=False` to `load_env` function:

```python
from env_loader import load_env, EnvTypes
env = load_env(auto_parse=False)
```

### Switching between setups
When you're loading your env settings, you can switch between 4 of a different setups of them: 
`default`, `development`, `production`  and `test`. By default, `default` is used, but you can
select different setup by passing a value to `env_type` argument of `load_env` function:

```python
from env_loader import load_env, EnvTypes
env = load_env(env_type=EnvTypes.DEVELOPMENT_ENV)
``` 

### Files hierarchy 

For each setup, files on the left have more priority than files on the right:

- default: `.env.local`, `.env`
- development: `.env.development.local`, `.env.development`, `.env.local`, `.env`
- production: `.env.production.local`, `.env.production`, `.env.local`, `.env`
- test: `.env.test.local`, `.env.test`, `.env` (note `.env.local` is missing)
