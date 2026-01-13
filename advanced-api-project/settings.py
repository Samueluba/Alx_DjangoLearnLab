# Use the custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Add media configuration for profile photo uploads
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
