from leapp.libraries.stdlib import call


def test_check_single_line_output():
    a_command = ['echo', 'This a single line test!']
    assert call(a_command) == [u'This a single line test!']


def test_check_single_line_output_no_split():
    a_command = ['echo', 'This a single line No Split test!']
    assert call(a_command, split=False) == u'This a single line No Split test!\n'


def test_check_multiline_output():
    a_command = ['echo', 'This a multi-\nline test!']
    assert call(a_command) == [u'This a multi-', u'line test!']


def test_check_multiline_output_no_split():
    a_command = ['echo', 'This a multi-\nline No Split test!']
    assert call(a_command, split=False) == u'This a multi-\nline No Split test!\n'
