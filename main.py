from flask import Flask, render_template, request,jsonify
import pickle


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            Alcohol=float(request.form['Alcohol'])
            Malic_acid = float(request.form['Malic acid'])
            Ash = float(request.form['Ash'])
            Alcalinity = float(request.form['Alcalinity of ash'])
            Magnesium = float(request.form['Magnesium'])
            Total_phenols = float(request.form['Total phenols'])
            Flavanoids = float(request.form['Flavanoids'])
            Nonflavanoid = float(request.form['Nonflavanoid phenols'])
            Proanthocyanins = float(request.form['Proanthocyanins'])
            Color = float(request.form['Color intensity'])
            Hue = float(request.form['Hue'])
            diluted = float(request.form['OD280/OD315 of diluted wines'])
            Proline = float(request.form['Proline'])


            
            filename = 'rf.pkl'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[Alcohol,Malic_acid,Ash,Alcalinity,Magnesium,Total_phenols,Flavanoids, Nonflavanoid,Proanthocyanins, Color, Hue,diluted, Proline]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=prediction[0])
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app
