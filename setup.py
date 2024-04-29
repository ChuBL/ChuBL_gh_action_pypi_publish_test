from setuptools import setup, find_packages

setup(
    name="chubl_pypi_action_test",
    version="0.0.2",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[],  # External packages as dependencies
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple example package",
    keywords="example",
)
