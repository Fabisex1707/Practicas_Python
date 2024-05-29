### Exersice Loops ###
"""""
number = 1
while number < 11:
    print(number)
    number+=1
else:
    print("The number is mayor than 10")

my_list=[1,2,3,4,5,6,7,8,9,10,11]

for element  in my_list:
    if element < 11:
        print(element)

else:
    print("The elemnt is mayor than 10")
    


number = 10
while number >= 0:
    print(number)
    number-=1
else:
    print("The number is minus than 0")


my_list=[1,2,3,4,5,6,7,8,9,10,11]

my_list.reverse()

for element  in my_list:
    if element > 0 and element <11:
        print(element)

else:
    print("The elemnt is Minus than 0 or it's mayor than 10")

symbol ="#"
while symbol != "########":
    print(symbol)
    symbol+= "#"
else:
    print("Ya quedo")


dgeyh=1

while dgeyh < 9:
    print("########")
    dgeyh+=1

numbre_one =0
numnber_two =0


while numbre_one < 11 and numbre_one <11:
    resul= numbre_one*numnber_two
    print(f"{numbre_one} x {numnber_two} = {resul}")
    numbre_one += 1
    numnber_two +=1

    

skills= ['Python', 'Numpy','Pandas','Django', 'Flask']

for element in skills:
    print(element)

    


numbers = list()
print(numbers)

sentinel = 0
while sentinel < 101:
    numbers.append(sentinel)
    sentinel += 1

print(numbers)

for element in numbers:
    if element % 2 == 0:
        print(element)


for element in numbers:
    if element % 2 != 0:
        print(element)
"""""
"""""
numbers = list()
print(numbers)

sentinel = 0
while sentinel < 101:
    numbers.append(sentinel)
    sentinel += 1

print(numbers)

sentinel =0
sum =0
for element in numbers:
    sum+=element

print(f"The sum of all numbers is {sum}")

sum_one =0
sum_two =0
for element in numbers:
    if element %2 ==0:
        sum_one += element
else:
    for element in numbers:
        if element %2 !=0:
            sum_two += element


print(f"The sum of all evens is {sum_one}. And the sum of all odds is {sum_two}.")
"""""

"""""
sum =0
for element in numbers:
    if element %2 !=0:
        sum += element
            

print(f"The sum of all numbers is {sum}")

"""""
""""
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
]



for element in countries:
    if "land" in element:
        print(element)

"""

fruit_list =['banana', 'orange', 'mango', 'lemon']


sentinel =0
while sentinel ==0:
    fruit_list.reverse()
    print(fruit_list)
    sentinel+=1








