from distutils.core import setup

setup(
    name = 'DbscanApi',
    packages = ['DbscanApi'],
    version = '1.2',
    description = 'A Dbscan api.',
    author = 'davidtnfsh',
    author_email = 'davidtnfsh@gmail.com',
    url = 'https://github.com/udicatnchu/DbscanApi',
    download_url = 'https://github.com/udicatnchu/DbscanApi/archive/v1.2.tar.gz',
    keywords = ['dbscan'],
    classifiers = [],
    license='MIT',
    install_requires=[
        'jieba',
        'sklearn',
        'numpy==1.12.1',
        'gensim==2.0.0'
    ],
    zip_safe=True
)
