from ._anvil_designer import ReportItemTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ReportItem(ReportItemTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("back_button", "click")
  def back_button_click(self, **event_args):
    open_form('Main')
    pass

  @handle("submit_button", "click")
  def submit_button_click(self, **event_args):

    item_dict = {
      "name": self.name_box.text,
      "title": self.title_box.text,
      "description": self.description_area.text,
      "item_type": self.type_dropdown.selected_value,
      "location": self.location_box.text,
      "date": self.date_picker.date,
      "contact": self.contact_box.text,
      "image": self.image_loader.file
    }

    if not item_dict["title"] or not item_dict["item_type"] or not item_dict["name"]:
      alert("Please enter a name, a title, and select lost/found.")
      return

    anvil.server.call("add_item", item_dict)

    alert("Item submitted for Admin Approval!")
    open_form('Main')

    # this function makes sure code works while offline.
if anvil.server.is_app_online():
  # safe to call server
  else:
    # offline mode

  try:
    anvil.server.call("add_item", item_dict)
except anvil.server.AppOfflineError:
anvil.storage.local.set("pending_items", item_dict)

if anvil.server.is_app_online():
  pending = anvil.storage.local.get("pending_items")
  if pending:
    anvil.server.call("add_item", pending)
    anvil.storage.local.delete("pending_items")
