from src.application import app
import logging
import kafka
from src.kafka_operations.KafkaPythonConsumer import KafkaPythonConsumer

# setup logging configuration
# Create a new handler for log messages that will send them to standard error
handler = logging.StreamHandler()

# Add a formatter that makes use of our new contextual information
log_format = "%(asctime)s\t%(levelname)s\t%(user_id)s\t%(ip)s\t%(method)s\t%(url)s\t%(message)s"
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)


if __name__ == '__main__':
    consumer = KafkaPythonConsumer(topic = 'generic_queue')
    app.run(port = 8765, debug=True, use_reloader=False, threaded=False)

