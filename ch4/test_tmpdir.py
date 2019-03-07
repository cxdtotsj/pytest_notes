
def test_tmpdir(tmpdir):

    a_file = tmpdir.join('something.txt')

    # you cna create directories
    a_sub_dir = tmpdir.mkdir('anything')

    # you can create files in directories (created when written)
    another_file = a_sub_dir.join('something_else.txt')

    # this write creates 'something.txt
    a_file.write('contents may settle during shipping.')

    # this write creates 'anthing/something_else.txt'
    another_file.write('something different')

    # you can read the files as well
    assert a_file.read() == 'contents may settle during shipping.'
    assert another_file.read() == 'something different'


def test_tmpdir_factory(tmpdir_factory):

    # you should will be the parent dir of 'mydir'
    # a dir 和 tmpdir fixture 中的 tmpdir 一样
    a_dir = tmpdir_factory.mktemp('mydir')

    base_temp = tmpdir_factory.getbasetemp()

    print('base:', base_temp)

    a_file = a_dir.join('something')
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')

    a_file.write('contents may settle during shipping.')
    another_file.write('something different')
    assert a_file.read() == 'contents may settle during shipping.'
    assert another_file.read() == 'something different'