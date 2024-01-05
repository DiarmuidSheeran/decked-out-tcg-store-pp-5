from pathlib import Path
import os
if os.path.isfile('env.py'):
    import env

BASE_DIR = Path(__file__).resolve().parent.parent

STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')