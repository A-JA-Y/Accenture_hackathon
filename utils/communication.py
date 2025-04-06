from datetime import datetime
from queue import Queue

message_queue = Queue()

class Message:
    def __init__(self, sender, receiver, message_type, content):
        self.sender = sender
        self.receiver = receiver
        self.message_type = message_type  # e.g., "REQUEST_FORECAST"
        self.content = content
        self.timestamp = datetime.now()

def send_message(sender_agent, receiver_agent, message_type, content):
    message = Message(sender_agent, receiver_agent, message_type, content)
    message_queue.put(message)
    return message
