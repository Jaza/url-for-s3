import os

import setuptools

module_path = os.path.join(os.path.dirname(__file__), 'url_for_s3.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version__')][0]

__version__ = version_line.split('__version__ = ')[-1][1:][:-2]

setuptools.setup(
    name="url-for-s3",
    version=__version__,
    url="https://github.com/Jaza/url-for-s3",

    author="Jeremy Epstein",
    author_email="jazepstein@gmail.com",

    description="Python function that generates a URL to a given S3 resource.",
    long_description=open('README.rst').read(),

    py_modules=['url_for_s3'],
    zip_safe=False,
    platforms='any',

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
