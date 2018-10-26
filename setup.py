import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="saint",
    version="0.0.1",
    author="deletescape",
    author_email="me@deletescape.ch",
    description="Software Aided Image Nuking Technology",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deletescape/SAINT",
    packages=setuptools.find_packages(),
    install_requires=['pillow>=5.2.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)