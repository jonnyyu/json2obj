import os
from setuptools import setup

min_version = os.getenv('MIN_VER', '0')

setup(name='json2obj',
      version=f'1.0.{min_version}',
      description='json2obj',
      url='https://git.autodesk.com/AutoCAD-CI/json2obj',
      author='AutoCAD CI Team',
      author_email='autocad.ci@autodesk.com',
      license='ADSK',
      packages=['src'],
      zip_safe=False)
