print('\n PROGRAM SUHU \n')
print('CELCIUS \n')

celcius = float(input('Masukan Celcius = '))
print('Celcius = ',celcius)

reamur = (4/5) * celcius
print('Celcius to reamur = ',reamur)

kelvin = celcius + 273
print('Celcius to kelvin = ',kelvin)

farenhein = (9/5) * celcius + 32
print('Celcius to farenheint = ',farenhein)

print('\nREAMUR \n')

input_reamur = float(input('Masukan Reamur = '))

r_celcius = (5/4) * input_reamur
print('Reamur to celcius = ',r_celcius)

r_kelvin = kelvin * (5/4) * input_reamur + 273
print('Reamur to kelvin = ',r_kelvin)

r_farenheint = (9/4) * input_reamur + 32
print('Reamur to farenheint ',r_farenheint)

print('\nFARENHEINT \n')
input_farenheint = float(input('Masukan Farenheint = '))

f_celcius = 5/9 * (input_farenheint-32)
print('Farenheint to celcius = ',f_celcius)

f_reamur = 4/9 * (input_farenheint-32)
print('Farenheint to reamur = ',f_reamur)

f_kelvin = 5/9 * (input_farenheint - 32) + 273
print('Farenheint to kelvin = ',f_kelvin)

print('\nKELVIN \n')
input_kelvin = float(input('Masukan kelvin = '))

k_celcius = input_kelvin - 273
print('Kelvin to celcius = ',k_celcius)

k_reamur = 4/5 * (input_kelvin - 273)
print('Kelvin to reamur = ',k_reamur)

k_farenhein = 9/5 * (input_kelvin-273) + 32
print('Kelvin to farenheint = ',k_farenhein)

print('-----------------------------------------')
print('-----------------from--------------------')
print('----------- shegi-developer -------------')
