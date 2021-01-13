import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='python-env-loader',
    version='0.0.2',
    author="Rafał Jusiak",
    author_email="kontakt@rafaljusiak.pl",
    description="Reads the variables from .env files and adds them to environment, also automatically guesses and parses to correct types in Python. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafaljusiak/python-env-loader",
    packages=["env_loader"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
