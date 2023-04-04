import pytest


@pytest.fixture(scope='session')
# scope = session - запускать сессию один раз в пакете тестов (например открыть браузер 1 раз, а не каждый раз на каждый тест)
def browser():
    return 'Chrome'


@pytest.fixture()
def user():
    yield 123
    # после yield код выполняется после тестов
    print('WoWoWoW')
    return 123
    # Id USER


def test_addition(browser, user):
    assert browser == 'Chrome'
    a = 1 + 2
    assert a == 3
