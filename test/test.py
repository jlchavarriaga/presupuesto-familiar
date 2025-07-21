import pytest
from app import create_app, db

@pytest.fixture
def app():
    app = create_app('config.Config')
    with app.app_context():
        yield app

def test_db_connection(app):
    with app.app_context():
        try:
            db.session.execute('SELECT 1')
            assert True
        except Exception as e:
            pytest.fail(f"Error de conexión a la BD: {e}")


            #pytest tests/test_db.py -v