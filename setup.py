"""
PBR usage https://docs.openstack.org/pbr/latest/user/using.html
"""

from setuptools import setup

setup (
    name='cmdstash',
    setup_requires=['pbr>=2.0.0'],
    pbr=True
)
