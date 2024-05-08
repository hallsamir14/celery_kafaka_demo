import unittest
from celery import Celery

class TestCelery(unittest.TestCase):
    def test_create_instance(self):
        try:
            app = Celery('my_celery_app', broker='confluentkafka://localhost:9092')
            self.assertIsInstance(app, Celery)
        except Exception as e:
            self.fail(f"Creating Celery instance failed with error {e}")

