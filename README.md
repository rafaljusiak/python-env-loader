# python-env-loader


Reads the variables from `.env` files in similar way that is used in 
[React.js](https://create-react-app.dev/docs/adding-custom-environment-variables/#what-other-env-files-can-be-used) 
and adds them to environment variables, automatically guessing and parsing to correct types in 
Python. It is great for managing app settings during development, tests and in production 
without writing additional configuration, and to hold settings separated by 
environment type clearly in a one place. 


## Example usages

Call `load_env` on the application start, and it will load environment variables from a 
certain set of `.env` files in the selected directory and return and `EnvFile` object.
After that, you can get values by using `get` method of `EnvFile` object, or by reading it
directly from the environment variables (by using `os.environ`).

Example `.env` file looks like this:

```shell script
DOMAIN=example.com
DEBUG=true
ALLOWED_HOSTS=127.0.0.1:8000,0.0.0.0:8000,localhost:8000
```

## Getting started

Install the latest version with:

```shell script
pip install -U python-env-loader
```

Assuming you have created the `.env` and `.env.local` files inside your project root directory:

    .
    ├── .env
    └── .env.local

Add the following code to your settings module - for example `settings.py` in Django:
# TODO add .env and .env.local examples and write more about example usage

```python
# settings.py
from env_loader import load_env
env = load_env()
```

At this point, parsed key/value from the `.env` file is now present as
system environment variable and they can be conveniently accessed via
`os.getenv()`:

```python
# settings.py
import os
SECRET_KEY = os.getenv("EMAIL")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
```

## Files hierarchy 

For each setup, files on the left have more priority than files on the right:

- default: `.env.local`, `.env`
- development: `.env.development.local`, `.env.development`, `.env.local`, `.env`
- production: `.env.production.local`, `.env.production`, `.env.local`, `.env`
- test: `.env.test.local`, `.env.test`, `.env` (note `.env.local` is missing)
