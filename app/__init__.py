from kivymd.app import MDApp
from kivy.utils import QueryDict, rgba
from kivy.metrics import dp, sp
from kivy.core.window import Window
from .home import Home
from kivy.config import Config 

from datetime import date, datetime


class Moresh(MDApp):
    colors = QueryDict()
    colors.primary = rgba('#2D9CD8')
    colors.secondary = rgba('#16213E')
    colors.sucess = rgba('#1FC98E')
    colors.warning = rgba('#F2C94C')
    colors.danger = rgba('#EB5757')
    colors.grey_dark = rgba('#c4c4c4')
    colors.grey_light = rgba('#f2f2f2')
    colors.black = rgba('#a1a1a1')
    colors.white = rgba('#f1f1f1')
    
    user = "Moresh"
    Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nove","Dec"]
    d = datetime.now()
    cur_date = f"{d.day}-{Month[d.month-1]}-{d.year}"

    
    fonts = QueryDict()
    fonts.size = QueryDict()
    fonts.size.h1 = dp(24)
    fonts.size.h2 = dp(22)
    fonts.size.h3 = dp(18)
    fonts.size.h4 = dp(16)
    fonts.size.h5 = dp(14)
    fonts.size.h6 = dp(12)
    
    # fonts.heading = 'assets/fonts/Roboto/Roboto-Bold.ttf'
    # fonts.subheading = 'assets/fonts/Roboto/Roboto-Regular.ttf'
    # fonts.body = 'assets/fonts/Roboto/Roboto-Light.ttf'




    def build(self):
        self.icon = "../icons/3d-glasses.png"
        # Config.set('graphics', 'fulscreen', 'auto')
        # Config.set('graphics', 'window_state', 'maximized')
        # Config.write()

        Window.size = (500,700)
        # Window.maximize()
        Window.top = 30
        Window.left = 0
        return Home()
       
