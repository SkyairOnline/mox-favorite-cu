from src import favorites
from moccasin.boa_tools import VyperContract

def deploy_favorites() -> VyperContract:
    favorites_contract: VyperContract = favorites.deploy()
    starting_number: int = favorites_contract.retrieve()
    print(f"Starting number: {starting_number}")

    favorites_contract.store(10)
    updated_number: int = favorites_contract.retrieve()
    print(f"Updated number: {updated_number}")
    return favorites_contract
          
def moccasin_main() -> VyperContract:
    deploy_favorites()