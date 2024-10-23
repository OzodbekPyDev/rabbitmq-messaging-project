# RabbitMQ Messaging Project

This project provides a simple example of using **RabbitMQ** for message queuing with Python, utilizing **pika** as the client library. It includes a **publisher** that sends messages to a queue and a **consumer** that processes the messages asynchronously.

## Project Structure

- **config.py**: Contains configuration details such as RabbitMQ connection parameters and utility functions for logging and connection handling.
- **consumer.py**: Defines a consumer that processes incoming messages from the queue.
- **publisher.py**: Implements a publisher that sends messages to the queue.
- **docker-compose.yaml**: Provides a Docker setup to run RabbitMQ locally for testing.
- **requirements.txt**: Lists the Python dependencies for the project.

## Requirements

- Python 3.8+
- RabbitMQ instance (you can use Docker to run RabbitMQ locally)
- Required Python packages are listed in `requirements.txt`

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/rabbitmq-messaging-project.git
    cd rabbitmq-messaging-project
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Start RabbitMQ with Docker**:
    If you have Docker installed, use the provided `docker-compose.yaml` file to start RabbitMQ.
    ```bash
    docker-compose up -d
    ```

    This will start RabbitMQ with the default credentials (username: `guest`, password: `guest`).

## Running the Project

1. **Start the Consumer**

   The consumer listens for messages on a queue (`news`) and processes them. Start the consumer as follows:

    ```bash
    python consumer.py
    ```

   The consumer will wait for messages and process each one by simulating a 5-second task.

2. **Start the Publisher**

   The publisher sends a message to the RabbitMQ queue. You can run it as follows:

    ```bash
    python publisher.py
    ```

   Each time the publisher is run, it will send a "Hello World" message with a timestamp to the `news` queue.

## Configuration

You can adjust the configuration (host, port, credentials) in the `config.py` file. By default, the project connects to RabbitMQ running on `localhost` at port `5672` with the default guest credentials.

```python
# config.py
RMQ_HOST = "localhost"
RMQ_PORT = 5672
RMQ_USER = "guest"
RMQ_PASSWORD = "guest"
MQ_ROUTING_KEY = "news"
```

# Logging

Logging is configurable via the `configure_logging` function in the `config.py` file. By default, logging is set to `INFO` for the publisher and `WARNING` for the consumer. You can modify the log level by passing a different log level when calling `configure_logging`.

### Example:

```python
# Set logging to DEBUG level
configure_logging(logging.DEBUG)
```
Here is the logging format example written in proper markdown:

### Logging Format

The logging format includes the following details:

- **Timestamp**
- **Function name**
- **File name and line number**
- **Log level** (INFO, WARNING, DEBUG, etc.)
- **Log message**

### Example Log Output

```bash
[2024-10-23 15:43:12.345]      process_message consumer:43 WARNING  - Start processing message b'Hello World!'
[2024-10-23 15:43:17.345]      process_message consumer:48 INFO     - Finished processing message b'Hello World!'
```

### Acknowledgments

The project uses:

- **pika**: A pure Python RabbitMQ client library for handling AMQP protocol.