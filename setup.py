from setuptools import setup

setup(
    name='proxy-pool',
    version='1.0.0',
    description='Proxy pool',
    author=['YingJoy'],
    author_email='yzk.1314@outlook.com',
    url='https://github.com/yingzk/ProxyPool',
    packages=[
        'proxy-pool'
    ],
    py_modules=['run'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'aiohttp',
        'requests',
        'flask',
        'redis',
        'pyquery'
    ],
    entry_points={
        'console_scripts': ['proxy_pool_run=run:cli']
    },
    license='apache 2.0',
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)
