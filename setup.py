from setuptools import setup, find_packages

setup(
    name='gskit',
    version='0.1',
    description='Groth-Sahai utilities',
    author='Benjamín Hurtado',
    author_email='bhurtado@dcc.uchile.cl',
    url='https://users.dcc.uchile.cl/~bhurtado/gskit',
    packages=find_packages(),
    install_requires=["numpy", "lark"],
)