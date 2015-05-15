import tempfile
import pygit2
import time

# Set incoming parameters. These would be in the web request.

committer_name = 'Drupal Druplicon'
committer_email = 'druplicon@example.com'
branch_name = 'hello_world'

file_path = 'hello.txt'
file_content = 'Hello, world!'
commit_message = 'Adding hello.txt.'

# Preliminary setup for proof-of-concept purposes

tmpdir = tempfile.TemporaryDirectory(suffix='.git', prefix='branchandcommit-')
print('Creating bare repository: {}'.format(tmpdir.name))
repo = pygit2.init_repository(tmpdir.name, True)

# Create the branch (if non-existent).

print('Creating branch: {}'.format(branch_name))

# Create a git blob with the file content.

print('Creating blob with content: {}'.format(file_content))

blob = repo.create_blob(file_content)

# Create the tree with the file.

print('Creating tree for file: {}'.format(file_path))

tb = repo.TreeBuilder()
tb.insert(file_path, blob, pygit2.GIT_FILEMODE_BLOB)

# Creating author.

author = pygit2.Signature(committer_name, committer_email, int(time.time()))

# Commit the file to the branch.

print('Creating commit: {}'.format(commit_message))

precommit = tb.write()
commit = repo.create_commit('refs/heads/master', author, author, commit_message, precommit, [])

input("Press Enter to clean up the temporary git repository and exit...")
