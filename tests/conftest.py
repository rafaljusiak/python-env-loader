import pytest


@pytest.fixture
def env_file(tmp_path):
    file = tmp_path / '.env'
    file.write_bytes(b"""
A=default
BOOL=true
INT=100
FLOAT=1.25
INT_LIST=5,1,2
IP_LIST=127.0.0.1,0.0.0.0,localhost
STRING_LIST=cat,dog,mouse,pig
MIXED_LIST=1,cat,2.5
SINGLE_ELEMENT_LIST=1,
EMPTY_LIST=,
    """)
    yield str(file)


@pytest.fixture
def env_local_file(tmp_path):
    file = tmp_path / '.env.local'
    file.write_bytes(b'A=local')
    yield str(file)
