from setuptools import find_packages, setup

setup(
    name="assets_1",
    packages=find_packages(exclude=["assets_1_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
