import pytest

from logs import configure_logging


if __name__ == "__main__":
    configure_logging()

    parameters = ["-v", "-s"]
    pytest.main(parameters)
