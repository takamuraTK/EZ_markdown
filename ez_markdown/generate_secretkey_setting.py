"""
git clone時に以下を実行することで、SECRET_KEYが実行される
$ python generate_secretkey_setting.py > local_settings.py
"""

from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
text = 'SECRET_KEY = \'{0}\''.format(secret_key)
print(text)