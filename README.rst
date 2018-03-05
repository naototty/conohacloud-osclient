====================
conohacloud-osclient
====================


Metapackage to install python-openstackclient for Juno release and ConoHa Cloud extensions


pip Install
=======

.. code-block:: bash

  pip install git+https://github.com/naototty/conohacloud-osclient.git


or 

.. code-block:: bash

  $ git clone https://github.com/naototty/conohacloud-osclient.git
  $ cd conohacloud-osclient/
  $ pip install -r pip-freeze-centos7-py27.txt


Better Install with virtualenv-wrapper
=======


CentOS7

1) install virtualenv, virtualenvwrapper
.. code-block:: bash

  $ sudo yum yum install python-virtualenvwrapper.noarch python3-virtualenv-doc.noarch python-virtualenv.noarch


2) create and load setup rc_file (for bash)

.. code-block:: bash

  $ cat > rc_bash_venv_wrapper_setup.sh << __EOF
  #!/bin/bash
  
  if [ -f /usr/bin/virtualenvwrapper.sh ]; then
    ## export WORKON_HOME=$HOME/.virtualenvs
    export WORKON_HOME=$HOME/devel/API-test-env/.openstack/.virtualenvs
    export PROJECT_HOME=$HOME/devel/API-test-env
    
    source /usr/bin/virtualenvwrapper.sh
  fi
  __EOF
  
  (openstack)[n-gohko@appdev02 API-test-env(ent-main-test-ze#2)]$ cat rc_bash_venv_wrapper_setup.sh
  #!/bin/bash
  
  if [ -f /usr/bin/virtualenvwrapper.sh ]; then
    ## export WORKON_HOME=$HOME/.virtualenvs
    export WORKON_HOME=$HOME/devel/API-test-env/.openstack/.virtualenvs
    export PROJECT_HOME=$HOME/devel/API-test-env
    
    source /usr/bin/virtualenvwrapper.sh
  fi


load env.

.. code-block:: bash

  source rc_bash_venv_wrapper_setup.sh


3) mkvirtualenv openstack

.. code-block:: bash

  $ mkvirtualenv openstack


4) git clone and osc install by virtualenv

.. code-block:: bash

  $  git clone https://github.com/naototty/conohacloud-osclient.git
  $  cd conohacloud-osclient/
  $  pip install -r pip-freeze-centos7-py27.txt



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
