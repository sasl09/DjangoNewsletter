from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Tag, TagsNewsletter, Subscriber
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .forms import SubscriberForm, UnSubscribeForm
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .serializers import NewsletterSerializer, UsersSerializer, TagsSerializer, SubscribersSerializer


# Create your views here.

def newsletter_main(request):
    context = {
        'tags': Tag.objects.all(),
    }
    template = 'newsLetterApp/main.html'
    return render(request, template, context)


def newsletter_bulletins(request):
    context = {
        'bulletins': TagsNewsletter.objects.all()
    }
    template = 'newsLetterApp/bulletins.html'
    return render(request, template, context)


def newsletter_categories(request):
    req = str(request)
    req = req[47:-2].capitalize()
    context = {
        'categories': TagsNewsletter.objects.filter(tags__name=req),
        'tags': Tag.objects.filter(name=req)
    }
    template = 'newsLetterApp/categories.html'
    return render(request, template, context)


# Helper Functions
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)


@csrf_exempt
def newsletter_subscribe(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=sub.email,
            subject='Newsletter Confirmation',
            html_content='Thank you for signing up for my email newsletter! \
                Please complete the process by \
                <a href="{}?email={}&conf_num={}"> clicking here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('/confirm_email/'),
                                                    sub.email,
                                                    sub.conf_num))

        sg = SendGridAPIClient(settings.EMAIL_HOST_PASSWORD)
        response = sg.send(message)
        return render(request, 'newsLetterApp/subscribe.html', {'email': sub.email, 'action': 'added', 'form': SubscriberForm()})
    else:
        return render(request, 'newsLetterApp/subscribe.html', {'form': SubscriberForm()})


def confirm_email(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'newsLetterApp/subscribe.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'newsLetterApp/subscribe.html', {'email': sub.email, 'action': 'denied'})


def newsletter_unsubscribe(request):
    if request.method == 'POST':
        sub = Subscriber.objects.filter(email=request.POST['email']).first()
        sub.delete()
        return render(request, 'newsLetterApp/unsubscribe.html', {'email': sub.email, 'action': 'unsubscribed', 'form': UnSubscribeForm()})
    else:
        return render(request, 'newsLetterApp/unsubscribe.html', {'form': UnSubscribeForm()})


class NewslettersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = NewsletterSerializer

    def get_queryset(self):
        return TagsNewsletter.objects.filter(author=self.request.user).order_by('date_added')


class TagsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer


class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class SubscribersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Subscriber.objects.all()
    serializer_class = SubscribersSerializer


