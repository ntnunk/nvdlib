import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='nvdlib',
    packages=find_packages(include=['nvdlib']),
    version='0.8.3',
    install_requires = ['requests'],
    extras_require={
        "dev": [
            "responses==0.18.0",
            "pytest==7.0.1",
        ]
    },
    python_requires='>=3.11.0',
    description='National Vulnerability Database CPE/CVE API Library for Python',
    author='Vehemont',
    author_email="brad@nvdlib.com",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Vehemont/nvdlib/",
    license='MIT',
)
