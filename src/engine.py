from dateutil import parser
from jinja2 import Environment, FileSystemLoader

engine = Environment(loader=FileSystemLoader(["templates", "automation/templates"]))


def datetime_format(value, format="%d-%m-%y"):
    return parser.isoparse(value).strftime(format)


engine.filters["datetime_format"] = datetime_format
