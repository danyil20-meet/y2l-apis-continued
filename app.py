from flask import Flask, render_template, request
import json, requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
	headers = {'Authorization': 'Key 814705368f074d60b8604409fd6a3f9d'}

	api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"

	image_url = request.form['url-input']
	
	data ={"inputs": [
	{
	"data": {
		"image": {
			"url": image_url
		}
	}
	}
	]}

	response = requests.post(api_url, headers=headers, data=json.dumps(data))
	
	response_dict = json.loads(response.content)

	results = response_dict["outputs"][0]["data"]["concepts"]#[0]["name"]

	return render_template('data.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)