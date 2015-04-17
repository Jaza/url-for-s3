url-for-s3
==========

Python function that generates a URL to a given S3 resource.

Example
-------

.. code:: python

    url_for_s3('static', bucket_name='my-cool-foobar-bucket',
               scheme='https', filename='pics/logo.png')

Will return:
https://my-cool-foobar-bucket.s3.amazonaws.com/static/pics/logo.png

Note: this function assumes that the given resource exists on S3 and is publicly accessible.

Based loosely on Flask-S3's `url_for()`.

For a complete, working Flask app that demonstrates url-for-s3 in action, have a look at `flask-s3-save-example <https://github.com/Jaza/flask-s3-save-example>`_.
