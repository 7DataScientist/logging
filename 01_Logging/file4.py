import logging
logging.basicConfig(filename="file55.log",level=logging.CRITICAL, format=('%(asctime)s - %(name)s  - %(levelname)s  %(message)s'))


logging.debug("This is debug")
logging.info("This is info")
logging.warning("This is warning")
logging.error("This is error")
logging.critical("This is critical")

logging.critical("-----------------------------")