import plotly.express as px
import csv

with open("Icecream.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = "Temperature",y = "Ice-cream Sales( ₹ )")
    fig.show()

with open("cups.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = "week",y = "Coffee in ml")
    fig.show()
with open("T.V.size.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = "Size of TV",y = "Average time spent watching TV in a week (hours)")
    fig.show()
with open("studentMarks.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = "Roll No",y = "Marks In Percentage)")
    fig.show() 
with open("data.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = "student_id,",y = "level)")
    fig.show()