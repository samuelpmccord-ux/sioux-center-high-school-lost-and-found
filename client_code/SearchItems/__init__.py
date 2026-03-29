from ._anvil_designer import SearchItemsTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class SearchItems(SearchItemsTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.do_search() 

    # Any code you write here will run before the form opens.

  def do_search(self):
    print("Search running")
    query = self.search_box.text or ""
    item_type = self.filter_dropdown.selected_value or None

    rows = anvil.server.call("search_items", query, item_type)
    print("Rows returned:", rows)
    self.results_panel.items = rows

  @handle("search_button", "click")
  def search_button_click(self, **event_args):
    self.do_search()

  @handle("back_button", "click")
  def back_button_click(self, **event_args):
    open_form("Main")
