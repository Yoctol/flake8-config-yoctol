from setuptools import setup


setup(
    name='flake8-config-yoctol',
    version='0.0.11',
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
        'flake8==3.6.0',
        'flake8-bugbear==17.4.0;python_version>="3.5"',
        'flake8-commas==0.4.3',
        'flake8-builtins==1.0',
        'flake8-class-newline==1.6.0',
        'flake8-debugger==3.0.0',
        'flake8-print==3.0.1',
    ],
)
