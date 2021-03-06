import pytest
import os
import tempfile

import pytest
# from src.app import create_app
# from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

# @pytest.fixture
# def app():
#     db_fd, db_path = tempfile.mkstemp()

#     app = create_app({
#         'TESTING': True,
#         'DATABASE': db_path,
#     })

#     # with app.app_context():
#     #     init_db()
#     #     get_db().executescript(_data_sql)

#     yield app

#     # os.close(db_fd)
#     # os.unlink(db_path)

def pytest_addoption(parser):
    # ability to test API on different hosts
    parser.addoption("--host", action="store", default="http://localhost:5000")

@pytest.fixture(scope="session")
def host(request):
    return request.config.getoption("--host")

@pytest.fixture(scope="session")
def api_v1_host(host):
    return os.path.join(host, "api", "v1")