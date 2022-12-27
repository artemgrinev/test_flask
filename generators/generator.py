from data.data import Users
from randomuser import RandomUser

random_user = RandomUser({'nat': 'us'})


def generator_user():
    yield Users(
        name=random_user.get_username(),
        email=random_user.get_email(),
        password=random_user.get_password()
    )

