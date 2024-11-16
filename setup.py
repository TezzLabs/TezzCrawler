from setuptools import setup, find_packages

# Function to read the requirements from requirements.txt
def parse_requirements(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

setup(
    name='TezzCrawler',
    version='0.1.0',
    author='Japkeerat Singh (TezzLabs)',
    author_email='japkeerat@tezzlabs.com',
    description='A web crawler that converts web pages to markdown and prepares them for LLM consumption',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/TezzLabs/TezzCrawler',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=parse_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            'tezzcrawler=tezzcrawler.main:app',
        ],
    },
    include_package_data=True,
)
