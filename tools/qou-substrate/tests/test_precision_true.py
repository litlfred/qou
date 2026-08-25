"""str_at_true_precision — serialize at the precision a value actually carries.

The inverse defects are both live in the corpus, which is why this is decided
per value rather than per producer: writing 50 dps of a 53-bit kernel result
fakes precision, and shortening a full-precision result destroys it. See
docs/audits/2026-08-07-producer-repadding-empirical-sweep.md.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))

from mpmath import mp, mpf  # noqa: E402

from qou_substrate.precision import (  # noqa: E402
    fmt, str_at_true_precision, set_compute_dps,
)


def setup_module(_):
    set_compute_dps()


def test_f64_sourced_value_is_written_short():
    """A value that reached mpf from a 53-bit source must not print 50 dps."""
    v = mpf(float(1.5597586581034242))          # numpy trace -> mpf
    assert str_at_true_precision(v) == "1.5597586581034242"
    # and that is exactly what fmt would have overstated
    assert fmt(v).startswith("1.5597586581034241781")


def test_full_precision_value_is_written_in_full():
    """The inverse defect: shortening a value that really carries >53 bits."""
    v = mpf(1) / mpf(7)
    out = str_at_true_precision(v)
    assert out.startswith("0.14285714285714285714285714285714")
    assert len(out) > 20, "a genuine 50-dps value must not be shortened"


def test_value_preserving_in_both_directions():
    for v in (mpf(float(0.1)), mpf(1) / mpf(7), mpf("0.5"), mpf(0), mpf(-2)):
        assert float(str_at_true_precision(v)) == float(v)


def test_representable_by_coincidence_loses_nothing():
    """A full-precision result that happens to be a double is exact short."""
    v = mpf(2) ** 10          # 1024, exactly representable
    assert float(str_at_true_precision(v)) == 1024.0


def test_non_mpf_falls_through_to_str():
    assert str_at_true_precision(0.1) == str(0.1)
    assert str_at_true_precision("not-a-number") == "not-a-number"
    assert str_at_true_precision(3) == str(3)


def test_untouched_path_matches_str_not_fmt():
    """The fallback must be str(), or every non-f64 value silently changes.

    fmt() serializes at OUTPUT_DPS while str() uses the live mp.dps, and
    producers set them differently — so routing the untouched path through
    fmt would rewrite values this helper is not meant to affect.
    """
    from qou_substrate.precision import OUTPUT_DPS
    mp.dps = OUTPUT_DPS + 10
    v = mpf(1) / mpf(7)               # not representable -> untouched path
    assert str_at_true_precision(v) == str(v)
    set_compute_dps()
