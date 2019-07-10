from flask import Flask, render_template, url_for, request, redirect
import sqlite3
from time import gmtime, strftime

conn = sqlite3.connect('jobslogDB.db', check_same_thread=False) # this is to connect database to Flask
db = conn.cursor()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    entry = db.execute("SELECT * FROM LogTable")
    if request.method == 'GET':
        return render_template('homepage.html', entry=entry)
    else:
        date = request.form.get("job_date") # Date in LogTable
        time = request.form.get("job_time") # Time in LogTable
        job = request.form.get("job_options") # Job in LogTable
        description = request.form.get("job_description") # Description in LogTable
        outcome = request.form.get("job_outcome") # Outcome in LogTable
        comments = request.form.get("job_outcome") # Comments in LogTable
        date_entry = strftime("%d-%m-%y", gmtime()) # Date_Entry in LogTable
        time_entry = strftime("%H:%M", gmtime()) # Time_Entry in LogTable
        
        db.execute("INSERT INTO LogTable (Date, Time, Job, Description, Outcome, Comments, Date_Entry, Time_Entry) VALUES (?,?,?,?,?,?,?,?)", (date, time, job, description, outcome, comments, date_entry, time_entry))
        conn.commit()
        
        return redirect(url_for("home"))
        

@app.route('/job_reports', methods=['GET', 'POST'])
def job_reports():
    entry = db.execute("SELECT * FROM LogTable")
    if request.method == 'GET':
        return render_template('jobsLog_reports.html')        
    else:
        # btn = request.form.get('sub_btn')

        # # if request.method.post == None
        # #     return redirect(url_for('home'))
        # else:
        if request.form.get("report_options") == "installs":
            entry = db.execute("SELECT * FROM LogTable WHERE Job = ?", ("installs",))
            return render_template('jobsLog_reports.html', entry=entry)
        elif request.form.get("report_options") == "maintenance":
            entry = db.execute("SELECT * FROM LogTable WHERE Job = ?", ("maintenance",))
            return render_template('jobsLog_reports.html', entry=entry)
        elif request.form.get("report_options") == "room_check":
            entry = db.execute("SELECT * FROM LogTable WHERE Job = ?", ("room_check",))
            return render_template('jobsLog_reports.html', entry=entry)
        elif request.form.get("report_options") == "audit_checks":
            entry = db.execute("SELECT * FROM LogTable WHERE Job = ?", ("audit_checks",))
            return render_template('jobsLog_reports.html', entry=entry)
        elif request.form.get("report_options") == "project_installs":
            entry = db.execute("SELECT * FROM LogTable WHERE Job = ?", ("project_installs",))
            return render_template('jobsLog_reports.html', entry=entry)
        else:
            if request.form.get("report_options") == None:
                return redirect(url_for('job_reports'))
                # this redirects you back to the page if the user presses the Submit Report button without entering the table
        
                    


@app.route('/outcome_reports', methods=['GET', 'POST'])
def outcome_reports():
    entry = db.execute("SELECT * FROM LogTable")
    if request.method == 'GET':
        return render_template('outcomeLog_reports.html')
    else:
        if request.form.get("job_outcome") == "issue_resolved":
            entry = db.execute("SELECT * FROM LogTable WHERE Outcome = ?", ("issue_resolved",))
            return render_template('outcomeLog_reports.html', entry=entry)
        elif request.form.get("job_outcome") == "ongoing_issue":
            entry = db.execute("SELECT * FROM LogTable WHERE Outcome = ?", ("ongoing_issue",))
            return render_template('outcomeLog_reports.html', entry=entry)
        elif request.form.get("job_outcome") == "placed_order":
            entry = db.execute("SELECT * FROM LogTable WHERE Outcome = ?", ("placed_order",))
            return render_template('outcomeLog_reports.html', entry=entry)
        elif request.form.get("job_outcome") == "escalated":
            entry = db.execute("SELECT * FROM LogTable WHERE Outcome = ?", ("escalated",))
            return render_template('outcomeLog_reports.html', entry=entry)
        else:
            if request.form.get("job_outcome") == None:
                return redirect(url_for('outcome_reports'))
                # this redirects you back to the page if the user presses the Submit Report button without entering the table

if __name__ == '__main__':
    app.run(debug=True)
