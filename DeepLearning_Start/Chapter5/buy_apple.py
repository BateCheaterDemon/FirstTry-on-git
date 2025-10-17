from layer_naive import Mullayer

apple = 100
apple_num = 2
tax = 1.1

# layer
mul_apple_layer = Mullayer()
mul_tax_layer = Mullayer()

# forward
apple_price = mul_apple_layer.forward(apple,apple_num)
price = mul_tax_layer.forward(apple_price,tax)

print("forward price cal:",price)

# backward
dprice = 1
dapple_price,dtax = mul_tax_layer.backword(dprice)
dapple, dapple_num = mul_apple_layer.backword(dapple_price)

print("backward:",dapple,dapple_num,dapple_price)

