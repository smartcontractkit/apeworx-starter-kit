from ape import config, project, Contract, networks
from scripts.helper_config import network_config
from scripts.helper_functions import (
    get_or_deploy_contract,
    get_account,
)


def create_subscription():
    ecosystem = networks.active_provider.network.ecosystem.name
    chain_name = networks.active_provider.network.name

    if network_config[ecosystem][chain_name].get("subscription_id", False) == False:
        account = get_account()
        vrf_coordinator = get_or_deploy_contract("VRFCoordinatorV2")
        print("Creating subscription...")
        tx = vrf_coordinator.createSubscription(sender=account)
        subscription_id = int.from_bytes(tx.logs[0]["topics"][1], "big")
        print(
            f"Your subscription Id is {subscription_id}. Please save it in your helper_config.py file for network \n{ecosystem}/{chain_name}"
        )
    else:
        subscription_id = network_config[ecosystem][chain_name].get(
            "subscription_id", False
        )
        print(f"You already have subscription {subscription_id}")
    return subscription_id


def fund_subscription(subscription_id=1):
    print("Funding subscription...")
    ecosystem = networks.active_provider.network.ecosystem.name
    chain_name = networks.active_provider.network.name
    account = get_account()
    fund_amount = network_config[ecosystem][chain_name].get("fund_amount", False)
    link_token = get_or_deploy_contract("LinkToken")
    vrf_coordinator = get_or_deploy_contract("VRFCoordinatorV2")
    approve_tx = link_token.approve(
        vrf_coordinator.address, fund_amount, sender=account
    )
    vrf_coordinator.fundSubscription(subscription_id, fund_amount)
    print("Subscription Funded!")


def is_funded(subscription_id):
    ecosystem = networks.active_provider.network.ecosystem.name
    chain_name = networks.active_provider.network.name
    print(f"Getting details for sub_id {subscription_id}...")
    vrf_coordinator = get_or_deploy_contract("VRFCoordinatorV2")
    fund_amount = network_config[ecosystem][chain_name].get("fund_amount", False)
    subscription_details = vrf_coordinator.getSubscription(subscription_id)
    print(f"Subscription details: {subscription_details}")
    if subscription_details[0] >= fund_amount:
        return True
    return False


def create_and_fund():
    subscription_id = create_subscription()
    if not is_funded(subscription_id):
        fund_subscription(subscription_id=subscription_id)
    else:
        print("Already funded!")
    return subscription_id


def main():
    create_and_fund()
