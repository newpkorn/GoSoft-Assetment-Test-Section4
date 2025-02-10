import sys
from setuptools import find_packages, setup

if "--with-xunit" in sys.argv:
    sys.argv.remove("--with-xunit")

packages = [
    'selenium==4.10.*',
    'chromedriver-binary-auto',
    'pytest',
    'pytest-runner==5.2',
]

setup(
    name='python-selenium-medium-zoo-clinic',
    version='1.0.0',
    author='Devskiller.com',
    author_email='support@devskiller.com',
    python_requires='>=3.5',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    test_suite='test',
    install_requires=packages + ['setuptools'],
    tests_require=packages,
)
