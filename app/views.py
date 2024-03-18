from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import telebot

# Create your views here.


TOKEN = '7185375595:AAFbV63qDyU0ubm06SFV8-PIsI0VTHmyTDE'

URL = 'https://aedd-94-141-68-35.ngrok-free.app/bot/'


bot = telebot.TeleBot(TOKEN)

def home(request):
    return HttpResponse('hello')


@csrf_exempt
async def bot_view(request):
    if request.method == 'GET':
        return HttpResponse('This is a GET request')
    elif request.method == 'POST':
        try:
            update = telebot.types.Update.de_json(request.body.decode('utf-8'))
            bot.process_new_updates([update])
            return HttpResponse(status=200, content='POST request processed')
        except Exception as e:
            print(e)
