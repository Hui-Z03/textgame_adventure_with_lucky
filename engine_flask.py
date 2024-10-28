# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import content

app = Flask(__name__)

# Initialize global variable for tracking current scene
current_scene = 'start'

@app.route('/', methods=['GET', 'POST'])
def game():
    global current_scene
    error_message = None
    
    if request.method == 'POST':
        choice = request.form.get('choice')
        # check if restart
        if choice == 'restart':
            current_scene = 'start'
        # check if input valid
        elif choice in content.game_content[current_scene]['choices']:
            current_scene = content.game_content[current_scene]['choices'][choice]
        else:
            error_message = 'Invalid choice, please try again.'

    # sence and choice
    scene = content.game_content[current_scene]
    return render_template('game.html',
                           description = scene['description'],
                           choices = scene['choices'],
                           image = scene['image'],
                           error_message=error_message)


# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
