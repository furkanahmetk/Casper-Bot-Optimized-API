from src.app import create_app
from flask_apscheduler import APScheduler
from src.service.repeated_tasks import Repeated_Task

app = create_app()
#Start application, before starting flask application it configures and runs cron job to retrieve data
if __name__ == '__main__':
    
    scheduler = APScheduler()
    task = Repeated_Task()
    scheduler.add_job(id = '1', func = task.data_cron, trigger = 'interval', seconds = 5*60)
    scheduler.start()
    app.run(host='0.0.0.0',port=5555, debug=False,use_reloader=False)
