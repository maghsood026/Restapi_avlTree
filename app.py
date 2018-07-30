from flask import Flask, request, render_template
import AvlTree

myAvl = AvlTree.AVL()
root = None


app = Flask(__name__)


@app.route('/home')
def index():
    return "hello"

@app.route('/insert', methods=['POST'])
def insert():
    content = request.get_json()
    value = content['value']
    global root
    root = myAvl.insert(root, value)
    return "the %s inserted" % value


@app.route('/search', methods=['POST'])
def search():
    content = request.get_json()
    value = content['value']
    global root
    if myAvl.search(root, value):
        return "%s is found" % value
    else:
        return "%s not found" % value


@app.route('/delete', methods=['POST'])
def delete():
    content = request.get_json()
    value = content['value']
    global root
    root = myAvl.delete(root, value)
    return " %s deleted ... " % value


if __name__ == '__main__':
    app.run(threads='true',host='127.0.0.1', port=8000)
