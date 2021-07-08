"""
Flask-Markdown is a markdown processing filter for Flask.

This is a maintenance fork of Flask-Markdown.

This project can be found at: https://github.com/brmullikin/flask-markdown
The original is at: http://github.com/dcolish/flask-markdown

The goal of this fork is to eventually get merged back into the original.
"""
from setuptools import setup


setup(
    name='Flask-Markdown',
    version='0.4',
    url='http://github.com/brmullikin/flask-markdown',
    license='BSD',
    author='Dan Colish (author), B. R. Mullikin (forker)',
    author_email='dcolish@gmail.com (author), ben@brmullikin.com (forker)',
    description='Small extension to make using markdown easy',
    long_description=__doc__,
    packages=['flask_markdown'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'markdown',
    ],
    tests_require=[
        'pytest',
        'pytest-flask'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
