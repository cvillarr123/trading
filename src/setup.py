from setuptools import find_packages, setup
setup(
    name='pypm',
    packages=find_packages(include=['pypm']),
    version='0.1.0',
    description='algorithmic-trading-with-python',
    author='ChrisConlan',
    license='GNU',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)