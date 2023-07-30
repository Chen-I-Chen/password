answer = 'a123456'
chance = 3
while chance > 0:
	chance = chance - 1
	password = input('請輸入密碼：')
	if password == answer:
		print('登入成功')
		break
	else:
		print('登入失敗')
		if chance > 0:
			print('你還有' ,chance, '次機會')
		else:
			print('沒機會嘗試了')