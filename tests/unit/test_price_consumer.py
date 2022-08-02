from scripts.deploy_price_feed_consumer import deploy_price_consumer
from scripts.helper_functions import get_account


def test_price_consumer(only_for_local, mocks):
    # Arrange / Act
    price_feed_consumer = deploy_price_consumer()
    # Assert
    value = price_feed_consumer.get_latest_price()
    assert value > 0
    assert isinstance(value, int)
