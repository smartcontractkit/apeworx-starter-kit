from ape import networks, accounts, project, config, Contract

# All local chains across "ecosystems" have the same name
LOCAL_CHAIN_NAMES = ["local", "development"]
FORKED_CHAIN_NAMES = ["mainnet-fork"]

CONTRACT_NAME_TO_MOCK = {
    "AggregatorV3Interface": project.MockV3Aggregator,
    "VRFCoordinatorV2": project.VRFCoordinatorV2Mock,
    "LinkToken": project.LinkToken,
}

## Mock Contract Initial Values
DECIMALS = 18
INITIAL_VALUE = 2000_000000000000000000
BASE_FEE = 1_00000000000000000  # 0.1
GAS_PRICE_LINK = 1_000000000  # Some value calculated depending on the Layer 1 cost and Link. This is 1e9


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if networks.active_provider.network.name in LOCAL_CHAIN_NAMES:
        return accounts.test_accounts[0]
    if networks.active_provider.chain_id == 31337:
        return accounts.load("local-default")
    return accounts.load("default")


def main():
    pass


def deploy_mocks():
    """
    Deploys mock contracts to a local network. Should take care to make sure you
    only call this function when running on a local network.
    """
    print(f"The active network is {networks.active_provider.network.name}")
    print("Deploying mocks...")
    account = get_account()
    print("Deploying mock v3 aggregator...")
    mock_price_feed = account.deploy(project.MockV3Aggregator, DECIMALS, INITIAL_VALUE)
    print(f"Deployed to {mock_price_feed.address}")

    print("Deploying mock VRF coordinator...")
    mock_vrf_coordinator = account.deploy(
        project.VRFCoordinatorV2Mock, BASE_FEE, GAS_PRICE_LINK
    )
    print(f"Deployed to {mock_vrf_coordinator.address}")
    print("Mocks Deployed!")


def get_or_deploy_contract(contract_name):
    """If you want to use this function, go to the ape config and add a new entry for
    the contract that you want to be able to 'get'. Then add an entry in the variable 'CONTRACT_NAME_TO_MOCK'.
    You'll see examples like the 'price_feed'.
        This script will then either:
            - Get a address from the config
            - Or deploy a mock to use for a network that doesn't have it

        Args:
            contract_name (name of ape.contracts.base.ContractContainer): This is the name that is referred to in the
            'CONTRACT_NAME_TO_MOCK' variable. It could be something like `project.AggregatorV3Interface`. It takes
            a contract or deployment on a real chain, and gets the mock version of it.

        Returns:
            contract
    """
    mock_contract_type = CONTRACT_NAME_TO_MOCK[contract_name]
    if (
        networks.active_provider.network.name in LOCAL_CHAIN_NAMES
        or networks.active_provider.chain_id == 31337
    ):
        if len(mock_contract_type.deployments) <= 0:
            deploy_mocks()
        contract = mock_contract_type.deployments[-1]
    else:
        try:
            ecosystem = networks.active_provider.network.ecosystem.name
            chain_name = networks.active_provider.network.name
            contract_addresses = [
                contract_and_address["address"]
                for contract_and_address in config.deployments[ecosystem][chain_name]
                if contract_and_address["contract_type"] == contract_name
            ]
            contract = mock_contract_type.at(contract_addresses[0])
        except KeyError:
            raise Exception(
                f"{networks.active_provider.network.name} address not found, perhaps you should add it to the ape-config.yaml or CONTRACT_NAME_TO_MOCK in the helper_functions.py file?"
            )
    return contract


def listen_for_event(ape_contract, event, timeout=200, poll_interval=2):
    """Listen for an event to be fired from a contract.
    We are waiting for the event to return, so this function is blocking.

    Args:
        ape_contract ([ape.contracts.base.ContractInstance]):
        An ape contract of some kind.

        event ([string]): The event you'd like to listen for.

        timeout (int, optional): The max amount in seconds you'd like to
        wait for that event to fire. Defaults to 200 seconds.

        poll_interval ([int]): How often to call your node to check for events.
        Defaults to 2 seconds.
    """
    # TODO
    pass
