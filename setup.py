import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

SSHTarpit_packages = setuptools.find_packages()
SSHTarpit_packages.append('twisted.plugins')

setuptools.setup(
    name="SSHTarpit",
    version="0.0.1",
    author="Thomas Westfeld",
    author_email="westfeld@mac.com",
    description="Dummy SSH server that will hold incoming connections forever",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["twisted"],
    url="https://github.com/westfeld/sshtarpit",
    packages=SSHTarpit_packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
