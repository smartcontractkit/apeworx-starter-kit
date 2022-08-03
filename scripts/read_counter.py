from ape import project, accounts, networks
from scripts.helper_functions import get_account, get_or_deploy_contract


def read_counter():
    account = get_account()
    ecosystem = networks.active_provider.network.ecosystem.name
    chain_name = networks.active_provider.network.name

    keepers_consumer = project.KeepersConsumer.deployments[-1]
    response = keepers_consumer.counter()
    print(f"The current count is {response}")
    return keepers_consumer


def main():
    read_counter()
