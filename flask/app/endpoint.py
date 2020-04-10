import json
from app import app
from nameparser import HumanName


@app.route("/parse/<name>")
def index(name):
  return_name = HumanName(name)
  return json.dumps(return_name.as_dict())
