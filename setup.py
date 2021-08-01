import setuptools
from pathlib import Path

setuptools.setup(
    name='gym_manipulation',
    author="SM Arifuzzaman",
    author_email="sarifuzzaman@mun.ca",
    version='0.0.1',
    description="An OpenAI Gym Env for mycobot",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(include="gym_manipulation*"),
    install_requires=['gym', 'pybullet', 'numpy'],  
    classifiers=[
        "Programming Language :: Python :: 3",        
        "Operating System :: OS Independent",
        ],
    python_requires='>=3.6'
)
