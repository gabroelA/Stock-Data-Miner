class ControllerState:
    def __init__(self, name, dataset):
        self.name = name
        self.dataset = dataset
        self.states = []

    def getName(self):
        return self.name

    def executeFlow(self, input):
        pass

    def sendDatasetToRecommendationEngine(self):
        pass

