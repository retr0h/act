import act


def test_app_name_version():
    assert "unknown" == act.__version__
