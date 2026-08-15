"""`wrap_legacy` must adopt payload assertions, never discard them.

`assertions` and `allPassed` sit in `_RESERVED_LEGACY_KEYS`, on the reasoning
that `build()` recomputes both from assertions registered via `add_assertion`.
For a producer that writes its checks as a payload literal — the prevailing
legacy shape — that reasoning silently DISCARDED them, and `build()` emitted

    "assertions": [], "allPassed": true

with `allPassed` true *vacuously*, because nothing had been registered. No
warning and no exception: a probe whose headline check FAILED reported success.

Measured before the fix: 29 producers passed `assertions` in a `wrap_legacy`
payload, 28 without also calling `add_assertion`; 389 of the 2083 witnesses
carrying an `allPassed` field (19 %) had it true with zero assertions.

The property that matters most here is `test_failing_payload_assertion_is_not
_swallowed`: it is the exact shape that shipped a false green, and it is
indistinguishable from working behaviour for any producer whose checks happen
to pass — which is why this file exists rather than a spot check.
"""

import pytest

from qou_substrate.witness import WitnessBuilder

# Any real file works; the builder only hashes it.
SCRIPT = __file__


def _build(assertions, **payload):
    doc = {"computation": "t", **payload}
    if assertions is not None:
        doc["assertions"] = assertions
    return WitnessBuilder.wrap_legacy(
        "t", doc, script_path=SCRIPT,
    ).build()


def test_failing_payload_assertion_is_not_swallowed():
    """The regression: a false check must not surface as allPassed: true."""
    out = _build([{"name": "headline", "passed": False}], allPassed=True)
    assert len(out["assertions"]) == 1
    assert out["assertions"][0]["passed"] is False
    assert out["allPassed"] is False


def test_passing_payload_assertion_is_adopted():
    out = _build([{"name": "ok", "passed": True}])
    assert len(out["assertions"]) == 1
    assert out["allPassed"] is True


def test_explicit_passed_beats_a_derivable_comparison():
    """Adoption must not silently re-decide a producer's stated verdict.

    Several producers carry BOTH an explicit `passed` and a computed/expected
    pair. Deriving would override what the producer asserted, which is a
    different bug from the one being fixed.
    """
    out = _build([{"name": "x", "computed": 1, "expected": 2, "passed": True}])
    assert out["assertions"][0]["passed"] is True
    assert out["allPassed"] is True


@pytest.mark.parametrize(
    "rec,expected",
    [
        ({"name": "x", "computed": "5", "expected": "5"}, True),
        ({"name": "x", "computed": "5", "expected": "6"}, False),
        ({"name": "x", "computed": "1.0", "expected": "5.0",
          "tolerance": "0.1"}, False),
        ({"name": "x", "computed": "5.00", "expected": "5.01",
          "tolerance": "0.1"}, True),
    ],
)
def test_derived_when_no_explicit_passed(rec, expected):
    assert _build([rec])["assertions"][0]["passed"] is expected


def test_one_failure_fails_the_witness():
    out = _build([{"name": "a", "passed": True},
                  {"name": "b", "passed": False},
                  {"name": "c", "passed": True}])
    assert len(out["assertions"]) == 3
    assert out["allPassed"] is False


def test_adoption_is_lossless():
    """Corpus assertions carry keys beyond the schema; they must survive.

    `detail`, `manifold` and `particle` all appear on real payload assertions.
    Dropping them would make adoption a partial fix that reads as a total one.
    """
    out = _build([{"name": "x", "passed": True, "detail": "why",
                   "manifold": "4_1", "particle": "neutrino"}])
    a = out["assertions"][0]
    assert a["detail"] == "why"
    assert a["manifold"] == "4_1"
    assert a["particle"] == "neutrino"


def test_extras_cannot_shadow_a_schema_key():
    """An adopted extra must not overwrite the computed verdict."""
    out = _build([{"name": "x", "passed": False, "passed_extra": 1}])
    assert out["assertions"][0]["passed"] is False


def test_no_assertions_key_is_unchanged():
    """Producers with no checks keep the previous vacuous-true behaviour."""
    out = _build(None)
    assert out["assertions"] == []
    assert out["allPassed"] is True


def test_empty_assertion_list_is_unchanged():
    out = _build([])
    assert out["assertions"] == []
    assert out["allPassed"] is True


def test_add_assertion_still_works_alongside_adoption():
    """The two registration paths compose; neither drops the other."""
    b = WitnessBuilder.wrap_legacy(
        "t", {"computation": "t", "assertions": [{"name": "a", "passed": True}]},
        script_path=SCRIPT,
    )
    b.add_assertion("b", computed="0", expected="1", tolerance="0")
    out = b.build()
    assert {a["name"] for a in out["assertions"]} == {"a", "b"}
    assert out["allPassed"] is False
