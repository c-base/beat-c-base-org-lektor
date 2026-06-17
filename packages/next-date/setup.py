from setuptools import setup

setup(
    name='lektor-next-date',
    version='0.1',
    py_modules=['lektor_next_date'],
    install_requires=['python-dateutil'],
    entry_points={
        'lektor.plugins': [
            'next-date = lektor_next_date:NextDatePlugin',
        ]
    }
)
