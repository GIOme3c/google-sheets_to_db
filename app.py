from flask import Flask
from flask_cors import CORS, cross_origin
from apscheduler.schedulers.background import BackgroundScheduler
from sys import argv

import database
import spreadsheet
import cbrf


is_schedule = '--schedule' in argv
app = Flask(__name__)
cors = CORS(app)
sched = BackgroundScheduler(daemon=True)

app.config['CORS_HEADERS'] = 'Content-Type'

def update_db():
    ss_page_token = spreadsheet.get_page_token()
    
    if not database.check_page_token(ss_page_token):
        ss_table_data = spreadsheet.get_data()
        database.update_orders(ss_table_data, ss_page_token)

    cb_usd_course = cbrf.get_usd_course()
    database.update_usd_course(cb_usd_course) 

if is_schedule :
    sched.add_job(update_db,'interval',seconds=10)

@cross_origin
@app.route('/',methods=["GET"])
def get_data():
    if not is_schedule:
        update_db()
    return {"orders":database.get_orders()},200


if __name__ == "__main__":
    sched.start()
    app.run(debug=True, host='0.0.0.0')