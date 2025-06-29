def test_starting_values(favorites_contract):
    assert favorites_contract.retrieve() == 10

def test_can_change_values(favorites_contract):
    # Act
    favorites_contract.store(20)
    # Assert
    assert favorites_contract.retrieve() == 20

def test_can_add_people(favorites_contract):
    # Arrange
    new_person = "Alice"
    favorite_number = 10
    # Act
    favorites_contract.add_person(new_person, favorite_number)
    # Assert
    assert favorites_contract.list_of_people(0) == (favorite_number, new_person)