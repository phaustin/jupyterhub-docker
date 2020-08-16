FROM jupyterhub/jupyterhub:1.1

COPY jupyterhub_config.py .

RUN printenv

RUN pip install --upgrade pip \
    && \
    pip install \
       wheel \
       dockerspawner==0.11.1 \
       jupyterhub-idle-culler==1.0 \
       oauthenticator==0.11.0 \
       jupyterhub-traefik-proxy==0.1.6
