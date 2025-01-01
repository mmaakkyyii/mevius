from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'mevius'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('lib/python3.12/site-packages',package_name,'models'),glob('models/*.*')),
        (os.path.join('lib/python3.12/site-packages',package_name,'models'),glob('models/meshes/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ma-king',
    maintainer_email='ma-king@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mevius_main = mevius.mevius_main:main'
        ],
    },
)
