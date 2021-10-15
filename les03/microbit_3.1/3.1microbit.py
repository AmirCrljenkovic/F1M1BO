from microbit import *


threshold = 200


class Counter:
    counter = 0
    
    
    def __init__(self):
        self.refresh_display()
        
        
    def run(self):
        while True:
            if button_a.is_pressed():
                self.counter -= 1
                self.refresh_display()
            elif button_b.is_pressed():
                self.counter += 1
                self.refresh_display()
            sleep(threshold)
            
            
    def refresh_display(self):
        display.show(str(self.counter))
        

if __name__ == '__main__':
    Counter().run()