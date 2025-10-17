from layer_naive import Mullayer, AddLayer

apple = 100
apple_num = 2
orange = 150
orange_num = 3
tax = 1.1

# layer
mul_apple_layer = Mullayer()
mul_orange_layer = Mullayer()

add_apple_orange_layer = AddLayer()
mul_tax_layer = Mullayer()

# forward
apple_price = mul_apple_layer.forward(apple,apple_num)
orange_price = mul_orange_layer.forward(orange,orange_num)
all_price = add_apple_orange_layer.forward(apple_price,orange_price)
price = mul_tax_layer.forward(all_price,tax)

# backward
dprice = 1
dall_price, dtax = mul_tax_layer.backword(dprice)
dapple_price, dorange_price = add_apple_orange_layer.backward(dall_price)
dorange, dorange_num = mul_orange_layer.backword(dorange_price)
dapple, dapple_num = mul_apple_layer.backword(dapple_price)

print(price)
print(dapple_num,dapple,dorange,dorange_num,dtax)

