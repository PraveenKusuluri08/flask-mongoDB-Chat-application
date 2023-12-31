from mongoengine import *
from datetime import datetime

class Rooms(Document):
    name = StringField(required=True,max_length=100)
    created_by = StringField(required=True,max_length=100)
    created_at = DateTimeField(default = datetime.now())
    isGroup = BooleanField(required=True)
    roomCode = StringField(required=True)
    isActive = BooleanField(required=True,default=False)
    
class RoomMemebers(Document):
    _id:{
        "room_id": StringField(required=True),
        "username":StringField(required=True,max_length=100)
    }
    room_name:StringField(required=True,max_length=100)
    added_by:StringField(required=True,max_length=100)
    added_at:DateTimeField(default=datetime.now())
    isGroup:BooleanField(required=True)
    is_room_admin: BooleanField(required=True)