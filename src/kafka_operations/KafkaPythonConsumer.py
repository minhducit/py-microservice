import threading
from kafka import KafkaConsumer

class KafkaPythonConsumer(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, topic = None, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval
        self.topic = topic

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        consumer = KafkaConsumer(bootstrap_servers='kafka:9092',
                             auto_offset_reset='latest',
                             group_id=None)
        consumer.subscribe([self.topic])
        for msg in consumer:
            print("Message retrieved")
            if msg is None:
                continue
            print(msg.value.decode("utf-8"))