import os
import setuptools

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, "pyteams_msg", "__about__.py"), encoding="utf-8") as f: 
    exec(f.read(), about)
    
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyteams_msg",
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    description="Build and post messages to Microsoft Teams",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmillana/pyteams_msg",
    project_urls={
        "Bug Tracker": "https://github.com/jmillana/pyteams_msg/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=["pyteams_msg", "pyteams_msg.sections"],
    python_requires=">=3.6",
)
