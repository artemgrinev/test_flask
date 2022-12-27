import sqlite3

import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from db import Session
from generators.generator import generator_user


@pytest.fixture(scope='function')
def driver() -> WebDriver:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()


def _writing_data(data: dict):
    with open("users.json", "a") as write_file:
        json.dump(data, write_file)
        write_file.write('\n')


@pytest.fixture
def writing_data():
    return _writing_data


@pytest.fixture
def generated_valid_data():
    generated_user = next(generator_user())
    name = generated_user.name
    email = generated_user.email
    password = generated_user.password
    return email, name, password


@pytest.fixture
def get_users():
    with open(r'users.json', 'r') as outfile:
        data = [eval(i) for i in outfile]
    return data


@pytest.fixture
def not_valid_email():
    with open(r'not_valid_email.txt', 'r') as outfile:
        data = outfile.read().splitlines()
    return data


@pytest.fixture
def get_db_session():
    """
    Создание сессии для работы с базой данных.
    """
    session = Session()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def create_connection_db():
    return _create_connection


def _create_connection(column, value):
    with sqlite3.connect(r'/home/artemgrinev/PycharmProjects/test_task/data_base/db.sqlite') as connection:
        cursor = connection.cursor()
        cursor.execute(f"select {column} from user where {column} = '{value}'")
        tables = cursor.fetchone()
        return tables[0]




