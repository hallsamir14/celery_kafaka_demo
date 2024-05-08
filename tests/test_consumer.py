import sys
sys.path.append("/home/hallwork/webApps")
from celery_kafaka_demo.kafka_consumer.consumer import consume_messages
import time
def test_consume_messages():
    assert True