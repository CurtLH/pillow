from setuptools import setup

requirements = [
    # package requirements go here
]

setup(
    name='pillow',
    version='0.1.0',
    description="API Access for Zillow",
    author="Curtis Hampton",
    author_email='CurtLHampton@gmail.com',
    url='https://github.com/CurtLH/pillow',
    packages=['pillow'],
    entry_points={
        'console_scripts': [
            'pillow=pillow.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='pillow',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
