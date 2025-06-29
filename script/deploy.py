from src import favorites

def deploy_favorites():
    favorites_contract = favorites.deploy()
    starting_number = favorites_contract.retrieve()
    print(f"Starting number: {starting_number}")

    favorites_contract.store(10)
    updated_number = favorites_contract.retrieve()
    print(f"Updated number: {updated_number}")
    return favorites_contract
          
def moccasin_main():
    deploy_favorites()