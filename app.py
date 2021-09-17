import webbrowser
import sqlite3
from datetime import datetime
import random
import pandas as pd
import time
from sqlalchemy import create_engine
import io
import xlwt
import psycopg2
import psycopg2.extras
# from Autobo.Auth import main
# from Autobo import db
from flask import render_template, request, redirect, url_for, flash, session, Response, jsonify
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError, ProgrammingError
from sqlalchemy import func


# url = 'http://127.0.0.1:5000/'


# Windows
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# webbrowser.get(chrome_path).open(url)

#Auth/__init__.py
import os.path
# from flask import Blueprint

main = ('main', __name__)

#autobo/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# def create_app(config_type):

    # app = Flask(__name__)
    # configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    # #'C:\\Users\\ppasha\\PycharmProjects\\GESBO\\config\\dev,py'
    # app.config.from_pyfile(configuration)
    # db.init_app(app)
    #
    # from Autobo.Auth import main  #import Blueprint
    # app.register_blueprint(main)  #register Blueprint
    # app.app_context().push()
    # return app
    
ALLOWED_HOSTS = ['https://appbo.azurewebsites.net']

main = Flask(__name__, template_folder='templates')

# main.config.update(
#     SECRET_KEY = 'topsecret',
#     # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost/auto_bo',
#     SQLALCHEMY_TRACK_MODIFICATIONS = True
# )
# //its9010290/cae_root/cae_data/GES BO/GES_BO_DB/ges.db;

main.config['SECRET_KEY']='topsecret'
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auto_bo.db'
# main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////its9010290/cae_root/cae_data/GES BO/auto_bo.db'
main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# conn = create_engine("sqlite:///its9010290\\cae_root\\cae_data\\GES BO\\auto_bo.db")

# from Autobo import create_app, db
db = SQLAlchemy(main)



# from flask_wtf.file import FileField
# from wtforms import SubmitField
# from flask_wtf import Form

if __name__ == '__main__':
    # flask_app = create_app('dev')
    # with flask_app.app_context():
    #     db.create_all()
    # flask_app.run()

    # conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)

    engine = create_engine("sqlite:///auto_bo.db")
    conn = engine = create_engine("sqlite:///auto_bo.db")
    conn= engine.raw_connection()
    cursor = conn.cursor()
    # conn = psycopg2.connect(dbname='auto_bo', user='postgres', password='1234', host='localhost')




# @main.route('/')
# def display_auths():
#     auths = Auths.query.all()
#     return render_template('front.html', auths=auths)

# dd= pd.pipe(display_rm, engine)
#
# dd.to_excel("demo.xlsx")



@main.route('/rmtesting')
def rmtesting():
    # rmtesta = Rmtest11.query.all()
    rmtesta = db.session.query(Rmtest11.id, Rmtest11.cdsid, Rmtest11.name, Rmtest11.company, Rmtest11.gender,
                              Rmtest11.billing_status, Rmtest11.project,
                              Rmtest11.project_name, Rmtest11.seating_location, Rmtest11.pm_cdsid, Rmtest11.lm_cdsid,
                              Rmtest11.job_family,
                              Rmtest11.month_of_joining_ges, Rmtest11.previous_experience, Rmtest11.project_ll5_cdsid,
                              Rmtest11.grade,
                              Rmtest11.workstation_number, Rmtest11.education, Rmtest11.education_details,
                              Rmtest11.funding_organisation, Rmtest11.funding_function, Rmtest11.funding_region,
                              Rmtest11.phase, Rmtest11.attribute, Rmtest11.product, Rmtest11.process,
                              Rmtest11.method_domain, Rmtest11.name, Rmtest11.tmm,
                              Rmtest11.primary_tool, Rmtest11.level, Rmtest11.remarks, easset4.COMPUTER_NAME,
                              easset4.BLUE_DOLLAR_CONFIGURATION).select_from(Rmtest11).join(easset4).all()
    for rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, \
        rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, rmtest11, \
        rmtest11, rmtest11, rmtest11, Easset4, Easset4 in rmtesta:

       return render_template('test.html', rmtesta=rmtesta)



@main.route('/rmlive1')
def rmlive1():
    # rmlive3=Rmlive3
    rmlivea = Rmlive4.query.all()
    print(rmlivea)
    return render_template('rmlive.html', rmlivea=rmlivea)

@main.route('/eassettest')
def results():

    rrpage13=Rrpage13
    # Pcrenew12=pcrenew12
    # engine5 = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/auto_bo").connect()
    engine5 = create_engine("sqlite:///auto_bo.db")

    # engine6 = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/auto_bo").connect()

    livea= pd.read_sql_table('rrpage13',engine5)
    print(livea.head)

    liveb= pd.read_sql_table('pcrenew12',engine5)
    print(liveb.head)

    ablive = pd.merge(livea,liveb, left_on='it_request_number', right_on='Request_Number')
    engine.dispose()
    return render_template('eassettest.html',ablive=ablive)



@main.route('/')
def index_rm():
    return render_template('index.html')

@main.route('/front')
def display_rm():
    # rmtestall = Rmtest11.query.all()
    # rmtest11 = Rmtest11
    # Easset3 = easset3
    engine = create_engine("sqlite:///auto_bo.db")
    conn = engine = create_engine("sqlite:///auto_bo.db")
    conn = engine.raw_connection()
    cursor = conn.cursor()

    rmtest = db.session.query(Rmtest11.id, Rmtest11.cdsid, Rmtest11.name, Rmtest11.company, Rmtest11.gender,Rmtest11.billing_status, Pmtest3.dorf_id,
                              Pmtest3.project_name, Rmtest11.seating_location,Pmtest3.pm_cdsid,Pmtest3.lm_cdsid,Pmtest3.project_category,Pmtest3.project_subcategory,
                              Rmtest11.job_family,
                              Rmtest11.month_of_joining_ges,Rmtest11.previous_experience,Rmtest11.project_ll5_cdsid,Rmtest11.grade,
                              Rmtest11.workstation_number,Rmtest11.education,Rmtest11.education_details,Pmtest3.funding_organisation, Pmtest3.funding_function, Rmtest11.funding_region,
                              Rmtest11.phase, Rmtest11.attribute, Rmtest11.product,Rmtest11.process, Rmtest11.method_domain, Rmtest11.name, Rmtest11.tmm,
                              Rmtest11.primary_tool, Rmtest11.level, Rmtest11.remarks,easset4.COMPUTER_NAME,easset4.BLUE_DOLLAR_CONFIGURATION).select_from(Rmtest11).join(easset4).join(Pmtest3).all()
    for rmtest11, rmtest11, rmtest11, rmtest11, rmtest11,rmtest11,pmtest3,pmtest3,pmtest3,pmtest3,pmtest3,pmtest3,pmtest3,pmtest3,rmtest11,rmtest11,\
        rmtest11,rmtest11,rmtest11,rmtest11,rmtest11,rmtest11, rmtest11, rmtest11,rmtest11, rmtest11, rmtest11,rmtest11, rmtest11, rmtest11, rmtest11,\
        rmtest11, rmtest11, rmtest11,Easset4, Easset4 in rmtest:

        df = pd.DataFrame(rmtest, columns=['id','cdsid', 'name','company','gender','billing_status','dorf_id',
                              'project_name', 'seating_location','pm_cdsid','lm_cdsid','project_category','project_subcategory','job_family',
                              'month_of_joining_ges','previous_experience','project_ll5_cdsid','grade',
                              'workstation_number','education','education_details','funding_organisation', 'funding_function', 'funding_region',
                              'phase', 'attribute', 'product','process', 'method_domain', 'name', 'tmm',
                              'primary_tool', 'level', 'remarks','COMPUTER_NAME','BLUE_DOLLAR_CONFIGURATION']);
        # excelPath = "./rmexcel.xls"

        writer = pd.ExcelWriter(time.strftime('RM_PM_ %Y-%m-%d-%H-%S.xlsx'))

        df.to_excel(writer,'sheet1', index=False)
        writer.save();

        return render_template('front.html',rmtest=rmtest)




@main.route('/test')
def display_rm_pm():
    # rmtestall = Rmtest11.query.all()
    # rmtest11 = Rmtest11
    # Easset3 = easset3

    rmtest = db.session.query(Rmtest11.id, Rmtest11.cdsid, Rmtest11.name, Rmtest11.company, Rmtest11.gender,Rmtest11.billing_status, Pmtest3.dorf_id,
                              Pmtest3.project_name,Pmtest3.project_category, Rmtest11.seating_location,Rmtest11.pm_cdsid,Rmtest11.lm_cdsid,Rmtest11.job_family,
                              Rmtest11.month_of_joining_ges,Rmtest11.previous_experience,Rmtest11.project_ll5_cdsid,Rmtest11.grade,
                              Rmtest11.workstation_number,Rmtest11.education,Rmtest11.education_details,Rmtest11.funding_organisation, Rmtest11.funding_function, Rmtest11.funding_region,
                              Rmtest11.phase, Rmtest11.attribute, Rmtest11.product,Rmtest11.process, Rmtest11.method_domain, Rmtest11.name, Rmtest11.tmm,
                              Rmtest11.primary_tool, Rmtest11.level, Rmtest11.remarks,easset4.COMPUTER_NAME,easset4.BLUE_DOLLAR_CONFIGURATION).select_from(Rmtest11).join(easset4).join(Pmtest3).all()
    for rmtest11, rmtest11, rmtest11, rmtest11, rmtest11,rmtest11,pmtest3,pmtest3,pmtest3,rmtest11,rmtest11,rmtest11,rmtest11,rmtest11,rmtest11,rmtest11,rmtest11,rmtest11,\
        rmtest11,rmtest11,rmtest11, rmtest11, rmtest11,rmtest11, rmtest11, rmtest11,rmtest11, rmtest11, rmtest11, rmtest11,\
        rmtest11, rmtest11, rmtest11,Easset4, Easset4 in rmtest:
        #
            df = pd.DataFrame(rmtest, columns=['id','cdsid', 'name','company','gender','billing_status','dorf_id',
                                  'project_name', 'project_category','seating_location','pm_cdsid','lm_cdsid','job_family',
                                  'month_of_joining_ges','previous_experience','project_ll5_cdsid','grade',
                                  'workstation_number','education','education_details','funding_organisation', 'funding_function', 'funding_region',
                                  'phase', 'attribute', 'product','process', 'method_domain', 'name', 'tmm',
                                  'primary_tool', 'level', 'remarks','COMPUTER_NAME','BLUE_DOLLAR_CONFIGURATION']);
            # excelPath = "./rmexcel.xls"

            writer = pd.ExcelWriter(time.strftime('RM_PM_EAST %Y-%m-%d-%H-%S.xlsx'))

            df.to_excel(writer,'sheet1', index=False);
            # print(df.head)
            # writer.close()
            return render_template('test.html',rmtest=rmtest, df=df)

