from setuptools import setup, find_packages


setup(
    name='hpz',
    version='0.1.0',
    author='Etienne Mueller',
    author_email='etienne.mueller@unimelb.edu.au',
    description='High Performance Zebrafish',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/EtienneMueller/hpz',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'requests',
        'numpy',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            's2p=hpz:s2p',
            'warp=slits:warp',
            ]
    }
)
