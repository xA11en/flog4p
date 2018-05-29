
from distutils.core import setup

PACKAGE = "flog4p"
NAME = "flog4p"
DESCRIPTION = "Lightweight python log frame"
AUTHOR = "Allen Chen"
AUTHOR_EMAIL = "1010584905@qq.com"
URL = "https://github.com/xA11en/flog4p.git"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    # long_description=read("README.md"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache License, Version 2.0",
    url=URL,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    packages=["flog4p"],
    zip_safe=False,
)
