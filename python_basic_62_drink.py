from python_basic_62_menu_item import MenuItem

class Drink(MenuItem):
    def __init__(self, name, price, amount):
        super().__init__(name, price)
    # __init__ メソッドを定義してください
    # 引数にname, price, amountを受け取れるようにしてください。
    # super()を用いて、親クラスの__init__メソッドを呼び出してください。
    # __init__メソッドの中で、self.amountに引数amountの値を代入してください。
        self.amount = amount

    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.amount) + 'mL)'