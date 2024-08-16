#ejercios de listas
#creando una lista
#con la funcion list()

lst = list()

#con corchetes

lst = []

# funcion len() para saber cuantos elementos tiene la lista

fruits = ['banana','orange','mango', 'lemon']
print(fruits)
print('Numero de frutas:', len(fruits))

# la lista puede contener diferentres tipos de datos

lst = ['Abel', 36, True,{'contry':'Mexico', 'city':'Puebla'}]

#acceder a una lista de manera positiva

fruits = ['banana','orange','mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)

##acceder a una lista de manera negativa

fruits = ['banana','orange','mango', 'lemon']
first_fruit = fruits[-4]
print(first_fruit)

#Desembalaje de elmentos de la lista

# Primer ejemplo
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# segundo ejemplo
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# tercer ejemplo
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

#cortando elementos de una lista

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
print(all_fruits)
all_fruits = fruits[0:]
print(all_fruits)#de ambas formas obtienes todos los elementos de la lista
orange_and_mango = fruits[1:3]
print(orange_and_mango)#solo obtienes dos elementos de la lista

#cortando elementos de una lista con indexacion negativa

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]#retorna todos los elementos de la lista
print(all_fruits)
orange_and_mango = fruits[-3:-1]
print(orange_and_mango) #retorna dos elementos de la lista

#modificando una lista

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)  

#tambien se puede de manera negativa
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits) 

#checar elementos de una lista on in

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist) 

#agregar elementos a una lista append()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits) 

#insertar elementos a una lista insert()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insertara apple entre orange y mango
print(fruits)           
fruits.insert(3, 'lime')   # insertara ime entre apple y mango
print(fruits)

# remover elementos de una lista con remove()

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)
fruits.remove('lemon')
print(fruits)

# remover elementos usando pop()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)  #si no se especifica el valor eliminara el ultimo elemento
fruits.pop(0)
print(fruits)    #aqui se especifica y elimina el primer elemento

#removiendo usando Del

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)      #elimina el primer elemento
del fruits[1]
print(fruits)       #elimina el segundo elemento
del fruits[1:3]     # elimina los elementos entre el indice 1 a 3
print(fruits)       # ['orange', 'lime']
del fruits
#print(fruits)       # Esto deberia dar: NameError: name 'fruits' is not defined


# limpiando elementos de una lista clear()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

#copiando una lista copy()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy) 

# Uniendo listas
# Opedador +

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)

# agregando una lista a otra metodo extend()

num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers.extend(zero)  # cada que se agrega una lista la listo original se modifica
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)

# encontrar elementos de una lista, es decir cuantas veces esta ese elemento en la lista

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))  
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))  

#encontrar el indice de una lista, este encontara la primer ocurrencia

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))     

# invertir los elementos en una lista

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) 
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

# ordenar elementos de una lista usando sort(), esta acccion modifica la lista

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits) 
fruits.sort(reverse=True)
print(fruits)

# ordenando una lista usando sorted(), esta accion no modifica la lista

fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True) #con reverse = true ordena la lista de manera invertida
print(fruits)    

# ejercicios

# 1- declara una lista
hija_menor = ['Odette', 2, 'mexicana']

# 2- declara una lista con 5 elementos
hija_mayor = ['Veronica', 9, 'mexicana', 'Cuarto de primaria', 'Jugar minecraf']

# 3- encuentra length de tu lista
print(len(hija_mayor))

#4- obten los elementos: primero, de en medio y ultimo
hija_mayor = ['Veronica', 9, 'mexicana', 'Cuarto de primaria', 'Jugar minecraf']
primer_valor, segundo_valor, tercer_valor, cuarto_valor, quinto_valor = hija_mayor
print(primer_valor)
print(tercer_valor)
print(quinto_valor)

#5- declara una lista
mixed_data_types = ['Abel', 36, 1.68, 'casado', 'Mexico']

#6 delcara una lista
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']

#7. imprime la lista
print(it_companies)

#8. imprime el numero de it en la lista
print(len(it_companies))

 #9 impimer primero, de en medio y ultimo
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

#10.imprime la lista despues de modificarla
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
it_companies[0] = 'acer'
print(it_companies)

# 11. agrega una it
it_companies.append('BLACKCAT')
print(it_companies)

#12. inserta una it en medio de la lista
it_companies.insert(4, 'Dell')
print(it_companies)

#13. Cambie uno de los nombres de it_companies a mayúsculas
print(it_companies[0].swapcase())

#14. Únase a it_companies con una cadena '#;  '
result = '#; '.join(it_companies)
print(result)

#15. Compruebe si una determinada empresa existe en la lista
does_exist = 'HP' in it_companies
print(does_exist)

#16. Ordenar la lista usando el método sort()
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.sort()
print(it_companies)

#17. Ordenar la lista al reves usando el método sort() 
it_companies.sort(reverse=...)
print(it_companies)

#18. Elimine las primeras 3 empresas de la lista
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle',  'Amazon']
del it_companies[0:3]
print(it_companies)

#19. Elimine las últimas 3 empresas de la lista
del it_companies[1:4]
print(it_companies)

#20. Elimine la empresa o empresas de TI intermedias de la lista
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle',  'Amazon']
del it_companies[3]
print(it_companies)

#21. Elimina el primer elemento de la lista
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle',  'Amazon']
it_companies.remove('Facebook')
print(it_companies)

#22. Eliminar la empresa o empresas de TI intermedias de la lista
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle',  'Amazon']
it_companies.pop(3)
print(it_companies)

#23. Eliminar la última empresa de TI de la lista
it_companies.pop(5)
print(it_companies)

#24. Eliminar todas las empresas de TI de la lista
limpiar_lista = it_companies.clear()
print('lista:',it_companies)

#25. elimina la lista
del it_companies




#26 join list
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
result = ' '.join(full_stack)
print(result)

#ejercicios nivel 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
first_ages = ages[0]
print(first_ages)
last_ages = ages[-1]
print(last_ages)
print(ages)
print(len(ages))
first_num = ages[4]
secon_num = ages[5]
suma_1 = int(first_num)
suma_2 = int(secon_num)
edad_media = (suma_1 + suma_2) / 2
print(edad_media)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
a,b,c,d,e,f,g,h,i,j = ages
promedio = (a+b+c+d+e+f+g+h+i+j)/10
print(promedio)
ages.sort()
rango_max = ages[-1]
rango_min = ages[0]
rango = rango_max - rango_min
print(rango)
comparacion = abs(rango_max - rango_min)
print(comparacion)
com_pro = abs((a+b+c+d+e+f+g+h+i+j)/10)
print(com_pro)

#contries

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
print(len(countries))
print(int(len(countries))/2)
middle = countries[96]
print(middle)
list_one = countries[0:95]
print(list_one)
list_two = countries[96:193]
print(list_two)

new_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch,rs,usa,*scanic = new_countries
print(scanic)



