file = open('test', 'r').readlines()[1:]

for i in file:
    name = i.strip().split('\t')[0]
    name1 = name.lower()
    kor = i.strip().split('\t')[1]
    it = str(i.strip().split('\t')[2])
    print('<tr>')
    print('<td onclick="window.location.href=\'https://potato-web-p8jl.onrender.com/cultivar/' + name1 + '\';" style="cursor: pointer;">' + name + '</td>')
    print('<td onclick="window.location.href=\'https://potato-web-p8jl.onrender.com/cultivar/' + name1 + '\';" style="cursor: pointer;">' + kor + '</td>')
    print('<td onclick="window.location.href=\'https://potato-web-p8jl.onrender.com/cultivar/' + name1 + '\';" style="cursor: pointer;">' + it + '</td>')
    print('<td>0</td>')
    print('</tr>')
