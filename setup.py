from distutils.core import setup

setup(
        name='gcrypter',
        packages=['gcrypter'],
        version='0.1',  # Start with a small number and increase it with every change you make
        license='BSD 3-Clause',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
        description='Is an encryption algorithm based on bytes and their correspondent numbers to encode strings',  # Give a short description about your library
        author='Nurul-GC',  # Type in your name
        author_email='nuruldecarvalhol@gmail.com',  # Type in your E-Mail
        url='https://github.com/Nurul-GC/gcrypter',  # Provide either the link to your github or to your website
        download_url='https://github.com/Nurul-GC/gcrypter/archive/refs/tags/v0.1.zip',  # I explain this later on
        keywords=['python-encryption', 'encryption-decryption', 'encryption-algorithm'],  # Keywords that define your package best
        install_requires=[],
        classifiers=[
                'Development Status :: 5 - Production/Stable',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
                'Intended Audience :: Developers',  # Define that your audience are developers
                'Topic :: Software Development :: Build Tools',
                'License :: OSI Approved :: BSD 3-Clause License',  # Again, pick a license
                'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
                'Programming Language :: Python :: 3.4',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
                'Programming Language :: Python :: 3.9',
        ],
)
