from ._anvil_designer import AboutUsTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AboutUs(AboutUsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("home_page_button", "click")
  def home_page_button_click(self, **event_args):
    open_form('Main')
    pass

  @handle("about_us_button", "click")
  def about_us_button_click(self, **event_args):
    open_form('AboutUs')
    pass

