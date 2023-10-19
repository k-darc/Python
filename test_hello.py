from hello import hello # importing from hello.py the function "hello"


def test_default():
    assert hello() == "hello, world" # this is the default value in hello.py

def test_argument():
    for anme in ["Hermione", "Harry", "Ron"]
        assert hello(name) == f"hello, {name}"
