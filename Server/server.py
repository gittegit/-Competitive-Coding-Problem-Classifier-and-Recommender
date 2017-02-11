# @app.route("/postData", methods=['POST'])
# def postData():
#     page_url = request.form.get('page')
#     # c = CodechefProblemPage.getCodechefProblem(page_url)
#     # print 'Got problem: ' + c.name
#     # result = predict.predict(c)
#     return jsonify({'Status': str(78)})
__author__ = 'Pranay'
from flask import Flask, request, jsonify
import codechef_problem
import predictCategory
print 'import complete'

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route("/getData", methods=['GET'])
def getData():

    entry2Value = request.args.get('entry2_id')
    entry1Value = request.args.get('entry1_id')

    var1 = int(entry2Value) + int(entry1Value)
    var2 = 10
    var3 = 15
    print entry1Value
    return jsonify({ 'var1': var1, 'var2': var2, 'var3': var3 })


@app.route("/postData", methods=['POST'])
def postData():
    problem_content = request.form.get('page')
    c = codechef_problem.getProblemFromDescription(problem_content)
    result = predictCategory.predict_category(c)
    return jsonify({'result':result})

# app.run(debug=True)
if __name__ == '__main__':
    print 'Starting'
    app.run(debug=True)