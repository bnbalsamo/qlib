from setuptools import setup, find_packages

def readme():
    with open("README.md", 'r') as f:
        return f.read()

setup(
    name = "qlib",
    version = "0.0.1",
    description = "A library for use by the digital repository " +
    "microservices to handle queuing operations",
    long_description = readme(),
    packages = find_packages(
        exclude = [
        ]
    ),
    install_requires = [
        'redis'
    ],
)