@main.route('/dfmerge')
def dftestmerge():
    rmfinal1=Rmfinal1
    # Easset4=easset4
    # Eassetfinal1= eassetfinal1
    pmfinal=Pmfinal

    # engine1 = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/auto_bo").connect()
    engine1 = create_engine("sqlite:///auto_bo.db")

    # engine2 = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/auto_bo").connect()
    engine2 = create_engine("sqlite:///auto_bo.db")

    daaf = pd.read_sql_table('rmfinal1', engine1)
    print(daaf.head)

    edaaf = pd.read_sql_table('eassetfinal1', engine2)

    pdaaf = pd.read_sql_table('pmfinal', engine1)
    print(pdaaf.head)
    double_daaf = pd.merge(daaf,edaaf, left_on='cdsid', right_on='DEVICE_USER_CDSID')

    tridaaf = pd.merge(double_daaf,pdaaf, left_on='project',right_on='dorf_id')
    print(double_daaf.head)
    engine.dispose()
    return render_template('dfmerge.html',double_daaf=double_daaf, tridaaf=tridaaf)


@main.route('/easset')
def resultsa():
    rmtest11 = Rmtest11
    Easset4 = easset4

    resultsa = db.session.query(Rmtest11.cdsid,Rmtest11.company, Pmtest3.project_name, Pmtest3.dorf_id, Pmtest3.cbg, easset4.COMPUTER_NAME,
                               easset4.BLUE_DOLLAR_CONFIGURATION).select_from(Rmtest11).join(easset4).join(Pmtest3).all()
    for rmtest11,rmtest11, pmtest3,pmtest3,pmtest3, Easset4, Easset4 in resultsa:

        return render_template('easset.html', resultsa=resultsa)


@main.route('/rmfree')
def rmtestb():
    # rmtestb = Rmtest11.query.all()
    # return render_template('rmtesting.html', rmtestb=rmtestb)
    engine = create_engine("sqlite:///auto_bo.db")
    conn = engine = create_engine("sqlite:///auto_bo.db")
    conn= engine.raw_connection()
    cursor = conn.cursor()

    cur = conn.cursor()
    s = "SELECT * FROM Rmtest11"
    cur.execute(s) # Execute the SQL
    rmtestba = cur.fetchall()
    return render_template('rmtesting.html', rmtestba=rmtestba)
#
@main.route('/edita/<int:id>', methods=['POST', 'GET'])
def edit_rm(id):
    conn = engine.raw_connection()

    cur = conn.cursor()
    selectquery = "SELECT * FROM Rmtest11"
    cur.execute(selectquery)
    dataa = cur.fetchone()
    for data in dataa:
        print(data)
    return render_template('rmedit.html', dataa=dataa)

@main.route('/update/<id>', methods=['POST'])
def update_rm(id):

    conn = engine.raw_connection()

    cur = conn.cursor()
    if request.method == 'POST':
        cdsid = request.form['cdsid']
        name = request.form['name']
        company = request.form['company']
        gender = request.form['gender']
        billing_status = request.form['billing_status']
        project = request.form['project']
        project_name = request.form['project_name']

        cur.execute("""
            UPDATE Rmtest11
            SET cdsid = ?,
                name = ?,
                company = ?,
                gender = ?,
                billing_status = ?,
                project = ?,
                project_name = ?
            WHERE id = ?
        """, (cdsid, name, company, gender, billing_status, project, project_name, id))
        flash('Updated Successfully')
        cur.commit()
        return redirect(url_for('index_rm'))


@main.route('/bopage', methods=["GET","POST"])
def bopage_rr():
    engine = create_engine("sqlite:///auto_bo.db")
    conn = engine = create_engine("sqlite:///auto_bo.db")
    conn = engine.raw_connection()
    cursor = conn.cursor()

    cur = conn.cursor()
    s = "SELECT * FROM Rrpage13"
    cur.execute(s) # Execute the SQL
    rrtest = cur.fetchall()
    return render_template('bopage.html', rrtest=rrtest)

@main.route('/edit/<id>', methods=['POST', 'GET'])
def get_edit(id):
    conn = engine.raw_connection()

    cur = conn.cursor()
    cur.execute('SELECT * FROM Rrpage13 WHERE id = ?')
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', data=data)

@main.route('/updatebo/<id>', methods=['POST'])
def update_bo(id):
    if request.method == 'POST':
        it_request_number = request.form['it_request_number']
        unshare_it_req_number = request.form['unshare_it_req_number']
        it_connect_stage = request.form['it_connect_stage']
        bo_status = request.form['bo_status']
        remarks = request.form['remarks']

        conn = engine.raw_connection()

        cur = conn.cursor()
        cur.execute("""
            UPDATE Rrpage13
            SET it_request_number = ?,
                unshare_it_req_number = ?,
                it_connect_stage = ?,
                bo_status = ?,
                remarks = ?
            WHERE id = ?
        """, (it_request_number, unshare_it_req_number, it_connect_stage, bo_status, remarks, id))
        flash('Updated Successfully')
        conn.commit()
        return redirect(url_for('index_rm'))



@main.route('/delete_bo/<id>/', methods=['GET', 'POST'])
def delete_bo(id):
    my_data = Rrpage13.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")
    return redirect(url_for('index_rm'))

# @main.route('/edit/<id>', methods=['GET','POST'])
# def edit(id):
#
#     if request.method == 'POST':
#             my_data = Rrpage13.query.filter_by(id).first()
#             my_data.it_request_number = request.form['it_request_number']
#             my_data.unshare_it_req_number = request.form['unshare_it_req_number']
#             my_data.it_connect_stage = request.form['it_connect_stage']
#             my_data.bo_status = request.form['bo_status']
#             my_data.remarks = request.form['remarks']
#
#             db.session.commit()
#             # return redirect(url_for('main.edit/'+id))
#
#     return render_template('bopage.html',my_data=my_data)

@main.route('/livebopage')
def bopage_r1():
    # rrpage13=Rrpage13
    # # Pcrenew12=pcrenew12
    # engine5 = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/auto_bo").connect()
    # # engine6 = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/auto_bo").connect()
    #
    # livea= pd.read_sql_table('rrpage13',engine5)
    # print(livea.head)
    #
    # liveb= pd.read_sql_table('pcrenew12',engine5)
    # print(liveb.head)
    #
    # ablive = pd.merge(livea,liveb, left_on='it_request_number', right_on='Request_Number')
    # engine.dispose()


    rrtestbo = db.session.query(Rrpage13.cdsid, Rrpage13.pm_request_time, Rrpage13.request_type, Rrpage13.new_assert_type,
                              Rrpage13.service_tag, pcrenew12.Status, pcrenew12.Request_Number, pcrenew12.Assigned_Group_QueueName).select_from(pcrenew12).join(Rrpage13).all()
    for rrpage13, rrpage13, rrpage13, rrpage13, rrpage13, Pcrenew12, Pcrenew12, Pcrenew12 in rrtestbo:

        return render_template('bopage2.html',rrtestbo=rrtestbo)


@main.route('/importxl')
def importxl():

    engine3 = create_engine("sqlite:///auto_bo.db").connect()

    with pd.ExcelFile('Book1.xlsx') as xls:
        dfxl = pd.read_excel(xls)
        dfxl.to_sql(name='rmtest11', con=engine, if_exists='replace', index=False)

    # with pd.ExcelFile('PCRenewalReport11.xlsx') as xls:
    #     dfpcxl = pd.read_excel(xls)
    #     dfpcxl.to_sql(name='pcrenew12', con=engine, if_exists='replace', index=False)
    #
    # with pd.ExcelFile('Projectmaster.xlsx') as xls:
    #     dfpmxl = pd.read_excel(xls)
    #     dfpmxl.to_sql(name='pmtest3', con=engine, if_exists='replace', index=False)

    engine.dispose()

    return render_template('index.html',dfxl=dfxl)


@main.route('/importxlpm')
def importxlpm():
    engine3 = create_engine("sqlite:///auto_bo.db").connect()

    with pd.ExcelFile('Projectmaster.xlsx') as xls:
        dfpmxl = pd.read_excel(xls)
        dfpmxl.to_sql(name='pmtest3', con=engine, if_exists='replace', index=False)

    engine.dispose()

    return render_template('index.html', dfpmxl=dfpmxl)

@main.route('/importxlpcrenew')
def importxlpcrenew():
    engine3 = create_engine("sqlite:///auto_bo.db").connect()

    with pd.ExcelFile('PCRenewalReport11.xlsx') as xls:
        dfpcxl = pd.read_excel(xls)
        dfpcxl.to_sql(name='pcrenew12', con=engine, if_exists='replace', index=False)
    engine.dispose()

    return render_template('index.html', dfpcxl=dfpcxl)


@main.route('/importrmlive1xl')
def importrmlive1xl():
    # rmfinal1=Rmfinal1
    engine5 = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/auto_bo").connect()

    with pd.ExcelFile('live2_rm.xlsx') as xls:
        dfrmxl = pd.read_excel(xls)
        dfrmxl.to_sql(name='rmlive4', con=engine, if_exists='replace', index=False)

    engine.dispose()

    return render_template('index.html',dfrmxl=dfrmxl)

