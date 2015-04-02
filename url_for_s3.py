__version__ = '0.1.0'


def url_for_s3(endpoint, bucket_name, bucket_domain=None, scheme='',
               url_style='host', cdn_domain=None, filename=None):
    """
    Generates an S3 URL to the given endpoint, using the
    given bucket config.

    Example:
    url_for_s3('static', bucket_name='my-cool-foobar-bucket',
               scheme='https', filename='pics/logo.png')

    Will return:
    https://my-cool-foobar-bucket.s3.amazonaws.com/static/pics/logo.png

    Note: this function assumes that the given resource exists on S3
    and is publicly accessible.

    Based loosely on Flask-S3's url_for().
    """

    if not bucket_name:
        raise ValueError('Bucket name is required when calling url_for_s3().')

    if url_style == 'host':
        url_format = '%(bucket_name)s.%(bucket_domain)s'
    elif url_style == 'path':
        url_format = '%(bucket_domain)s/%(bucket_name)s'
    else:
        raise ValueError('Invalid S3 URL style: "%s"'
                         % url_style)

    if bucket_domain == None:
        bucket_domain = u's3.amazonaws.com'

    bucket_path = url_format % {
        'bucket_name': bucket_name,
        'bucket_domain': bucket_domain,
    }

    if cdn_domain:
        bucket_path = '%s' % cdn_domain

    # The return statement below is equivalent to:
    #
    # urls = app.url_map.bind(bucket_path, url_scheme=scheme)
    # return urls.build(endpoint, values=values, force_external=True)
    #
    # (assuming that this function receives a **values parameter
    # instead of filename).
    #
    # But we do it manually instead, so we can avoid dependency on
    # flask.current_app and werkzeug.routing.MapAdapter.

    return str('%s//%s/%s%s' % (
        scheme + (':' if scheme else ''),
        bucket_path,
        endpoint + ('/' if endpoint else ''),
        filename.lstrip('/')
    ))

