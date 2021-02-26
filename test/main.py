from flask import Flask, render_template, url_for
from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'


@app.route('/')
def main():
    db_session.global_init('db/mars_explorer.db')
    db_sess = db_session.create_session()

    # Код создания базы данных
    '''data = (('Deployment of residential modules 1 and 2', 'Scott Ridley', 15, '2, 3', False),
            ('Exploration of mineral resources', 'Weir Andy', 15, '4, 3', False),
            ('Development of a management system', 'Sanders Teddy', 25, '5', False))
    for inform_job in data:
        job = Jobs()
        job.job, job.team_leader, job.work_size, job.collaborators,\
            job.is_finished = inform_job
        db_sess.add(job)'''
    jobs = db_sess.query(Jobs).all()
    db_sess.commit()

    param = {
        'css_file': url_for('static', filename='css/style.css'),
        'jobs': jobs
    }
    return render_template('index.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

