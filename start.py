"""
Sets up the config file

Fuck bash/sed.
"""

import os
import ConfigParser

conf_filename = '/var/awslogs/etc/awslogs.conf'
def main():
    logstream = os.environ['LOGSTREAM_NAME']
    
    config = ConfigParser.ConfigParser()
    config.read([conf_filename])
    config.set('syslog', 'log_stream_name', logstream)

    with open(conf_filename, 'w') as f:
        config.write(f)

    os.system('sudo service awslogs stop')
    os.execv('/usr/local/bin/supervisord', [''])



if __name__ == '__main__':
    main()