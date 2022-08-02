import pytest
from scripts.helper_functions import (
    LOCAL_CHAIN_NAMES,
    get_account,
    deploy_mocks,
)
from ape import networks


@pytest.fixture(scope="session")
def mocks():
    return deploy_mocks()


@pytest.fixture(scope="session")
def owner(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def receiver(accounts):
    return accounts[1]


@pytest.fixture
def sudo(accounts):
    return accounts[-1]


@pytest.fixture
def only_for_local():
    if networks.active_provider.network.name not in LOCAL_CHAIN_NAMES:
        pytest.skip("Only for local testing")


@pytest.fixture
def only_for_testnet():
    if networks.active_provider.network.name in LOCAL_CHAIN_NAMES:
        pytest.skip("Only for testnet testing")


@pytest.fixture
def price_feed_consumer():
    price_feed_consumer = account.deploy(project.PriceConsumer, account)
    # deploy it as fixture
    # Make scripts a built-in fixture. Read in the scripts and do: scripts.deploy_price_consumer
    price_feed_consumer = deploy_price_consumer()
