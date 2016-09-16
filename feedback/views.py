# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from feedback.form import FeedbackForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

# Create your views here.


def feedback(request):
    form = FeedbackForm(request.POST or None, request.FILES or None)
    args = {}
    args['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            feedback = form.save()
            name = feedback.name
            email = feedback.email
            phone = feedback.phone
            text = feedback.text
            file = feedback.file or None
            date = feedback.date
            subject, from_email, to = 'Оставлен отзыв на сайте',\
                                      're.wew2016@yandex.ru',\
                                      'stream-92@mail.ru'
            text_content = '.None'
            html_content = '<p>Имя: {}</p> <p>Email: {}</p>' \
                           ' <p>Телефон: {}</p> <p>Текст сообщения:'\
                           ' {}</p> Дата: {}'.format(
                                                    name,
                                                    email,
                                                    phone,
                                                    text,
                                                    date)
            msg = EmailMultiAlternatives(subject, text_content,
                                         from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            if file != None:
                msg.attach_file(file.path)
                msg.send()
            elif file == None:
                msg.send()
            return redirect('feedback:feedback')
    return render(request, 'feedback.html', args)


