from flask import Flask,jsonify,abort
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



if __name__ == "__main__":
    app.run(debug=True)