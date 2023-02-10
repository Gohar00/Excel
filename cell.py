from color import Color
from datetime import datetime


class Cell:
    def __init__(self, value=None, color=Color.WHITE):
        self.value = str(value) if value is not None else ""
        self.color = color

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_color(self, color):
        if isinstance(color, Color):
            self.color = color
        else:
            raise ValueError("Invalid color")

    def get_color(self):
        return self.color

    def to_int(self):
        try:
            return int(self.value)
        except ValueError:
            print(f"Cannot convert '{self.value}' to integer")

    def to_float(self):
        try:
            return float(self.value)
        except ValueError:
            print(f"Cannot convert '{self.value}' to float")

    def to_date(self):
        date_formats = ["%Y-%m-%d", "%m/%d/%Y", "%d-%b-%y"]
        for data_format in date_formats:
            try:
                return datetime.strptime(self.value, data_format)
            except ValueError:
                pass
        return (f"Cannot convert '{self.value}' to date")

    def reset(self):
        self.color = Color.WHITE
        self.value = ""
