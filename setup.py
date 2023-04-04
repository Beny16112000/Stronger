from setuptools import setup, find_packages


# Setup


setup(
    name='stronger',
    version='0.1.0',
    description='A package for password security',
    author='Benjamin Shtainberg',
    author_email='benny132001@gmail.com',
    url='https://github.com/Beny16112000/Stronger',
    packages=find_packages(),
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
        'dependency1',
        'dependency2',
        'pyotp',
    ],
)

