def test_construction(player_one):
    assert 'Tatiana' == player_one.first_name
    assert 'Jones' == player_one.last_name
    assert [] == player_one.guardians


def test_add_guardian(player_one, guardians):
    player_one.add_guardian(guardians[0])
    assert [guardians[0]] == player_one.guardians


# @pytest.mark.skip(reason='Have not implemented method')
def test_add_guardians(player_one, guardians):
    # Add one guardian
    player_one.add_guardian(guardians[0])
    # Later, add some more
    player_one.add_guardians((guardians[1], guardians[2]))
    assert list(guardians) == player_one.guardians


# @pytest.mark.skip()
def test_primary_guardian(player_one, guardians):
    assert player_one.primary_guardian
    # Add one guardian
    player_one.add_guardian(guardians[0])
    # Later, add some more
    player_one.add_guardians((guardians[1], guardians[2]))
    assert guardians[0] == player_one.primary_guardian
