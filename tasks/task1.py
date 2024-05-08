# tasks/task1.py
from celery_kafaka_demo.celery import app

@app.task
def printSomething(someString:str):
    print(someString)

