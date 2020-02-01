# Twitchtistics
#### Visualizing view count for Twitch videos
This project is run on Flask, which creates a simple webpage allowing to submit the name of the
streamer. After submitting, a chart (source for the graph can be found
[here](https://blog.ruanbekker.com/blog/2017/12/14/graphing-pretty-charts-with-python-flask-and-chartjs/)), is brought up that plots each of the user's videos with their view count.

#### Code
* `app.py`: runs the Flask app
* `twitch.py`: connects to the Twitch API
* `requirements.txt`: the required packages
* `templates/d3.html`: d3.js code to display the chart
* `templates/form.html`: basic form to query Twitch API
