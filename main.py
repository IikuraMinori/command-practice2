import calc_bmi

w = int(input('体重を入力:'))
h = int(input('身長を入力:')) / 100
print(calc_bmi.get_bmi(w, h))
