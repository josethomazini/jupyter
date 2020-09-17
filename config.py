import configparser


# Read secret hash from the volume on /home/pyuser/secret/
config = configparser.ConfigParser()
config.read('/home/pyuser/secret/secret.ini')
jupyter_hash = config['DEFAULT']['JUPYTER_HASH']

# Get Jupyter config
config = get_config()

# Define the hashed password on Jupyter
config.NotebookApp.password = str(jupyter_hash)

# Define the location of the notebooks to be saved in the data volume
config.NotebookApp.notebook_dir = '/home/pyuser/data'

config.NotebookApp.allow_origin = '*'
