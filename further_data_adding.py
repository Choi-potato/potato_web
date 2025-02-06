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
    print("'"+ name + "'" + ' : {"name": "' + name + '", "korean_name": "' + korean_name + '", "it_number": "' + it_number + '", "yield": ' + str(yie) + ', "img": "' + img + '", "pedigree": "' + pedigree + '", "male": "' + male + '", "female": "' + female + '", "alt_name": "' + alt_name + '", "alt_english_name": "' + alt_english_name + '", "yield_graph": "' + yield_graph + '", "lw_graph": "' + lw_graph + '", "category": "' + category + '", "market": "' + market + '", "maturity": "' + maturity + '", "release_year": "' + release_year + '", "breeding_project": "' + breeding_project + '"},')
'''
    print('<tr>')
    print('\t' + '<td>' + name + '</td>')
    print('\t' + '<td>' + korean_name + '</td>')
    print('\t' + '<td>' + it_number + '</td>')
    print('\t' + '<td>' + str(yie) + '</td>')
    print('</tr>')
'''