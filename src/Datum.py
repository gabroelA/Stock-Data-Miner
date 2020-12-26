class Datum:
    def __init__(self, name, value):
        self.name = name
        self.inputs = []
        self.value = value


    def addInput(self, datum):
        self.inputs.append(datum)

    def getDatum(self, name):
        value = None
        for x in self.inputs:
            if x.name == name:
                value = x
            break

        return value

    def getName(self):
        return self.name

    def dateValue(self):
        return datetime.strptime(self.value)

    def integerValue(self):
        return int(self.value)

    def stringValue(self):
        return self.value

    

