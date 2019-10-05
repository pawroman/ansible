# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Paweł Romanowski <pawroman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import pytest

from ansible.module_utils.common.text.formatters import percent_format_multiple


def test_percent_format_multiple():
    result = percent_format_multiple("I see %s, %s everywhere", "percents")
    assert result == "I see percents, percents everywhere"


def test_percent_format_multiple_non_string_values():
    result = percent_format_multiple("%s + %s == %s", 0)
    assert result == "0 + 0 == 0"


def test_percent_format_multiple_one_arg():
    result = percent_format_multiple("%s", "just stuff")
    assert result == "just stuff"


def test_percent_format_multiple_no_args_error():
    with pytest.raises(ValueError, match="^string must contain %s: No markers here$"):
        percent_format_multiple("No markers here", "nope")


def test_percent_format_multiple_no_args_error_arg_hint():
    with pytest.raises(ValueError, match="^validate must contain %s: command --flag$"):
        percent_format_multiple("command --flag", "null", argument_name_hint="validate")
