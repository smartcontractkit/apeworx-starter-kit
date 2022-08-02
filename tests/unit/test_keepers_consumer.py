from scripts.deploy_keepers_consumer import deploy_keepers_consumer
from scripts.helper_functions import get_account


def test_keepers_consumer(only_for_local):
    # Arrange / Act
    keepers_consumer = deploy_keepers_consumer()
    upkeepNeeded, performData = keepers_consumer.checkUpkeep(b"")
    # Assert
    assert isinstance(upkeepNeeded, bool)
    assert isinstance(performData, bytes)
