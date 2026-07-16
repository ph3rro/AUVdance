from setuptools import find_packages, setup

package_name = 'tutorial_virtualenvs'
import os
virtualenv_name = "tutorials"
home_path = os.path.expanduser("~")
executable_path = os.path.join(home_path, '.virtualenvs', virtualenv_name, 'bin', 'python')

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pherro',
    maintainer_email='aiden.t.yun@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'virtualenvs = tutorial_virtualenvs.virtualenvs:main',
            'physics_sim = tutorial_virtualenvs.physics_sim:main',

        ],
    },
    options={
        'build_scripts': {
            'executable': executable_path,
        }
    },
)
