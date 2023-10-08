from flask import Flask, render_template, request
import pickle
#import numpy as np

# setup application
app = Flask(__name__)

def prediction(lst):
   filename = 'model/PREDICTION_FIREWOOD_NEW_UPDATE.pickle'
   with open(filename, 'rb') as file:
       model = pickle.load(file)
   pred_value = model.predict([lst])
   return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    # return "Hello World"
    pred_value = 0
    if request.method == 'POST':
        weight = request.form['weight']
        rate = request.form['rate']
        rainy = request.form['rainy']
        month = request.form['Month']
        Wtype = request.form['Wtype']
        
        
        feature_list = []

        feature_list.append(int(weight))
        feature_list.append(float(rate))
        feature_list.append(int(rainy))
        
        month_list = ['April', 'August', 'December', 'February', 'January', 'July', 'June', 'March', 'May', 'November', 'October', 'September']
        wood_list = ['Cashew','Halmilla','Mahogany','Mango','Mara','Other','Teak']
        

        # for item in company_list:
        #     if item == company:
        #         feature_list.append(1)
        #     else:
        #         feature_list.append(0)

        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        
        traverse_list(wood_list, Wtype)
        traverse_list(month_list, month )

        print(feature_list)

        pred_value = prediction(feature_list)
        print(pred_value)
        
        

        

    return render_template('prediction.html',pred_value=pred_value)


if __name__ == '__main__':
    app.run(debug=True)