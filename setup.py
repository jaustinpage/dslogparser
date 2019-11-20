from setuptools import setup

setup(name='dslogparser',
      version='0.0.1',
      description='FRC Driver Station logs parser',
      url='http://github.com/ligerbots/dslogparser',
      author='Paul Rensing',
      author_email='',
      license='',
      packages=['dslogparser'],
      install_requires=[
          'bitstring',
      ],
      zip_safe=False)
