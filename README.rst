====================
conohacloud-osclient
====================


Metapackage to install python-openstackclient for Juno release and ConoHa Cloud extensions


Install
=======

::

  pip install git+https://github.com/naototty/conohacloud-osclient.git


Usage
=====

This metapackage will ensure that python-openstackclient and these extensions
are installed that are compatible with the ConoHa cloud (OpenStack Juno based):

install_requires
  - os-client-config==1.17
  - keystoneauth1==2.6.0
  - openstacksdk==0.8.5
  - oslo.config==3.9.0

... etc. (Juno release OpenStack Client)


Changed
=====

additional install
  - python-ironicclient==1.3.1 (mitaka)
