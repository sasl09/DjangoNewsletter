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


<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 28a4ca38c4cd9385736f9ad15eeb5ae7488ffd53
class NewslettersViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = NewsletterSerializer

    def get_queryset(self):
        return TagsNewsletter.objects.all().order_by('date_added')
        # return TagsNewsletter.objects.filter(author=self.request.user).order_by('date_added')


class TagsViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
class NewslettersViewSet(viewsets.ModelViewSet):
=======
<<<<<<< HEAD
class NewslettersViewSet(viewsets.ModelViewSet):
=======
<<<<<<< HEAD
class NewslettersViewSet(viewsets.ModelViewSet):
=======
<<<<<<< HEAD
class NewslettersViewSet(viewsets.ModelViewSet):
=======
class NewslettersViewSet(viewsets.ReadOnlyModelViewSet):
>>>>>>> b45c2250c6ca585848e16ee36ed4d5b47c91bea1
>>>>>>> 6fbf1c87481d04d8b2b9e4646d7dee9dd692d903
>>>>>>> 4a51a5607dbdc881353c89d80ffa8b61fbfb97fd
>>>>>>> 83dc61fee60c4eba1255746d125f42f15fceaa24
    permission_classes = (IsAuthenticated,)
    serializer_class = NewsletterSerializer

    def get_queryset(self):
        return TagsNewsletter.objects.filter(author=self.request.user).order_by('date_added')


class TagsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
>>>>>>> d60f817bc5b4c51445fc8a176c2960a3e9e5a9a2
>>>>>>> 28a4ca38c4cd9385736f9ad15eeb5ae7488ffd53
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer


class UsersViewSet(viewsets.ModelViewSet):
<<<<<<< HEAD
    # permission_classes = (IsAuthenticated,)
=======
<<<<<<< HEAD
    # permission_classes = (IsAuthenticated,)
=======
    permission_classes = (IsAuthenticated,)
>>>>>>> d60f817bc5b4c51445fc8a176c2960a3e9e5a9a2
>>>>>>> 28a4ca38c4cd9385736f9ad15eeb5ae7488ffd53
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class SubscribersViewSet(viewsets.ModelViewSet):
<<<<<<< HEAD
    # permission_classes = (IsAuthenticated,)
=======
<<<<<<< HEAD
    # permission_classes = (IsAuthenticated,)
=======
    permission_classes = (IsAuthenticated,)
>>>>>>> d60f817bc5b4c51445fc8a176c2960a3e9e5a9a2
>>>>>>> 28a4ca38c4cd9385736f9ad15eeb5ae7488ffd53
    queryset = Subscriber.objects.all()
    serializer_class = SubscribersSerializer


