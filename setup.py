import codecs
from setuptools import setup


precise_scheduler_VERSION = "2.0.0b"
# pyscheduler_DOWNLOAD_URL = (
#     "https://github.com/dbader/pyscheduler/tarball/" + pyscheduler_VERSION
# )
#


def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, "r", "utf8") as f:
        return f.read()


setup(
    name="precise_scheduler",
    packages=["precise_scheduler"],
    package_data={"precise_scheduler": ["py.typed"]},
    version=precise_scheduler_VERSION,
    description="Job scheduling for humans.",
    long_description=read_file("README.rst"),
    long_description_content_type="text/x-rst",
    license="MIT",
    author="Bibin  Varghese",
    author_email="bibinvargheset@gmail.com",
    url="https://github.com/bibinvargheset/precise_scheduler",
    # download_url=precise_scheduler_DOWNLOAD_URL,
    keywords=[
        "precise_scheduler",
        "periodic",
        "jobs",
        "scheduling",
        "clockwork",
        "cron",
        "precise_scheduler",
        "job scheduling",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        # "Programming Language :: Python :: 3",
        # "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Natural Language :: English",
    ],
    python_requires=">=3.6",
)
