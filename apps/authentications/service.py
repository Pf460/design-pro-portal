from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class AuthenticationViewFunction:
    @staticmethod
    def register_user(validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            fio=validated_data['fio'],
            password=validated_data['password1']
        )

    @staticmethod
    def login_user(username, password):
        return authenticate(username=username, password=password)

