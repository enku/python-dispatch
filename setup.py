import sys
from setuptools import setup, find_packages

setup_requires = []
if 'bdist_wheel' in sys.argv:
    setup_requires.append('setuptools-markdown')


setup(
    name = "python-dispatch",
    version = "v0.0.1",
    author = "Matthew Reid",
    author_email = "matt@nomadic-recording.com",
    description = "Lightweight Event Handling",
    url='https://github.com/nocarryr/python-dispatch',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    setup_requires=setup_requires,
    long_description_markdown_filename='README.md',
    keywords='event properties dispatch',
    platforms=['any'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
