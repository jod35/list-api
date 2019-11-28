from flask import Flask,jsonify
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


@app.route('/tasks',methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})



if __name__ == "__main__":
    app.run(debug=True)