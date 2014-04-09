from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name='skadi',
    version='0.1',
    description='A Dota 2 replay parser.',
    long_description=open('README.md').read(),
    author='Joshua Morris',
    author_email='onethirtyfive@skadistats.com',
    zip_safe=True,
    url='https://github.com/skadistats/skadi',
    license='MIT',
    packages=find_packages(),
    keywords='dota replay',
    install_requires=[
      'protobuf==2.5',
      'python-snappy==0.5',
      'bitstring==3.1.2',
      'cython>=0.19.1'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Database",
    ],
    ext_modules=cythonize([
      "skadi/io/cBitstream.pyx",
      "skadi/io/unpacker/cProp.pyx",
      "skadi/io/unpacker/cEntity.pyx",
      "skadi/engine/dt/cRecv.pyx",
    ])
)
