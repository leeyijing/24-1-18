from flask import Flask, render_template, request, session
from wtforms import Form, StringField, validators, IntegerField, SelectField

import Processing
import uobitems
app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/uobrewardtrending')
def uobrewardtrending():
    return render_template('uobrewardtrending.html')

@app.route('/uobrewardtrendingpt')
def uobrewardtrendingpt():
    return render_template('uobrewardtrendingpt.html')

@app.route('/uobrewardall')
def uobrewardall():
    return render_template('uobrewardall.html')

@app.route('/uobrewardallpt')
def uobrewardallpt():
    return render_template('uobrewardallpt.html')

@app.route('/uobrewardretail')
def uobrewardretail():
    return render_template('uobrewardretail.html')

@app.route('/uobrewardretailpt')
def uobrewardretailpt():
    return render_template('uobrewardretailpt.html')

@app.route('/uobrewarddining')
def uobrewarddining():
    return render_template('uobrewarddining.html')

@app.route('/uobrewarddiningpt')
def uobrewarddiningpt():
    return render_template('uobrewarddiningpt.html')

@app.route('/uobrewardleisure')
def uobrewardleisure():
    return render_template('uobrewardleisure.html')

@app.route('/uobrewardleisurept')
def uobrewardleisurept():
    return render_template('uobrewardleisurept.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/alldecredemption')
def alldecredemption():
    return render_template('alldecredemption.html')

@app.route('/uobdecredemption')
def uobdecredemption():
    return render_template('uobdecredemption.html')

@app.route('/ocbcdecredemption')
def ocbcdecredemption():
    return render_template('ocbcdecredemption.html')

@app.route('/dbsdecredemption')
def dbsdecredemption():
    return render_template('dbsdecredemption.html')

@app.route('/allnovredemption')
def allnovredemption():
    allnovredemptionList = []
    allnovredemptionList = Processing.processsallnovredemption(session['user'], session["cardno"])
    return render_template('allnovredemption.html', allnovredemption=allnovredemptionList)


@app.route('/uobnovredemption')
def uobnovredemption():
    return render_template('uobnovredemption.html')

@app.route('/ocbcnovredemption')
def ocbcnovredemption():
    return render_template('ocbcnovredemption.html')

@app.route('/dbsnovredemption')
def dbsnovredemption():
    return render_template('dbsnovredemption.html')

@app.route('/allredemption')
def allredemption():
    allredemptionList = []
    allredemptionList = Processing.processallredemption(session['user'],session["cardno"])
    return render_template('allredemption.html', allredemptions=allredemptionList)

@app.route('/alluobredemption')
def alluobredemption():
    return render_template('alluobredemption.html')

@app.route('/allocbcredemption')
def allocbcredemption():
    return render_template('allocbcredemption.html')

@app.route('/alldbsredemption')
def alldbsredemption():
    return render_template('alldbsredemption.html')

@app.route('/updateuobrewardretail')
def updateuobrewardretail():
    return render_template('updateuobrewardretail.html')

@app.route('/updateuobrewarddining')
def updateuobrewarddining():
    return render_template('updateuobrewarddining.html')

@app.route('/updatepart2uobdining')
def updatepart2uobdining():
    return render_template('updatepart2uobdining.html')

@app.route('/test')
def test():
    return render_template('test.html')



@app.route('/trying',methods=['GET', 'POST'])
def trying():
    session["cart"]={}
    session['user']="Rubbish"
    session["cardno"]= "9888-6121-0824-1112"
  #  listqty=Processing.list_qty(session['user'],session["cardno"])
    uob_currentpts = Processing.processpoints(session['user'],session["cardno"])
    uob_trenditems = Processing.processtrenditems(session['user'],session["cardno"])
    uob_allitems = Processing.processallitems(session['user'],session["cardno"])
    uob_retialitems = Processing.processretailitems(session['user'],session["cardno"])
    uob_diningitems = Processing.processdiningitems(session['user'],session["cardno"])
    uob_leisureitems = Processing.processleisureitems(session['user'],session["cardno"])
    #user = session["user"], cardno = session["cardno"],



    return render_template('trying.html',uobcurrentpts=uob_currentpts, uobtrenditems = uob_trenditems, uoballitems = uob_allitems,uobretialitems=uob_retialitems, uobdiningitems=uob_diningitems, uobleisureitems=uob_leisureitems)

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()
