#!/usr/bin/env python3
"""Regression tests for the q0 provenance audit's classifier.

Every case here is a real corpus string that a previous revision of
`false_precision` got wrong, with the count of witnesses it mis-filed. The
function has now been rewritten twice; both rewrites were caught by counting
buckets, not by a test, which is why these exist.
"""
import decimal
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from q0_provenance_audit import (  # noqa: E402
    Q_MUON_50,
    Q_MUON_50_WRONG,
    _backed_digits,
    _sig_digits,
    false_precision,
    is_anchor_key,
)


def verdict(s):
    r = false_precision(s)
    if r is None:
        return "clean"
    return "stale" if "does not reproduce" in r else "unknown"


def test_f64_renderings_are_clean():
    """repr(float) emits 17 significant digits; that is not false precision.

    The first version gated on `>16`, so every ordinary f64 rendering tripped
    it -- and at 18 characters could never match the 20-character prefix it
    was tested against, making the flag impossible to clear. 79 witnesses
    carrying the canonical value were reported as "origin UNKNOWN".
    """
    assert verdict("1.1099785955541805") == "clean"
    assert verdict("1.1099785827513808") == "clean"
    assert verdict("1.1099785955573347") == "clean"
    assert verdict("1.10998") == "clean"


def test_rounded_last_digit_is_the_same_constant():
    """A serializer that rounds rather than truncates shares no prefix.

    `...0878015` -> `...087802`. The second version compared strings over
    their full overlap and moved 145 witnesses on the known stale constant,
    plus ~80 on the canonical one, into "origin genuinely unknown".
    """
    assert verdict("1.1099785955573347198997632204832250266562084087802") == "stale"
    assert verdict("1.1099785955573347199") == "stale"
    assert verdict("1.10997859555418057528159407961") == "clean"
    assert verdict("1.1099785955541805753") == "clean"


def test_trailing_zero_in_the_canonical_constant_is_padding():
    """Q_MUON_50's 51st digit is a padding zero; the true value runs ...58686.

    Counting it as significant made the tolerance 10x too tight and pushed 13
    witnesses carrying the canonical value at 60 digits out by a factor 1.24.
    """
    assert Q_MUON_50.endswith("0")
    assert _sig_digits(Q_MUON_50) == _backed_digits(Q_MUON_50) + 1
    for s in ("1.10997859555418057528159407960950937799328227995868622546675",
              "1.109978595554180575281594079609509377993282279958686225466751689153746"):
        assert verdict(s) == "clean", s


def test_genuinely_different_values_stay_flagged():
    """The residue must survive: these diverge at digits 12, 17, 28 and 38."""
    for s in ("1.1099785956402395783775060672867905833417555643376",
              "1.1099785955541805169583001889887986763787613849839",
              "1.109978595554180575281594079609518150067234842238",
              "1.1099785955541805752815940796095093779667618976181"):
        assert verdict(s) == "unknown", s


def test_zero_padded_stale_string_is_still_flagged():
    """17 real digits padded to 30 zeros claims precision it cannot back.

    It is flagged (claimed digits exceed 17) and attributed to the stale
    constant (backed digits agree with it), which is the informative answer.
    """
    s = "1.109978595557334700000000000000"
    assert _sig_digits(s) == 31 and _backed_digits(s) == 17
    assert verdict(s) == "stale"


def test_proton_pin_is_out_of_scope():
    """The 50-dps proton string is not a muon value and must not be flagged.

    613 witnesses carry it -- by far the largest single string in the corpus.
    """
    assert verdict("1.1099785827513808075916690956107688798744991218736") == "clean"


def test_anchor_key_pattern():
    """Name and range must BOTH hold; `*_at_q0` names the other quantity."""
    for k in ("q0", "q_0", "q0Value", "q0_50dps", "q_0_numeric", "q_proton",
              "substrate_q0", "q"):
        assert is_anchor_key(k), k
    for k in ("tr_M_at_q0", "chi_lambda_at_q0", "jones_at_q0", "z_at_q0",
              "value", "frobenius_norm", "miss_x", "q_beta"):
        assert not is_anchor_key(k), k


def test_the_two_known_constants_disagree_where_documented():
    """Divergence at digit 13, and the RELATIVE gap is the documented 2.842e-12.

    Pinned exactly, in Decimal, because that number is quoted in the audit
    module's header. The ABSOLUTE gap is 3.154e-12 -- a different figure for
    the same fact, and the one it is easy to confuse this with.
    """
    assert Q_MUON_50[:13] == Q_MUON_50_WRONG[:13]
    assert Q_MUON_50[13] != Q_MUON_50_WRONG[13]
    with decimal.localcontext() as ctx:
        ctx.prec = 60
        a, b = decimal.Decimal(Q_MUON_50), decimal.Decimal(Q_MUON_50_WRONG)
        assert abs(abs(a - b) / a - decimal.Decimal("2.842e-12")) < decimal.Decimal("1e-15")
        assert abs(abs(a - b) - decimal.Decimal("3.154e-12")) < decimal.Decimal("1e-15")
    assert verdict(Q_MUON_50_WRONG) == "stale"
    assert verdict(Q_MUON_50) == "clean"


if __name__ == "__main__":
    import pytest
    sys.exit(pytest.main([__file__, "-v"]))
