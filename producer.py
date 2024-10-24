import logging
import time
from typing import TYPE_CHECKING

import config
from config import (
    get_connection,
    configure_logging,
    MQ_EXCHANGE,
    MQ_ROUTING_KEY
)

from rabbit.common import EmailUpdatesRabbit

if TYPE_CHECKING:
    from pika.adapters.blocking_connection import BlockingChannel

log = logging.getLogger(__name__)


class Producer(EmailUpdatesRabbit):



    def produce_message(self, idx: int) -> None:

        message_body = f"Hello World! {time.time()}"
        log.info("Publish message %s", message_body)
        self.channel.basic_publish(
            exchange=config.MQ_EMAIL_UPDATES_EXCHANGE_NAME,
            routing_key="",
            body=message_body
        )
        log.warning("Published message %s", message_body)

def main():
    configure_logging(logging.WARNING)
    with Producer() as producer:
        producer.declare_email_updates_exchange()
        for idx in range(1, 6):
            producer.produce_message(idx)
            time.sleep(0.5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.warning("Bye!")
