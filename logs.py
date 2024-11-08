import logging


def configure_logging():
    """Sets up a basic config for the logging to use a given message format, date and
    level.
    """
    formatter = (
        "[%(asctime)s.%(msecs)03d][%(levelname)s][%(module)s]"
        "[%(funcName)s]: %(message)s"
    )
    date_format = "%H:%M:%S"
    logging.basicConfig(datefmt=date_format, format=formatter, level=logging.INFO)
