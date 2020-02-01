from flask import Flask, request, render_template
from wtforms import Form, StringField, validators

import twitch

app = Flask(__name__)
app.debug = True


class InputForm(Form):
    user_login = StringField(validators=[validators.InputRequired()])


@app.route('/', methods=['POST', 'GET'])
def home():
    form = InputForm(request.form)
    user_login = form.user_login.data

    user_query = twitch.get_user_query(user_login)
    user_info = twitch.get_response(user_query)

    twitch.print_response(user_info)

    try:
        user_id = user_info['data'][0]['id']
        img_url = user_info['data'][0]['profile_image_url']

        user_videos_query = twitch.get_user_videos_query(user_id)
        videos_info = twitch.get_response(user_videos_query)
        twitch.print_response(videos_info)

        videos_info_json_data = videos_info['data']
        videos_info_json_data_reversed = videos_info_json_data[::-1]

        x_labels = []
        x_values = []
        title = user_login + '\'s Video Stats'

        for item in videos_info_json_data_reversed:
            if len(item['title']) == 0:
                x_labels.append('Name Not Found')
            elif len(item['title']) > 20:
                x_labels.append(item['title'][:20] + '...')
            else:
                x_labels.append(item['title'])
            x_values.append(item['view_count'])

        return render_template('d3.html', title=title, max=max(x_values) + 10, labels=x_labels,
                               values=x_values, img_url=img_url)
    except:
        return render_template("form.html", form=form)


if __name__ == '__main__':
    app.run()
