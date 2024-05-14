"""""
#### Lists ###
#List: is a collection which is ordered and changeable(MODIFIABLE). Allows duplicate members.
lst_one=list() #this is the way to create a list 1
print(len(lst_one)) #items=0 list is empty

lst_two=[] # this is the way you can fiil it 2
print(len(lst_two)) #items=0 list is empty

"""
lst_one=list()#here we're creating it
lst_one=["Fabian","Castro",18,1.5,"Fabisex"]#here we're filling it 
print(lst_one)
print(len(lst_one))
print(lst_one[0])
print(lst_one[2])
print(lst_one[3])
mixed_data_types =list()
mixed_data_types=["Fabian",18,1.50,"singel","Pino de arizona #323"]
it_companies=list()
it_companies =["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(mixed_data_types)
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[3])
print(it_companies[4])
print(it_companies)
it_companies[3]="Opera"
print(it_companies)
it_companies.insert(7,"Google")
print(it_companies)
it_companies[3]="tata consultancy services"
print(it_companies)
print(it_companies[0].upper())
##print(it_companies+"#;  ")
print(it_companies)
it_companies.sort()#here we're ordening the list whith sort(), but sort() ordening things with a alphabetical order
print(it_companies)#here we're watching the oder with sort()
it_companies.sort(reverse=True)#If an argument of sort() method reverse is equal to TRUE, it will arrange the list in descending order.
print(it_companies)###descending order
print(it_companies[0:3])
print(it_companies[3])
it_companies.remove("tata consultancy services") 
it_companies.pop(3)
del it_companies[4]
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies #here we're destroying the it_companies list jkhdfjkshfkj

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end+back_end)
full_stack=front_end+back_end
print(type(full_stack))

full_stack.append("Python")
full_stack.append("SQL")
print(full_stack)
full_stack.append("Redux")
print(full_stack)
ages=list()
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] 
ages.sort() #order min to max
print(ages)
print(ages[4:5])
print("the number in the middel is: ",((24+24)/2))
print("the average is:",228/len(ages))
print("the Range of the ages is:",26-19)
print(abs(16-22.8))# aqui vemos el valor ABSOLUTO de la resta osea lo spunto de cimal 
print(abs(26-22.8))
ages.sort(reverse=True)#order max to min
print(ages)

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
print(len(countries))
countries.sort()
print(countries)
print(countries[97])
list_one=countries[0:97]
print(len(list_one))
list_two=countries[97:193]
print(len(list_two))
countries_two=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(countries_two.pop(0))
print(countries_two.pop(0))
print(countries_two.pop(0))
print(countries_two)





