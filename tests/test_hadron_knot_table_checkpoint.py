"""The hadron-knot-table checkpoint must round-trip EXACTLY, or it corrupts.

Bean `qou-uiut`. The table is a multi-hour run that writes its witness only at
the end, so it now caches each atom as it completes and resumes from that
cache. The cache is therefore an input to a committed witness, and a codec
that loses a digit would put reduced-precision numbers into the corpus with
nothing to show it happened.

`compute_atom` returns a mix: plain floats from `round(float(x), 12)`, but
also mpf from `round(mp.log(abs(tr)), 12)` and `round(B, 4)`. A decimal
round-trip is exact for the float half and NOT for the mpf half, which is the
trap this file exists to keep shut.

Note the module cannot simply be imported: its driver loop is at module level,
so `import hadron_knot_table` RUNS all 19 atoms. (I did that by accident while
writing this and started a multi-hour job.) The codec is therefore loaded by
exec'ing the file's head. Guarding the driver behind `if __name__ ==
"__main__":` is the real fix and is left for after the current run — it edits
a file the live checkpoint is keyed on.
"""

from __future__ import annotations

import importlib.util
import os
import sys
import types

import pytest

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _p in (os.path.join(_ROOT, "computations"),
           os.path.join(_ROOT, "computations", "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

mp = pytest.importorskip("mpmath").mp


@pytest.fixture(scope="module")
def hkt():
    """The producer's namespace, WITHOUT running its module-level driver."""
    spec = importlib.util.find_spec("hadron_knot_table")
    if spec is None or spec.origin is None:
        pytest.skip("hadron_knot_table not importable")
    src = open(spec.origin, encoding="utf-8").read()
    marker = "\nresults = []"
    assert marker in src, "driver marker moved; update this fixture"
    head = src.split(marker)[0]
    mod = types.ModuleType("hkt_head")
    mod.__file__ = spec.origin
    try:
        exec(compile(head, spec.origin, "exec"), mod.__dict__)
    except Exception as exc:                       # pragma: no cover
        pytest.skip(f"could not load producer head: {type(exc).__name__}: {exc}")
    return mod


# Values chosen to break a decimal round-trip: a non-terminating binary
# fraction, a denormal-ish exponent, an irrational, and a short-decimal mpf.
#
# The last case used to be written `round(mp.mpf(1) / 7, 12)`, on the stated
# grounds that "`round(mpf, n)` returns mpf, which is exactly what
# `compute_atom` stores". BOTH halves of that are now wrong:
#
#   * `round(mpf, n)` returns **float** on mpmath 1.3.0, and this project pins
#     `mpmath>=1.3,<1.5` — so the case fed a FLOAT into a test of mpf
#     round-tripping and failed `isinstance(back, mp.mpf)`. It passed only on
#     whichever 1.4.x an earlier container happened to resolve. A test whose
#     verdict depends on which supported version is installed is not testing
#     the codec.
#   * `compute_atom` no longer rounds at all — it serialises with
#     `_precision.fmt` (bean qou-uiut, NO-FLOAT64), so no `round()`ed mpf ever
#     reaches this codec now.
#
# The short-decimal case is kept, because a value carrying few significant
# digits is still exactly what the producer stores; it is just constructed so
# it IS an mpf on every version in the pin range.
def _mpf_cases():
    with mp.workdps(50):
        return [mp.mpf(1) / 7, mp.mpf("-1e-300"), mp.mpf(0), mp.mpf(1),
                mp.log(mp.mpf(3)) / 9, mp.mpf(mp.nstr(mp.mpf(1) / 7, 12)),
                -mp.pi, mp.mpf("1e300")]


def test_mpf_round_trips_bit_exactly(hkt):
    """Not "close" — equal. A lost digit here is a corrupted witness."""
    with mp.workdps(50):
        for v in _mpf_cases():
            back = hkt._ckpt_dec(hkt._ckpt_enc(v))
            assert isinstance(back, mp.mpf)
            assert back == v, f"{mp.nstr(v, 30)} != {mp.nstr(back, 30)}"
            assert back._mpf_ == v._mpf_, "same value, different limbs"


def test_round_trip_survives_json(hkt):
    """The cache is JSON on disk; the gmpy2 `mpz` mantissa needs int()."""
    import json
    with mp.workdps(50):
        for v in _mpf_cases():
            blob = json.dumps(hkt._ckpt_enc(v))
            assert hkt._ckpt_dec(json.loads(blob)) == v


def test_nested_structures_round_trip(hkt):
    """`compute_atom` returns dicts of lists of mixed float/mpf."""
    import json
    with mp.workdps(50):
        row = {"name": "x", "Z": 1, "N": 2, "frobenius_stable": True,
               "ln_abs_tr": mp.log(mp.mpf(3)) / 9, "tr_M": 0.1 + 0.2,
               "V_per_gen": [1.5, mp.mpf(1) / 7, -0.0],
               "nf": {"γ": mp.mpf(1) / 3, "σ₀": 2.25},
               "knot_type": None}
        back = hkt._ckpt_dec(json.loads(json.dumps(hkt._ckpt_enc(row))))
        assert back == row
        assert isinstance(back["ln_abs_tr"], mp.mpf)
        assert isinstance(back["nf"]["γ"], mp.mpf)
        assert isinstance(back["tr_M"], float)


def test_plain_floats_are_not_promoted(hkt):
    """A float must come back a float — silently promoting changes the witness."""
    back = hkt._ckpt_dec(hkt._ckpt_enc({"a": 1.0, "b": 2, "c": "s"}))
    assert type(back["a"]) is float and type(back["b"]) is int


def test_key_changes_when_a_keyed_source_changes(hkt, tmp_path, monkeypatch):
    """The cache must not survive an edit to the code that produced it.

    Conservative by design: it will discard a long run for a comment change.
    The opposite failure — resuming stale numbers into a witness — is the one
    that cost this table months of wrong values (the YSN matrices were not a
    representation of H_n(q) until `qou-uiut`).
    """
    before = hkt._ckpt_key()
    assert before == hkt._ckpt_key(), "key is not stable across calls"
    # Point the key at a copy of this producer, then perturb the copy.
    fake = tmp_path / "fake_producer.py"
    fake.write_text("# stand-in\n")
    monkeypatch.setattr(hkt, "__file__", str(fake))
    perturbed_a = hkt._ckpt_key()
    assert perturbed_a != before, "key ignored the producer source"
    fake.write_text("# stand-in\n# one more comment\n")
    assert hkt._ckpt_key() != perturbed_a, "key ignored a source edit"
