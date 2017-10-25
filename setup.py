from setuptools import setup


setup(
    name='flake8-config-yoctol',
    version='0.0.1',
    url='https://github.com/Yoctol/flake8-config-yoctol',
    author="cph",
    author_email='cph@yoctol.com',
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'Framework :: Flake8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
    keywords='flake8,yoctol',
    install_requires=[
        'flake8',
    ],
)
