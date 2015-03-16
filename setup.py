from setuptools import setup

setup(
    name = 'sysd_minmon',
    version = '0.0.1',
    author = 'Rendaw',
    author_email = 'spoo@zarbosoft.com',
    packages = ['sysd_minmon'],
    url = 'https://github.com/Rendaw/sysd_minmon',
    download_url = 'https://github.com/Rendaw/sysd_minmon/tarball/v0.0.1',
    license = 'BSD',
    description = 'Monitor systemd units for state changes.',
    long_description = open('readme.txt', 'r').read(),
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Monitoring',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points = {
        'console_scripts': [
            'sysd_minmon = sysd_minmon.sysd_minmon:main',
        ],
    },
    data_files = [
        ('/etc/dbus-1/system/', 'com.zarbosoft.sysd_minmon.conf'),
    ],
)
