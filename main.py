from rtmbot import RtmBot
from rtmbot.core import Plugin

import secret

def answer(text):
    if "지영" in text:
        reply = "왱"
    elif "주사위" == text:
        reply = str(random.randint(1, 6))
    else:
        reply = None
    # reply는 반드시 존재하게 됨. 불렀어, 주사위, None --> slack과는 무관해
    return reply


class HelloPlugin(Plugin):
    def process_message(self, data):
        reply = answer(data["text"]) # assignment... 오른쪽에 있는  expression을 왼쪽에 담아.
        if reply is not None:
            self.outputs.append([data["channel"], reply])



config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
