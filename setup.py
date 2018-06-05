#   Copyright 2012-2013 Rackspace
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import setuptools


conohacloud_osclient_extensions = [
    'pbr==1.9.1;python_version=="2.7"',           ## juno cli python lib
    'pytz==2018.3;python_version=="2.7"',         ## juno cli python lib
    'prettytable==0.7.2;python_version=="2.7"',   ## juno cli python lib
    'cliff==2.0.0;python_version=="2.7"',         ## juno cli python lib
    'PyYAML==3.11;python_version=="2.7"',         ## juno cli python lib
    'keystoneauth1==2.6.0;python_version=="2.7"',   ## keystone auth1 libs
    'openstacksdk==0.8.5;python_version=="2.7"',      ## openstack sdk libs
    'oslo.config==3.9.0;python_version=="2.7"',           ## oslo config libs
    'oslo.i18n==3.5.0;python_version=="2.7"',             ## oslo i18n libs
    'oslo.serialization==2.4.0;python_version=="2.7"',    ## oslo serialization libs
    'oslo.utils==3.8.0;python_version=="2.7"',            ## oslo utils libs
    'python-cinderclient==1.6.0;python_version=="2.7"',     ## Juno cinder client
    'python-designateclient==2.1.0;python_version=="2.7"',  ## Juno designate client
    'python-glanceclient==2.0.0;python_version=="2.7"',     ## Juno glance client
    'python-keystoneclient==2.3.1;python_version=="2.7"',   ## Juno keystone client (v2 auth)
    'python-novaclient==3.4.0;python_version=="2.7"',       ## Juno nova client
    'python-swiftclient==3.0.0;python_version=="2.7"',      ## Juno Swift client
    'python-openstackclient==2.3.0;python_version=="2.7"',  ## Juno openstack client
    'python-ironicclient=1.3.1;python_version=="2.7"',      ## Mitaka Ironic client
]


setuptools.setup(
    name='conohacloud-osclient',
    version='0.2.1',
    author='naototty',
    author_email='naoto-gohko@plastic-machine.red',
    description='Metapackage to install python-openstackclient for Juno release and ConoHa Cloud '
                'extensions',
    license='Apache License, Version 2.0',
    url='https://github.com/naototty/conohacloud-osclient',
    install_requires=['os-client-config==1.17;python_version=="2.7"'] + conohacloud_osclient_extensions,
    
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ]
)