@main.route('/importeassetxl')
def importeassetxl():
    engine = create_engine("sqlite:///auto_bo.db").connect()

    with pd.ExcelFile('Easset.xlsx') as xls:
        df = pd.read_excel(xls)
        dot = df.rename(columns={'SERIAL NUMBER': 'SERIAL_NUMBER', 'DEVICE USER CDSID': 'DEVICE_USER_CDSID',
                                 'FORD MANAGER': 'FORD_MANAGER',
                                 'COMPUTER NAME': 'COMPUTER_NAME', 'SLS LAST USER': 'SLS_LAST_USER',
                                 'BLUE DOLLAR CONFIGURATION': 'BLUE_DOLLAR_CONFIGURATION',
                                 'LAST LOG DATE': 'LAST_LOG_DATE', 'DEVICE STATUS': 'DEVICE_STATUS',
                                 'LOCATION DESCRIPTION': 'LOCATION_DESCRIPTION',
                                 'LEASE END DATE': 'LEASE_END_DATE'})
        # print(dot)
        # fkey = ForeignKey
        # if fkey is None:
        #     pass
        # dot[df.duplicated('DEVICE_USER_CDSID', keep=False)]
        # posta = pd.read_sql('SELECT cdsid FROM rmtest13', con=engine)
        # dot = posta.ix['cdsid':'DEVICE_USER_CDSID']

        dot.to_sql(name='easset4', con=engine, if_exists='replace', index=False)

    # with pd.ExcelFile('Easset.xlsx') as xls:
    #     dfeasset = pd.read_excel(xls)
    #     dfeasset.to_sql(name='eassetfinal', con=engine, if_exists='replace', index=False)
        return render_template('index.html',dot=dot)


# this route is for inserting data to database via html forms
@main.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        id = request.form['id']
        cdsid = request.form['cdsid']
        name = request.form['name']
        company = request.form['company']
        gender = request.form['gender']
        billing_status = request.form['billing_status']
        project = request.form['project']
        project_name = request.form['project_name']
        seating_location = request.form['seating_location']
        pm_cdsid= request.form['pm_cdsid']
        lm_cdsid= request.form['lm_cdsid']
        job_family= request.form['job_family']
        month_of_joining_ges= request.form['month_of_joining_ges']
        year_of_joining_ges= request.form['year_of_joining_ges']
        previous_experience= request.form['previous_experience']
        modified= request.form['modified']
        modified_by= request.form['modified_by']
        project_ll5_cdsid= request.form['project_ll5_cdsid']
        grade= request.form['grade']
        workstation_number= request.form['workstation_number']
        education= request.form['education']
        education_details= request.form['education_details']
        item_type= request.form['item_type']
        path= request.form['path']
        funding_organisation= request.form['funding_organisation']
        funding_function= request.form['funding_function']
        funding_region= request.form['funding_region']
        phase= request.form['phase']
        attribute= request.form['attribute']
        product= request.form['product']
        process= request.form['process']
        method_domain= request.form['method_domain']
        tmm= request.form['tmm']
        primary_tool= request.form['primary_tool']
        level= request.form['level']
        remarks= request.form['remarks']
        wb= request.form['wb']
        aaa= request.form['aaa']
        project2= request.form['project2']
        cbg= request.form['cbg']
        discipline= request.form['discipline']
        column1= request.form['column1']
        month_year_joining= request.form['month_year_joining']
        ges_experience= request.form['ges_experience']
        total_experience= request.form['total_experience']
        column2= request.form['column2']

        my_data = Rmtest11(id, cdsid, name, company, gender, billing_status, project, project_name, seating_location, pm_cdsid, lm_cdsid, job_family, month_of_joining_ges,
        year_of_joining_ges, previous_experience, modified, modified_by, project_ll5_cdsid, grade, workstation_number, education, education_details,
        item_type, path, funding_organisation, funding_function, funding_region, phase, attribute, product, process, method_domain, tmm, primary_tool,
        level, remarks, wb, aaa, project2, cbg, discipline, column1, month_year_joining, ges_experience, total_experience, column2)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for('main.display_rm'))

    # This route is for deleting our employee
@main.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Rmtest11.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('main.display_rm'))


@main.route('/search')
def search():
    return render_template('search.html')

@main.route('/precheck')
def index():
    return render_template('precheck.html')

@main.route("/ajaxlivesearch",methods=["POST","GET"])
def ajaxlivesearch():
    engine = create_engine("sqlite:///auto_bo.db")
    conn = engine = create_engine("sqlite:///auto_bo.db")
    conn = engine.raw_connection()
    cursor = conn.cursor()

    cur = conn.cursor()
    if request.method == 'POST':
        search_word = request.form['query']
        print(search_word)
        if search_word == '':
            query = "SELECT * from Rmlive4 ORDER BY id"
            cur.execute(query)
            Rmlive4 = cur.fetchone()

        else:
            cur.execute('SELECT * FROM Rmlive4 WHERE cdsid LIKE %(cdsid)s', { 'cdsid': '%{}%'.format(search_word)})
            numrows = int(cur.rowcount)
            Rmlive4 = cur.fetchall()

            print(numrows)
    return jsonify({'htmlresponse': render_template('response.html', Rmlive4=Rmlive4, numrows=numrows)})


@main.route('/rrmpage')
def testrrmpage():
    rtest = Rrpage13.query.all()
    return render_template('rrpage.html', rtest=rtest)

@main.route('/rpage')
def rpage():
    rtest = db.session.query(Rrpage13.id,Rrpage13.requestor_cdsid,Rrpage13.cdsid, Rrpage13.ll6_cdsid, Rrpage13.pm_request_time, Rrpage13.request_type,
                             Rrpage13.new_assert_type, Rrpage13.new_location ,Rrpage13.service_tag ,Rrpage13.sharing ,Rrpage13.unshare,
                             pcrenew12.Request_Number, pcrenew12.Status, pcrenew12.Assigned_Group_QueueName).select_from(pcrenew12).join(Rrpage13).all()
    for rrpage13, rrpage13, rrpage13, rrpage13, rrpage13,rrpage13,rrpage13,rrpage13,rrpage13,rrpage13,rrpage13, Pcrenew12, Pcrenew12, Pcrenew12 in rtest:
        return render_template('bopage2.html', rrtest=rtest)
    rtest = Rrpage13.query.all()
    return render_template('rrpage.html', rtest=rtest)

@main.route('/mrpage')
def testrpage():
    return render_template('mrpage.html')

@main.route('/mrpage', methods=['POST'])
def mrpage():
    if request.method == 'POST':
        requestor_cdsid = None
        cdsid = request.form['cdsid']
        ll6_cdsid = None
        pm_request_time = None
        request_type = request.form['request_type']
        new_location = request.form['new_location']
        new_assert_type = request.form['new_assert_type']
        service_tag = request.form['service_tag']
        sharing = request.form['sharing']
        unshare = request.form.getlist('unshare')
        it_request_number = None
        unshare_it_req_number = None
        it_req_raisedby = None
        it_connect_stage= None
        bo_status= None
        remarks= None
        if unshare == 'yes':
            unshare=('yes')
        else:
            unshare=('no')
        if sharing == 'true':
            sharing= (True)
        else:
            sharing= (False)
        if cdsid == '' or request_type == '':
            return render_template('mrpage.html', message='Please fill fields to place request')
        if db.session.query(Rrpage13).filter(Rrpage13.cdsid == cdsid).count()==0:
            data = Rrpage13(requestor_cdsid,cdsid,ll6_cdsid,pm_request_time, request_type, new_location, new_assert_type, service_tag, sharing,unshare,
                           it_request_number, unshare_it_req_number,it_req_raisedby,it_connect_stage,bo_status,remarks)
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('index_rm'))
        return render_template('mrpage.html', message='Requested check your email for Status')




@main.route('/pm/<int:page_num>')
def pm_call(page_num):
    pmall = Pmfinal.query.paginate(per_page = 100, page = page_num, error_out=True)
    return render_template('pmlive.html', pmall=pmall)




@main.route('/insertpm', methods=['POST'])
def insertpm():
    if request.method == 'POST':

        fecode = request.form['fecode']
        project_name = request.form['project_name']
        dorf_id = request.form['dorf_id']
        cbg = request.form['cbg']
        customer_contact = request.form['customer_contact']
        csat_customer_contact = request.form['csat_customer_contact']
        customer_contact_secondary = request.form['customer_contact_secondary']
        project_manager = request.form['project_manager']
        manager = request.form['manager']
        actual_forecast= request.form['actual_forecast']
        project_subcategory= request.form['project_subcategory']
        project_category= request.form['project_category']
        discipline= request.form['discipline']
        pm_cdsid= request.form['pm_cdsid']
        lm_cdsid= request.form['lm_cdsid']
        ll5_cdsid= request.form['ll5_cdsid']
        po_value= request.form['po_value']
        currency= request.form['currency']
        po_number_sow_number= request.form['po_number_sow_number']
        year= request.form['year']
        csr_required= request.form['csr_required']
        jan_offshore= request.form['jan_offshore']
        jan_onsite= request.form['jan_onsite']
        feb_offshore= request.form['feb_offshore']
        feb_onsite= request.form['feb_onsite']
        mar_offshore= request.form['mar_offshore']
        mar_onsite= request.form['mar_onsite']
        apr_offshore= request.form['apr_offshore']
        apr_onsite= request.form['apr_onsite']
        may_offshore= request.form['may_offshore']
        may_onsite= request.form['may_onsite']
        jun_offshore= request.form['jun_offshore']
        jun_onsite= request.form['jun_onsite']
        jul_offshore= request.form['jul_offshore']
        jul_onsite= request.form['jul_onsite']
        aug_offshore= request.form['aug_offshore']
        aug_onsite= request.form['aug_onsite']
        sep_offshore= request.form['sep_offshore']
        sep_onsite= request.form['sep_onsite']
        oct_offshore= request.form['oct_offshore']
        oct_onsite= request.form['oct_onsite']
        nov_offshore= request.form['nov_offshore']
        nov_onsite= request.form['nov_onsite']
        dec_offshore= request.form['dec_offshore']
        dec_onsite= request.form['dec_onsite']
        pd_non_pd= request.form['pd_non_pd']
        acc_code= request.form['acc_code']
        gsdb_code= request.form['gsdb_code']
        sub_acct_code= request.form['sub_acct_code']
        po_received_date= request.form['po_received_date']
        previous_year_dorfid= request.form['previous_year_dorfid']
        quote_submission_date= request.form['quote_submission_date']
        dept_cost_center= request.form['dept_cost_center']
        remarks= request.form['remarks']
        funding_function= request.form['funding_function']
        funding_organisation= request.form['funding_organisation']

        my_datapm = Pmtest3(fecode, project_name, dorf_id, cbg, customer_contact, csat_customer_contact, customer_contact_secondary, project_manager,
                           manager, actual_forecast, project_subcategory, project_category, discipline, pm_cdsid, lm_cdsid, ll5_cdsid, po_value, currency,
                           po_number_sow_number, year, csr_required, jan_offshore, jan_onsite, feb_offshore, feb_onsite, mar_offshore, mar_onsite,
                           apr_offshore, apr_onsite, may_offshore, may_onsite, jun_offshore, jun_onsite, jul_offshore, jul_onsite, aug_offshore,
                           aug_onsite, sep_offshore, sep_onsite, oct_offshore, oct_onsite, nov_offshore, nov_onsite, dec_offshore, dec_onsite, pd_non_pd,
                           acc_code, gsdb_code, sub_acct_code, po_received_date, previous_year_dorfid, quote_submission_date, dept_cost_center, remarks,
                           funding_function, funding_organisation)
        db.session.add(my_datapm)
        db.session.commit()

        flash("Pm Inserted Successfully")

        return redirect(url_for('main.pm_call'))






