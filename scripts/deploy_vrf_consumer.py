from ape import project, accounts, networks
from scripts.helper_functions import get_account, get_or_deploy_contract
from scripts.helper_config import network_config


def deploy_vrf_consumer(sub_id=None):
    account = get_account()
    ecosystem = networks.active_provider.network.ecosystem.name
    chain_name = networks.active_provider.network.name

    vrf_coordinator = get_or_deploy_contract("VRFCoordinatorV2")
    sub_id = (
        sub_id if sub_id else network_config[ecosystem][chain_name]["subscription_id"]
    )
    vrf_consumer = account.deploy(
        project.VRFConsumerV2,
        sub_id,
        vrf_coordinator.address,
        network_config[ecosystem][chain_name]["key_hash"],
    )
    return vrf_consumer


def main():
    deploy_vrf_consumer()
