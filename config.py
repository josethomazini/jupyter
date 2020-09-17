import configparser


# Read secret hash from volume on /home/pyuser/secret/
config = configparser.ConfigParser()
config.read('/home/pyuser/secret/secret.ini')
jupyter_hash = config['DEFAULT']['JUPYTER_HASH']

# Get Jupyter config
config = get_config()

# Define the hashed password on Jupyter
config.NotebookApp.password = str(jupyter_hash)
