
from distutils.core import setup

PACKAGE = "flog4p"
NAME = "flog4p"
DESCRIPTION = "Lightweight python log frame"
AUTHOR = "Allen Chen"
AUTHOR_EMAIL = "1010584905@qq.com"
URL = "git@github.com:xA11en/flog4p.git"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    # long_description=read("README.md"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    # "Apache License, Version 2.0",
    url=URL,
    packages=["flog4p"],
    zip_safe=False,
)