class Auths(db.Model):
    __tablename__ = 'auths'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

    def __init__(self,id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'Auth is {}'.format(self.name)


class Rrpage3(db.Model):
    __tablename__ = 'rrpage3'

    id = db.Column(db.Integer, primary_key=True)
    # requestor_cdsid = db.Column(db.String, primary_key=True)
    cdsid = db.Column(db.String(80))
    # ll6_cdsid = db.Column(db.String, primary_key = True)
    # pm_request_time = db.Column(db.DateTime, default=datetime.utcnow(), primary_key=True)
    request_type = db.Column(db.String(80))
    new_location = db.Column(db.String(80))
    new_assert_type = db.Column(db.String(80))
    service_tag=db.Column(db.String(80))
    sharing = db.Column(db.Boolean)
    # unshare = db.Column(db.String, primary_key=True)

    def __init__(self, cdsid, request_type, new_location, new_assert_type, service_tag, sharing):
        # self.requestor_cdsid = requestor_cdsid
        self.cdsid = cdsid
        # self.ll6_cdsid = ll6_cdsid
        # self.pm_request_time = pm_request_time
        self.request_type= request_type
        self.new_location= new_location
        self.new_assert_type = new_assert_type
        self.service_tag= service_tag
        self.sharing = sharing
        # self.unshare = unshare

class Rrpage2(db.Model):
    __tablename__ = 'rrpage2'

    id = db.Column(db.Integer, primary_key=True)
    requestor_cdsid = db.Column(db.String)
    cdsid = db.Column(db.String(80))
    ll6_cdsid = db.Column(db.String)
    pm_request_time = db.Column(db.DateTime, default=datetime.utcnow())
    request_type = db.Column(db.String(80))
    new_location = db.Column(db.String(80))
    new_assert_type = db.Column(db.String(80))
    service_tag = db.Column(db.String(80))
    sharing = db.Column(db.Boolean)
    unshare = db.Column(db.String)

    def __init__(self, requestor_cdsid, cdsid, ll6_cdsid, pm_request_time, request_type, new_location, new_assert_type, service_tag, sharing, unshare):

        self.requestor_cdsid = requestor_cdsid
        self.cdsid = cdsid
        self.ll6_cdsid = ll6_cdsid
        self.pm_request_time = pm_request_time
        self.request_type = request_type
        self.new_location = new_location
        self.new_assert_type = new_assert_type
        self.service_tag = service_tag
        self.sharing = sharing
        self.unshare = unshare


class easset3(db.Model):
    __tablename__ = 'easset3'

    id = db.Column(db.Integer, primary_key=True)
    Row_Number = db.Column(db.Integer)
    SERIAL_NUMBER = db.Column(db.String)
    DEVICE_USER_CDSID = db.Column(db.String, db.ForeignKey('rmtest11.cdsid'))
    FORD_MANAGER= db.Column(db.String)
    COMPUTER_NAME= db.Column(db.String)
    SLS_LAST_USER = db.Column(db.String)
    BLUE_DOLLAR_CONFIGURATION = db.Column(db.String)
    LAST_LOG_DATE = db.Column(db.Date)
    DEVICE_STATUS = db.Column(db.String)
    LOCATION_DESCRIPTION = db.Column(db.String)
    COMPUTER_MODEL = db.Column(db.String)
    BLDG_CODE = db.Column(db.Integer)
    EQUIPMENT_TYPE = db.Column(db.String)
    FIRST_LOG_DATE = db.Column(db.Date)
    INSTALL_DATE = db.Column(db.Date)
    LEASE_END_DATE= db.Column(db.Date)
    SUPERVISOR_CDSID= db.Column(db.String)
    TRANSFER_STATUS= db.Column(db.String)
    EMPLOYEE_TYPE= db.Column(db.String)
    DEVICE_TYPE= db.Column(db.String)
    LEASE_TERM = db.Column(db.String)
    SLS_BLDG_CODE= db.Column(db.String)
    TICKET_NUMBER= db.Column(db.String)

    def __init__(self,Row_Number,SERIAL_NUMBER,DEVICE_USER_CDSID,FORD_MANAGER,COMPUTER_NAME,SLS_LAST_USER,BLUE_DOLLAR_CONFIGURATION,
                 LAST_LOG_DATE,DEVICE_STATUS,LOCATION_DESCRIPTION,COMPUTER_MODEL,BLDG_CODE,EQUIPMENT_TYPE,FIRST_LOG_DATE,INSTALL_DATE,
                 LEASE_END_DATE,SUPERVISOR_CDSID,TRANSFER_STATUS,EMPLOYEE_TYPE,DEVICE_TYPE,LEASE_TERM,SLS_BLDG_CODE, TICKET_NUMBER):

        self.Row_Number = Row_Number
        self.SERIAL_NUMBER= SERIAL_NUMBER
        self.DEVICE_USER_CDSID = DEVICE_USER_CDSID
        self.FORD_MANAGER = FORD_MANAGER
        self.COMPUTER_NAME = COMPUTER_NAME
        self.SLS_LAST_USER = SLS_LAST_USER
        self.BLUE_DOLLAR_CONFIGURATION = BLUE_DOLLAR_CONFIGURATION
        self.LAST_LOG_DATE = LAST_LOG_DATE
        self.DEVICE_STATUS = DEVICE_STATUS
        self.LOCATION_DESCRIPTION = LOCATION_DESCRIPTION
        self.COMPUTER_MODEL = COMPUTER_MODEL
        self.BLDG_CODE = BLDG_CODE
        self.EQUIPMENT_TYPE = EQUIPMENT_TYPE
        self.FIRST_LOG_DATE = FIRST_LOG_DATE
        self.INSTALL_DATE = INSTALL_DATE
        self.LEASE_END_DATE = LEASE_END_DATE
        self.SUPERVISOR_CDSID = SUPERVISOR_CDSID
        self.TRANSFER_STATUS = TRANSFER_STATUS
        self.EMPLOYEE_TYPE = EMPLOYEE_TYPE
        self.DEVICE_TYPE = DEVICE_TYPE
        self.LEASE_TERM = LEASE_TERM
        self.SLS_BLDG_CODE = SLS_BLDG_CODE
        self.TICKET_NUMBER = TICKET_NUMBER


class easset5(db.Model):
    __tablename__ = 'easset5'

    id = db.Column(db.Integer, primary_key=True)
    SERIAL_NUMBER = db.Column(db.String)
    DEVICE_USER_CDSID = db.Column(db.String)
    FORD_MANAGER= db.Column(db.String)
    COMPUTER_NAME= db.Column(db.String)
    SLS_LAST_USER = db.Column(db.String)
    BLUE_DOLLAR_CONFIGURATION = db.Column(db.String)
    LAST_LOG_DATE = db.Column(db.Date)
    DEVICE_STATUS = db.Column(db.String)
    LOCATION_DESCRIPTION = db.Column(db.String)
    LEASE_END_DATE= db.Column(db.Date)

    def __init__(self,SERIAL_NUMBER,DEVICE_USER_CDSID,FORD_MANAGER,COMPUTER_NAME,SLS_LAST_USER,BLUE_DOLLAR_CONFIGURATION,
                 LAST_LOG_DATE,DEVICE_STATUS,LOCATION_DESCRIPTION,LEASE_END_DATE):

        self.SERIAL_NUMBER= SERIAL_NUMBER
        self.DEVICE_USER_CDSID = DEVICE_USER_CDSID
        self.FORD_MANAGER = FORD_MANAGER
        self.COMPUTER_NAME = COMPUTER_NAME
        self.SLS_LAST_USER = SLS_LAST_USER
        self.BLUE_DOLLAR_CONFIGURATION = BLUE_DOLLAR_CONFIGURATION
        self.LAST_LOG_DATE = LAST_LOG_DATE
        self.DEVICE_STATUS = DEVICE_STATUS
        self.LOCATION_DESCRIPTION = LOCATION_DESCRIPTION
        self.LEASE_END_DATE = LEASE_END_DATE


class Rmlive4(db.Model):
    __tablename__ = 'rmlive4'

    cdsid = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80))
    company = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    billing_status = db.Column(db.String(80))
    project = db.Column(db.Float)
    project_name = db.Column(db.String(200))
    pm_cdsid = db.Column(db.String(80))
    lm_cdsid = db.Column(db.String(80))
    job_family = db.Column(db.String(80))
    month_of_joining_ges = db.Column(db.Integer)
    year_of_joining_ges = db.Column(db.Integer)
    previous_experience = db.Column(db.Float)
    project_ll5_cdsid = db.Column(db.String(80))
    grade = db.Column(db.String(80))
    education = db.Column(db.String(80))
    education_details = db.Column(db.String(80))
    funding_organisation = db.Column(db.String(80))
    funding_function = db.Column(db.String(80))
    funding_region = db.Column(db.String(80))
    phase = db.Column(db.String(80))
    attribute = db.Column(db.String(80))
    product = db.Column(db.String(80))
    process = db.Column(db.String(80))
    method_domain = db.Column(db.String(80))
    tmm = db.Column(db.String(80))
    primary_tool = db.Column(db.String(80))
    level = db.Column(db.String(80))
    MDL_Access = db.Column(db.String(80))
    GTBC_location= db.Column(db.String(80))
    Status= db.Column(db.String(80))
    Request_center_location= db.Column(db.String(80))
    GTBC_final_location= db.Column(db.String(80))
    Final_service_tag= db.Column(db.String(80))
    Final_asset_type= db.Column(db.Integer)
    Seat_count= db.Column(db.String(80))
    Sharing_Y_N2= db.Column(db.String(80))
    Fixed_Sharing= db.Column(db.String(80))
    Building= db.Column(db.String(80))
    Floor= db.Column(db.String(80))
    Seat= db.Column(db.String(80))
    Count= db.Column(db.Integer)
    WB= db.Column(db.Integer)
    Request_center_service_tag= db.Column(db.String(80))
    Service_tag= db.Column(db.String(80))
    Asset_type= db.Column(db.String(80))
    Req_center_asset_type= db.Column(db.String(80))
    Length= db.Column(db.String(80))
    Dual_Signle_Asset= db.Column(db.String(80))
    Machine_Count= db.Column(db.Integer)
    Project_ID2= db.Column(db.Integer)
    Discipline= db.Column(db.String(80))

    def __init__(self,cdsid, name, company, gender, billing_status, project, project_name, pm_cdsid, lm_cdsid, job_family, month_of_joining_ges,
    year_of_joining_ges, previous_experience,  project_ll5_cdsid, grade, education, education_details,
    funding_organisation, funding_function, funding_region, phase, attribute, product, process, method_domain, tmm, primary_tool,
    level, MDL_Access, GTBC_location, Status, Request_center_location,GTBC_final_location,Final_service_tag, Final_asset_type,Seat_count,
    Sharing_Y_N2,Fixed_Sharing,Building,Floor,Seat,Count,WB,Request_center_service_tag,Service_tag,Asset_type,Req_center_asset_type,
    Length,Dual_Signle_Asset,Machine_Count,Project_ID2,Discipline):

        self.cdsid = cdsid
        self.name= name
        self.company= company
        self.gender=gender
        self.billing_status= billing_status
        self.project= project
        self.project_name= project_name
        self.pm_cdsid=pm_cdsid
        self.lm_cdsid= lm_cdsid
        self.job_family=job_family
        self.month_of_joining_ges=month_of_joining_ges
        self.year_of_joining_ges=year_of_joining_ges
        self.previous_experience=previous_experience
        self.project_ll5_cdsid=project_ll5_cdsid
        self.grade=grade
        self.education=education
        self.education_details=education_details
        self.funding_organisation=funding_organisation
        self.funding_function=funding_function
        self.funding_region=funding_region
        self.phase=phase
        self.attribute=attribute
        self.product=product
        self.process=process
        self.method_domain=method_domain
        self.tmm=tmm
        self.primary_tool=primary_tool
        self.level=level
        self.MDL_Access=MDL_Access
        self.GTBC_location=GTBC_location
        self.Status=Status
        self.Request_center_location=Request_center_location
        self.GTBC_final_location=GTBC_final_location
        self.Final_service_tag=Final_service_tag
        self.Final_asset_type=Final_asset_type
        self.Seat_count=Seat_count
        self.Sharing_Y_N2=Sharing_Y_N2
        self.Fixed_Sharing=Fixed_Sharing
        self.Building=Building
        self.Floor=Floor
        self.Seat=Seat
        self.Count=Count
        self.WB=WB
        self.Request_center_service_tag=Request_center_service_tag
        self.Service_tag=Service_tag
        self.Asset_type=Asset_type
        self.Req_center_asset_type=Req_center_asset_type
        self.Length=Length
        self.Dual_Signle_Asset=Dual_Signle_Asset
        self.Machine_Count=Machine_Count
        self.Project_ID2=Project_ID2
        self.Discipline=Discipline


