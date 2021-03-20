from flake8_functions_names.validators import validate_returns_bool_if_names_said_so


def test_validate_returns_bool_if_names_said_so_raises_no_error_for_ok_function(fine_funcdef_info):
    assert not validate_returns_bool_if_names_said_so(fine_funcdef_info)