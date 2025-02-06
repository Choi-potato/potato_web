#Data adding for app.py and cultivar_list.html

file = open('test', 'r').readlines()[1:]

for i in file:
    contents = i.strip().split('\t')
    name = contents[0]
    korean_name = contents[1]
    it_number = contents[2]
    yie =0 
    img = 'potatoes/' + name + '.png'
    pedigree = 'pedigree/' + name + '.png'
    pedigree2 = 'pedigree/' + name + '2.png'
    pedigree3 = 'pedigree/' + name + '3.png'
    alt_name = contents[6]
    alt_english_name = contents[7]
    male = contents[8]
    female = contents[9]
    yield_graph = 'graph/' + name + '_yield.png'
    lw_graph = 'graph/' + name + '_lw.png'
    category = contents[10]
    market = contents[11]
    maturity = contents[12]
    release_year = str(contents[13])
    breeding_project = contents[14]
    male_male = contents[15]
    male_female = contents[16]
    female_male = contents[17]
    female_female = contents[18]
    male_male_male = contents[19]
    male_male_female = contents[20]
    male_female_male = contents[21]
    male_female_female = contents[22]
    female_male_male = contents[23]
    female_male_female = contents[24]
    female_female_male = contents[25]
    female_female_female = contents[26]
    print("'"+ name + "'" + ' : {"name": "' + name + '", "korean_name": "' + korean_name + '", "it_number": "' + it_number + '", "yield": ' + str(yie) + ', "img": "' + img + '", "pedigree": "' + pedigree + '", "pedigree2": "' + pedigree2 + '", "pedigree3": "' + pedigree3 + '", "male": "' + male + '", "female": "' + female + '", "alt_name": "' + alt_name + '", "alt_english_name": "' + alt_english_name + '", "yield_graph": "' + yield_graph + '", "lw_graph": "' + lw_graph + '", "category": "' + category + '", "market": "' + market + '", "maturity": "' + maturity + '", "release_year": "' + release_year + '", "breeding_project": "' + breeding_project + '", "male_male": "' + male_male + '", "male_female": "' + male_female + '", "female_male": "' + female_male + '", "female_female": "' + female_male + '", "female_female": "' + female_female + '", "male_male_male": "' + male_male_male + '", "male_male_female": "' + male_male_female + '", "male_female_male": "' + male_female_male + '", "male_female_female": "' + male_female_female + '", "female_male_male": "' + female_male_male + '", "female_male_female": "' + female_male_female + '", "female_female_male": "' + female_female_male + '", "female_female_female": "' + female_female_female + '"},')
'''
    print('<tr>')
    print('\t' + '<td>' + name + '</td>')
    print('\t' + '<td>' + korean_name + '</td>')
    print('\t' + '<td>' + it_number + '</td>')
    print('\t' + '<td>' + str(yie) + '</td>')
    print('</tr>')
'''