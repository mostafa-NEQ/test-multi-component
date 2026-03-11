class ComponentOneComponent:
    def __init__(self, config):
        self.config = config

    def process(self, inputs):
        return {"result": f"Component One received: {inputs.get('text')}"}
