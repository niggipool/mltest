
from setuptools import setup, find_packages

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> list[str]:
    with open(file_path, "r") as file_obj:
        requirements = [
            req.strip()
            for req in file_obj.readlines()
            if req.strip() and not req.strip().startswith("#")
        ]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="mltest",
    version="0.0.1",
    author="niggipool",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
