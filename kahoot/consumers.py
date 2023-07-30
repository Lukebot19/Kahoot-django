import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class QuizConsumer(WebsocketConsumer):

    def connect(self):
        # Called when the websocket is handshaking as part of initial connection.
        self.quiz_id = self.scope['url_route']['kwargs']['quiz_id']
        self.room_group_name = f'quiz_{self.quiz_id}'

        # Join the WebSocket room specifc to the quiz.
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        self.accept()

    def disconnect(self, close_code):
        # Called when the WebSocket closes for any reason.
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )
        self.accept()

    def receive(self, text_data):
        # Called when a message is received with either text or bytes depending
        # on what has been sent over the WebSocket.
        pass

    def quiz_update(self, event):
        self.send(text_data=event['message'])