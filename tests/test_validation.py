import json

import pytest
from jsonschema import validate
from pathlib import Path

SCHEMA_NAME = 'tokenlist.schema.json'


@pytest.fixture()
def get_schema():
    with open(f'tests/{SCHEMA_NAME}') as f:
        return json.load(f)


@pytest.mark.parametrize('file', Path(Path().root).glob('*.json'))
def test_token_list_schema(file, get_schema):
    with open(file) as f:
        token_list = json.load(f)
        validate(token_list, get_schema)
