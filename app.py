from flask import Flask, render_template, request, abort, jsonify
import pickle
import numpy
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/server')
def server():
    return render_template('server.html')
@app.route('/readme')
def readme():
    return render_template('readme.html')
@app.route('/downloads')
def downloads():
    return render_template('benchmarkData.html')
@app.route('/citation')
def citation():
    return render_template('citation.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contributors')
def contributors():
    return render_template('contributors.html')

@app.route('/results',methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        fasta = request.form['fasta']
        step = request.form['step']
        step = int(step)
        import os
        this_folder = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(this_folder,'sample.txt')
        ############### starting to write ####################
        fw = open(filename,'w')
        fw.write(fasta)
        fw.close()
        ############## validity check ########################
        import isValidity
        X, Y, nameFASTA, Verdict = isValidity.runValidity()
        for value in Verdict:
            if value == 'Invalid FASTA':
                return render_template('validity.html', nameFASTA = nameFASTA, Verdict = Verdict)
        ############# predicting #####################
        import gF
        Sequences = gF.fastaTOprediction(step, X, Y)
        return render_template('results.html', nameFASTA = nameFASTA, Sequences = Sequences)
    return render_template('server.html')

@app.route('/trap',methods=['GET', 'POST'])
def trap():
    if request.method == 'POST':
        da = request.form['da']
        return render_template('details.html',da=da)
if __name__ == '__main__':
    app.run(debug=True, port=5004)
