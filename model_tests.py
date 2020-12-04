from posts.models import User

pablo= User.objects.create(
    email='pablo@gmail.com',
    password='1234567',
    first_name='Pablo',
    last_name='Trinidad'
)
