def notas (*n, sit=True):
    r= dict()
    r['total '] = len(n)
    r['maior'] = max(n)
    r['menor']= min(n)
    r['média']=sum(n)/len(n)
    if sit:
        if r['média'] >=7:
            r['situação'] = 'BOA'
        elif r ['média'] >=5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação']= 'RUIM'
    return r


resp= notas(5.5, 2.5, 8.5)
print(resp)
