# modifcations for node07

working directory in /ScratchSSD/docker/jupyterhub_opendreamkit/test_compose

secrets stored in readonly .env

to change jupyterhub then run

```
sudo docker-compose down
sudo docker-compose build --no-cache jupyterhub
sudo docker-compose up
```
This fails to start traefik with the error message:

```
reverse-proxy exited with code 1
reverse-proxy    | 2020/08/17 18:16:17 command traefik error: field not found, node: statistics
```

Reference:  https://opendreamkit.org/2018/10/17/jupyterhub-docker/


# testing traefik
following https://github.com/jupyterhub/traefik-proxy/issues/55

The following works for me:

```
cd test_traefik
sudo mkdir -p /usr/local/bin/traefik
sudo chmod a+r,a+w,a+x /usr/local/bin/traefik
conda env create -f environment.yml
conda activate jhub-traefik
python -m jupyterhub_traefik_proxy.install --traefik --output=/usr/local/bin/traefik
```

* now start 3 terminals, activate jhub-traefik in each and cd  to /ScratchSSD/docker/test_traefik


* in terminal 1 do:

/usr/local/bin/traefik/traefik --debug -c traefik.toml

* in terminal 2 do:

python -m jupyterhub -f jupyterhub_config.py --debug

* in terminal 3 do:

curl -v -u "admin:admin" localhost:8099

and traefik should report "Basic auth succeeded"

* Next in terminal 3 do:

curl -v localhost:8081

and you should get a reponse that includes the jupyterhub version.




# JupyterHub deployment in use at Université de Versailles

This is a [JupyterHub](https://jupyter.org/hub) deployment based on
Docker currently in use at [Université de
Versailles](https://jupyter.ens.uvsq.fr/).

## Features

- Containerized single user Jupyter servers, using
  [DockerSpawner](https://github.com/jupyterhub/dockerspawner);
- Central authentication to the University CAS server;
- User data persistence;
- HTTPS proxy.

## Learn more

This deployment is described in depth in [this blog
post](https://opendreamkit.org/2018/10/17/jupyterhub-docker/).

### Adapt to your needs

This deployment is ready to clone and roll on your own server. Read
the [blog
post](https://opendreamkit.org/2018/10/17/jupyterhub-docker/) first,
to be sure you understand the configuration.

Then, if you like, clone this repository and apply (at least) the
following changes:

- In [`.env`](.env), set the variable `HOST` to the name of the server you
  intend to host your deployment on.
- In [`reverse-proxy/traefik.toml`](reverse-proxy/traefik.toml), edit
  the paths in `certFile` and `keyFile` and point them to your own TLS
  certificates. Possibly edit the `volumes` section in the
  `reverse-proyx` service in
  [`docker-compose.yml`](docker-compose.yml).
- In
  [`jupyterhub/jupyterhub_config.py`](jupyterhub/jupyterhub_config.py),
  edit the *"Authenticator"* section according to your institution
  authentication server.  If in doubt, [read
  here](https://jupyterhub.readthedocs.io/en/stable/getting-started/authenticators-users-basics.html).

Other changes you may like to make:

- Edit [`jupyterlab/Dockerfile`](jupyterlab/Dockerfile) to include the
  software you like. Do not forget to change
  [`jupyterhub/jupyterhub_config.py`](jupyterhub/jupyterhub_config.py)
  accordingly, in particular the *"user data persistence"* section.

### Run!

Once you are ready, build and launch the application with

```
docker-compose build
docker-compose up -d
```

Read the [Docker Compose manual](https://docs.docker.com/compose/) to
learn how to manage your application.

## Acknowledgements

<img src="https://opendreamkit.org/public/logos/Flag_of_Europe.svg" height="20"> Work partially funded by the EU H2020 project
[OpenDreamKit](https://opendreamkit.org/).
