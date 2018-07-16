import vk_api
from time import sleep
from datetime import datetime
import options as o

def date():
	global dat
	dat = datetime.strftime(datetime.now(), "[%Y.%m.%d][%H:%M:%S]")

vk = vk_api.VkApi(o.login, o.password)
try:
	date()
	print('{}[Попытка авторизации...]'.format(dat)) 
	vk.auth() #авторизация
	date()
	print('{}[Авторизация прошла успешно!]'.format(dat))
except vk_api.exceptions.BadPassword:
	date()   
	print('{}[Ошибка авторизации!][Неверный пароль.]'.format(dat))	
	exit(0)

postidlist1 = vk.method('wall.get', {'owner_id':o.man_id, 'count':1, 'offset':o.offset}) #получаем последний пост
postid1 = postidlist1['items'][0]['id']	

while True: #зацикливаем
	date()   
	print('{}[Ожидание новых постов в группе...]'.format(dat))
	try:
		postidlist2 = vk.method('wall.get', {'owner_id':o.man_id, 'count':1, 'offset':o.offset}) #получаем последний пост снова
		postid2 = postidlist2['items'][0]['id']
	except Exception:
		date()
		print('{}[Ошибка проверки постов в группе!]'.format(dat))
	if postid1 != postid2:
		try:
			vk.method('wall.createComment', {'owner_id':o.man_id, 'post_id':postid2, 'message':o.mess})
			postid1 = postid2
			date()   
			print('{}[Оставлен комментарий в группе.]'.format(dat))
		except Exception:
			date()
			print('{}[Не удалось оставить комментарий!]'.format(dat))
	sleep(2)


