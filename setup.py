from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as changelog_file:
    changelog = changelog_file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('dev_requirements.txt') as f:
    dev_requirements = f.read().splitlines()

setup(
    author='Luiz F. Matos',
    author_email='lfmatosmelo@id.uff.br',
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description='A package to run embedded topic modelling',
    install_requires=requirements,
    license='MIT license',
    long_description=readme + changelog,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='embedded_topic_model',
    name='embedded_topic_model',
    packages=find_packages(include=['embedded_topic_model', 'embedded_topic_model.models', 'embedded_topic_model.utils']),
    setup_requires=dev_requirements,
    test_suite='tests',
    tests_require=dev_requirements,
    url='https://github.com/lffloyd/embedded-topic-model',
    version='1.0.2',
    zip_safe=False,
)
