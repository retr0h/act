import pytest

from act import topo


@pytest.mark.parametrize(
    "d, x",
    [
        (
            dict(
                a={"needs": ["b", "c"]},
                b={},
                c={},
                d={},
                e={"needs": ["a", "b", "c", "d"]},
            ),
            {"a", "b", "c", "d"},
        )
    ],
)
def test_get_all_deps(d, x):
    assert x == topo.get_all_deps("e", d)


@pytest.mark.parametrize(
    "d, x",
    [
        (
            dict(
                a={"needs": ["b", "c"]},
                b={},
                c={},
                d={},
                e={"needs": ["a", "b", "c"]},
            ),
            [{"c", "b", "a"}, {"e"}],
        )
    ],
)
def test_get_topo_for(d, x):
    assert x == topo.get_topo_for("e", d)


@pytest.mark.parametrize(
    "d, x",
    [
        (
            dict(
                a={"needs": ["b", "c"]},
                b={},
                c={},
                d={},
                e={"needs": ["a", "b", "c"]},
            ),
            [{"c", "b", "d"}, {"a"}, {"e"}],
        )
    ],
)
def test_get_topo(d, x):
    assert x == topo.get_topo(d)


@pytest.mark.parametrize(
    "d",
    [
        dict(
            a={"needs": ["b", "c"]},
            b={"needs": ["b", "c"]},
            c={"needs": ["b", "c"]},
            d={"needs": ["b", "c"]},
        ),
    ],
)
def test_get_topo_raises_on_circular_dependencies(d):
    with pytest.raises(SystemExit) as e:
        topo.get_topo(d)

    assert 1 == e.value.code
