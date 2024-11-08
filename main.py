import pytest

from logs import configure_logging


if __name__ == "__main__":
    configure_logging()
    pytest.main(["-v", "-s"])
