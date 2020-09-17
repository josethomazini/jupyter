# My Jupyter

This is a Jupyter Notebook with some other libs, described on the requirements.txt file.

## Building the docker image

Either build the docker image....

```
docker build -t my-jupyter .
```

... or download it from Dockerhub

```
docker pull josethomazini/my-jupyter
```

## Create the password

Make a temporary container, just to create the password:

```
docker run -it --rm --entrypoint /bin/bash my-jupyter
```

Define your password to be hashed:

```
python -c 'from notebook.auth import passwd; print(passwd())'
```

Let your password being equal to:

```
abc
```

The output would be:

```
argon2:$argon2id$v=19$m=10240,t=10,p=8$xxFDz55TKfPsfzF6juFXPg\$WHN5ZiUVw7xj2doX9RS/IA
```

And your **secret.ini** file should be like that:

```
[DEFAULT]
JUPYTER_HASH=argon2:$argon2id$v=19$m=10240,t=10,p=8$xxFDz55TKfPsfzF6juFXPg\$WHN5ZiUVw7xj2doX9RS/IA
```

That file must be saved out of the container, into the volume folder named **secret**.

Exit the python shell and the container, so the last will be terminated.

## Create the real container

```
docker run --rm -d -it -v /path/to/the/data:/home/pyuser/data/ -v /path/to/the/secret:/home/pyuser/secret/ -p 8888:8888 --name my-jupyter my-jupyter
```

Jupyter Notebook will be listening on:

http://localhost:8888/

# Thanks

I would like to thank CodingEntrepreneurs for this amazing video, from which I've borrow many ideas.

https://www.youtube.com/watch?v=GoJ6qR2VMTA
