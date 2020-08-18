FROM jupyterhub/jupyterhub:1.1

COPY jupyterhub_config.py .

RUN pip install --upgrade pip \
    && \
    pip install \
       wheel \
   && \
    pip install dockerspawner==0.11.1 \
       jupyterhub-idle-culler==1.0 \
       oauthenticator==0.11.0 \
       jupyterhub-traefik-proxy==0.1.6

RUN python3 -m jupyterhub_traefik_proxy.install --traefik --etcd --consul --output=/usr/local/bin

RUN echo "path is ${PATH}"
