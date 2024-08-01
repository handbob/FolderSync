import os
import shutil
import pytest
from pyfoldersync.sync import synchronize_folders
from pyfoldersync.logger import setup_logging


@pytest.fixture
def setup_test_environment():
    base_dir = 'test_data'
    source = os.path.join(base_dir, 'source')
    replica = os.path.join(base_dir, 'replica')
    log_file = 'logs/test_sync.log'

    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)

    os.makedirs(source, exist_ok=True)
    os.makedirs(replica, exist_ok=True)

    with open(os.path.join(source, 'file1.txt'), 'w') as f:
        f.write('this is file1.')

    os.makedirs(os.path.join(source, 'dir1'), exist_ok=True)
    with open(os.path.join(source, 'dir1/file2.txt'), 'w') as f:
        f.write('this is file2.')

    setup_logging(log_file)

    yield source, replica


def test_synchronization(setup_test_environment):
    source, replica = setup_test_environment

    synchronize_folders(source, replica)

    assert os.path.exists(os.path.join(replica, 'file1.txt'))
    assert os.path.exists(os.path.join(replica, 'dir1'))
    assert os.path.exists(os.path.join(replica, 'dir1/file2.txt'))

    with open(os.path.join(source, 'file1.txt'), 'w') as f:
        f.write('this is an updated file1.')

    with open(os.path.join(source, 'dir1/file2.txt'), 'w') as f:
        f.write('this is an updated file2.')

    synchronize_folders(source, replica)

    with open(os.path.join(replica, 'file1.txt'), 'r') as f:
        assert f.read() == 'this is an updated file1.'

    with open(os.path.join(replica, 'dir1/file2.txt'), 'r') as f:
        assert f.read() == 'this is an updated file2.'

    shutil.rmtree(os.path.join(source, 'dir1'))
    os.remove(os.path.join(source, 'file1.txt'))

    synchronize_folders(source, replica)

    assert not os.path.exists(os.path.join(replica, 'file1.txt'))
    assert not os.path.exists(os.path.join(replica, 'dir1'))

    with open('logs/test_sync.log', 'r') as f:
        logs = f.read()
    assert 'create file: test_data/replica/file1.txt' in logs
    assert 'create directory: test_data/replica/dir1' in logs
    assert 'create file: test_data/replica/dir1/file2.txt' in logs
    assert 'update file: test_data/replica/file1.txt' in logs
    assert 'update file: test_data/replica/dir1/file2.txt' in logs
    assert 'delete file: test_data/replica/file1.txt' in logs
    assert 'delete directory: test_data/replica/dir1' in logs
