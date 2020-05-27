import sys
from lib.prophet import Prophet
from lib.utils import StopTalking
from lib.core.colors import Colors


class Chat:
    def __init__(self, respondent:Prophet):
        self.respondent = respondent
        self.user_prompt = Colors.colorise('(жду) ', Colors.lowcontrastgrey)

    def wait_input(self):
        print(self.user_prompt, end='')
        return input()

    def run(self):
        self.respondent.welcome()
        user_inp = self.wait_input()
        
        while True:
            try:
                self.respondent.listen(user_inp)
            except StopTalking as e:
                break
            except Exception as e:
                self.end(e)
            user_inp = self.wait_input()
        self.end()
    
    @classmethod
    def end(cls, e=None):
        print(Colors.reset, end='')

        if e is not None:
            raise e
        else:
            sys.exit(0)
