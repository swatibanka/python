import schedule

def job():
    print("hello python students")
    print("sunday we have class")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
