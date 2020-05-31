import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wordtodigits", # Replace with your own username
    version="1.0.2",
    author="Abhishek Rawat",
    author_email="abhishek18.official@gmail.com",
    description="To convert numbers in word form to digits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhishek-rawat18/wordtodigits",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
