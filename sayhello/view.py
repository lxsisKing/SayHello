from flask import flash, redirect, render_template, url_for
from sayhello import app
from sayhello.form import HelloForm
from sayhello.models import Message
from sayhello.extensions import db




@app.route('/', methods=['GET', 'POST'])
def index():
    # 加载所有记录
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)  # 实例化模型类，创建记录
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))  # 重定向到首页

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)