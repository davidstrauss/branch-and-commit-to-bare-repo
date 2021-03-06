import tempfile
import pygit2

def add_commit(repo, ref, msg, author, path=None, content=None, parent=None):
    tb = repo.TreeBuilder()
    if path is not None:
        blob = repo.create_blob(file_content)
        tb.insert(file_path, blob, pygit2.GIT_FILEMODE_BLOB)
    parents = []
    if parent is not None:
        parents = [parent]
    precommit = tb.write()
    commit = repo.create_commit(ref, author, author, msg, precommit, parents)

# Set incoming parameters. These would be in the web request.

committer_name = 'Drupal Druplicon'
committer_email = 'druplicon@example.com'

git_short_name = 'druplicon'
issue_number = 123456
comment_number = 45678
file_path = 'hello.txt'
file_content = 'Hello, world!'
commit_message = 'Adding hello.txt.'

# Create an author.

author = pygit2.Signature(committer_name, committer_email)

# Preliminary setup for proof-of-concept purposes. Creates a master
# branch with a single, empty commit.

tmpdir = tempfile.TemporaryDirectory(suffix='.git', prefix='branchandcommit-')
print('Creating bare repository: {}'.format(tmpdir.name))
repo = pygit2.init_repository(tmpdir.name, True)

# This should always be true for the temporary repo, but it's a good check.
if repo.head_is_unborn:
    add_commit(repo, 'refs/heads/master', 'Initial commit.', author)

# Create the branch (if non-existent).


ref= 'refs/namespaces/issue_{}/refs/heads/{}/comment_{}'.format(
	issue_number,
	git_short_name,
	comment_number)
print('Reference name: {}'.format(ref))
branch = repo.create_branch(ref, repo.head.get_object(), True)

# Commit the change.

#parent = repo.head.target
#parent = None
add_commit(repo, ref, commit_message, author, file_path, file_content, branch.target)

repo.create_reference('refs/namespaces/issue_{}/refs/heads/latest_{}'.format(issue_number, git_short_name), ref)

input("Press Enter to clean up the temporary git repository and exit...")
