from data_dls import data
def PlayerFinderWithName(func_name):
	data_list = []
	for player in data: 
		first_name = player.get("First Name","Bizda bunday futbolchi mavjud emas!Yoki futbolchi ismida imloviy xatolar qildingiz!")
		last_name = player.get("Last Name","Bizda bunday futbolchi mavjud emas!Yoki futbolchi ismida imloviy xatolar qildingiz!")
		func_name = func_name.lower()
		first_name = first_name.lower()
		last_name = last_name.lower()

		if first_name==func_name or last_name == func_name or f"{first_name}-{last_name}"==func_name or f"{last_name}-{first_name}"==func_name or f"{last_name} {first_name}"==func_name or f"{first_name} {last_name}"==func_name:
			ism = player.get("First Name","")
			familiya = player.get("Last Name","")
			narx = player.get("Price","")
			millat = player.get("Nationality","")
			klub = player.get("Club","")
			pozitsiya = player.get("Position","")
			oyoq = player.get("Foot","")
			baholanish = player.get("Rating","")
			boyi = player.get("Height (cm)","")
			tezlik = player.get("Speed","")
			tezlanish = player.get("Acceleration","")
			bardoshlilik = player.get("Stamina","")
			boshqaruv = player.get("Control","")
			kuch = player.get("Strength","")
			hal_qilish = player.get("Tackling","")
			pass_berish = player.get("Passing","")
			udar = player.get("Shooting","")
			rasm_id = player.get("Player ID")
			
			if rasm_id == "":rasm_id=False


			datas = [ism,familiya,narx,millat,klub,pozitsiya,oyoq,baholanish,boyi,tezlik,tezlanish,bardoshlilik,boshqaruv,kuch,hal_qilish,pass_berish,udar,rasm_id]
			
			data_list.append(datas)
	return data_list
