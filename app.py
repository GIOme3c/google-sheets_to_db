from flask import Flask

import database
import spreadsheet

app = Flask(__name__)


@app.route('/',methods=["GET"])
def get_data():
    

    ss_page_token = spreadsheet.get_page_token()

    return {},200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')