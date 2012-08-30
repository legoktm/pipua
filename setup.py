"""
pipua
----------

pipua is a script that effectively checks for updates on all of your installed packages
"""

from setuptools import setup, find_packages

setup(
    name='pipua',
    version='0.0.1',
    author='Kunal Mehta',
    author_email='legoktm@gmail.com',
    packages=find_packages(),
    url='https://github.com/legoktm/pipua/',
    license='MIT License',
    description='pipua is a script that effectively checks for updates on all of your installed packages',
#    long_description=open('README.md').read(),
    long_description='Updates all installed pip packages',
    install_requires=open('requirements.txt').read().split("\n"),
    package_data={
        '': ['*.txt', '*.md']
    },
    classifiers=[
      'License :: OSI Approved :: MIT License',
      'Operating System :: MacOS :: MacOS X',
      'Operating System :: Microsoft :: Windows',
      'Operating System :: POSIX',
      'Environment :: Console',
      'Programming Language :: Python',
    ],
    entry_points = {
        'console_scripts': [
            'pipua = pipua:main'
        ],
    }
)
