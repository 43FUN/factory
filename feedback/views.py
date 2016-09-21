# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from feedback.form import FeedbackForm
from django.core.mail import EmailMultiAlternatives


def feedback(request):
    form = FeedbackForm(request.POST or None, request.FILES or None)
    args = {}
    args['title'] = 'Контакты'
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
            subject, from_email, to = ('Оставлен отзыв на сайте',
                                       're.wew2016@yandex.ru',
                                       'stream-92@mail.ru')
            data = {'name': name, 'email': email, 'phone': phone,
                    'text': text, 'date': date}
            text_content = render_to_string('email_text.html', data)
            html_content = render_to_string('email_html.html', data)
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


