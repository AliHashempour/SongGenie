import hashlib
import logging

from flask import Flask, render_template, request, redirect
import sqlite3
import string
import random

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
