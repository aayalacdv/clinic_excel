import pyautogui as gui 
import win32clipboard as clip 
import time as time 


class UserData: 
    name_position = [ 398, 301]
    surname_position = [489, 301]
    surname2_position = [ 648, 301]
    price_position = [ 454, 692]
    payment_method_position = [ 530, 688] 

    def get_param(self, position): 
        
        gui.doubleClick(position)
        time.sleep(0.50)
        gui.hotkey('ctrl', 'c')

        clip.OpenClipboard()
        name = clip.GetClipboardData()
        clip.CloseClipboard()

        return name  

    def __init__(self) :
        self.name = self.get_param(self.name_position)
        self.surname = self.get_param(self.surname_position)
        self.surname2 = self.get_param(self.surname2_position)
        self.price = self.get_param(self.price_position)
        self.payment_method = self.get_param(self.payment_method_position)
        print(self.name + ' ' +  self.surname + ' '  + self.surname2 + ' ' + self.payment_method + ' ' + self.price)












