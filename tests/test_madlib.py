import pytest
from madlib_cli.madlib import read_template, parse_template


def test_read_template_returns_stripped_string():
    actual = read_template("/Users/wulmotch/codefellow/401/labs/madlib-cli/assets/madlib.txt")
    expected = "I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}"
    assert actual == expected


def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}"
    )
    expected_stripped = "I the {} and {} {} have {}{}"
    expected_parts = ["Adjective", "Adjective", "A First Name","Past Tense Verb","A First Name"]

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

def test_merge():
    actual = merge("A {} and {} {}.", ["dark", "stormy", "night"])
    expected = "A dark and stormy night."
    assert actual == expected
