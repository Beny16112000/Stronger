import setuptools


# Setup


with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()



setuptools.setup(
    name='Stronger',
    version='0.0.2',
    description='A package for password security',
    long_description=long_description,
    long_description_content_type = "text/markdown",
    author='Benjamin Shtainberg',
    author_email='benny132001@gmail.com',
    url='https://github.com/Beny16112000/Stronger',
    packages= setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',    
    ],
    install_requires=[
        'pyotp',
    ],
)

