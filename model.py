from dataclasses import dataclass

@dataclass
class Record:
    number: str
    first : str
    sur   : str=''
    last  : str=''
    comment: str=''



class Phone_booK:
    def __init__(self, records = []):
        self.records = self.set(records)    
        self.filtered = self.records

    def get(self):
        records = []
        return records

    def set(self, records = []):
        return records

    def filter_by_field(self, filter, field):
        self.filterd = list(filter(lambda x: filter in x[field], self.records))
        return self.filtered

    def clear_filter(self):
        return self.records    

    def add_record(self, record):
        self.records.append(record)

    def del_records(self, records):
        self.records = list(filter(lambda record: record not in records, self.records))

    def change_record(self, before, after):
        self.del_records([before])
        self.add_record(after)
