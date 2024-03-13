from setuptools import setup

setup (
  name= 'frog',
  version = '0.1',
  package = ['frog'],
  entry_points = {
    'console_scripts': [
      'frog = frog.frog_cli:main'
    ]
  }

)