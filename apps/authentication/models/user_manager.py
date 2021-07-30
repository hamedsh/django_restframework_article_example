from django.contrib.auth.models import BaseUserManager, User


class UserManager(BaseUserManager):
    def create_user(self, username: str, email: str, password: str=None) -> User:
        if username is None:
            raise TypeError('new user should have username')
        if email is None:
            raise TypeError('new user should have email')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username: str, email: str, password: str) -> User:
        if password.strip() == '':
            raise TypeError('new user should have password')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
