import tempfile
import pygit2


tmpdir = tempfile.TemporaryDirectory(suffix='.git', prefix='branchandcommit-')

print('Creating bare repository: {}'.format(tmpdir.name))

repo = pygit2.init_repository(tmpdir.name, True)
