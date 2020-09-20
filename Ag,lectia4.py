#Problema 1
print('struguri      100      kg')
print('Mere      10      tone')
print('cartofi      250      kg')
print('Varză     1000      q')
#Problema 2
a=int(input('introduceti nr.a='))
b=int(input('introduceti nr.b='))
print ('suma numerilor este', a+b)
print ('diferenta numerilor este', a-b)
print ('catul impartirii numerilor este', a//b)
print ('restul numerilor este', a%b)
print ('produsul numerilor este', a*b)
print ('Ridicarea la putere numerilor este', a**b)
#PROBLEMA 3
l=int(input('introduceti lungimea laturii cubului='))
print('perimetrul suprafetei este', 4*l)
print('aria tuturor suprafete este', 6*l**2)
print('volumul este', l**3)
#problema 4
n=int(input('introduceti nr.natural='))
print('transformarea din metri in centimetri este',n*100)
print('transformarea din kg in mg este', n*1000000)
print('transformarea din ani in luni este',n*12 )
print('transformarea din ani in saptamini este', n*52)
print('transformarea din ani in zile este', n*365)
#problema 5
x = True
y = False
print ('x     y      x and y      x or y      not x')
print (x," " ,x," " ,x and x," " ,x or x, " " ,not x)
print (x," " ,y," " ,x and y," " ,x or y, " " ,not x)
print (y," " ,x," " ,y and x," " ,y or x, " " ,not y)
print (y," " ,y," " ,y and y," " ,y or y, " " ,not y)
#Prooblema 6
n=int(input('introduceti nr.natural='))
print ('Ultima cifră a acestui număr, {n} = ', n%10)
print ('Penultima cifră a acestui număr,{n} =' , n//10%10)
print ('Restul şi câtul împărţirii acestui număr la 9, {n} =' , n%9, 'si', n//9 )
