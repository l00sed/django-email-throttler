import os
from os.path import abspath, dirname, join
from setuptools import setup


# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Get proper long description for package
current_dir = dirname(abspath(__file__))

# Get the long description from README.md
setup(
    name="django-email-throttler",
    version="0.2.4",
    packages=["django-email-throttler"],
    include_package_data=True,
    license="GPLv3",
    description="An email throttler for Django",
    long_description="A Django email backend and more to limit the amount of mails sent out",
    url="https://github.com/robert-kisteleki/django-email-throttler",
    download_url="https://github.com/robert-kisteleki/django-email-throttler",
    author="Robert Kisteleki",
    author_email="kistel@gmail.com",
    install_requires=[
        "Django>=1.8",
    ],
    keywords=['Django', 'email'],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
