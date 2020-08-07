from utils import normalize_path


def test_normalize_path():
    test_data = ["/","hello","hello/",]
    expected = ["/", "hello/", "hello/",]


    for i in range (3):
        t=test_data[i]
        e=expected[i]
        g=normalize_path(t)

        assert g == e, f"path {t} normalize to {g}, while {e} expected"

