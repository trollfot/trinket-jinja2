from os import path
from setuptools import setup, find_packages


def read(filename):
    with open(path.join(path.dirname(__file__), filename)) as f:
        return f.read()


install_requires = [
    "jinja2 >= 2.10"
    ]

tests_require = [
    "curio >= 0.9",
    "trinket >= 0.1.2",
    "pytest",
    ]

setup(name='trinket_jinja2',
      version='0.1',
      description="Trinket webserver Jinja2 templating utility",
      long_description="%s\n\n%s" % (
          read('README.rst'), read(path.join('docs', 'HISTORY.rst'))),
      keywords="Curio Trinket",
      author="",
      author_email="",
      license="BSD",
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require={'test': tests_require},
      )
