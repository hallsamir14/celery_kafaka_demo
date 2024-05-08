# Celery Integration With Kafka

This system integrates Celery and Kafka. This setup is ideal for asynchronous processing and dissemination of information within a microservice architecture.

## General Overview

Celery is a distributed task queue system that allows you to handle a large number of tasks concurrently. It provides an easy-to-use framework for task management, scheduling, and execution across multiple workers or nodes. By using Celery, you can delegate time-consuming or resource-intensive tasks to separate workers, enabling parallel processing and improving overall application performance.

Kafka, is a distributed streaming platform that provides a fault-tolerant and scalable messaging system. It excels at handling real-time data streams and facilitates reliable communication between various components of your application. Kafka offers high throughput, low latency, and strong durability, making it an ideal choice for building event-driven architectures.

<h3><b>The system comprises of the following components:</b></h3>

1. **Kafka Producer**: Writes messages to Kafka topic (Kafka broker).
2. **Kafka Consumer**: Reads messages from Kafka (Kafka broker>).
4. **Celery Tasks**: Instance of a specific funtion/job (task) that is executed by Celery.
5. **Celery Worker**: Instance of a Celery app that is responsible for executing tasks.
6. **Celery Beat**: Periodic task scheduler that executes tasks at a specified interval.


### 1. Kafka Producer

This component is a Python script designed to run within a microservice architecture. It takes messages from command-line input or default messages, encodes them into JSON format, and sends them to a designated Kafka topic.

**Features**:
- Configurable Kafka server settings including acknowledgments and retries for robust message delivery.
- Dynamic message content through command-line arguments.
- Continuous asynchronous message production.

**Dependencies**:
- `confluent_kafka`
- `pydantic_settings`
- `asyncio`
- `argparse`

### 2. Kafka Consumer

A Python script that continuously listens for messages on a specified Kafka topic, processes them, and performs designated actions based on the content.

**Purpose**:
- Decouples message receiving from processing, enhancing scalability and reliability.
- Facilitates asynchronous processing of data received through Kafka.

**Operation**:
- Initializes a Kafka consumer with specified settings, subscribes to a topic, and listens for new messages.
- Upon receiving a message, checks for errors, processes valid messages, and logs information.



**Workflow**:
- Subscribes to a Kafka topic and listens for messages.
- Consumer reads messages from topic and output via celery task (printSomething())
- Provides real-time stream of messages, using celery as mechansism for handling the display of messages.

## Setup and Configuration

### Requirements

- Python 3.7+
- Celery
- Kafka Cluster (Via docker container in my case)


**Configuration Files**:
- Ensure all components are configured via `.env` files for environment-specific settings.
- Logging configurations are managed through `logging_config.json` for each component.