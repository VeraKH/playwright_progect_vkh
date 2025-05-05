import pytest

#A helper test that only calls the store_authenticated_state fixture
# in order to save the session to a JSON file once.
@pytest.mark.asyncio
async def test_generate_customer01_auth_session(store_authenticated_state):
    pass
