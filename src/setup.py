from setuptools import setup, find_packages

setup(
    name='strips_hgn',
    version='0.1',
    packages=find_packages(include=['strips_hgn', 'strips_hgn.*']),
    include_package_data=True,
    install_requires=[
        # Add your dependencies here
        # 'numpy>=1.18.0',
        # 'torch>=1.7.0',
    ],
    entry_points={
        'console_scripts': [
            # Define any command-line scripts here
            # 'script_name=module_name:main_function',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
