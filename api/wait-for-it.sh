#!/bin/bash

# Function to check if RabbitMQ container is ready
wait_for_rabbitmq() {
    local host="$1"
    local port="$2"
    local timeout="$3"

    echo "Waiting for RabbitMQ container to start..."

    while ! nc -z "$host" "$port"; do
        if ((timeout <= 0)); then
            echo "Timeout: RabbitMQ container did not start within the specified time."
            exit 1
        fi

        ((timeout--))
        sleep 1
    done

    echo "RabbitMQ container started."
}

# Function to start the FastAPI app with Uvicorn
start_fastapi_app() {
    local host="$1"
    local port="$2"

    echo "Starting FastAPI app with Uvicorn..."

    uvicorn main:app --host "$host" --port "$port"
}

# Wait for RabbitMQ container to start
wait_for_rabbitmq "rabbitmq" 5672 30

# Start the FastAPI app with Uvicorn
start_fastapi_app "0.0.0.0" 8000
