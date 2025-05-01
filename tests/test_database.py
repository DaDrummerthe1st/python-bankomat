import pytest

from database import ConnectDatabase

def test_connect_database():
    db = ConnectDatabase()
    db.connect()
    assert db is True