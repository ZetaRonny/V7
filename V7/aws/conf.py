import datetime
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

AWS_GROUP_NAME = "S3Bucket"
AWS_USER_NAME =  "V7BucketUser"
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'V7.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'V7.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME ='variantseven'
S3DIRECT_REGION = 'us-east-2'
S3_URL = '//%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL +'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GTM")

AWS_HEADER = {
	'expires':expires,
	'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()),),
}

