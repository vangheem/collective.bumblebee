from setuptools import setup, find_packages
import os

version = '1.0a1'

setup(name='collective.bumblebee',
      version=version,
      description="Integration of Bumblebee into plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone theming diazo deliverance bumblebee',
      author='Nathan Van Gheem',
      author_email='vangheem@gmail.com',
      url='https://github.com/vangheem/collective.bumblebee',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Bumblebee',
          'plone.transformchain',
          'plone.app.registry'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
