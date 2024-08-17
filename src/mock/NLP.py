# Load MetaMap
from pymetamap import MetaMap

# Import os to make system calls
import os

# For pausing
from time import sleep

# Setup UMLS Server
metamap_base_dir = '/gwshare/umls_2021/metamap/public_mm/'
metamap_bin_dir = 'bin/metamap20'
metamap_pos_server_dir = 'bin/skrmedpostctl'
metamap_wsd_server_dir = 'bin/wsdserverctl'

# Start servers
os.system(metamap_base_dir + metamap_pos_server_dir + ' start') # Part of speech tagger
os.system(metamap_base_dir + metamap_wsd_server_dir + ' start') # Word sense disambiguation

# Sleep a bit to give time for these servers to start up
sleep(60)