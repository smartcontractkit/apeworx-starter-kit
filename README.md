*Note: This repo has been recently updated to use Goerli.*

# Apeworx (Vyper) Starter Kit

<br/>
<p align="center">
<a href="https://chain.link" target="_blank">
<img src="./img/apeworx-chainlink.png" width="225" alt="Chainlink Apeworx logo">
</a>
</p>
<br/>


This is a repo to work with and use Chainlink smart contracts in a python, [apeworx](https://www.apeworx.io/) & [vyper](https://vyper.readthedocs.io/en/stable/index.html) environment. If you're brand new to Chainlink, check out the beginner walk-through in remix to [learn the basics.](https://docs.chain.link/docs/beginners-tutorial)

It shows how to use the these frameworks and languages as well as the following Chainlink features:
 - [Chainlink Price Feeds](https://docs.chain.link/docs/using-chainlink-reference-contracts)
 - [Chainlink VRF](https://docs.chain.link/docs/chainlink-vrf)
 - [Chainlink Keepers](https://docs.chain.link/docs/chainlink-keepers/introduction/)

# Table of Contents

- [Apeworx (Vyper) Starter Kit](#apeworx-vyper-starter-kit)
- [Table of Contents](#table-of-contents)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Quickstart](#quickstart)
- [Usage](#usage)
  - [Deploying Contracts](#deploying-contracts)
    - [Price Feed Consumer](#price-feed-consumer)
    - [Keepers Consumer](#keepers-consumer)
    - [VRFv2 Consumer](#vrfv2-consumer)
  - [Deploying to Local, Adhoc, Mainnet, and Testnets](#deploying-to-local-adhoc-mainnet-and-testnets)
    - [Importing an account](#importing-an-account)
    - [Deploy to a local or adhoc network](#deploy-to-a-local-or-adhoc-network)
    - [Deploy to a mainnet or test network](#deploy-to-a-mainnet-or-test-network)
    - [Interacting with Contracts](#interacting-with-contracts)
      - [Price Feed Consumer](#price-feed-consumer-1)
      - [VRF Consumer](#vrf-consumer)
      - [Keeper Consumer](#keeper-consumer)
- [Miscellaneous](#miscellaneous)
  - [Contributing](#contributing)
  - [Resources](#resources)

# Getting Started

It's recommended that you've gone through the [apeworx getting started documentation](https://docs.apeworx.io/ape/stable/userguides/quickstart.html) before proceeding here. 

## Requirements

- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  - You'll know you did it right if you can run `git --version` and you see a response like `git version x.x.x`
- [Python](https://www.python.org/downloads/)
  - You'll know you've installed python right if you can run:
    - `python --version` or `python3 --version` and get an ouput like: `Python x.x.x`
- [pipx](https://pypa.github.io/pipx/installation/)
  - `pipx` is different from [pip](https://pypi.org/project/pip/)
  - You may have to close and re-open your terminal 
  - You'll know you've install it right if you can run:
    - `pipx --version` and see something like `x.x.x.x`
- [eth-ape (ape)](https://docs.apeworx.io/ape/stable/userguides/quickstart.html#installation)
  - We recommend using `pipx` but you can [follow the ape documentation](https://docs.apeworx.io/ape/stable/userguides/quickstart.html#installation) for other installation methods.
  - You'll know you've done it right if you run `ape --version` and see an output like `x.x.x`

## Quickstart

1. Clone repo and install dependencies

```bash
git clone https://github.com/smartcontractkit/apeworx-starter-kit
cd apeworx-starter-kit
ape plugins install alchemy vyper
```

2. You're ready to go!


Run tests:

```
ape test
```

# Usage

If you run `ape --help` you'll get an output of all the tasks you can run. 

## Deploying Contracts

The following will deploy your contracts to a temporary ape test network. Additionally, if on a local network, it will deploy mock Chainlink contracts for you to interact with. If you'd like to interact with your deployed contracts, skip down to [Interacting with Deployed Contracts](#interacting-with-deployed-contracts). 

After your script completes, the network deletes itself. 

### Price Feed Consumer

```
ape run scripts/deploy_price_feed_consumer.py
```

### Keepers Consumer

```
ape run scripts/deploy_keepers_consumer.py
```

### VRFv2 Consumer

```
ape run scripts/deploy_vrf_consumer.py
```

## Deploying to Local, Adhoc, Mainnet, and Testnets

In order to deploy to a local, adhoc, mainnet, or testnet , you'll need to first create accounts. For the scripts we currently have, it'll default to the "default" account. If you'd like to have the scripts point to a different account, go to `helper_functions.py` and change the `get_account` function to look for you account instead of `default. 

Ape doesn't support `.env` files or keeping your private keys in plaintext, which means it's harder for you to release your private key to the world!

### Importing an account

To import an account into ape, run the following:

```
ape accounts import default
```

Where `default` will be the name of your account. Ape will then prompt you for your private key and password, and encrypt it on your computer. The only way to use this key moving forward will be to decrypt the key with your password. 

### Deploy to a local or adhoc network

Ape doesn't come with a built in local network like hardhat or ganache, so we will have to use our own. Ape also prefers users to build plugins for working additional networks, [you can find a list of the plugins on their github.](https://github.com/ApeWorX?q=ape-&type=all&language=&sort=)

We recommend using [Foundry's Anvil](https://book.getfoundry.sh/anvil/) as your local network. 

1. Install Foundry / Anvil

You'll know you did it right if you can run `anvil --version` and get an output like `anvil 0.1.0 (f016135 2022-07-04T00:15:02.655418Z)`

2. Start up anvil

Run:

```
anvil
```

You'll see an output with many private keys. 

If you'd like to use this as your main "default" account, run the following:

```
ape accounts delete default
```
And then, re-import your private key from anvil by following [the importing an account guide](#importing-an-account)

3. Run your script 

> Note: This will only work since the chain Id is `31337` for anvil! For working with non-local networks, please see [Deploy to a mainnet or testnet](#deploy-to-a-main-or-test-network)

```
ape run scripts/deploy_price_feed_consumer.py --network http://127.0.0.1:8545
```

You'll be prompted for your password. 


### Deploy to a mainnet or test network

1. Import an account

Please see [import an account](#importing-an-account). And be sure your account has plenty of testnet or mainnet tokens if working on live network. See [this faucet](https://faucets.chain.link/) for testnet tokens. 

2.  Set your RPC_URL

Since we are working with Alchemy, create an [environment variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html) called `WEB3_ALCHEMY_PROJECT_ID` or `WEB3_ALCHEMY_API_KEY`. If using a linux or mac environment, you can set it by running:

```
export WEB3_ALCHEMY_PROJECT_ID=MY_API_TOKEN
```

> Note: At this time, it's really tricky to change networks with Ape. If you want to use another network ape doesn't have a plugin for, you can use an adhoc network as shown above. 

3. Update your `helper_config.py`

If you're using a network not covered in `helper_config.py` be sure to add it. 

4. Run your script!

```
ape run scripts/deploy_price_feed_consumer.py --network ethereum:goerli:alchemy
```

### Interacting with Contracts

To interact with contracts, we recommend using the console.

```
ape console --network ethereum:goerli:alchemy
```

Or, you can follow along and run the scripts to see the end-to-end functionaltiy.

#### Price Feed Consumer

1. Deploy the contract

```
ape run scripts/deploy_price_feed_consumer.py --network ethereum:goerli:alchemy
```

2. Read it

```
ape run scripts/read_price_feed.py --network ethereum:goerli:alchemy
```



#### VRF Consumer

1. Create subscription and fund it with LINK.

You can do that with the script, or going to the UI at [vrf.chain.link](https://vrf.chain.link)

```
ape run scripts/create_subscription.py --network ethereum:goerli:alchemy
```

2. Update your `helper_config.py` with your subscription Id. 

3. Deploy vrf consumer

```
ape run scripts/deploy_vrf_consumer.py --network ethereum:goerli:alchemy
```

4. [Add your contract/consumer to the VRF UI](https://docs.chain.link/docs/get-a-random-number/#create-and-fund-a-subscription)


5. Request a random number and wait for a response


```
ape run scripts/request_and_read_randomness.py --network ethereum:goerli:alchemy
```

#### Keeper Consumer

1. Deploy the contract

```
ape run scripts/deploy_keepers_consumer.py --network ethereum:goerli:alchemy
```

2. Register your upkeep on the Keepers UI

You can go to [keepers.chain.link](https://keepers.chain.link/new-custom-logic)

3. Watch for your counter to automatically start going up!

After a delay, run:

```
ape run scripts/read_counter.py --network ethereum:goerli:alchemy
```

And it should be updated!




# Miscellaneous

1. Testing and forking is a bit tricky at the moment. 


## Contributing

Contributions are always welcome! Open a PR or an issue!

Thank You!

## Resources

- [Chainlink Documentation](https://docs.chain.link/)
- [Ape Documentation](https://docs.apeworx.io/ape/stable/)
