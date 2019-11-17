from setuptools import setup

setup(name='dslog',
      version='0.0.1',
      description='FRC Driver Station logs parser',
      url='http://github.com/ligerbots/dslog',
      author='Paul Rensing',
      author_email='',
      license='',
      packages=['dslog'],
      install_requires=[
          'bitstring',
      ],
      zip_safe=False)
