from src.application import app
import logging
import kafka
from kafka import KafkaConsumer, KafkaProducer
import threading

# setup logging configuration
# Create a new handler for log messages that will send them to standard error
handler = logging.StreamHandler()

# Add a formatter that makes use of our new contextual information
log_format = "%(asctime)s\t%(levelname)s\t%(user_id)s\t%(ip)s\t%(method)s\t%(url)s\t%(message)s"
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

class KafkaConsumerThread(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        consumer = KafkaConsumer(bootstrap_servers='127.0.0.1:9092',
                             auto_offset_reset='latest',
                             group_id=None)
        consumer.subscribe(['test_queue1'])
        for msg in consumer:
            print("Message retrieved")
            if msg is None:
                continue
            print(msg.value.decode("utf-8"))



if __name__ == '__main__':
    example = KafkaConsumerThread()
    app.run(port = 8765, debug=True, use_reloader=False, threaded=False)

