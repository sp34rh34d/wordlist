#!/usr/bin/env python3

years=['83','1983','15','16','17','18','19','20','21','22','23','24','25','26','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025','2026','2027','2028','2029','2030','2077']
months=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre','Honduras','Jesus','Jehova']
chars=['!','@','#','$','%','*','-','+','.','**','.*','*.','***','$#@','$@','$#','#$@',';','*;','++',';*','_','#@','#$','@$#','@#','@$','@@','$$','%%','$*','#*','#.','@.','@*','*$','*#','*@','##']
words=['Target','T4rg3t','T@rg3t','Targ3t','T4rget','T@rget']


def common():
	for month in months:
		for year in years:
			print(f"{month}{year}")
			for char in chars:
				print(f"{month}{year}{char}")
				print(f"{month}{char}{year}")

def target():
	for word in words:
		for year in years:
			print(f"{word}{year}")
			for char in chars:
				print(f"{word}{year}{char}")
				print(f"{word}{char}{year}")
				for char2 in chars:
					print(f"{word}{char}{year}{char2}")


target()
