from flask import Flask, render_template, url_for, redirect, request
import requests

app = Flask(__name__) 

app.config["DEBUG"] = True

@app.route("/")
def render_landing_page():
	return render_template("landing-page.html",  username = "Heicoders", account_type = "Premium")



# @app.route("/search", methods = ["POST", "GET"])
# def search():
		
# 	# This line will get our input from our HTML form from the HTML element that has 
# 	# the attribute name of "search_query"
# 	video_title = request.form["search_query"]

# 	url = "https://imdb8.p.rapidapi.com/title/auto-complete"

# 	querystring = {"q": video_title} # change the fixed string to video_title variable

# 	headers = {
# 	'x-rapidapi-key': "41ba84bceamsh0f0505ff8889433p109f62jsn805dcabb92a2",
# 	'x-rapidapi-host': "imdb8.p.rapidapi.com"
# 	}

# 	response = requests.request("GET", url, headers=headers, params=querystring)

# 	data = response.json()

# 	return render_template("search-result.html", data = data)

@app.route("/search", methods=['POST'])
def form_submit():
    user_query = request.form['search_query'] # matches name attribute of query string input (HTML)
    redirect_url = url_for('.search_imdb', query_string=user_query)  # match search_imdb function name (Python flask)
    return redirect(redirect_url)

@app.route("/search/<query_string>", methods=['GET'])
def search_imdb(query_string):
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"
    querystring = {"q": query_string}
    headers = {
        'x-rapidapi-key': "41ba84bceamsh0f0505ff8889433p109f62jsn805dcabb92a2",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        return render_template("search-result.html", data=data)
    except:
        return render_template("error404.html")

if __name__ == "__main__":
	app.run(port="5000") # 0.0.0.0 does not work here