class Rmfinal1(db.Model):
    __tablename__ = 'rmfinal1'

    id = db.Column(db.Integer, primary_key=True)
    cdsid = db.Column(db.String(80))
    name = db.Column(db.String(80))
    company = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    billing_status = db.Column(db.String(80))
    project = db.Column(db.Float)
    project_name = db.Column(db.String(200))
    seating_location = db.Column(db.String(80))
    pm_cdsid = db.Column(db.String(80))
    lm_cdsid = db.Column(db.String(80))
    job_family = db.Column(db.String(80))
    month_of_joining_ges = db.Column(db.Integer)
    year_of_joining_ges = db.Column(db.Integer)
    previous_experience = db.Column(db.Float)
    modified = db.Column(db.DateTime)
    modified_by = db.Column(db.String(80))
    project_ll5_cdsid = db.Column(db.String(80))
    grade = db.Column(db.String(80))
    workstation_number = db.Column(db.String(80))
    education = db.Column(db.String(80))
    education_details = db.Column(db.String(80))
    item_type = db.Column(db.String(80))
    path = db.Column(db.String(80))
    funding_organisation = db.Column(db.String(80))
    funding_function = db.Column(db.String(80))
    funding_region = db.Column(db.String(80))
    phase = db.Column(db.String(80))
    attribute = db.Column(db.String(80))
    product = db.Column(db.String(80))
    process = db.Column(db.String(80))
    method_domain = db.Column(db.String(80))
    tmm = db.Column(db.String(80))
    primary_tool = db.Column(db.String(80))
    level = db.Column(db.String(80))
    remarks = db.Column(db.String(80))
    wb = db.Column(db.Integer)
    aaa = db.Column(db.Integer)
    project2 = db.Column(db.Integer)
    cbg = db.Column(db.String(80))
    discipline = db.Column(db.String(80))
    column1 = db.Column(db.String(80))
    month_year_joining = db.Column(db.String)
    ges_experience = db.Column(db.Float)
    total_experience = db.Column(db.Float)
    column2 = db.Column(db.String(80))


    def __init__(self,id,cdsid, name, company, gender, billing_status, project, project_name, seating_location, pm_cdsid, lm_cdsid, job_family, month_of_joining_ges,
    year_of_joining_ges, previous_experience, modified, modified_by, project_ll5_cdsid, grade, workstation_number, education, education_details,
    item_type, path, funding_organisation, funding_function, funding_region, phase, attribute, product, process, method_domain, tmm, primary_tool,
    level, remarks, wb, aaa, project2, cbg, discipline, column1, month_year_joining, ges_experience, total_experience, column2):

        self.id = id
        self.cdsid = cdsid
        self.name= name
        self.company= company
        self.gender=gender
        self.billing_status= billing_status
        self.project= project
        self.project_name= project_name
        self.seating_location=seating_location
        self.pm_cdsid=pm_cdsid
        self.lm_cdsid= lm_cdsid
        self.job_family=job_family
        self.month_of_joining_ges=month_of_joining_ges
        self.year_of_joining_ges=year_of_joining_ges
        self.previous_experience=previous_experience
        self.modified=modified
        self.modified_by=modified_by
        self.project_ll5_cdsid=project_ll5_cdsid
        self.grade=grade
        self.workstation_number=workstation_number
        self.education=education
        self.education_details=education_details
        self.item_type=item_type
        self.path=path
        self.funding_organisation=funding_organisation
        self.funding_function=funding_function
        self.funding_region=funding_region
        self.phase=phase
        self.attribute=attribute
        self.product=product
        self.process=process
        self.method_domain=method_domain
        self.tmm=tmm
        self.primary_tool=primary_tool
        self.level=level
        self.remarks=remarks
        self.wb=wb
        self.aaa=aaa
        self.project2=project2
        self.cbg=cbg
        self.discipline=discipline
        self.column1=column1
        self.month_year_joining=month_year_joining
        self.ges_experience=ges_experience
        self.total_experience=total_experience
        self.column2=column2


