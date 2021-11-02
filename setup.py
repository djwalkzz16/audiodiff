#! /usr/bin/env python
import os
import sys
from setuptools.command.test import test
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from audiodiff import __version__


install_requires = [
    'mutagenwrapper == 0.0.5',
    'termcolor == 1.1.0',
]


def readme():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
            return f.read()
    except Exception:
        return ''


class pytest(test):

    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        from pytest import main
        errno = main(self.test_args)
        raise SystemExit(errno)


# Hack to prevent stupid TypeError: 'NoneType' object is not callable error on
# exit of python setup.py test # in multiprocessing/util.py _exit_function when
# running python setup.py test (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing
except ImportError:
    pass


setup(
    name='audiodiff',
    version=__version__,
    url='https://github.com/clee704/audiodiff',
    license='MIT',
    author='Choongmin Lee',
    author_email='choongmin@me.com',
    description='Small library for comparing audio files',
    long_description=readme(),
    packages=['audiodiff'],
    install_requires=install_requires,
    tests_require=[
        'pytest == 2.5.2',
        'pytest-cov == 1.6',
        'pytest-pep8 == 1.0.5',
    ],
    cmdclass={'test': pytest},
    entry_points={
        'console_scripts': [
            'audiodiff = audiodiff.commandlinetool:main_func',
        ],
    },
    keywords='lossless audio metadata comparison',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'Topic :: Utilities',
    ],
)
