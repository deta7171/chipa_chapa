from flask import Flask, render_template
from db import DatabaseManager
from form import getTable

app = Flask(__name__)

bibaboba=0
@app.route('/')
def home():
    algebra=getTable('alg')
    namesForm=[]
    for el in algebra:
        item=[]
        item.append(algebra.index(el))
        item.append(el[2])
        namesForm.append(item)

    geometr=getTable('geom')
    namesForm1=[]
    for el in geometr:
        item=[]
        item.append(geometr.index(el))
        item.append(el[2])
        namesForm1.append(item)

    fiz=getTable('fiz')
    namesForm2=[]
    for el in fiz:
        item=[]
        item.append(fiz.index(el))
        item.append(el[2])
        namesForm2.append(item)

    inf=getTable('inf')
    namesForm3=[]
    for el in inf:
        item=[]
        item.append(inf.index(el))
        item.append(el[2])
        namesForm3.append(item)

    eco=getTable('eco')
    namesForm4=[]
    for el in eco:
        item=[]
        item.append(eco.index(el))
        item.append(el[2])
        namesForm4.append(item)

    chem=getTable('chem')
    namesForm5=[]
    for el in chem:
        item=[]
        item.append(chem.index(el))
        item.append(el[2])
        namesForm5.append(item)
    
    bio=getTable('bio')
    namesForm6=[]
    for el in bio:
        item=[]
        item.append(bio.index(el))
        item.append(el[2])
        namesForm6.append(item)

    geogr=getTable('geogr')
    namesForm7=[]
    for el in geogr:
        item=[]
        item.append(geogr.index(el))
        item.append(el[2])
        namesForm7.append(item)

    return render_template('elements.html',data=namesForm, data1=namesForm1, data2=namesForm2, data3=namesForm3, data4=namesForm4, data5=namesForm5, data6=namesForm6, data7=namesForm7)


@app.route('/algeb<index>')
def algebThema(index):
    algebra=getTable('alg')
    tema=algebra[int(index)]
    return render_template('formalgebra.html', tema = tema[2], form = tema[0], example = tema[1])


@app.route('/geometr<index>')
def geometrThema(index):
    geometr=getTable('geom')
    tema=geometr[int(index)]
    return render_template('formgeom.html', tema1 = tema[2], form1 = tema[0], example1 = tema[1])


@app.route('/fiz<index>')
def fizThema(index):
    fiz=getTable('fiz')
    tema=fiz[int(index)]
    
    return render_template('formfiz.html', tema2 = tema[2], form2 = tema[0], example2 = tema[1])


@app.route('/inf<index>')
def infThema(index):
    inf=getTable('inf')
    tema=inf[int(index)]
    
    return render_template('forminf.html', tema3 = tema[2], form3 = tema[0], example3 = tema[1])


@app.route('/eco<index>')
def ecoThema(index):
    eco=getTable('eco')
    tema=eco[int(index)]
    
    return render_template('formeco.html', tema4 = tema[2], form4 = tema[0], example4 = tema[1])

@app.route('/chem<index>')
def chemThema(index):
    chem=getTable('chem')
    tema=chem[int(index)]
    
    return render_template('formchem.html', tema5 = tema[2], form5 = tema[0], example5 = tema[1])

@app.route('/bio<index>')
def bioThema(index):
    bio=getTable('bio')
    tema=bio[int(index)]
    
    return render_template('formbio.html', tema6 = tema[2], form6 = tema[0], example6 = tema[1])

@app.route('/geogr<index>')
def geogrThema(index):
    geogr=getTable('geogr')
    tema=geogr[int(index)]
    
    return render_template('formgeog.html', tema7 = tema[2], form7 = tema[0], example7 = tema[1])


@app.route('/test')
def test():
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)