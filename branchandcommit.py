import tempfile
import pygit2

# Set incoming parameters. These would be in the web request.

committer_name = 'Drupal Druplicon'
committer_email = 'druplicon@example.com'
file_path = 'hello.txt'
file_content = 'Hello, world!'
branch_name = 'hello_world'
commit_message = 'Adding hello.txt.'

# Preliminary setup for proof-of-concept purposes

tmpdir = tempfile.TemporaryDirectory(suffix='.git', prefix='branchandcommit-')
print('Creating bare repository: {}'.format(tmpdir.name))
repo = pygit2.init_repository(tmpdir.name, True)

# Create the branch (if non-existent).

print('Creating branch: {}'.format(branch_name))

# Create the tree with the file.

print('Creating tree for file: {} (content: "{}")'.format(file_path, file_content))

# Commit the file to the branch.

print('Creating commit: {}'.format(commit_message))
