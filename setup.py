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
        'h5py==2.10.0',
        'importlib-metadata',
        'matplotlib',
        'mkl',
        'natsort',
        'numba',
        'numpy==1.23.4',
        'paramiko',
        'pyqt5',
        'pyqt5.sip',
        'pyqt5-tools',
        'pyqtgraph',
        'pynrrd',
        'pynwb',
        'pytest',
        'rastermap>0.1.0'
        'requests',
        'sbxreader',
        'scanimage-tiff-reader>=1.4.1',
        'scikit-learn',
        'scipy>=1.4.0',
        'suite2p',
        'tbb',
        'tifffile',
        'torch>=1.7.1',
    ],
    entry_points={
        'console_scripts': [
            's2p=hpz:s2p',
            'warp=slits:warp',
            ]
    }
)
