import logging

def writelogs(error):
    logging.basicConfig(
        level=logging.Error,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt="%Y-%m-%d %H:%M:",
        filename="logs-tracer.log"
        )
    logging.error(error)