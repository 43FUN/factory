from django.shortcuts import render
from feedback.form import FeedbackForm

# Create your views here.


def feedback(request):
    form = FeedbackForm(request.POST or None)
    args = {}
    args['form'] = form
    if request.method == 'POST':
            form.save()
            return redirect('feedback:feedback')
    return render(request, 'feedback.html', args)

'''def feedback(request):
    args = {}
    args['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/articles/get/%s/' % article_id)
    return render(request, 'article_edit.html', args)'''
