from setuptools import setup

with open('README.md', 'r') as rf:
    longdesc = rf.read()

setup(
        name='gcrypter',
        packages=['gcrypter'],
        version='0.1',
        license='BSD 3-Clause',
        description='Encryption algorithm based on bytes and their correspondent numbers to encode strings',
        long_description=longdesc,
        long_description_content_type="text/markdown",
        author='Nurul-GC',
        author_email='nuruldecarvalhol@gmail.com',
        url='https://github.com/Nurul-GC/gcrypter',
        download_url='https://github.com/Nurul-GC/gcrypter/archive/refs/tags/v0.1.zip',
        project_urls={
                "Bug Tracker": "https://github.com/Nurul-GC/gcrypter/issues",
        },
        keywords=['python-encryption', 'encryption-decryption', 'encryption-algorithm'],
        install_requires=[],
        classifiers=[
                'Development Status :: 5 - Production/Stable',
                'Intended Audience :: Developers',
                'Topic :: Software Development :: Build Tools',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
                'Programming Language :: Python :: 3.9',
        ],
        python_requires=">=3.6",
)
