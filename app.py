from flask import Flask, render_template, request, jsonify
from pusher import Pusher
import json

app = Flask(__name__)

pusher = Pusher(
  app_id='555480',
  key='de825b7cc253e460debb',
  secret='95596eda6a750ea3aa3d',
  cluster='ap2',
  ssl=True
)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/add-todo', methods=['POST'])
def addTodo():
	data = json.loads(request.data)
	pusher.trigger('todo', 'item-added', data)
	return jsonify(data)

@app.route('/remove-todo/<item_id>')
def removeTodo(item_id):
	data = {'id' : item_id}
	pusher.trigger('todo', 'item-removed', data)
	return jsonify(data)

@app.route('/update-todo/<item_id>', methods=['POST'])
def updateTodo(item_id):
	data = {
		'id' : item_id,
		'completed' : json.loads(request.data).get('completed', 0)
		}
	pusher.trigger('todo', 'item-updated', data)
	return jsonify(data)

if __name__ == '__main__' :
	app.run(debug = True)















