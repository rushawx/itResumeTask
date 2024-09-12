import pytest
from solution import Bucket

@pytest.mark.parametrize(
        "keys, values",
        [([1, 2, 3], [0.2, 0.2, 0.6]),
        ([1, 2, 3], [0.33, 0.33, 0.34]),
        ([1, 2, 3], [1.0, 0.0, 0.0]),
        ([1, 2, 3], [0.5, 0.5, 0.0]),
        ([1, 2, 3], [0.3, 0.2, 0.5])],
)
def test_get(keys, values):
    bucket = Bucket(keys=keys, values=values)
    counter = [0 for x in keys]
    for _ in range(1_000_000):
        v = bucket.get()
        counter[keys.index(v)] += 1
    output = [x / sum(counter) for x in counter]
    
    assert bucket.probs[0][0] == pytest.approx(0, abs=0.025)
    
    assert bucket.probs[-1][1] == pytest.approx(1, abs=0.05)
    
    for x, y in zip(output, values):
        assert y == pytest.approx(x, abs=0.025)
