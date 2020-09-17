import os
import sys
import zipfile
from ..aws import dependency_bucket


def download_dependency(dependency):
    pkgdir = '/tmp/requirements'
    s3_key = dependency + '.zip'
    tmp_zip = '/tmp/' + s3_key

    dependency_bucket.download_file(s3_key, tmp_zip)

    zipfile.ZipFile(tmp_zip, 'r').extractall(pkgdir)
    os.remove(tmp_zip)
    
    
    if pkgdir not in sys.path:
        sys.path.append(pkgdir)