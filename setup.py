from setuptools import setup, find_packages

setup(
        name='data_analysis',
        version='0.0.1',
        url='www.github.com/benhoff/data_analysis',
        license='MIT',
        author='Behdad Karimi',
        packages=find_packages(),
        install_requires=['PyQt5',
                          'pandas',
                          'sqlalchemy',
                          'nltk',
                          'numpy',
                          'jupyter',
                          'PyQtChart',
                          'lda',
                          'matplotlib',
                          'scipy',
                          'tweepy',
                          'python-twitter'],
        entry_points={},
        extras_require={'dev': ['flake8',]},
)