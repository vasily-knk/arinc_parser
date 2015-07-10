import json


class AutoJSONable():
    pass


class FieldDesc(AutoJSONable):
    def __init__(self, min_pos, max_pos, description, format_code):
        self.min_pos = min_pos
        self.max_pos = max_pos
        self.description = description
        self.format_code = format_code


class RecordDesc(AutoJSONable):
    def __init__(self, codes, description, conts):
        self.codes = codes
        self.description = description
        self.conts = conts


class ArincJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, AutoJSONable):
            return o.__dict__
        return json.JSONEncoder.default(self, o)
