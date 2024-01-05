class Haydovchi:
    def __init__(self, ismi) -> None:
        self._ismi = ismi

    @property
    def ismi(self):
        return self._ismi
    
    def __str__(self) -> str:
        return self.ismi