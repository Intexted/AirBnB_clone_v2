#!/usr/bin/python3
""" Function that compress a folder """
from datetime import datetime
from fabric.api import local
<<<<<<< HEAD
import os


def do_pack():
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        archive_path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except:
=======


def do_pack():
    """
    must return the archive path if the archive has been correctly
    generated. Otherwise, it should return None
    """
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        rout = "versions/web_static_{}.tgz".format(date)
        _gzip = local("tar -cvzf {} web_static".format(rout))
        return rout
    except Exception:
>>>>>>> fd751b50dedd119159c602252dc658eacb6973d8
        return None
