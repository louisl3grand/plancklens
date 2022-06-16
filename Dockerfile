
# Dockerfile adapted from jupyter/scipy-notebook 
# https://github.com/jupyter/docker-stacks/blob/master/scipy-notebook/Dockerfile

ARG OWNER=jupyter
ARG BASE_CONTAINER=$OWNER/scipy-notebook
FROM $BASE_CONTAINER

USER root


# We need a fortran compiler for plancklens
RUN apt-get update --yes
RUN apt-get install gfortran --yes


# Install plancklens 
WORKDIR "${HOME}"
RUN git clone https://github.com/louisl3grand/plancklens.git
WORKDIR "${HOME}/plancklens"
RUN git checkout tutorial
RUN pip install -r requirements.txt
RUN pip install -e .

# Install lenspyx
WORKDIR "${HOME}"
RUN git clone https://github.com/carronj/lenspyx.git
WORKDIR "${HOME}/lenspyx"
RUN pip install -r requirements.txt
RUN pip install -e .

WORKDIR "${HOME}"


# Setting the plancklens env variable for writing stuff
ENV PLENS="${HOME}/plens_write"
