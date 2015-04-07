from flask import render_template, json
from app import app, db, models
from .models import Element
from sqlalchemy import func
import subprocess

@app.route('/')
@app.route('/index')
def index():
    return render_template('Index.html')


@app.route('/api/<name>')
@app.route('/api/element/<name>')
def api_handling(name):
    if name == 'element':
        return handle_element()
    else:
        return handle_individual_element(name)


@app.route('/models/<name>')
def models(name=1):
    e = Element.query.get(1)
    return e.element


@app.route('/about')
def about():
    return render_template('Groups.html')


@app.route('/group/<name>')
def group(name=None):
    if name == 'alkali':
        return render_template('alkaliLayout.html', name=name)
    elif name == 'alkaline-earth':
        return render_template('alkalinearthLayout.html', name=name)
    elif name == 'halogen':
        return render_template('halogenLayout.html', name=name)
    else:
        return "Page not found!"


@app.route('/element/<name>')
def element(name=None):
    if name == 'helium':
        return render_template('Helium.html', name=name)
    elif name == 'hydrogen':
        return render_template('Hydrogen.html', name=name)
    elif name == 'fluorine':
        return render_template('Fluorine.html', name=name)
    else:
        return "Page not found!"


@app.route('/period/<name>')
def period(name=None):
    if name == '1':
        return render_template('periodLayout.html', name=name, period_num=name)
    elif name == '2':
        return render_template('periodLayout.html', name=name, period_num=name)
    elif name == '3':
        return render_template('periodLayout.html', name=name, period_num=name)    
    if name == '4':
        return render_template('periodLayout.html', name=name, period_num=name)
    elif name == '5':
        return render_template('periodLayout.html', name=name, period_num=name)
    elif name == '6':
        return render_template('periodLayout.html', name=name, period_num=name)    
    if name == '7':
        return render_template('periodLayout.html', name=name, period_num=name)
    elif name == '8':
        return render_template('periodLayout.html', name=name, period_num=name)
    else:
        return "Page not found!"


@app.route('/tests/')
def run_tests_executor():
    return render_template("tests_executor.html")

@app.route('/testexecute/')
def run_tests():
    #os.system("./tests.py 2> output.txt")
    p = subprocess.Popen(['./tests.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,err = p.communicate()
    print(err)
    return render_template('tests.html', name=err)


#api handlers
def handle_element():
    elements = list(Element.query.all())
    result_list = []
    column_names = []
    for c in Element.__table__.columns:
        column_names.append(str(c).split("elements.")[1])    

    for element in elements:
        d = dict()
        for c_name in column_names:
            d[c_name] = element.__dict__[c_name]
        result_list.append(d)
    
    return json.dumps(result_list)
        
def handle_individual_element(element_symbol):
    element = Element.query.filter(func.lower(Element.symbol)==func.lower(element_symbol)).first()
    result_list = []    

    column_names = []
    for c in Element.__table__.columns:
        column_names.append(str(c).split("elements.")[1])
        
    d = dict()
    for c_name in column_names:
        d[c_name] = element.__dict__[c_name]

    result_list.append(d)
    return json.dumps(result_list)
