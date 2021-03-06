# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Loading the Linear Regression model
filename = 'Batting-score-LassoReg-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/forecast', methods=['POST'])
def forecast():
    temp_array = list()
    if request.method == 'POST':
        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Capitals':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Punjab Kings':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Capitals':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Punjab Kings':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
        venue = request.form['venue']
        if venue == 'M Chinnaswamy Stadium, Bangalore':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif venue == 'Eden Gardens, Kolkata':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif venue == 'Feroz Shah Kotla, Delhi':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif venue == 'MA Chidambaram Stadium, Chennai':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif venue == 'Punjab Cricket Association Stadium, Mohali':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif venue == 'Wankhede Stadium, Mumbai':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif venue == 'Sawai Mansingh Stadium, Jaipur':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif venue == 'Rajiv Gandhi International Stadium, Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
        
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        data = np.array([temp_array])
        my_prediction = int(regressor.predict(data)[0])
              
        return render_template('forecast.html', lower_limit = my_prediction-10, upper_limit = my_prediction+5, 
                                                batting_team = batting_team, bowling_team = bowling_team, 
                                                    venue = venue, overs = overs, runs = runs, wickets = wickets, 
                                                        runs_in_prev_5 = runs_in_prev_5, wickets_in_prev_5 = wickets_in_prev_5)

if __name__ == '__main__':
	app.run(debug=True)