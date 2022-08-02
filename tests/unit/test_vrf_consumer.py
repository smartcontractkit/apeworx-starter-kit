from scripts.deploy_vrf_consumer import deploy_vrf_consumer
from scripts.helper_functions import get_account, get_or_deploy_contract
from scripts.create_subscription import create_and_fund

from ape import project


def test_returns_random_number(only_for_local, mocks):
    # Arrange
    account = get_account()
    subscription_id = create_and_fund()
    vrf_consumer = deploy_vrf_consumer(sub_id=subscription_id)
    vrf_coordinator = get_or_deploy_contract("VRFCoordinatorV2")

    # Act
    tx = vrf_consumer.request_random_words(sender=account)
    request_id = int.from_bytes(tx.logs[0]["topics"][2], "big")
    fulfill_tx = vrf_coordinator.fulfillRandomWords(
        request_id, vrf_consumer.address, sender=account
    )

    # Assert
    ## We find 77 in the mock coordinator as a dummy value for the random number
    assert vrf_consumer.random_words(0) == 77
