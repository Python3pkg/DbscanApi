from distutils.core import setup

setup(
    name = 'DbscanApi',
    packages = ['DbscanApi'],
    version = '1.1',
    description = 'A Dbscan api.',
    author = 'davidtnfsh',
    author_email = 'davidtnfsh@gmail.com',
    url = 'https://github.com/udicatnchu/DbscanApi',
    download_url = 'https://github.com/udicatnchu/DbscanApi/archive/v1.1.tar.gz',
    keywords = ['dbscan'],
    classifiers = [],
    license='MIT',
    install_requires=[
        'jieba',
        'numpy',
        'sklearn',
        'gensim'
    ],
    zip_safe=True
)
