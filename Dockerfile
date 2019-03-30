FROM jupyter/tensorflow-notebook:59b402ce701d

USER $NB_USER

ADD . $HOME/repo
