from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(
    name='ckanext-wmspreview',
    version=version,
    description="WMS preview plugin",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Ivan Ermilov',
    author_email='ivan.s.ermilov@gmail.com',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.wmspreview'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        wmspreview=ckanext.wmspreview.plugin:WMSPreview
    ''',
)
