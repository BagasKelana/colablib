from setuptools import setup, find_packages

setup(
    name='colablib',
    version='0.1.7',
    packages=find_packages(),
    install_requires=[
        'safetensors==0.3.3',
        'requests==2.31.0',
        'tqdm==4.66.1',
        'PyYAML==6.0.1',
        'gdown==4.7.1',
        'toml==0.10.2',
        'rarfile==4.0',
        'xmltodict==0.13.0',
        'pydantic==2.3.0',
        'urllib3==2.0.4',
        'chardet==5.2.0',
        'charset-normalizer==3.2.0'
        
    ],
    author='Furqanil Taqwa',
    author_email='furqanil.taqwa@gmail.com',
    description='A utility library for Google Colab',
    url='https://github.com/BagasKelana/colablib',
)
