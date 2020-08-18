FROM jupyter/scipy-notebook:7d0e50e30763

LABEL maintainer="paustin@eoas.ubc.ca <https://eoas-ubc.github.io/>"

USER root

# APT packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    tzdata \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID

# Conda packages
RUN conda install --quiet --yes jupyterhub=1.1.0 \
    && conda clean -t -i -p -q -y \
    && fix-permissions $CONDA_DIR

ENV CPATH=$CONDA_DIR/include

RUN fix-permissions $CONDA_DIR

# Add conda env hook
COPY ./conda-activate.sh /usr/local/bin/before-notebook.d/
