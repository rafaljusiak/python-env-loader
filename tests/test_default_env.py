from src.env_loader import load_env, EnvTypes


def test_local_is_overriding_base_env(tmp_path, env_file, env_local_file):
    env = load_env(env_type=EnvTypes.DEFAULT_ENV, dir_path=tmp_path, raise_file_not_found=True)
    v = env.get("A")
    assert v == "local"


def test_return_default_value_when_key_is_missing(tmp_path, env_file):
    env = load_env(env_type=EnvTypes.DEFAULT_ENV, dir_path=tmp_path)
    v = env.get("B", "default_value")
    assert v == "default_value"


def test_return_bool(tmp_path, env_file):
    env = load_env(env_type=EnvTypes.DEFAULT_ENV, dir_path=tmp_path)
    v = env.get("BOOL")
    assert type(v) is bool
    assert v is True


def test_return_int(tmp_path, env_file):
    env = load_env(env_type=EnvTypes.DEFAULT_ENV, dir_path=tmp_path)
    v = env.get("INT")
    assert type(v) is int
    assert v == 100


def test_return_float(tmp_path, env_file):
    env = load_env(env_type=EnvTypes.DEFAULT_ENV, dir_path=tmp_path)
    v = env.get("FLOAT")
    assert type(v) is float
    assert v == 1.25


def test_return_int_list(tmp_path, env_file):
    env = load_env(env_type=EnvTypes.DEFAULT_ENV, dir_path=tmp_path)
    v = env.get("INT_LIST")
    assert type(v) is list
    assert v == [5, 1, 2]


def test_return_ip_list(tmp_path, env_file):
    env = load_env(env_type=EnvTypes.DEFAULT_ENV, dir_path=tmp_path)
    v = env.get("IP_LIST")
    assert type(v) is list
    assert v == ["127.0.0.1", "0.0.0.0", "localhost"]


def test_return_string_list(tmp_path, env_file):
    env = load_env(env_type=EnvTypes.DEFAULT_ENV, dir_path=tmp_path)
    v = env.get("STRING_LIST")
    assert type(v) is list
    assert v == ["cat", "dog", "mouse", "pig"]


def test_return_mixed_list(tmp_path, env_file):
    env = load_env(env_type=EnvTypes.DEFAULT_ENV, dir_path=tmp_path)
    v = env.get("MIXED_LIST")
    assert type(v) is list
    assert v == [1, "cat", 2.5]


def test_return_single_element_list(tmp_path, env_file):
    env = load_env(env_type=EnvTypes.DEFAULT_ENV, dir_path=tmp_path)
    v = env.get("SINGLE_ELEMENT_LIST")
    assert type(v) is list
    assert v == [1]


def test_return_empty_list(tmp_path, env_file):
    env = load_env(env_type=EnvTypes.DEFAULT_ENV, dir_path=tmp_path)
    v = env.get("EMPTY_LIST")
    assert type(v) is list
    assert v == []


def test_auto_parse_false_is_not_parsing(tmp_path, env_file):
    env = load_env(env_type=EnvTypes.DEFAULT_ENV, dir_path=tmp_path, auto_parse=False)
    v = env.get("EMPTY_LIST")
    assert type(v) is str
    assert v == ","


def test_iterator(tmp_path, env_file):
    keys = ['A', 'BOOL', 'INT', 'FLOAT', 'INT_LIST', 'IP_LIST',
            'STRING_LIST', 'MIXED_LIST', 'SINGLE_ELEMENT_LIST',
            'EMPTY_LIST']
    env = load_env(env_type=EnvTypes.DEFAULT_ENV, dir_path=tmp_path)
    for k, v in env:
        assert k in keys
        assert v is not None
