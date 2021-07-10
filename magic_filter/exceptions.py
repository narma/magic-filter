class SwitchMode(Exception):
    pass


class SwitchModeToAll(SwitchMode):
    def __init__(self, key: slice) -> None:
        self.key = key


class SwitchModeToAny(SwitchMode):
    pass