class Rmtest11(db.Model):
    __tablename__ = 'rmtest11'

    id = db.Column(db.Integer, primary_key=True)
    cdsid = db.Column(db.String(80), primary_key=True, unique=True)
    name = db.Column(db.String(80))
    company = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    billing_status = db.Column(db.String(80))
    project = db.Column(db.Float, unique=True)
    project_name = db.Column(db.String(200))
    seating_location = db.Column(db.String(80))
    pm_cdsid = db.Column(db.String(80))
    lm_cdsid = db.Column(db.String(80))
    job_family = db.Column(db.String(80))
    month_of_joining_ges = db.Column(db.Integer)
    year_of_joining_ges = db.Column(db.Integer)
    previous_experience = db.Column(db.Float)
    modified = db.Column(db.DateTime)
    modified_by = db.Column(db.String(80))
    project_ll5_cdsid = db.Column(db.String(80))
    grade = db.Column(db.String(80))
    workstation_number = db.Column(db.String(80))
    education = db.Column(db.String(80))
    education_details = db.Column(db.String(80))
    item_type = db.Column(db.String(80))
    path = db.Column(db.String(80))
    funding_organisation = db.Column(db.String(80))
    funding_function = db.Column(db.String(80))
    funding_region = db.Column(db.String(80))
    phase = db.Column(db.String(80))
    attribute = db.Column(db.String(80))
    product = db.Column(db.String(80))
    process = db.Column(db.String(80))
    method_domain = db.Column(db.String(80))
    tmm = db.Column(db.String(80))
    primary_tool = db.Column(db.String(80))
    level = db.Column(db.String(80))
    remarks = db.Column(db.String(80))
    wb = db.Column(db.Integer)
    aaa = db.Column(db.Integer)
    project2 = db.Column(db.Integer)
    cbg = db.Column(db.String(80))
    discipline = db.Column(db.String(80))
    column1 = db.Column(db.String(80))
    month_year_joining = db.Column(db.String)
    ges_experience = db.Column(db.Float)
    total_experience = db.Column(db.Float)
    column2 = db.Column(db.String(80))


    def __init__(self,id,cdsid, name, company, gender, billing_status, project, project_name, seating_location, pm_cdsid, lm_cdsid, job_family, month_of_joining_ges,
    year_of_joining_ges, previous_experience, modified, modified_by, project_ll5_cdsid, grade, workstation_number, education, education_details,
    item_type, path, funding_organisation, funding_function, funding_region, phase, attribute, product, process, method_domain, tmm, primary_tool,
    level, remarks, wb, aaa, project2, cbg, discipline, column1, month_year_joining, ges_experience, total_experience, column2):

        self.id = id
        self.cdsid = cdsid
        self.name= name
        self.company= company
        self.gender=gender
        self.billing_status= billing_status
        self.project= project
        self.project_name= project_name
        self.seating_location=seating_location
        self.pm_cdsid=pm_cdsid
        self.lm_cdsid= lm_cdsid
        self.job_family=job_family
        self.month_of_joining_ges=month_of_joining_ges
        self.year_of_joining_ges=year_of_joining_ges
        self.previous_experience=previous_experience
        self.modified=modified
        self.modified_by=modified_by
        self.project_ll5_cdsid=project_ll5_cdsid
        self.grade=grade
        self.workstation_number=workstation_number
        self.education=education
        self.education_details=education_details
        self.item_type=item_type
        self.path=path
        self.funding_organisation=funding_organisation
        self.funding_function=funding_function
        self.funding_region=funding_region
        self.phase=phase
        self.attribute=attribute
        self.product=product
        self.process=process
        self.method_domain=method_domain
        self.tmm=tmm
        self.primary_tool=primary_tool
        self.level=level
        self.remarks=remarks
        self.wb=wb
        self.aaa=aaa
        self.project2=project2
        self.cbg=cbg
        self.discipline=discipline
        self.column1=column1
        self.month_year_joining=month_year_joining
        self.ges_experience=ges_experience
        self.total_experience=total_experience
        self.column2=column2

# class Rmtest11_2(db.Model):
#     __tablename__ = 'Rmtest11_2'
#
#     id = db.Column(db.Integer, primary_key=True)
#     cdsid = db.Column(db.String(80), primary_key=True, unique=True)
#     name = db.Column(db.String(80))
#     company = db.Column(db.String(80))
#     gender = db.Column(db.String(80))
#     billing_status = db.Column(db.String(80))
#     project = db.Column(db.Float, unique=True)
#     project_name = db.Column(db.String(200))
#     seating_location = db.Column(db.String(80))
#     pm_cdsid = db.Column(db.String(80))
#     lm_cdsid = db.Column(db.String(80))
#     job_family = db.Column(db.String(80))
#     month_of_joining_ges = db.Column(db.Integer)
#     year_of_joining_ges = db.Column(db.Integer)
#     previous_experience = db.Column(db.Float)
#     modified = db.Column(db.DateTime)
#     modified_by = db.Column(db.String(80))
#     project_ll5_cdsid = db.Column(db.String(80))
#     grade = db.Column(db.String(80))
#     workstation_number = db.Column(db.String(80))
#     education = db.Column(db.String(80))
#     education_details = db.Column(db.String(80))
#     item_type = db.Column(db.String(80))
#     path = db.Column(db.String(80))
#     funding_organisation = db.Column(db.String(80))
#     funding_function = db.Column(db.String(80))
#     funding_region = db.Column(db.String(80))
#     phase = db.Column(db.String(80))
#     attribute = db.Column(db.String(80))
#     product = db.Column(db.String(80))
#     process = db.Column(db.String(80))
#     method_domain = db.Column(db.String(80))
#     tmm = db.Column(db.String(80))
#     primary_tool = db.Column(db.String(80))
#     level = db.Column(db.String(80))
#     remarks = db.Column(db.String(80))
#     wb = db.Column(db.Integer)
#     aaa = db.Column(db.Integer)
#     project2 = db.Column(db.Integer)
#     cbg = db.Column(db.String(80))
#     discipline = db.Column(db.String(80))
#     column1 = db.Column(db.String(80))
#     month_year_joining = db.Column(db.String)
#     ges_experience = db.Column(db.Float)
#     total_experience = db.Column(db.Float)
#     column2 = db.Column(db.String(80))
#
#
#     def __init__(self,id,cdsid, name, company, gender, billing_status, project, project_name, seating_location, pm_cdsid, lm_cdsid, job_family, month_of_joining_ges,
#     year_of_joining_ges, previous_experience, modified, modified_by, project_ll5_cdsid, grade, workstation_number, education, education_details,
#     item_type, path, funding_organisation, funding_function, funding_region, phase, attribute, product, process, method_domain, tmm, primary_tool,
#     level, remarks, wb, aaa, project2, cbg, discipline, column1, month_year_joining, ges_experience, total_experience, column2):
#
#         self.id = id
#         self.cdsid = cdsid
#         self.name= name
#         self.company= company
#         self.gender=gender
#         self.billing_status= billing_status
#         self.project= project
#         self.project_name= project_name
#         self.seating_location=seating_location
#         self.pm_cdsid=pm_cdsid
#         self.lm_cdsid= lm_cdsid
#         self.job_family=job_family
#         self.month_of_joining_ges=month_of_joining_ges
#         self.year_of_joining_ges=year_of_joining_ges
#         self.previous_experience=previous_experience
#         self.modified=modified
#         self.modified_by=modified_by
#         self.project_ll5_cdsid=project_ll5_cdsid
#         self.grade=grade
#         self.workstation_number=workstation_number
#         self.education=education
#         self.education_details=education_details
#         self.item_type=item_type
#         self.path=path
#         self.funding_organisation=funding_organisation
#         self.funding_function=funding_function
#         self.funding_region=funding_region
#         self.phase=phase
#         self.attribute=attribute
#         self.product=product
#         self.process=process
#         self.method_domain=method_domain
#         self.tmm=tmm
#         self.primary_tool=primary_tool
#         self.level=level
#         self.remarks=remarks
#         self.wb=wb
#         self.aaa=aaa
#         self.project2=project2
#         self.cbg=cbg
#         self.discipline=discipline
#         self.column1=column1
#         self.month_year_joining=month_year_joining
#         self.ges_experience=ges_experience
#         self.total_experience=total_experience
#         self.column2=column2


class eassetfinal1(db.Model):
    __tablename__ = 'eassetfinal1'

    DEVICE_USER_CDSID = db.Column(db.String, primary_key=True)
    FORD_MANAGER= db.Column(db.String)
    COMPUTER_NAME= db.Column(db.String)
    SLS_LAST_USER = db.Column(db.String)
    BLUE_DOLLAR_CONFIGURATION = db.Column(db.String)
    LAST_LOG_DATE = db.Column(db.Date)
    DEVICE_STATUS = db.Column(db.String)
    LOCATION_DESCRIPTION = db.Column(db.String)
    LEASE_END_DATE= db.Column(db.Date)

    def __init__(self,DEVICE_USER_CDSID,FORD_MANAGER,COMPUTER_NAME,SLS_LAST_USER,BLUE_DOLLAR_CONFIGURATION,
                 LAST_LOG_DATE,DEVICE_STATUS,LOCATION_DESCRIPTION,LEASE_END_DATE):

        self.DEVICE_USER_CDSID = DEVICE_USER_CDSID
        self.FORD_MANAGER = FORD_MANAGER
        self.COMPUTER_NAME = COMPUTER_NAME
        self.SLS_LAST_USER = SLS_LAST_USER
        self.BLUE_DOLLAR_CONFIGURATION = BLUE_DOLLAR_CONFIGURATION
        self.LAST_LOG_DATE = LAST_LOG_DATE
        self.DEVICE_STATUS = DEVICE_STATUS
        self.LOCATION_DESCRIPTION = LOCATION_DESCRIPTION
        self.LEASE_END_DATE = LEASE_END_DATE


class easset4(db.Model):
    __tablename__ = 'easset4'

    id = db.Column(db.Integer, primary_key=True)
    SERIAL_NUMBER = db.Column(db.String)
    DEVICE_USER_CDSID = db.Column(db.String, db.ForeignKey('rmtest11.cdsid'))
    FORD_MANAGER= db.Column(db.String)
    COMPUTER_NAME= db.Column(db.String)
    SLS_LAST_USER = db.Column(db.String)
    BLUE_DOLLAR_CONFIGURATION = db.Column(db.String)
    LAST_LOG_DATE = db.Column(db.Date)
    DEVICE_STATUS = db.Column(db.String)
    LOCATION_DESCRIPTION = db.Column(db.String)
    LEASE_END_DATE= db.Column(db.Date)

    def __init__(self,SERIAL_NUMBER,DEVICE_USER_CDSID,FORD_MANAGER,COMPUTER_NAME,SLS_LAST_USER,BLUE_DOLLAR_CONFIGURATION,
                 LAST_LOG_DATE,DEVICE_STATUS,LOCATION_DESCRIPTION,LEASE_END_DATE):

        self.SERIAL_NUMBER= SERIAL_NUMBER
        self.DEVICE_USER_CDSID = DEVICE_USER_CDSID
        self.FORD_MANAGER = FORD_MANAGER
        self.COMPUTER_NAME = COMPUTER_NAME
        self.SLS_LAST_USER = SLS_LAST_USER
        self.BLUE_DOLLAR_CONFIGURATION = BLUE_DOLLAR_CONFIGURATION
        self.LAST_LOG_DATE = LAST_LOG_DATE
        self.DEVICE_STATUS = DEVICE_STATUS
        self.LOCATION_DESCRIPTION = LOCATION_DESCRIPTION
        self.LEASE_END_DATE = LEASE_END_DATE

