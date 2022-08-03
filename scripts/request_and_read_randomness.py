from ape import project, accounts, networks
from scripts.helper_functions import get_account, get_or_deploy_contract
import time


def request_and_read_randomness():
    account = get_account()
    ecosystem = networks.active_provider.network.ecosystem.name
    chain_name = networks.active_provider.network.name

    vrf_consumer = project.VRConsumerV2.deployments[-1]
    request_tx = vrf_consumer.request_random_words(sender=account)

    print("Request sent! Let's wait for a response...")

    randomness = wait_for_randomness(vrf_consumer)
    if randomness:
        print(f"The random number was {randomness}")
    else:
        print("No random number found")


def wait_for_randomness(vrf_consumer, timeout=200, poll_interval=2):
    print("Waiting for random response...")
    start_time = time.time()
    current_time = time.time()
    while current_time - start_time < timeout:
        response = vrf_consumer.random_words(0)
        if response > 0:
            return response
        time.sleep(poll_interval)
        current_time = time.time()
    print("Done waiting!")
    return None


def main():
    request_and_read_randomness()
