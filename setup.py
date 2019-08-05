from setuptools import setup

setup(
    name='spinsearch',
    description='API client for InfoEd SPIN search engine',
    url='https://github.com/harvard-vpal/spin-search',
    author='Andrew Ang',
    author_email='andrew_ang@harvard.edu',
    license='Apache-2.0',
    packages=['spinsearch'],
    install_requires=['requests'],
    use_scm_version=True,
    setup_requires=['setuptools_scm']
)
