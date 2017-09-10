from setuptools import setup, find_packages

required_packages = [
  'graphene>=2.0',
  'bottle>=0.12.13'
]

setup(
    name='Graphene-Bottle',
    version='0.1.0',
    description='Adds GraphQL support to your Bottle application',
    long_description=open('README.rst').read(),
    url='https://github.com/danielbdias/graphene-bottle',
    download_url='https://github.com/danielbdias/graphene-bottle/releases',
    author='Daniel Baptista Dias',
    author_email='danielbpdias@gmail.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='api graphql protocol rest bottle',
    packages=find_packages(exclude=['tests']),
    install_requires=required_packages,
    tests_require=['pytest>=2.7.3'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
)
