from flask import Flask, render_template, request, redirect,session
from datetime import datetime, time
import random


app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
dev = True

@app.route('/')
def my_portfolio():
    if 'gold' not in session:
        session['gold'] = 0
    if 'current_activity' not in session:
        session['current_activity'] = []
    return render_template('index.html') 


@app.route('/process_money', methods=['POST'])
def process_money():
    earn_type = request.form['building']
    # print choice
    current_gold = 0
    if earn_type == 'farm':
        current_gold = random.randint(10, 20)
        #print session['gold']
    elif earn_type == 'cave':
        current_gold = random.randint(5, 10)
        #print session['gold']
    elif earn_type == 'house':
        current_gold = random.randint(2, 5)
        #print session['gold']
    elif earn_type == 'casino':
        current_gold = random.randint(-50, 50)
        print session['current_activity']
        #print session['gold']
        session['gold'] += current_gold
        print current_gold
        if current_gold < 0:
            if session['gold'] > 0:
                session['current_activity'].append("Entered a {} and You lost {} golds... Ouch.. ({})".format(earn_type, current_gold, datetime.now()))
                print session['current_activity']
            else:
                session['current_activity'].append("You enterd a {} are in dept {} golds... Ouch.. ({})".format(earn_type, current_gold, datetime.now()))
                return redirect('/')
        else:
            session['current_activity'].append("Entered a {} and won {} golds... Feeling Lucky.. ({})".format(
                earn_type, current_gold, datetime.now()))
        return redirect('/')
                
    session['gold'] += current_gold
    
    session['current_activity'].append("Earned {} golds from the {}! ({})".format(
        current_gold, earn_type, datetime.now()))
                
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop("gold")
    session.pop('current_activity')
    return redirect('/')

app.run(debug=dev)
