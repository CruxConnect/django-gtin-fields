from setuptools import setup

setup(
    name='django-gtin-fields',
    version='0.1.0',
    description=str(
        'Provides model fields and validation for GTIN codes '
        '(EAN, UPC, GTIN, ISBN)'
    ),

    url='https://github.com/DobaTech/django-gtin-fields',
    author='John T. Prince, under employ of Doba Inc.',
    author_email='jtprince@doba.com, jtprince@gmail.com',

    license='LPGL',

    keywords=[
        'django',
        'gtin',
        'upc',
        'ean',
        'isbn',
        'model',
        'field'
        'UPC-A',
        'UPC-E',
        'EAN-13',
        'GTIN-14',
        'ASIN',
        'Amazon Standard Identification Number',
    ],

    classifiers=[
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
        str(
            'License :: OSI Approved :: '
            'GNU Lesser General Public License v3 (LGPLv3)'
        ),
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ],

    # Package
    packages=['gtin_fields'],
    install_requires=['Django', 'python-stdnum>=1.5'],
    zip_safe=False,
    include_package_data=True,
)
