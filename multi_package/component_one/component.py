from iflow_engine_sdk.interfaces.output import ComponentOutput

class ComponentOneComponent:
    def __init__(self, config):
        self.config = config

    def process(self, text=None, **kwargs):
        return ComponentOutput(result={'result': f'Component One received: {text}'})
