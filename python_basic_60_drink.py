from python_basic_60_menu_item import MenuItem

class Drink(MenuItem):
    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.amount) + 'mL)'
    # info メソッドを定義してください
    # 定義したinfoメソッドの中で、以下の文字列を戻り値として返してください。
    # self.name + ': ¥' + str(self.price) + ' (' + str(self.amount) + 'mL)'