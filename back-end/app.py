##########################IMPORTS
from sys import argv
from datetime import date

from flask import Flask
from flask_cors import CORS, cross_origin
from apscheduler.schedulers.background import BackgroundScheduler

import database
import spreadsheet
import cbrf
import bot

##########################INITIALIZATION
is_schedule = '--schedule' in argv
app = Flask(__name__)
cors = CORS(app)
sched = BackgroundScheduler(daemon=True)

app.config['CORS_HEADERS'] = 'Content-Type'

##########################UTILS
def update_db(): #Check google sheet for updates
    ss_page_token = spreadsheet.get_page_token()
    
    if not database.check_page_token(ss_page_token):
        ss_table_data = spreadsheet.get_data()
        database.update_orders(ss_table_data, ss_page_token)

    cb_usd_course = cbrf.get_usd_course()
    database.update_usd_course(cb_usd_course) 


def check_delivery_dates(): #Check db for old deliveries and send TG message 
    update_db()
    orders = database.get_orders()
    now = date.today()
    old_orders_lst = [str(x['order_id']) for x in orders if x['delivery_date'] <= now]
    if old_orders_lst:
        old_orders_str = ','.join(old_orders_lst)
        bot.send_message_to_all_users(f"Подошёл к концу срок доставки заказов с номерами: {old_orders_str}")
    

##########################ROUTES
@cross_origin
@app.route('/',methods=["GET"])
def get_data():
    if not is_schedule:
        update_db()
    return {"orders":database.get_orders()},200


##########################SCHEDULE
if is_schedule :
    sched.add_job(update_db,'interval',seconds=10)

sched.add_job(check_delivery_dates, 'cron', day_of_week='mon-sun', hour=8, minute=0)

##########################RUN
if __name__ == "__main__":
    check_delivery_dates()
    sched.start()
    app.run(debug=True, host='0.0.0.0')