from ._anvil_designer import MainTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Main(MainTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
   
  # Any code you write here will run before the form opens.

  @handle("report_button", "click")
  def report_button_click(self, **event_args):
    open_form("ReportItem")
    pass

  @handle("search_button", "click")
  def search_button_click(self, **event_args):
    open_form("SearchItems")
    pass

  @handle("home_page_button", "click")
  def home_page_button_click(self, **event_args):
    open_form("Main")
    pass

  @handle("about_us_button", "click")
  def about_us_button_click(self, **event_args):
    open_form("AboutUs")
    pass

  @handle("admin_button", "click")
  def admin_button_click(self, **event_args):
    user = anvil.users.login_with_form()

    if user and user["is_admin"]:
      open_form("AdminPanel")
    else:
      alert("You do not have admin access.")
    pass

