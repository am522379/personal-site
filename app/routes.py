
from flask import render_template, request, flash, redirect, url_for, current_app
import app.constants as constants
from app.forms import ContactForm
from app import app
from app.email import send_email

@app.route('/', methods=['GET', 'POST'])
# @app.route('/index', methods=['GET', 'POST'])
def index():

    form = ContactForm()

    if request.method == 'POST' and form.validate_on_submit():
        send_email(subject='Personal Site: New message from ' + form.name.data,
                    sender=current_app.config['ADMINS'][0],
                    recipients=[form.email.data],
                    text_body=form.message.data,
                    html_body=form.message.data
        )

        flash(message='Thanks for your message.', category='success')
        return redirect(url_for('index'))

    gallery = constants.obtain_gallery()

    return render_template('index.html',
                            books=constants.books,
                            certifications=constants.certifications,
                            education=constants.education,
                            skills=constants.skills,
                            gallery=gallery,
                            interests=constants.interests,
                            experiences=constants.experiences,
                            form=form
                            )