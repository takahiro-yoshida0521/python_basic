apple_price = 200
# 変数 money に数値 1000 を代入してください
money = 1000

input_count = input('購入するりんごの個数を入力してください：')
count = int(input_count)
total_price = apple_price * count

print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')

# money と total_price の比較結果によって条件を分岐してください

if money > total_price:
    print('りんごを買うことができます')

elif money == total_price:
    print('りんごを買うことができますが所持金が0円になります')

else:
    print('お金が足りません')