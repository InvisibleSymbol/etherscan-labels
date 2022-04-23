import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="etherscan_labels",
    version="v20220423",
    author="InvisibleSymbol",
    author_email="etherscan-labels@invis.cloud",
    description="Easily queryable Labels from Etherscan",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/InvisibleSymbol/etherscan-labels",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    package_data={'': ['./data/*.json']},
    install_requires=[
        'compress_json==1.0.5'
    ],
)
