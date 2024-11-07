import logging


def configure_logging():
    formatter = (
        "[%(asctime)s.%(msecs)03d][%(levelname)s][%(module)s]"
        "[%(funcName)s][%(lineno)d]: %(message)s"
    )
    date_format = "%H:%M:%S"
    logging.basicConfig(datefmt=date_format, format=formatter, level=logging.INFO)
