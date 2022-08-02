from ape import project, accounts, chain, config, networks
from scripts.helper_functions import get_account, get_or_deploy_contract


def deploy_price_consumer():
    account = get_account()
    ecosystem = networks.active_provider.network.ecosystem.name
    chain_name = networks.active_provider.network.name

    price_feed = get_or_deploy_contract("AggregatorV3Interface")
    price_feed_consumer = account.deploy(project.PriceConsumer, price_feed.address)
    print(f"Price Feed Consumer deployed to {price_feed_consumer.address}")
    return price_feed_consumer


def main():
    deploy_price_consumer()