def PlayerFinderWithStats(speed,acceleration,stamina,control,strength,tackling,passing,shooting):
	data_players = []
	updated_players_data = []
	for player in data: 
		speed1 = player.get("Speed","Bizda bunday futbolchi mavjud emas!Yoki futbolchi ismida imloviy xatolar qildingiz!")
		acceleration1 = player.get("Acceleration","Bizda bunday futbolchi mavjud emas!Yoki futbolchi ismida imloviy xatolar qildingiz!")
		stamina1 = player.get("Stamina","Bizda bunday futbolchi mavjud emas!Yoki futbolchi ismida imloviy xatolar qildingiz!")
		control1 = player.get("Control","Bizda bunday futbolchi mavjud emas!Yoki futbolchi ismida imloviy xatolar qildingiz!")
		strength1 = player.get("Strength","Bizda bunday futbolchi mavjud emas!Yoki futbolchi ismida imloviy xatolar qildingiz!")
		tackling1 = player.get("Tackling","Bizda bunday futbolchi mavjud emas!Yoki futbolchi ismida imloviy xatolar qildingiz!")
		passing1 = player.get("Passing","Bizda bunday futbolchi mavjud emas!Yoki futbolchi ismida imloviy xatolar qildingiz!")
		shooting1 = player.get("Shooting","Bizda bunday futbolchi mavjud emas!Yoki futbolchi ismida imloviy xatolar qildingiz!")
		a = False
		if speed==speed1 and acceleration == acceleration1 and   stamina==stamina1 and  control==control1 and strength==strength1 and tackling==tackling1 and passing1==passing and shooting==shooting1:
			ism = player.get("First Name","")
			familiya = player.get("Last Name","")
			data_players.append([ism,familiya])
			a=True 

		if not(a):
			try:

				if int(speed)-1==int(speed1):
					speed1=int(speed) 
				if int(speed)-2==int(speed1):
					speed1=int(speed) 
				if int(speed)-3==int(speed1):
					speed1=int(speed) 
				if int(speed)-4==int(speed1):
					speed1=int(speed) 
				if int(speed)-5==int(speed1):
					speed1=int(speed)

				if int(acceleration)-1==int(acceleration1):
					acceleration1=int(acceleration) 
				if int(acceleration)-2==int(acceleration1):
					acceleration1=int(acceleration)
				if int(acceleration)-3==int(acceleration1):
					acceleration1=int(acceleration)
				if int(acceleration)-4==int(acceleration1):
					acceleration1=int(acceleration)
				if int(acceleration)-5==int(acceleration1):
					acceleration1=int(acceleration)

				if int(stamina)-1==int(stamina1):
					stamina1=int(stamina)
				if int(stamina)-2==int(stamina1):
					stamina1=int(stamina)
				if int(stamina)-3==int(stamina1):
					stamina1=int(stamina)
				if int(stamina)-4==int(stamina1):
					stamina1=int(stamina)
				if int(stamina)-5==int(stamina1):
					stamina1=int(stamina)

				if int(control)-1==int(control1):
					control1=int(control)
				if int(control)-2==int(control1):
					control1=int(control)
				if int(control)-3==int(control1):
					control1=int(control)
				if int(control)-4==int(control1):
					control1=int(control)
				if int(control)-5==int(control1):
					control1=int(control)

				if int(stamina)-1==int(stamina1):
					stamina1=int(stamina)
				if int(stamina)-2==int(stamina1):
					stamina1=int(stamina)
				if int(stamina)-3==int(stamina1):
					stamina1=int(stamina)
				if int(stamina)-4==int(stamina1):
					stamina1=int(stamina)
				if int(stamina)-5==int(stamina1):
					stamina1=int(stamina)

				if int(strength)-1==int(strength1):
					strength1=int(strength)
				if int(strength)-2==int(strength1):
					strength1=int(strength)
				if int(strength)-3==int(strength1):
					strength1=int(strength)
				if int(strength)-4==int(strength1):
					strength1=int(strength)
				if int(strength)-5==int(strength1):
					strength1=int(strength)

				if int(tackling)-1==int(tackling1):
					tackling1=int(tackling)
				if int(tackling)-2==int(tackling1):					
					tackling1=int(tackling)
				if int(tackling)-3==int(tackling1):
					tackling1=int(tackling)
				if int(tackling)-4==int(tackling1):
					tackling1=int(tackling)
				if int(tackling)-5==int(tackling1):
					tackling1=int(tackling)


				if int(passing)-1==int(passing1):
					passing1=int(passing)
				if int(passing)-2==int(passing1):
					passing1=int(passing)
				if int(passing)-3==int(passing1):
					passing1=int(passing)
				if int(passing)-4==int(passing1):
					passing1=int(passing)
				if int(passing)-5==int(passing1):
					passing1=int(passing)


				if int(shooting)-1==int(shooting1):
					shooting1=int(shooting)
				if int(shooting)-2==int(shooting1):
					shooting1=int(shooting)
				if int(shooting)-3==int(shooting1):
					shooting1=int(shooting)
				if int(shooting)-4==int(shooting1):
					shooting1=int(shooting)
				if int(shooting)-5==int(shooting1):
					shooting1=int(shooting)

				speed=int(speed)
				speed1=int(speed1)
				acceleration=int(acceleration)
				acceleration1=int(acceleration1)
				stamina=int(stamina)
				stamina1=int(stamina1)
				control=int(control)
				control1=int(control1)
				strength=int(strength)
				strength1=int(strength1)
				tackling=int(tackling)
				tackling1=int(tackling1)
				passing=int(passing)
				passing1=int(passing1)
				shooting=int(shooting)
				shooting1=int(shooting1)
				if speed==speed1 and acceleration==acceleration and stamina==stamina1 and control==control1 and strength==strength1 and tackling==tackling1 and passing1==passing and shooting==shooting1:
					ism = player.get("First Name")
					familiya = player.get("Last Name")
					updated_players_data.append([ism,familiya])
			except Exception as e:pass#print(e)	

	return data_players,updated_players_data
if __name__ == '__main__':
	
	# data_player = PlayerFinderWithName("Lionel-Messi")
	data_player,updated_players_data = PlayerFinderWithStats("94","87","80","82","91","51","78","95")
	print(data_player,updated_players_data)






		
 