from frontend.config import Config

class Core:
    def __init__(self, config):
        self.config = config

        self.reset()
    
    def reset(self):
        self.currently_counting = True
        self.current_number     = 0
    
    # returns a json for an embed that contains the message
    # that the frontend should send. returns None if no message
    # should be sent. well, at some point itll return an embed.
    # for now ill return a string for testing.
    def get_response_to_message(self, message):
        if self.currently_counting:
            return self.get_response_to_message__counting(message)
        return None
    
    def get_response_to_message__counting(self, message):
        try:
            submitted_number = self.interpret_message_as_number(message)

            if submitted_number == self.current_number + 1:
                self.current_number = submitted_number
                return "good"
            else:
                return "bad"

        except ValueError:
            return None

    # may throw ValueError if cannot be interpretted as number
    def interpret_message_as_number(self, message):
        return int(message)

