from mycroft import MycroftSkill, intent_file_handler


class Tankstop(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tankstop.intent')
    def handle_tankstop(self, message):
        self.speak_dialog('tankstop')


def create_skill():
    return Tankstop()

