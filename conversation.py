import logging

logger = logging.getLogger(__name__)


class Conversation:
    def __init__(self, game, engine, xhr, version, challenge_queue):
        self.game = game
        self.engine = engine
        self.xhr = xhr
        self.version = version
        self.challengers = challenge_queue

    command_prefix = "!"

    def react(self, line, game):
        logger.info(f'*** {self.game.url()} [{line.room}] {line.username}: {line.text.encode("utf-8")}')
        if line.text[0] == self.command_prefix:
            self.command(line, game, line.text[1:].lower())

    def command(self, line, game, cmd):
        if cmd == "wait" and game.is_abortable():
            game.ping(60, 120, 120)
            self.send_reply(line, "Waiting 60 seconds...")
        elif cmd == "name":
            name = game.me.name
            self.send_reply(line, f"{name} running {self.engine.name()} (lichess-bot v{self.version})")

    def send_reply(self, line, reply):
        self.xhr.chat(self.game.id, line.room, reply)

    def send_message(self, room, message):
        if message:
            self.send_reply(ChatLine({"room": room}), message)


class ChatLine:
    def __init__(self, json):
        self.room = json.get("room")
        self.username = json.get("username")
        self.text = json.get("text")
