from winreg import *


class RegManager:
    def __init__(self, key_path: str, value_name: str):
        self.hive = HKEY_CURRENT_USER
        self.key_path = key_path
        self.value_name = value_name

    def __init_reg(self) -> None:
        key = None
        CreateKey(self.hive, self.key_path)
        while True:
            try:
                key = OpenKey(self.hive, self.key_path, 0, KEY_WRITE)
                break
            except FileNotFoundError:
                continue
        SetValueEx(key, self.value_name, 0, REG_SZ, '')
        CloseKey(key)

    def __validate_reg(self) -> bool:
        try:
            key = OpenKey(self.hive, self.key_path, 0, KEY_READ)
            QueryValueEx(key, self.value_name)
            CloseKey(key)
        except FileNotFoundError:
            return False
        return True

    def __read_reg(self) -> str:
        key = OpenKey(self.hive, self.key_path, 0, KEY_READ)
        return QueryValueEx(key, self.value_name)[0]

    def __save_reg(self, save_data: str) -> None:
        key = OpenKey(self.hive, self.key_path, 0, KEY_WRITE)
        SetValueEx(key, self.value_name, 0, REG_SZ, save_data)

    def handler(self, action: str, save_data: str = None) -> str or None:
        return_data = None
        if not self.__validate_reg():
            self.__init_reg()
        if action == 'read':
            return_data = self.__read_reg()
            if return_data == '':
                return_data = None
        elif action == 'save':
            self.__save_reg(save_data)
        return return_data
