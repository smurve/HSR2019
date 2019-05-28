FROM jupyter/tensorflow-notebook:abdb27a6dfbb

USER $NB_USER

ADD ./requirements.txt $HOME/

RUN pip install -r $HOME/requirements.txt --ignore-installed PyYAML && rm $HOME/requirements.txt

VOLUME [ "/home/$NB_USER/work" ]
