from flask import Flask, render_template
import socket
import random
import os
import argparse

app = Flask(__name__)
#red FF0000
#green 00FF00
#blue 0000FF
#olive 808000
#purple 800080
#navy 000080
color_codes = {
    "#FF0000": "#FF0000",
    "#00FF00": "#00FF00",
    "#0000FF": "#0000FF",
    "#808000": "#808000",
    "#800080": "#800080",
    "#000080": "#000080"
}

SUPPORTED_COLORS = ",".join(color_codes.keys())

# Get color from Environment variable
COLOR_FROM_ENV = os.environ.get('APP_COLORHEXCODE')
# Generate a random color
COLOR = random.choice(["#FF0000","#00FF00","#0000FF","#808000","#800080","#000080"])
# Get dynamic title from Environment variable
TITLE_FROM_ENV = os.environ.get('APP_TITLE')
# Set default title
TITLE = "Cloud Computing - University of West Attica"

@app.route("/")
def main():
    # return 'Hello'
    return render_template('index.html', name=socket.gethostname(), color=color_codes[COLOR], colorname=COLOR, title=TITLE)


if __name__ == "__main__":
    print("This is a simple flask webapp that displays a colored background and a greeting message. \n"
          "The color can be specified in two different ways: \n"
          "    1. As a command line argument with --colorhexcode as the argument. Accepts one of the following \n"
          "       colors according the list below. \n"
          "    2. As an Environment variable APP_COLORHEXCODE. Accepts one of the following hex colors according \n"
          "       the list below.\n"
          "In any other case, a random color is picked from the list below.\n"
          "\n"
          "Note 1: Accepted hex colors [" + SUPPORTED_COLORS + "] \n"
          "Note 2: Command line argument precedes over environment variable.\n"
          "\n"
          "")


    # Check for Command Line Parameters for color
    parser = argparse.ArgumentParser()
    parser.add_argument('--colorhexcode', required=False)
    # Check for Command Line Parameters for title
    parser.add_argument('--title', required=False)
    args = parser.parse_args()

    if args.colorhexcode:
        print("colorhexcode from command line argument =" + args.colorhexcode)
        COLOR = args.colorhexcode
        if COLOR_FROM_ENV:
            print("A colorhexcode was set through environment variable -" + COLOR_FROM_ENV + ". However, colorhexcode from command line argument takes precendence.")
    elif COLOR_FROM_ENV:
        print("No Command line argument. colorhexcode from environment variable =" + COLOR_FROM_ENV)
        COLOR = COLOR_FROM_ENV
    else:
        print("No command line argument or environment variable. Picking a Random colorhexcode =" + COLOR)

    # Check if input color is a supported one
    if COLOR not in color_codes:
        print("colorhexcode not supported. Received '" + COLOR + "' expected one of " + SUPPORTED_COLORS)
        exit(1)

    if args.title:
        print("Title from command line argument =" + args.title)
        TITLE = args.title
        if TITLE_FROM_ENV:
            print("A title was set through environment variable -" + TITLE_FROM_ENV + ". However, title from command line argument takes precendence.")
    elif TITLE_FROM_ENV:
        print("No Command line argument. Title from environment variable =" + TITLE_FROM_ENV)
        TITLE = TITLE_FROM_ENV
    else:
        print("No command line argument or environment variable. Picking a default title =" + TITLE)


    # Run Flask Application
    app.run(host="0.0.0.0", port=8000)
