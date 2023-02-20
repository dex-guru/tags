import json
from pathlib import Path

import pytest
from jsonschema import validate

SCHEMA_NAME = 'tokenlist.schema.json'


@pytest.fixture()
def get_schema():
    with open(f'tests/{SCHEMA_NAME}') as f:
        return json.load(f)


@pytest.mark.parametrize('file', Path(Path(Path().root, 'tokens')).glob('*.json'))
def test_token_list_schema(file, get_schema):
    with open(file) as f:
        token_list = json.load(f)
        validate(token_list, get_schema)


@pytest.mark.parametrize('file', Path(Path(Path().root, 'tokens')).glob('*.json'))
def test_token_tag_in_tags_list(file):
    """Check that all tokens in the list have a tag in the tags list."""
    with open(file) as f:
        token_list = json.load(f)
        for token in token_list['tokens']:
            for tag in token['tags']:
                assert tag in token_list['tags']


@pytest.mark.parametrize('file', Path(Path(Path().root, 'accounts')).glob('*.json'))
def test_account_tags_list_schema(file, get_schema):
    with open(file) as f:
        tags_list = json.load(f)
        validate(tags_list, get_schema)


@pytest.mark.parametrize('file', Path(Path(Path().root, 'accounts')).glob('*.json'))
def test_account_tag_in_tags_list(file):
    """Check that all conditions in the list have a tag in the tags list."""
    with open(file) as f:
        tags_list = json.load(f)
        for condition in tags_list['conditions']:
            assert condition['tag'] in tags_list['tags']


@pytest.mark.parametrize('file', Path(Path(Path().root, 'accounts')).glob('*.json'))
def test_account_tag_params_have_network(file):
    """Check that all conditions in the list have a network param."""
    with open(file) as f:
        tags_list = json.load(f)
        for condition in tags_list['conditions']:
            for param in condition['params']:
                if param['name'] == 'network':
                    break
            else:
                assert False, 'No network param in condition'

