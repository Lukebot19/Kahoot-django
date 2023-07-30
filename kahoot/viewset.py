from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

# Send real-time updates to the WebSocket clients.
channel_layer = get_channel_layer()
quiz_id = 1
async_to_sync(channel_layer.group_send)(
    f'quiz_{quiz_id}',
    {
        'type': 'quiz_update',
        'message': json.dumps({'quiestion_added': 'New quiestion added!'}),
    }
)