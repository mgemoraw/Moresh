from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar, MDBottomAppBar
from modules.cryptify import *

class Home(MDScreen):
	state = 0
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


	def flip(self):
		if self.state == 0:
			self.state = 1
			self.ids.toolbar.title = "Cipher Text Generator"
			self.ids.action_button.text = "Generate"
			self.ids.input_text.hint_text = "Paste Block Text Here"
			self.ids.output_text.hint_text = "Result Cipher Text"
			self.ids.output_text.disabled = False


		else:
			self.state = 0
			self.ids.toolbar.title = "Cipher Text Decrypter"
			self.ids.action_button.text = "Decrypt"
			self.ids.input_text.hint_text = "Paste Cipher Text Here"
			self.ids.output_text.hint_text = "Result Block Text"
			self.ids.output_text.disabled = False

	def generate(self):
		if self.state == 0:
			# self.ids.output_text.disabled = False
			block_text  = decrypt(self.ids.input_text.text)
			self.ids.output_text.text = block_text
		else:
			# self.ids.output_text.disabled = False
			cipher_text  = encrypt(self.ids.input_text.text)
			self.ids.output_text.text = cipher_text


	def export(self, text):
		pass



# class Moresh(MDApp):
# 	def build(self):
# 		return Home()

	

# if __name__ == "__main__":
# 	Moresh().run()
