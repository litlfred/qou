"""Tests for canonical Convention-D 3-strand quantum-trace Borromean helpers (TN-10 / qou-v4iw)."""
from __future__ import annotations

import warnings
from mpmath import mp

from qou_substrate import (
    q_at,
    qtrace_borromean_v3_diff_at,
    qtrace_conn_borromean_p_at,
    qtrace_conn_borromean_n_at,
    qtrace_conn_borromean_diff_at,
    tr_borromean_v3_at,
    tr_conn_borromean_p_at,
    tr_conn_borromean_n_at,
    tr_conn_borromean_diff_at,
)


def test_qtrace_borromean_identities_at_80dps() -> None:
    mp.dps = 80
    q0 = q_at(80)
    qdim3 = (q0 + 1 / q0) ** 3

    tp = qtrace_conn_borromean_p_at(q=q0, dps=70)
    tn = qtrace_conn_borromean_n_at(q=q0, dps=70)
    tdiff = qtrace_conn_borromean_diff_at(q=q0, dps=70)

    # Matches Lean `NucleonWeightSpaceQTrace.deltaT_adjacent_connected_eq`:
    # Δt_conn = t_conn(W_n) - t_conn(W_p).
    assert mp.fabs((tn - tp) - tdiff) < mp.mpf("1e-65")
    assert tp < 0
    assert tn > 0
    assert tdiff > 0

    # Pure V³ pivotal difference: (q⁻¹ - q) * tr(V³) / [2]_q³ ≈ -0.0769805346...
    tr_v3 = tr_borromean_v3_at(q=q0, dps=70)
    v3_diff = qtrace_borromean_v3_diff_at(q=q0, dps=70)
    expected_v3_diff = (1 / q0 - q0) * tr_v3 / qdim3
    assert mp.fabs(v3_diff - expected_v3_diff) < mp.mpf("1e-65")
    assert mp.fabs(v3_diff - mp.mpf("-0.0769805346")) < mp.mpf("1e-8")

    # Legacy unweighted (1/3) helpers emit DeprecationWarning and differ by ~2.60698x.
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", DeprecationWarning)
        legacy_p = tr_conn_borromean_p_at(q=q0, dps=70)
        legacy_n = tr_conn_borromean_n_at(q=q0, dps=70)
        legacy_diff = tr_conn_borromean_diff_at(q=q0, dps=70)

    assert len(caught) == 3
    assert mp.fabs(tp - (3 * q0 * legacy_p / qdim3)) < mp.mpf("1e-65")
    assert mp.fabs(tn - (3 * (1 / q0) * legacy_n / qdim3)) < mp.mpf("1e-65")
    ratio = legacy_diff / tdiff
    q2 = q0 ** 2
    exact_ratio = (
        (4 * (q2 ** 2) + q2 + 4) * ((q2 + 1) ** 3)
        / (3 * q2 * (q2 + 2) * (2 * (q2 ** 2) + 1))
    )
    assert mp.fabs(ratio - exact_ratio) < mp.mpf("1e-65")
    assert mp.fabs(ratio - mp.mpf("2.607175218")) < mp.mpf("1e-8")
