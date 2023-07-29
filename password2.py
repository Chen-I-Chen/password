answer = 'a123456'
chance = 3
while chance < 1:
	password = input('請輸入密碼：')
	if password == answer:
		print('登入成功')
		break
	else:
		chance = chance - 1
		print('登入失敗, 你還有' ,chance, '次機會')