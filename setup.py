import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sovt",
    version="0.0.3",
    author="Christopher Ulmschneider",
    author_email="ulmschneider.chris@gmail.com",
    description="Code for SOVT and HRM manuscript",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["pandas",
                      "numpy",
                      "hrmtools @ git+https://github.com/chris-ulmy/hrmtools@main"
                     ],
    url="https://github.com/chris-ulmy/sovt.git",
    packages=setuptools.find_namespace_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
