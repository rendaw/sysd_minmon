from setuptools import setup

setup(
    name = 'sysd_minmon',
    version = '0.0.1',
    py_modules = ['sysd_minmon'],
    entry_points = {
        'console_scripts': [
            'sysd_minmon = sysd_minmon:main',
        ],
    },
    data_files = [
        ('/etc/dbus-1/system/', ['com.zarbosoft.sysd_minmon.conf']),
    ],
)
