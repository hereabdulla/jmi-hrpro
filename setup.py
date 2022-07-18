from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hrpro/__init__.py
from hrpro import __version__ as version

setup(
	name="hrpro",
	version=version,
	description="HRPRO for JMI",
	author="TEAMPRO",
	author_email="hr@groupteampro.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
