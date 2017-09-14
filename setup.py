from setuptools import setup, find_packages


def readme():
    with open("README.md", 'r') as f:
        return f.read()


setup(
    name="qlib",
    description="A library for implementing 'unreliable' redis priority queues.",
    version="0.0.2",
    long_description=readme(),
    author="Brian Balsamo",
    author_email="brian@brianbalsamo.com",
    packages=find_packages(
        exclude=[
        ]
    ),
    include_package_data=True,
    url='https://github.com/bnbalsamo/qlib',
    install_requires=[
        'redis'
    ],
    tests_require=[
        'pytest'
    ],
    test_suite='tests'
)
