# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Mesure

class MesureConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def send_mesure_data(self, event):
        mesure = event['mesure']
        await self.send(json.dumps({
            'humidite': mesure.humidite,
            'timestamp': mesure.timestamp.isoformat(),
        }))

    @async_to_sync
    async def fetch_mesure_data(self, event):
        mesures = Mesure.objects.all()[:10]
        mesures_data = [{'humidite': str(mesure.humidite), 
                         'timestamp': mesure.timestamp.isoformat()} for mesure in mesures]
        await self.send(json.dumps({'mesures': mesures_data}))
