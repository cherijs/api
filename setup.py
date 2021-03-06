from setuptools import setup, find_packages


setup(
    name='cloudplayer.api',
    version='0.5.0.dev0',
    author='Nicolas Drebenstedt',
    author_email='hello@cloud-player.io',
    url='https://cloud-player.io',
    description='REST API for Cloud-Player',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='Apache-2.0',
    namespace_packages=['cloudplayer'],
    setup_requires=['setuptools_git'],
    install_requires=[
        'bugsnag',
        'isodate',
        'psycopg2-binary',
        'pycurl',
        'PyJWT',
        'redis',
        'setuptools',
        'sqlalchemy',
        'tornado'
    ],
    extras_require={
        'test': [
            'asynctest',
            'codecov',
            'pylint',
            'pytest-cov',
            'pytest-pep8',
            'pytest-postgresql==1.3.3',
            'pytest-redis',
            'pytest-remove-stale-bytecode',
            'pytest-timeout',
            'pytest-tornado',
            'pytest'
        ],
        'doc': [
            'recommonmark',
            'sphinx-autobuild',
            'sphinx',
        ]
    },
    entry_points={
        'console_scripts': [
            'api=cloudplayer.api.app:main',
            'pytest=pytest:main [test]',
            'test=pytest:main [test]'
        ]
    }
)
