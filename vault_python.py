## PYTHON
from pathlib import Path
from dotenv import load_dotenv
import hvac
import os

sec_path = 'rifr/ProfilesProd'

load_dotenv(Path.home() / '.mypylib' / '.env', override=True)
vault_client = hvac.Client(url=os.environ.get('VAULT_SERVER'),
                           token=os.environ.get('VAULT_TOKEN'))
                           
map_secrets = vault_client.read(sec_path)['data']