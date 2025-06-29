import pytest
from script.deploy_favorites import deploy_favorites

@pytest.fixture(scope="session")
def favorites_contract():
    favorites_contract = deploy_favorites()
    return favorites_contract