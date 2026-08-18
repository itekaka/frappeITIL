from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

setup(
	name="itil_master_control",
	version="1.0.0",
	description="ITIL 4 Master Control Panel - Enterprise ITSM & Service Value Stream Mapper built on Frappe Framework",
	author="ITIL Master Team",
	author_email="dev@itilmaster.local",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
