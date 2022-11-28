import pandas

class Phone_booK:
    def __init__(self, records = []):
        self.set(records)


    def get(self):
        return self.records

    
    def set(self, records = []):
        if records:
            self.records = records
        else:
            self.records = pandas.DataFrame(records)     


    def filter_by_field(self, dataset, filter):
        filtered = dataset[dataset.columns[0]].apply(lambda x: False)
        for field in dataset.columns:
            f = dataset[field].apply(lambda txt: filter in txt)
            filtered = f | filtered
        return dataset[filtered]
        

    def add_record(self, record):
        self.records.loc[len(self.records.index)] = record

    def del_record(self, index):
        self.records.drop(labels = [index],axis = 0, inplace=True)
        
    

