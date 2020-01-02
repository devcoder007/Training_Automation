from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.http import HttpResponse
import uuid
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# from django.urls import reverse
# from django.utils.encoding import force_bytes
# from django.utils.encoding import force_text
# from django.utils.http import urlsafe_base64_encode
# from django.contrib.auth.tokens import default_token_generator

# Create your views here.

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer,TrainerInfoSerializer,TrainerName,EmailSerializer,TokenSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import TrainerInfo,Trainer,EmailSend


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.User.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class TrainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TrainerInfo.objects.all()
    serializer_class = TrainerInfoSerializer
    def post(self,request):
        serializer = TrainerInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FetchUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    # queryset = User.objects.filter(username = request.data.username).filter(password = request.data.password)

    serializer_class = UserSerializer
    def get(self,request):
        queryset = User.objects.filter(username = request.data.username).filter(password = request.data.password)
        return Response(queryset, status=status.HTTP_200_OK)


class trainerName(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Trainer.objects.all()
    # queryset = User.objects.filter(username = request.data.username).filter(password = request.data.password)

    serializer_class = TrainerName
    def get(self,request):
        queryset = Trainer.objects.all()
        return Response(queryset, status=status.HTTP_200_OK)
        


def email(request,user):
    # random_str = str(uuid.uuid4())
    # random_str = random_str.upper()
    # random_str = random_str[:6]
    q = User.objects.filter(username = user)
    # q.update(token = random_str)
    # print(request)
    # subject = 'Thank you for registering to our site' + request['username']
    # message = ' it  means a world to us '
    # email_from = 'kampuskonnect.kk@gmail.com'
    # recipient_list = [request['email'],]
    # send_mail( subject, message, email_from, recipient_list )
    # # return HttpResponse("sent")
    text_content = 'Account Activation Email'
    subject = 'Email Activation'
    template_name = "activation.html"
    # from_email = settings.DEFAULT_FROM_EMAIL
    # recipients = [request['email']]
    # print(urlsafe_base64_encode(force_bytes(user.pk)))
    # kwargs = {
    #     "uid": urlsafe_base64_encode(force_bytes(user.pk)),
    #     "token": default_token_generator.make_token(user)
    # }
    # activation_url = reverse("activate_user_account", kwargs=kwargs)

    # activate_url = "{0}://{1}{2}".format(request.scheme, request.get_host(), activation_url)

    context = {
        'user': user,
        'activate_url': user.token,
        'email': request['email']
    }
    # subject = 'Thank you for registering to our site' + request['username']
    # message = ' it  means a world to us '+ context['activate_url']
    from_email = 'kampuskonnect.kk@gmail.com'
    recipients = [request['email']]
    # send_mail( subject, message, email_from, recipient_list )
    html_content = render_to_string(template_name, context)
    email = EmailMultiAlternatives(subject, text_content, from_email, recipients)
    email.attach_alternative(html_content, "text/html")
    email.send()





class EmailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmailSend.objects.all()
    serializer_class = EmailSerializer
    print("fsgd")
    def post(self,request):
        print("i m in email")
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            print(request.data)
            print("asdfs")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def sendMassEmail()
def test(request):
    dict_var = {'template_var' : 'I am used to tag a HTML file template with the Django'}
    return render(request,'test.html', {'template_var':'value'})


class sendToken(APIView):
    # print("hii")
    # # queryset = User.objects.all()
    # # # queryset = User.objects.filter(username = request.data.username).filter(password = request.data.password)

    # # serializer_class = TokenSerializer
    # print("bbb")
    
    # def get(self,request):
    #     print("dddd")
    #     print(request.GET['id'])
    #     queryset = User.objects.get(id = request.GET['id'])
    #     # print (queryset.token, queryset.id)
    #     return Response(querysetstatus=status.HTTP_200_OK)
    pass

class verifyRegister(APIView):
    def get(self,request):
        q = User.objects.filter(id = request.GET['id'])
        q.update(is_active = True)
        
        return Response({'st':'You are Authenticated'},status=status.HTTP_200_OK )