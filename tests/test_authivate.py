import pytest
from authivate import Authivate, AuthivateConfig, AuthivateResponse


@pytest.fixture()
def authivate_instance():
    authivate_config = AuthivateConfig(api_key="your-api-key", project_id="project-id")
    authivate_instance = Authivate(config=authivate_config)

    return authivate_instance


def test_auth_response_is_successful_for_status_code_lt_300():
    response = AuthivateResponse(json_data={}, status_code=201, )

    assert response.was_successful


def test_auth_response_is_unsuccessful_for_status_code_gt_300():
    response = AuthivateResponse(json_data={}, status_code=400, )

    assert not response.was_successful
