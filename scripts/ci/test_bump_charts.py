import bump_charts

def test_compare_yaml_files():
    res = bump_charts.compare_yaml_files('opsportal-9.yaml', 'opsportal-10.yaml')
    assert res == -1

    res = bump_charts.compare_yaml_files('opsportal-9.yaml', 'opsportal-9.yaml')
    assert res == 0

    res = bump_charts.compare_yaml_files('opsportal-10.yaml', 'opsportal-9.yaml')
    assert res == 1

def test_compare_versions():
    res = bump_charts.compare_versions('1.1.1', '1.1.12')
    assert res == -1

    res = bump_charts.compare_versions('1.1.1', '1.1')
    assert res == 1

    res = bump_charts.compare_versions('1.1.1', '1.1.1')
    assert res == 0

    res = bump_charts.compare_versions('1.1.1', '1.2.1')
    assert res == -1

def test_compare_subfolders():
    res = bump_charts.compare_subfolders('1.1.x', '1.2.x')
    assert res == -1

    res = bump_charts.compare_subfolders('1.2.x', '1.1.x')
    assert res == 1

    res = bump_charts.compare_subfolders('1.1.1', '1.1.1')
    assert res == 0

    res = bump_charts.compare_subfolders('1.1.x', '1.1.1')
    assert res == -1

def test_convert_repo_url():
    pass
