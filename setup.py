from pathlib import Path
from setuptools import setup, find_packages

REQUIREMENTS = [
    "numpy>=1.19.0",
    "onnx>=1.10.0",
    "py-cpuinfo>=8.0.0",
    "tensorflow>=2.7.0, <2.8.0",
    "tf2onnx>=1.8.4",
    "torch>=1.10.0",
]

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")
## PACKAGE_DATA ONLY IN BDIST, LOOK AT MANIFEST.IN
setup(
    name="nebullvm",
    version="0.2.0",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    package_data={
        # Include all bash and pwsh files:
        "": ["*.sh", "*.ps1"],
        # And include any file needed for config
        "nebullvm": ["*/config.cmake"],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)
