import configparser

global_config = configparser.ConfigParser()
global_config.read('test_config.ini')

class ConfigProvider:
    
    def __init__(self) -> None:
        self.config = global_config
    
    def get_ui_url(self) -> str:
        return self.config["ui"].get("base_url")
    
    def get_api_url(self) -> str:
        return self.config["api"].get("base_url")
   
   
   