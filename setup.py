from setuptools import setup

setup(
    name="Flask-Annex",
    version='0.0.3',
    packages=('flask_annex',),
    install_requires=(
        'Flask',
        'six'
    ),
    extras_require={
        's3': ('boto',)
    }
)
