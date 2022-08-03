from ape import project, accounts, networks
from scripts.helper_functions import get_account, get_or_deploy_contract


def read_price_feed():
    account = get_account()
    ecosystem = networks.active_provider.network.ecosystem.name
    chain_name = networks.active_provider.network.name

    price_feed_consumer = project.PriceConsumer.deployments[-1]
    response = price_feed_consumer.get_latest_price()
    print(f"The current price of ETH is {response}")
    return price_feed_consumer


def main():
    read_price_feed()
