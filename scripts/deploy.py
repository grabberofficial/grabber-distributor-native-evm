from brownie import chain
from brownie import accounts, network, config, DistributorNativeFactory

DEPLOYER = (0, "deployer_pk")

def set_distribution_parameters(distributor, admin, token, owner):
    amount_of_tokens_to_distribute = 100 * 10e18

    distributor.setDistributionParameters(
        amount_of_tokens_to_distribute,
        100,
        owner,
        token,
        { "from": admin })

def set_distribution_round(distributor, admin):
    registration_round_enddate = distributor.registrationRound()[1]
    
    distribution_startdate = registration_round_enddate + 60 * 60 * 24
    distribution_enddate = distribution_startdate + 60 * 60 * 24

    chain.sleep(60 * 60)

    distributor.setDistributionRound(distribution_startdate, distribution_enddate, { "from": admin })

def set_registration_round(distributor, admin):
    start_date = chain.time()
    end_date = start_date + 60 * 60 * 24
    # chain.sleep(60 * 60)

    distributor.setRegistrationRound(start_date, end_date, { "from": admin })

def deploy_factory(deployer):
    contract = DistributorNativeFactory.deploy({ "from": deployer })

    return contract

def get_account(account):
    dev_index = account[0]
    private_key = account[1]

    if network.show_active() == "development":
        return accounts[dev_index]
    else:
        return accounts.add(config["addresses"][private_key])


def deploy(deployer):
    deploy_factory(deployer)


def main():
    deployer = get_account(DEPLOYER)
    deploy(deployer)
