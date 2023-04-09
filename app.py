from flask import Flask

import database
import spreadsheet
import cbrf

app = Flask(__name__)


@app.route('/',methods=["GET"])
def get_data():
    
    ss_page_token = spreadsheet.get_page_token()
    
    if not database.check_page_token(ss_page_token):
        ss_table_data = spreadsheet.get_data()
        database.update_orders(ss_table_data, ss_page_token)

    cb_usd_course = cbrf.get_usd_course()
    database.update_usd_course(cb_usd_course) 

    return {"orders":database.get_orders()},200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')