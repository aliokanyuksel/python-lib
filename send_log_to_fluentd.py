#!/usr/bin/python3

from fluent import sender, event

# Connect to the fluentd sender on a tag...
logger = sender.FluentSender("debug", host="localhost", port=24224)

# Create a sample payload...
log_payload = {'prediction': 3.32, 'input1': 1.2, 'input2': 2.4}

# Emit event...
if not logger.emit('prediction', log_payload):
    print(logger.last_error)
    logger.clear_last_error()
