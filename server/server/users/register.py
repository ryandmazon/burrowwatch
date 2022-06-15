from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer, RegisterSerializer, UserSerializer


CustomUser = get_user_model()

class UserApi(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def get(self, request, *args, **kwargs):
        data = list(CustomUser.objects.all().values())
        return JsonResponse(data, safe=False)


class RegisterApi(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        '''
        mail_subject = 'Activate your account.'
        message = {
                    'user': user.email,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.id)),
                    'token': account_activation_token.make_token(user),
        }
        to_email = user.email
        m = json.dumps(message)
        send_mail(mail_subject, m, 'rm@inceptussecure.com', [to_email])
        '''
        return Response({
            "user": UserSerializer(user).data,
            "message": "User Created Successfully. Confirm email and perform Login to get your token",
        })


class LoginApi(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        user = serializer.validate(self, data=request.data)
        try:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        except:
            return user
