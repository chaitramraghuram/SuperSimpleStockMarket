from setuptools import find_packages, setup

setup(
    name="sssm",
    version="0.0.1",
    install_requires=["pandas", "numpy"],
    packages=find_packages(exclude=["tests", "tests.*", "*.tests", "*.tests.*", "notebooks"]),
    extras_require={"dev": ["pytest"]},
)
