# from scripts.deploy_vrf_consumer import deploy_vrf_consumer
# from scripts.helper_functions import (
#     get_account,
#     get_or_deploy_contract,
#     listen_for_event,
# )
# from scripts.create_subscription import create_and_fund

# from ape import project


# def test_returns_random_number_staging(only_for_testnet):
#     # Arrange
#     account = get_account()
#     subscription_id = create_and_fund()
#     vrf_consumer = deploy_vrf_consumer()
#     vrf_coordinator = get_or_deploy_contract("VRFCoordinatorV2")

#     # Act
#     tx = vrf_consumer.request_random_words(sender=account)
#     request_id = int.from_bytes(tx.logs[0]["topics"][2], "big")
#     # TODO:
#     # listen_for_event

#     # Assert
