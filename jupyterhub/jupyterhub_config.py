# JupyterHub configuration
#
## If you update this file, do not forget to delete the `jupyterhub_data` volume before restarting the jupyterhub service:
##
##     docker volume rm jupyterhub_jupyterhub_data
##
## or, if you changed the COMPOSE_PROJECT_NAME to <name>:
##
##    docker volume rm <name>_jupyterhub_data
##

import os
# https://jupyterhub-traefik-proxy.readthedocs.io/en/latest/toml.html
from jupyterhub_traefik_proxy import TraefikTomlProxy
## Generic
c.JupyterHub.admin_access = True
c.Spawner.default_url = '/lab'

#  reverse-proxy

# mark the proxy as externally managed
c.TraefikTomlProxy.should_start = True

# traefik's dynamic configuration file

# configure JupyterHub to use TraefikTomlProxy
c.JupyterHub.proxy_class = TraefikTomlProxy


## Authenticator
from oauthenticator.github import GitHubOAuthenticator
c.JupyterHub.authenticator_class = GitHubOAuthenticator
c.Authenticator.admin_users = { 'phaustin','henryk-modzelewski', 'CharlesKrzysik' }
c.Authenticator.whitelist = {'phaustin','CharlesKrzysik', 'henryk-modzelewski}
c.GitHubOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']

## Docker spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

# Other stuff
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '10G'


## Services
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]
