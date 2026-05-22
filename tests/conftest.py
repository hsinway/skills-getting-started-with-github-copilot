import copy
import pytest
from fastapi.testclient import TestClient
import src.app as app_module

# Save initial snapshot to restore between tests
ORIGINAL_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(scope="session")
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities():
    # Arrange: restore activities to original snapshot before each test
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))
    yield