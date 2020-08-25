# -*- coding: utf-8 -*-
import setuptools

import job_title_processing

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="job-title-processing-Dares",
    version="0.0.1",
    author="Dares",
    author_email="dares.projets-big-data@travail.gouv.fr'",
    description="A package to clean and label french job offers title",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://framagit.org/jocas/job_title_processing",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

