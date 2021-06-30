import os
import csv
from django.http import HttpResponse
import pandas as pd
import io
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# バックエンドを指定
matplotlib.use('Agg')

"""
# グラフ作成
def setPlt():
    x = ["07/01", "07/02", "07/03", "07/04", "07/05", "07/06", "07/07"]
    y = [3, 5, 0, 5, 6, 10, 2]
    plt.bar(x, y, color='#00d5ff')
    plt.title(r"$\bf{Running Trend  -2020/07/07}$", color='#3407ba')
    plt.xlabel("Date")
    plt.ylabel("km")

# SVG化


def plt2svg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

# 実行するビュー関数


def get_svg(request):
    setPlt()
    svg = plt2svg()  # SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response


"""


def index(request):
    return HttpResponse("indicators")


def index2(request):
    my_context = {
        "text": "test",
        "true": True,
        "number": 123,
        "list": [1, 2, 3],
    }
    return render(request, "index2.html", my_context)
    # {{text}}{{true}}


def index3(request):
    obj = ProductModel.objects.get(id=1)
    context = {
        "title": obj.title,
        "desc": obj.desc,
        "object": obj
    }
    return render(request, "index3.html", context)
    # html {{text}}{{desc}}{{object}}{{object.title}}
    # html {%  if obj.desc !=None and obj.desc !='' %}{{obj.desc}}{% else %}description coming soon{% endif %}
    if request.method == "POST":
        my_new_title = request.POST.get('title')
        print(my_new_title)  # form からPOSTしたデータを表示する


def index4(request):
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        context = {
            "form": my_form
        }
        return render(request, "index4", context)


def predict(request):
    # Visualize the close price data
    df = pd.readcsv("csv/FB_1D_1Y.csv")
    plt.figure(figsize=(16, 8))
    plt.title("FB_Daily")
    plt.xlabel("Date")
    plt.ylabel("USD")
    plt.plot(df["Close"])
    plt.show()

    # Create a variable to predict 'x' days out into the future
    future_days = 25
    df['Prediction'] = df[["Close"]].shift(-future_days)

    # Create the feature data set(X) and convert it to a numpy array and remove the last 'x' rows/days
    X = np.array(df.drop(['Prediction'], 1))[:future_days]
    # Create the target data set (Y) and convert it to a numpy array and get
    # all of the target values except the last "X" rows
    y = np.array(df['Prediction'])[:future_days]

    X_train, x_test, Y_train, y_test = train_test_split(X, y, test_size=0.25)
    # Create the models
    # Create the decision tree regressor model
    tree = DecisionTreeRegressor().fit(x_train, y_train)
    # Create the liner regression model
    lr = LinearRegression().fit(x_train, y_train)
    # Get the last "x" row of the feature date set
    x_future = df.drop(['Prediction'], 1)[:-future_days]
    x_future = x_future.tail(future_days)
    x_future = np.array(x_future)
    # Show the model tree prediction
    lr_prediction = lr.predict(x_future)
    # Visialize the date
    predictions = tree_prediction
    valid = df[X.shape[0]:]
    valid["Predictions"] = predictions
    plt.figure(figsize=(16, 8))
    plt.title("Model")
    plt.xlabel("days")
    plt.ylabel("usd")
    plt.plot(df['Close'])
    plt.plot(valid[["Close", "Predictions"]])
    plt.legend(["Orig", "Val", "Pred"])
    plt.show


"""
def setPlt2():
    df = pd.read_csv('csv/FB_1D_1Y.csv')
    print(df['Close'])
    print(df['Date'])
    y = df['Close']
    x = df['Date']
    plt.title("FB_Daily", color='#3407ba')
    plt.xlabel("Date")
    plt.ylabel("Close Price USD($)")
    plt.plot(x, y, color='#00d5ff')
    fig = plt.figure(figsize=(120, 80))
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    plt.show()


# SVG化
def plt2svg2():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

# 実行するビュー関数


def get_svg2(request):
    setPlt2()
    svg = plt2svg()  # SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response
"""
