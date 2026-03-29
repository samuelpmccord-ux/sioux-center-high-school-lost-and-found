from ._anvil_designer import AdminPanelTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AdminPanel(AdminPanelTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    user = anvil.users.get_user()
    if not user or not user['is_admin']:
      alert("Access denied.")
      open_form('Main')
      return

    self.refresh()

  def refresh(self, **event_args):
    rows = anvil.server.call('get_unapproved_items')
    self.repeating_panel.items = rows

  def repeating_panel_x_refresh(self, **event_args):
    self.refresh()

  @handle("back_button", "click")
  def back_button_click(self, **event_args):
    open_form('Main')

  @handle("refresh_button", "click")
  def refresh_button_click(self, **event_args):
    self.refresh()
