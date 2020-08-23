from utils import normalize_path, to_bytes

input_data_set = ["", "/", "hello", "hello/"]


def test_normalize_path() :
    test_data = ["/", "hello", "hello/", ]
    expected = ["/", "hello/", "hello/", ]

    for i in range(3) :
        t = test_data[i]
        e = expected[i]
        g = normalize_path(t)

        assert g == e, f"path {t} normalize to {g}, while {e} expected"


def test_to_bytes():

    test_text = ['x', b'm']
    expected_text = [b'x', b'm']

    for m in range(1):
        t=test_text[m]
        e=expected_text[m]
        b=to_bytes(mes=t)

    assert b == e

