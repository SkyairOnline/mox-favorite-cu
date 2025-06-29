from src import favorites, favorites_factory, five_more
from moccasin.boa_tools import VyperContract

def deploy_fav() -> VyperContract:
    favorites_contract: VyperContract = favorites.deploy()
    return favorites_contract

def deploy_factory(favorites_contract: VyperContract):
    factory_contract: VyperContract = favorites_factory.deploy(favorites_contract.address)
    factory_contract.create_favorites_contract()

    new_favorites_address: str = factory_contract.list_of_favorite_contracts(0)
    new_favorites_contract: VyperContract = favorites.at(new_favorites_address)
    new_favorites_contract.store(77)
    print(f"Store value is: {new_favorites_contract.retrieve()}")

    factory_contract.store_from_factory(0, 88)
    print(f"New contract stored value is: {new_favorites_contract.retrieve()}")
    print(f"Original contract stored value is: {favorites_contract.retrieve()}")

def deploy_five_more():
    five_more_contract = five_more.deploy()
    five_more_contract.store(99)
    print(five_more_contract.retrieve())
          
def moccasin_main() -> VyperContract:
    favorites_contract = deploy_fav()
    deploy_factory(favorites_contract)
    deploy_five_more()