class Pmfinal(db.Model):
    __tablename__ = 'pmfinal'

    fecode = db.Column(db.String(180), primary_key=True)
    project_name = db.Column(db.String(180))
    dorf_id = db.Column(db.Float)
    cbg = db.Column(db.String(180))
    customer_contact = db.Column(db.String(180))
    csat_customer_contact = db.Column(db.String(180))
    customer_contact_secondary = db.Column(db.String(180))
    project_manager = db.Column(db.String(180))
    manager = db.Column(db.String(180))
    actual_forecast = db.Column(db.String(180))
    project_subcategory = db.Column(db.String(180))
    project_category = db.Column(db.String(180))
    discipline = db.Column(db.String(180))
    pm_cdsid = db.Column(db.String(180))
    lm_cdsid = db.Column(db.String(180))
    ll5_cdsid = db.Column(db.String(180))
    po_value = db.Column(db.Integer)
    currency = db.Column(db.String(180))
    po_number_sow_number = db.Column(db.String(180))
    year = db.Column(db.Integer)
    csr_required = db.Column(db.String(180))
    jan_offshore = db.Column(db.String(180))
    jan_onsite = db.Column(db.String(180))
    feb_offshore = db.Column(db.String(180))
    feb_onsite = db.Column(db.String(180))
    mar_offshore = db.Column(db.String(180))
    mar_onsite = db.Column(db.String(180))
    apr_offshore = db.Column(db.String(180))
    apr_onsite = db.Column(db.String(180))
    may_offshore = db.Column(db.String(180))
    may_onsite = db.Column(db.String(180))
    jun_offshore = db.Column(db.String(180))
    jun_onsite = db.Column(db.String(180))
    jul_offshore = db.Column(db.String(180))
    jul_onsite = db.Column(db.String(180))
    aug_offshore = db.Column(db.String(180))
    aug_onsite = db.Column(db.String(180))
    sep_offshore = db.Column(db.String(180))
    sep_onsite = db.Column(db.String(180))
    oct_offshore = db.Column(db.String(180))
    oct_onsite = db.Column(db.String(180))
    nov_offshore = db.Column(db.String(180))
    nov_onsite = db.Column(db.String(180))
    dec_offshore = db.Column(db.String(180))
    dec_onsite = db.Column(db.String(180))
    pd_non_pd = db.Column(db.String(180))
    acc_code = db.Column(db.String(180))
    gsdb_code = db.Column(db.String(180))
    sub_acct_code = db.Column(db.String(180))
    po_received_date = db.Column(db.String(180))
    previous_year_dorfid = db.Column(db.String(180))
    quote_submission_date = db.Column(db.String(180))
    dept_cost_center = db.Column(db.String(180))
    remarks = db.Column(db.String(180))
    funding_function = db.Column(db.String(180))
    funding_organisation = db.Column(db.String(180))

    def __init__(self, fecode, project_name, dorf_id, cbg, customer_contact, csat_customer_contact, customer_contact_secondary, project_manager,
                 manager, actual_forecast, project_subcategory, project_category, discipline,pm_cdsid,lm_cdsid,ll5_cdsid,po_value, currency,
                 po_number_sow_number,year,csr_required, jan_offshore, jan_onsite, feb_offshore, feb_onsite, mar_offshore, mar_onsite,
                 apr_offshore, apr_onsite, may_offshore, may_onsite, jun_offshore, jun_onsite, jul_offshore, jul_onsite, aug_offshore,
                 aug_onsite, sep_offshore, sep_onsite, oct_offshore, oct_onsite, nov_offshore, nov_onsite, dec_offshore, dec_onsite,
                 pd_non_pd, acc_code, gsdb_code, sub_acct_code, po_received_date, previous_year_dorfid, quote_submission_date, dept_cost_center,
                 remarks, funding_function, funding_organisation):

        self.fecode = fecode
        self.project_name = project_name
        self.dorf_id = dorf_id
        self.cbg = cbg
        self.customer_contact = customer_contact
        self.csat_customer_contact = csat_customer_contact
        self.customer_contact_secondary = customer_contact_secondary
        self.project_manager = project_manager
        self.manager = manager
        self.actual_forecast = actual_forecast
        self.project_subcategory = project_subcategory
        self.project_category = project_category
        self.discipline = discipline
        self.pm_cdsid = pm_cdsid
        self.lm_cdsid = lm_cdsid
        self.ll5_cdsid = ll5_cdsid
        self.po_value = po_value
        self.currency = currency
        self.po_number_sow_number = po_number_sow_number
        self.year = year
        self.csr_required = csr_required
        self.jan_offshore = jan_offshore
        self.jan_onsite = jan_onsite
        self.feb_offshore = feb_offshore
        self.feb_onsite = feb_onsite
        self.mar_offshore = mar_offshore
        self.mar_onsite = mar_onsite
        self.apr_offshore = apr_offshore
        self.apr_onsite = apr_onsite
        self.may_offshore = may_offshore
        self.may_onsite = may_onsite
        self.jun_offshore = jun_offshore
        self.jun_onsite = jun_onsite
        self.jul_offshore = jul_offshore
        self.jul_onsite = jul_onsite
        self.aug_offshore = aug_offshore
        self.aug_onsite = aug_onsite
        self.sep_offshore = sep_offshore
        self.sep_onsite = sep_onsite
        self.oct_offshore = oct_offshore
        self.oct_onsite = oct_onsite
        self.nov_offshore = nov_offshore
        self.nov_onsite = nov_onsite
        self.dec_offshore = dec_offshore
        self.dec_onsite = dec_onsite
        self.pd_non_pd = pd_non_pd
        self.acc_code = acc_code
        self.gsdb_code = gsdb_code
        self.sub_acct_code = sub_acct_code
        self.po_received_date = po_received_date
        self.previous_year_dorfid = previous_year_dorfid
        self.quote_submission_date = quote_submission_date
        self.dept_cost_center = dept_cost_center
        self.remarks = remarks
        self.funding_function = funding_function
        self.funding_organisation = funding_organisation


class Pmtest3(db.Model):
    __tablename__ = 'pmtest3'

    fecode = db.Column(db.String(180), primary_key=True, unique=True)
    project_name = db.Column(db.String(180))
    dorf_id = db.Column(db.Float, db.ForeignKey('rmtest11.project'))
    cbg = db.Column(db.String(180))
    customer_contact = db.Column(db.String(180))
    csat_customer_contact = db.Column(db.String(180))
    customer_contact_secondary = db.Column(db.String(180))
    project_manager = db.Column(db.String(180))
    manager = db.Column(db.String(180))
    actual_forecast = db.Column(db.String(180))
    project_subcategory = db.Column(db.String(180))
    project_category = db.Column(db.String(180))
    discipline = db.Column(db.String(180))
    pm_cdsid = db.Column(db.String(180))
    lm_cdsid = db.Column(db.String(180))
    ll5_cdsid = db.Column(db.String(180))
    po_value = db.Column(db.Integer)
    currency = db.Column(db.String(180))
    po_number_sow_number = db.Column(db.String(180))
    year = db.Column(db.Integer)
    csr_required = db.Column(db.String(180))
    jan_offshore = db.Column(db.String(180))
    jan_onsite = db.Column(db.String(180))
    feb_offshore = db.Column(db.String(180))
    feb_onsite = db.Column(db.String(180))
    mar_offshore = db.Column(db.String(180))
    mar_onsite = db.Column(db.String(180))
    apr_offshore = db.Column(db.String(180))
    apr_onsite = db.Column(db.String(180))
    may_offshore = db.Column(db.String(180))
    may_onsite = db.Column(db.String(180))
    jun_offshore = db.Column(db.String(180))
    jun_onsite = db.Column(db.String(180))
    jul_offshore = db.Column(db.String(180))
    jul_onsite = db.Column(db.String(180))
    aug_offshore = db.Column(db.String(180))
    aug_onsite = db.Column(db.String(180))
    sep_offshore = db.Column(db.String(180))
    sep_onsite = db.Column(db.String(180))
    oct_offshore = db.Column(db.String(180))
    oct_onsite = db.Column(db.String(180))
    nov_offshore = db.Column(db.String(180))
    nov_onsite = db.Column(db.String(180))
    dec_offshore = db.Column(db.String(180))
    dec_onsite = db.Column(db.String(180))
    pd_non_pd = db.Column(db.String(180))
    acc_code = db.Column(db.String(180))
    gsdb_code = db.Column(db.String(180))
    sub_acct_code = db.Column(db.String(180))
    po_received_date = db.Column(db.String(180))
    previous_year_dorfid = db.Column(db.String(180))
    quote_submission_date = db.Column(db.String(180))
    dept_cost_center = db.Column(db.String(180))
    remarks = db.Column(db.String(180))
    funding_function = db.Column(db.String(180))
    funding_organisation = db.Column(db.String(180))

    def __init__(self, fecode, project_name, dorf_id, cbg, customer_contact, csat_customer_contact, customer_contact_secondary, project_manager,
                 manager, actual_forecast, project_subcategory, project_category, discipline,pm_cdsid,lm_cdsid,ll5_cdsid,po_value, currency,
                 po_number_sow_number,year,csr_required, jan_offshore, jan_onsite, feb_offshore, feb_onsite, mar_offshore, mar_onsite,
                 apr_offshore, apr_onsite, may_offshore, may_onsite, jun_offshore, jun_onsite, jul_offshore, jul_onsite, aug_offshore,
                 aug_onsite, sep_offshore, sep_onsite, oct_offshore, oct_onsite, nov_offshore, nov_onsite, dec_offshore, dec_onsite,
                 pd_non_pd, acc_code, gsdb_code, sub_acct_code, po_received_date, previous_year_dorfid, quote_submission_date, dept_cost_center,
                 remarks, funding_function, funding_organisation):

        self.fecode = fecode
        self.project_name = project_name
        self.dorf_id = dorf_id
        self.cbg = cbg
        self.customer_contact = customer_contact
        self.csat_customer_contact = csat_customer_contact
        self.customer_contact_secondary = customer_contact_secondary
        self.project_manager = project_manager
        self.manager = manager
        self.actual_forecast = actual_forecast
        self.project_subcategory = project_subcategory
        self.project_category = project_category
        self.discipline = discipline
        self.pm_cdsid = pm_cdsid
        self.lm_cdsid = lm_cdsid
        self.ll5_cdsid = ll5_cdsid
        self.po_value = po_value
        self.currency = currency
        self.po_number_sow_number = po_number_sow_number
        self.year = year
        self.csr_required = csr_required
        self.jan_offshore = jan_offshore
        self.jan_onsite = jan_onsite
        self.feb_offshore = feb_offshore
        self.feb_onsite = feb_onsite
        self.mar_offshore = mar_offshore
        self.mar_onsite = mar_onsite
        self.apr_offshore = apr_offshore
        self.apr_onsite = apr_onsite
        self.may_offshore = may_offshore
        self.may_onsite = may_onsite
        self.jun_offshore = jun_offshore
        self.jun_onsite = jun_onsite
        self.jul_offshore = jul_offshore
        self.jul_onsite = jul_onsite
        self.aug_offshore = aug_offshore
        self.aug_onsite = aug_onsite
        self.sep_offshore = sep_offshore
        self.sep_onsite = sep_onsite
        self.oct_offshore = oct_offshore
        self.oct_onsite = oct_onsite
        self.nov_offshore = nov_offshore
        self.nov_onsite = nov_onsite
        self.dec_offshore = dec_offshore
        self.dec_onsite = dec_onsite
        self.pd_non_pd = pd_non_pd
        self.acc_code = acc_code
        self.gsdb_code = gsdb_code
        self.sub_acct_code = sub_acct_code
        self.po_received_date = po_received_date
        self.previous_year_dorfid = previous_year_dorfid
        self.quote_submission_date = quote_submission_date
        self.dept_cost_center = dept_cost_center
        self.remarks = remarks
        self.funding_function = funding_function
        self.funding_organisation = funding_organisation


