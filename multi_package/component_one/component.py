class ComponentOneComponent:
    def __init__(self, config):
        self.config = config

    def process(self, text=None, **kwargs):
        return {"result": f"Component One received: {text}"}
