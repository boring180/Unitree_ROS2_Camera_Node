from setuptools import find_packages, setup

package_name = 'cv'

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
    maintainer='borong',
    maintainer_email='borong.xu@student.unsw.edu.au',
    description='This is a package for computer vision on the Go2 robot',
    license='MIT',
    entry_points={
        'console_scripts': [
            'cv_node = cv.cv:main',
        ],
    },
)
