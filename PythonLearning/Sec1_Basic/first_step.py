# 如果使用match语句，就可以写得更加简洁(match 是python3.10以上的功能)：
score = 'B'
match score:
    case 'A':
        print('score is A')
    case 'B':
        print('score is B')
    case 'C':
        print('score is C')
    case _:
        print('score is invalid')