# for Rmtest11, easset2 in results:
#     print(Rmtest11.cdsid, easset2.COMPUTER_NAME)

class User1(db.Model):
    user_id = db.Column(db.String(90), primary_key=True, unique=True)
    name = db.Column(db.String(90))
    cdsid = db.Column(db.String(90),db.ForeignKey('rmtest11.cdsid'))
    role = db.Column(db.String(90))


class Bopage4(db.Model):
    __tablename__ = 'bopage4'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    requestor_cdsid = db.Column(db.String(90), db.ForeignKey('user1.user_id'))
    cdsid = db.Column(db.String(90), db.ForeignKey('rmtest11.cdsid'))
    ll6_cdsid = db.Column(db.String(90))
    request_type = db.Column(db.String(90))
    pm_request_time = db.Column(db.DateTime)
    it_request_number= db.Column(db.String(90),unique=True)
    unshare_it_req_number = db.Column(db.String(90))
    it_req_raisedby = db.Column(db.String(90))
    it_connect_stage = db.Column(db.String(90))
    bo_status = db.Column(db.String(90))
    remarks = db.Column(db.String(90))

    def __init__(self, requestor_cdsid, cdsid, ll6_cdsid, request_type, pm_request_time, it_request_number, unshare_it_req_number,
                 it_req_raisedby, it_connect_stage, bo_status, remarks):
        self.requestor_cdsid = requestor_cdsid
        self.cdsid = cdsid
        self.ll6_cdsid = ll6_cdsid
        self.request_type = request_type
        self.pm_request_time = pm_request_time
        self.it_request_number = it_request_number
        self.unshare_it_req_number = unshare_it_req_number
        self.it_req_raisedby = it_req_raisedby
        self.it_connect_stage = it_connect_stage
        self.bo_status = bo_status
        self.remarks = remarks

class pcrenew12(db.Model):
    __tablename__ = 'pcrenew12'

    Request_Number= db.Column(db.String, db.ForeignKey('rrpage13.it_request_number'))
    Work_Order = db.Column(db.String, primary_key=True, unique=True)
    Support_Region = db.Column(db.String)
    Assigned_Group_QueueName = db.Column(db.String)
    Summary = db.Column(db.String)
    Requested_Configuration_Type = db.Column(db.String)
    Business_Case = db.Column(db.String)
    PC_and_Component_Specifications = db.Column(db.String)
    Host_Name = db.Column(db.String)
    Service_Type= db.Column(db.String)
    RequestQuantity= db.Column(db.String)
    Submit_Date = db.Column(db.String)
    Actual_Start_Date = db.Column(db.String)
    Actual_End_Date = db.Column(db.String)
    Completed_Date = db.Column(db.String)
    Status = db.Column(db.String)
    Approver_Full_Name = db.Column(db.String)
    Approver_CDSID = db.Column(db.String)
    Customer_First_Name = db.Column(db.String)
    Customer_Last_Name = db.Column(db.String)
    Submitter_CDSID = db.Column(db.String)
    Requested_By_Login_ID = db.Column(db.String)
    Requested_By_Login_Contact_Name = db.Column(db.String)
    Customer_Site = db.Column(db.String)
    Service_Location_Address = db.Column(db.String)
    Desk_Location = db.Column(db.String)
    Accounting_Number = db.Column(db.String)
    Customer_Department = db.Column(db.String)
    Customer_Organization = db.Column(db.String)
    Customer_Internet_E_mail = db.Column(db.String)
    Customer_Phone_Number = db.Column(db.String)
    Theft_report_number_and_associated_description = db.Column(db.String)
    Concat_Detailed_Description = db.Column(db.String)

    def __init__(self, Request_Number,Work_Order,Support_Region,Assigned_Group_QueueName,Summary,Requested_Configuration_Type,Business_Case,
                 PC_and_Component_Specifications,Host_Name,Service_Type,RequestQuantity,Submit_Date,Actual_Start_Date,Actual_End_Date,Completed_Date,
                 Status,Approver_Full_Name,Approver_CDSID,Customer_First_Name,Customer_Last_Name,Submitter_CDSID,Requested_By_Login_ID,
                 Requested_By_Login_Contact_Name, Customer_Site, Service_Location_Address,Desk_Location,Accounting_Number,Customer_Department,
                 Customer_Organization,Customer_Internet_E_mail,Customer_Phone_Number,Theft_report_number_and_associated_description,
                 Concat_Detailed_Description):

        self.Request_Number= Request_Number
        self.Work_Order = Work_Order
        self.Support_Region = Support_Region
        self.Assigned_Group_QueueName = Assigned_Group_QueueName
        self.Summary = Summary
        self.Requested_Configuration_Type = Requested_Configuration_Type
        self.Business_Case = Business_Case
        self.PC_and_Component_Specifications = PC_and_Component_Specifications
        self.Host_Name = Host_Name
        self.Service_Type = Service_Type
        self.RequestQuantity = RequestQuantity
        self.Submit_Date = Submit_Date
        self.Actual_Start_Date = Actual_Start_Date
        self.Actual_End_Date = Actual_End_Date
        self.Completed_Date = Completed_Date
        self.Status = Status
        self.Approver_Full_Name = Approver_Full_Name
        self.Approver_CDSID = Approver_CDSID
        self.Customer_First_Name = Customer_First_Name
        self.Customer_Last_Name = Customer_Last_Name
        self.Submitter_CDSID = Submitter_CDSID
        self.Requested_By_Login_ID = Requested_By_Login_ID
        self.Requested_By_Login_Contact_Name = Requested_By_Login_Contact_Name
        self.Customer_Site = Customer_Site
        self.Service_Location_Address = Service_Location_Address
        self.Desk_Location = Desk_Location
        self.Accounting_Number = Accounting_Number
        self.Customer_Department = Customer_Department
        self.Customer_Organization = Customer_Organization
        self.Customer_Internet_E_mail = Customer_Internet_E_mail
        self.Customer_Phone_Number = Customer_Phone_Number
        self.Theft_report_number_and_associated_description = Theft_report_number_and_associated_description
        self.Concat_Detailed_Description = Concat_Detailed_Description


class Rrpage13(db.Model):
    __tablename__ = 'rrpage13'

    id = db.Column(db.Integer, primary_key=True)
    requestor_cdsid = db.Column(db.String)
    cdsid = db.Column(db.String(80))
    ll6_cdsid = db.Column(db.String)
    pm_request_time = db.Column(db.DateTime, default=datetime.utcnow())
    request_type = db.Column(db.String(80))
    new_location = db.Column(db.String(80))
    new_assert_type = db.Column(db.String(80))
    service_tag = db.Column(db.String(80))
    sharing = db.Column(db.Boolean)
    unshare = db.Column(db.String)
    it_request_number= db.Column(db.String(90), unique=True)
    unshare_it_req_number = db.Column(db.String(90))
    it_req_raisedby = db.Column(db.String(90))
    it_connect_stage = db.Column(db.String(90))
    bo_status = db.Column(db.String(90))
    remarks = db.Column(db.String(90))

    def __init__(self, requestor_cdsid, cdsid, ll6_cdsid, pm_request_time, request_type, new_location, new_assert_type, service_tag, sharing, unshare,
                 it_request_number,unshare_it_req_number,it_req_raisedby,it_connect_stage,bo_status,remarks):

        self.requestor_cdsid = requestor_cdsid
        self.cdsid = cdsid
        self.ll6_cdsid = ll6_cdsid
        self.pm_request_time = pm_request_time
        self.request_type = request_type
        self.new_location = new_location
        self.new_assert_type = new_assert_type
        self.service_tag = service_tag
        self.sharing = sharing
        self.unshare = unshare
        self.it_request_number = it_request_number
        self.unshare_it_req_number = unshare_it_req_number
        self.it_req_raisedby = it_req_raisedby
        self.it_connect_stage = it_connect_stage
        self.bo_status = bo_status
        self.remarks = remarks



# results = db.session.query(Rmtest11, easset2).join(easset2).all()


if __name__== '__main__':
    # db.create_all()
    main.run(debug=True)
