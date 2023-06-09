data_dict = {}

key = input('keyを入力してください > ')  # 辞書のkeyを入力してもらう
value = input('valueを入力してください > ')  # 辞書のvalueを入力してもらう

data_dict[key] = value

print(data_dict)

print(data_dict[key])
print(data_dict.get(key))