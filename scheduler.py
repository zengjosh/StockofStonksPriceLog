import schedule
import time
import subprocess

def run_script():
    subprocess.run(["python", "D:/Desktop/sbBazaar/datalog.py"])

schedule.every(2).minutes.do(run_script)

while True:
    schedule.run_pending()
    time.sleep(1)
