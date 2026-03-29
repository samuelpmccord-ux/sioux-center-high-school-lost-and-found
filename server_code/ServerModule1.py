  # These are variables anvil automatically creates giving properties on whats one the form. 
from anvil import *
import anvil.secrets
import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from datetime import datetime
from anvil.tables import app_tables

  # This function calls the anvil server and defines what the variable add_item is.
  # This table of items calls the built in data tables, giving properties to call later in the code. 
@anvil.server.callable
def add_item(item_dict):
  return app_tables.items.add_row(
    name=item_dict.get("name", ""),
    title=item_dict.get("title", ""),
    description=item_dict.get("description", ""),
    item_type=item_dict.get("item_type", ""),
    location=item_dict.get("location", ""),
    date=item_dict.get("date", None),
    contact=item_dict.get("contact", ""),
    image=item_dict.get("image", None),
    created=datetime.utcnow(),
    approved=False,
    returned=False
  )

@anvil.server.callable
def search_items(query="", item_type=None):
  rows = app_tables.items.search(
    item_type=item_type, approved=True)

  query = query.lower()

  def matches(r):
    text = f"{r['title']} {r['description']} {r['location']}".lower()
    return query in text

  return [r for r in rows if matches(r)]

@anvil.server.callable
def search_found_items(query="", location=None):
  rows = app_tables.items.search(
    item_type="found",
    approved=True)

  query = query.lower()

  def matches(r):
    text = f"{r['title']} {r['description']} {r['location']}".lower()
    return query in text

  return [r for r in rows if matches(r)]

@anvil.server.callable
def get_all_items():
  return app_tables.items.search()

@anvil.server.callable
def get_unapproved_items():
  return app_tables.items.search(approved=False, returned=False)

@anvil.server.callable
def approve_item(row_id):
  row = app_tables.items.get_by_id(row_id)
  row['approved'] = True
  return True

@anvil.server.callable
def delete_item(row_id):
  row = app_tables.items.get_by_id(row_id)
  row.delete()
  return True

@anvil.server.callable
def mark_returned(row_id):
  row = app_tables.items.get_by_id(row_id)
  row['returned'] = True
  return True

def form_show(self, **event_args):
  self.delete_btn.visible = True

  