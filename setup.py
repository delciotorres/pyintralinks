from setuptools import setup

setup(
    name='pyintralinks',
    version='0.1.0',
    description='A python client for intralinks api.',
    long_description='Simplifies the use of Intralinks API.',
    url='https://github.com/delciotorres/pyintralinks',
    author='Delcio Torres',
    author_email='delciotorres@gmail.com',
    license='MIT',
    zip_safe=False,
    install_requires=['requests'],
    keywords=['intralinks', 'api'],
    classifiers=[
        "Classifier: Development Status :: 1 - Planning",
        "Classifier: Intended Audience :: Developers",
        "Classifier: License :: OSI Approved :: MIT License",
        "Classifier: Operating System :: OS Independent",
        "Classifier: Programming Language :: Python",
        "Classifier: Programming Language :: Python :: 3.6",
        "Classifier: Topic :: Communications :: File Sharing",
        "Classifier: Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
