import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pipLibraryPackageExample", # Replace with your own username
    version="0.0.1",
    author="cannavit",
    author_email="cannavit@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cannavit/pipLibraryPackageExample.git",
    project_urls={
        "Bug Tracker": "https://github.com/cannavit/pipLibraryPackageExample.git/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

install_requires = [
]
