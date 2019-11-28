from flask import Flask,jsonify,abort,make_response,request
app=Flask(__name__)



tasks=[
    {
        'id':1,
        'title':"Play Basketball",
        'description':u'Play basketball with friends this evening',
        'done':False
    },
     {
        'id':2,
        'title':"Reading",
        'description':u'Reading A Python Book',
        'done':False
    },
    {
        'id':3,
        'title':"Dinner with my bae ",
        'description':u'Date with my bae at KFC Tonight',
        'done':False
    }
]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}),'Not Found')



#fetch all tasks
@app.route('/tasks',methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})

#fetch a single task
@app.route('/tasks/<int:task_id>')
def get_task(task_id):
    task=[task for task in tasks if task['id']==task_id]
    if len(task)==0:
        abort(404)
    return jsonify({'task':task[0]})


@app.route('/tasks',methods=['POST'])
def create_tasks():
    if not request.json or not 'title' in request.json:
        abort(400)
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({'task':task}),201
    


if __name__ == "__main__":
    app.run(debug=True)