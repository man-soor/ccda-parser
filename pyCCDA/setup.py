from setuptools import setup, find_packages

setup(name='pyCCDA',
      version='1.0.0',
      description='CCDA Parser for Python 3',
      url='http://github.com/mansooralam/pyCCDA',
      author='Mansoor Alam',
      author_email='me@mansooralam.com',
      license='MIT',
      packages=find_packages(),
      python_requires='>=3.6',
      install_requires=[
          'lxml>=4.6.0',
      ],
      extras_require={
          'dev': [
              'pytest>=6.0.0',
              'flake8>=3.8.0',
              'twine>=3.4.0',
              'build>=0.7.0',
          ],
      },
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Topic :: Scientific/Engineering :: Medical Science Apps.',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      zip_safe=False)