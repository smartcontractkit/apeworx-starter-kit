from ape import project, accounts, chain, config, networks
from scripts.helper_functions import get_account
from scripts.helper_config import network_config


def deploy_keepers_consumer():
    account = get_account()
    ecosystem = networks.active_provider.network.ecosystem.name
    chain_name = networks.active_provider.network.name

    keepers_consumer = account.deploy(
        project.KeepersConsumer,
        network_config[ecosystem][chain_name]["update_interval"],
    )
    print(f"Keepers Consumer deployed to {keepers_consumer.address}")
    return keepers_consumer


def main():
    deploy_keepers_consumer()
