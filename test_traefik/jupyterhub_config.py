import os

from jupyterhub.auth import DummyAuthenticator
from jupyterhub.spawner import SimpleLocalProcessSpawner
from jupyterhub_traefik_proxy import TraefikTomlProxy

c = get_config()  # noqa

c.TraefikTomlProxy.should_start = False
c.JupyterHub.authenticator_class = DummyAuthenticator
c.JupyterHub.spawner_class = SimpleLocalProcessSpawner
c.JupyterHub.proxy_class = TraefikTomlProxy
c.JupyterHub.allow_named_servers = True

c.TraefikTomlProxy.traefik_api_username='admin'
c.TraefikTomlProxy.traefik_api_password='$apr1$kRsae0RF$9lut4Yc6NAypI80j9DNUX/'
