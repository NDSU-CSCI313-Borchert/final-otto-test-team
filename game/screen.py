#Abstract class, making sure that all subclasses at least attempt
# to implement the update, draw, and handle_keyboard_event methods

class Screen():
    
    def handle_keyboard_event(self, event):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError
        
    def draw(self, screen):
        raise NotImplementedError
