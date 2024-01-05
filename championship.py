from haydovchi import Haydovchi

class Championship:
    def __init__(self) -> None:
        self.driver_list:list[Haydovchi] = []

    def create_driver(self, ismi):
        haydovchi = Haydovchi(ismi)
        self.driver_list.append(haydovchi)
        return haydovchi
    
    def get_drivers(self):
        return self.driver_list
    
    def get_driver(self, driver_name):
        for driver in self.driver_list:
            if driver.ismi == driver_name:
                return driver
        return None

