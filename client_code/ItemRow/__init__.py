from ._anvil_designer import ItemRowTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemRow(ItemRowTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("", "show")
  def form_show(self, **event_args):
    row = self.item

    self.name_label.text = f"Name:  {row['name']}"
    self.title_label.text = f"Name of Item:  {row['title']}"
    self.type_label.text = f"Item Status:  {row['item_type']}"
    self.date_label.text = (
      f"Date item was last seen:  {row['date']}" if row["date"] else "Date: (not specified)"
    )
    self.location_label.text = f"Location item was last seen:  {row['location']}"
    self.contact_label.text = f"Contact Information:  {row['contact']}"
    self.description_label.text = f"Item Description:  {row['description']}"
    self.image_display.source = row ["image"]

  @handle("delete_button", "click")
  def delete_button_click(self, **event_args):
    if confirm("Are you sure you want to delete this item?"):
      anvil.server.call('delete_item', self.item.get_id())
      self.parent.raise_event('x-refresh')
