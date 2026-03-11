from iflow_engine_sdk.interfaces.output import ComponentOutput

class ComponentTwoComponent:
    def __init__(self, config):
        self.config = config

    def process(self, text=None, **kwargs):
        return ComponentOutput(result={'result': f'Component Two processed: {text}'})
