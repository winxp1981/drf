from fabric.api import *

env.hosts = ['ec2-54-254-207-247.ap-southeast-1.compute.amazonaws.com']
env.user = 'ubuntu'
#env.password = 'e4cu8whx'
env.key_filename = '/home/morris/project/AWS_EC2/roombacker.pem'
env.virtualenv_root = '/home/ubuntu/django_app/movenv'
env.activate = 'source /home/ubuntu/django_app/movenv/bin/activate'

TAR_FILE_NAME = 'server.tar.gz'


def virtualenv(command):
    """
    Run a command in the virtualenv. This prefixes the command with the source
    command.
    Usage:
        virtualenv('pip install django')
    """
    source = 'source %(virtualenv_root)s/bin/activate && ' % env
    run(source + command)

def create_virtualenv():
    """ setup virtualenv on remote host """
    require('virtualenv_root', provided_by=('staging', 'production'))
    args = '--clear --distribute'
    run('virtualenv --python=/usr/bin/python3.5 %s %s' % (args, env.virtualenv_root))

def pack():
    tar_files = ['server/*']
    local('rm -f %s' % TAR_FILE_NAME)

    local('tar -czvf %s %s' % (TAR_FILE_NAME, ' '.join(tar_files)))
    print('packing: %s' % TAR_FILE_NAME)

def deploy():
    pack()
    # run('ls -l /home/ec2-user')
    # run('pwd')

    remote_tmp_tar = '/tmp/%s' % TAR_FILE_NAME
    run('rm -f %s' % remote_tmp_tar)
    # copy tar.gz to remote
    put(TAR_FILE_NAME, remote_tmp_tar)

    remote_dist_dir = '/home/ubuntu/django_app'
    # create directory if not exist
    run('mkdir -p %s' % remote_dist_dir)
    run('rm -rfv %s' % env.virtualenv_root)
    create_virtualenv()

    with cd(remote_dist_dir):
        print('extract file to : %s' % remote_dist_dir)
        run('tar -xzvf %s' % remote_tmp_tar)
        print('install requirements.txt...')
        # sudo('pip install -r server/requirements.txt')   # user pip-3.4 for Amazon linux
        virtualenv('pip install -r server/requirements.txt')
        local('rm -f %s' % TAR_FILE_NAME)

def hello():
    print "Hello Fabric!"