import logging

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

try:
    x = 10 / 0
except Exception as e:
    logging.error("Error occurred : %s", e)
