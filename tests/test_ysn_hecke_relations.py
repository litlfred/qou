"""The YSN seminormal matrices must be a REPRESENTATION of H_n(q).

Bean `qou-uiut`. `_build_ysn_matrices` shipped for a long time with the
Hoefsmit diagonal written as ``a_rho = h / [rho]_q`` where the correct value
is ``q**rho / [rho]_q``. The matrices it returned satisfied the quadratic
relation and failed the braid relation by a constant 0.731513681083349 at
every partition — so they were not a representation, and every character,
trace and binding number computed from them was wrong.

The reason it survived is the whole point of this file. The producer checked
the quadratic relation, and the quadratic relation CANNOT see this error:
``a_neg = h - a_rho`` pins the 2x2 block's trace whatever ``a_rho`` is, and
``sigma^2 = h*sigma + 1`` constrains nothing else. Only the braid relation
distinguishes them. A test that checks the easy relation and not the hard one
is worse than no test, because it reads as coverage.

So: check all three defining relations of H_n(q), on both the dense and the
sparse code path, and on the hardcoded (2,2) constants that duplicate the
builder's output for H_4(q).
"""

from __future__ import annotations

import os
import sys

import pytest

_COMPUTATIONS = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "computations")
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

mp = pytest.importorskip("mpmath")

# NOTE: no `mp.mp.dps = 50` at module scope. pytest imports every test module
# at COLLECTION time, so a global precision assignment here lands before any
# other module's test runs — it made the five exact-equality checks in
# `tools/qou-substrate/tests/test_codata_table.py` fail purely by collection
# order. Precision is set per-test by the `_dps` fixture below instead, which
# is also the discipline `qou_substrate.constants` follows for its own `_MP`
# family ("so this module does NOT mutate the caller's mp.mp.dps").
#
# Importing `hecke_core_legacy` still raises the floor to 50 via `q_parameter`
# ("global dps 50 for compute accuracy", owner directive 2026-07-06), which is
# what makes the `_M22_*` constants below well-defined at all.
L = pytest.importorskip("hecke_core_legacy")
from q_parameter import HA_MP as H_MP  # noqa: E402

# mpf roundoff at dps=50 is ~1e-50; the measured worst case over these
# partitions is 4.677e-51. 1e-45 leaves five decades of headroom while still
# being ~44 orders of magnitude below the 0.7315 defect this pins.
MPF_TOL = mp.mpf("1e-45")


@pytest.fixture(autouse=True)
def _dps():
    """Run every test at 50 dps without leaking that setting to other modules."""
    with mp.workdps(50):
        yield

# Partitions of n = 3..7 with dim >= 2 (dim 1 has no generator to relate).
PARTITIONS = [(2, 1), (3, 1), (2, 2), (2, 1, 1), (3, 2), (3, 1, 1),
              (2, 2, 1), (4, 2), (4, 3), (3, 3, 1), (3, 2, 1, 1)]


def _dense(M, dim):
    """Materialise either code path's output as a list-of-lists.

    The sparse carrier is `_ExactCOO` (`row`/`col`/`data`), detected with the
    module's own `_is_sparse_sigma`. It was `_CooMPF` with a `.toarray()`
    until main's 2026-09-11 pass removed the scipy arms as unreachable —
    scipy's containers are float64 by construction and reject `dtype=object`,
    so they could never have held an exact seminormal family. This helper
    still called `L._is_coo_mpf`, which went with them, so every test in this
    file raised AttributeError in `_build` and none of the three relations
    was ever reached. Densify from the COO triple directly; there is no
    `.toarray()` on the new carrier and it does not need one.
    """
    if L._is_sparse_sigma(M):
        out = [[mp.mpf(0)] * dim for _ in range(dim)]
        for i, j, v in zip(M.row, M.col, M.data):
            out[i][j] = v
        return out
    return [[M[i][j] for j in range(dim)] for i in range(dim)]


def _mul(A, B, dim, zero):
    return [[sum((A[i][t] * B[t][j] for t in range(dim)), zero)
             for j in range(dim)] for i in range(dim)]


def _maxdiff(A, B, dim):
    return max(abs(A[i][j] - B[i][j]) for i in range(dim) for j in range(dim))


def _relations(mats, dim, h, zero, one):
    """Return (quadratic, braid, far-commutation) max-norm defects."""
    quad = braid = comm = zero
    for S in mats:
        S2 = _mul(S, S, dim, zero)
        for i in range(dim):
            for j in range(dim):
                want = h * S[i][j] + (one if i == j else zero)
                quad = max(quad, abs(S2[i][j] - want))
    for t in range(len(mats) - 1):
        A, B = mats[t], mats[t + 1]
        braid = max(braid, _maxdiff(_mul(_mul(A, B, dim, zero), A, dim, zero),
                                    _mul(_mul(B, A, dim, zero), B, dim, zero),
                                    dim))
    for a in range(len(mats)):
        for b in range(a + 2, len(mats)):
            A, B = mats[a], mats[b]
            comm = max(comm, _maxdiff(_mul(A, B, dim, zero),
                                      _mul(B, A, dim, zero), dim))
    return quad, braid, comm


def _build(partition, **kw):
    mats = L._build_ysn_matrices(partition, **kw)
    dim = len(list(L._standard_tableaux(partition)))
    return [_dense(M, dim) for M in mats], dim


@pytest.mark.parametrize("partition", PARTITIONS)
def test_ysn_satisfies_all_three_hecke_relations(partition):
    """sigma^2 = h*sigma + 1;  braid;  far-commutation. All three, at q0."""
    mats, dim = _build(partition)
    quad, braid, comm = _relations(mats, dim, H_MP, mp.mpf(0), mp.mpf(1))
    assert quad < MPF_TOL, f"quadratic relation: {mp.nstr(quad, 6)}"
    # The one that matters — this read 0.731513681083349 before `qou-uiut`.
    assert braid < MPF_TOL, f"BRAID relation: {mp.nstr(braid, 6)}"
    assert comm < MPF_TOL, f"far-commutation: {mp.nstr(comm, 6)}"


@pytest.mark.parametrize("partition", [(3, 2, 1), (4, 3), (3, 3, 1)])
def test_sparse_path_agrees_with_dense_entry_for_entry(partition):
    """The sparse path must produce the same matrices, not merely valid ones."""
    dense, dim = _build(partition, sparse_threshold=1 << 30)
    sparse_mats = L._build_ysn_matrices(partition, sparse_threshold=1)
    assert L._is_sparse_sigma(sparse_mats[0]), "expected the sparse path to be taken"
    sparse = [_dense(M, dim) for M in sparse_mats]
    for k, (A, B) in enumerate(zip(dense, sparse)):
        assert _maxdiff(A, B, dim) == 0, f"sigma_{k + 1} differs dense vs sparse"


def test_M22_constants_track_the_builder_at_the_callers_precision():
    """`_crossing_M22`'s (2,2) generators must BE the builder's, at this dps.

    They used to be three module-level tuples: a copy of the builder's output,
    carrying the same wrong diagonal AND frozen at whatever `mp.dps` happened
    to be at import (15 on the non-muon anchor path, so 17 digits, inside a
    module excised to mpf end to end). Both are gone — but a future edit could
    reintroduce either, so check the value AND the precision.
    """
    ref, dim = _build((2, 2))
    assert dim == 2
    # Compare the DERIVATION, not the accessor. `_crossing_M22` evaluates
    # `c*M + d` at the CALLER's ambient precision, outside the builder's
    # `workdps(COMPUTE_DPS)`, so even `c=1, d=0` rounds a 70-dps entry to the
    # ambient — 3.04e-52 here, which is ambient rounding and not a frozen
    # constant. Asserting equality through the accessor tests mpmath's
    # rounding, not this module's.
    got = list(L._m22_generators())
    for k in range(3):
        # Exact: same builder, same working precision, same call.
        assert _maxdiff(ref[k], got[k], 2) == 0, f"sigma_{k + 1} != builder"
    quad, braid, comm = _relations([[list(r) for r in M] for M in got],
                                   2, H_MP, mp.mpf(0), mp.mpf(1))
    assert max(quad, braid, comm) < MPF_TOL
    # Two different precisions are in play, and the distinction is the point.
    #
    # The BUILDER is pinned: `_build_ysn_matrices` wraps itself in
    # `workdps(COMPUTE_DPS)` (main, 2026-09-11), so its entries do not follow
    # the caller — which is right, because the ambient is **15** in a bare
    # import, exactly float64's significand. That pin is what the
    # `_maxdiff(...) == 0` check above verifies, against `_m22_generators`.
    #
    # The ACCESSOR is not pinned: `_crossing_M22` evaluates `c*M + d` at the
    # caller's ambient precision. So raising `mp.dps` DOES move its output,
    # and a frozen 15-dps constant would not move at all. That is what is
    # asserted here, and it is the original contract — an earlier edit of mine
    # replaced it with `low == high` on the theory that the pin covered the
    # accessor too. It does not: measured, `low` comes back
    # -0.9009182839557414723685724311508238315582275390625, a float64 value,
    # against a 50-digit `high`.
    with mp.workdps(15):
        low = L._crossing_M22(1, 0, 1)
    with mp.workdps(50):
        high = L._crossing_M22(1, 0, 1)
    assert abs(high[1][1] - low[1][1]) > mp.mpf("1e-25"), (
        "raising mp.dps did not change the (2,2) constants — they are frozen "
        "again, and the module is silently mixed-precision")


def test_q0_path_is_mpf_not_float64():
    """NO-FLOAT64. A float64 `q_int` put the off-diagonal blocks at ~17 digits.

    The braid defect then reads 2.649e-16 — float64 epsilon, four orders above
    the 1e-20 a casual tolerance would allow, and utterly unlike the 4.677e-51
    the mpf construction reaches. Assert the TYPE so the alias in
    `hecke_core_legacy`'s import block cannot be quietly reverted.
    """
    mats, dim = _build((3, 2, 1))
    entries = [mats[k][i][j] for k in range(len(mats))
               for i in range(dim) for j in range(dim)]
    assert entries, "no entries built"
    assert all(isinstance(v, mp.mpf) for v in entries), (
        "YSN entries are not mpf — a float64 scalar leaked into the builder")
    quad, braid, _ = _relations(mats, dim, H_MP, mp.mpf(0), mp.mpf(1))
    assert braid < mp.mpf("1e-40"), (
        f"braid {mp.nstr(braid, 6)} is float64-grade, not mpf-grade")


@pytest.mark.parametrize("partition", [(2, 1), (2, 2), (3, 2), (3, 2, 1)])
def test_q_override_is_mpf_and_still_a_representation(partition):
    """The `q=` override (used by `sdp_cross_channel`'s sweep) is a rep, in mpf.

    That sweep kept a private copy of this builder, with the same wrong
    diagonal. It now delegates here, so the override path needs its own
    coverage.

    This test used to assert the OPPOSITE — that a float `q` yields float
    matrices — because the override dispatched arithmetic on the operand type
    to stay bit-identical to the private f64 copy it replaced. That preserved
    a float64 path on purpose, which NO FLOAT64 EVER (owner directive)
    forbids: bit-compatibility with an f64 predecessor is not a reason to keep
    computing in f64. The override now promotes whatever it is handed, and
    this test pins that direction so it cannot drift back.
    """
    qv = 1.1099785827513808          # a float on purpose: the caller's grid
    mats = L._build_ysn_matrices(partition, sparse_threshold=1 << 30, q=qv)
    dim = len(list(L._standard_tableaux(partition)))
    mats = [_dense(M, dim) for M in mats]
    assert all(isinstance(mats[k][i][j], mp.mpf)
               for k in range(len(mats)) for i in range(dim) for j in range(dim)), (
        "a float `q` must still yield mpf matrices — NO FLOAT64 EVER")
    q_m = mp.mpf(qv)
    quad, braid, comm = _relations(mats, dim, q_m - mp.mpf(1) / q_m,
                                   mp.mpf(0), mp.mpf(1))
    assert max(quad, braid, comm) < MPF_TOL


@pytest.mark.parametrize("partition", [(2, 1), (3, 2), (3, 2, 1)])
def test_q_to_one_gives_youngs_orthogonal_form(partition):
    """At q = 1, H_n(q) degenerates to C[S_n] and the seminormal form must
    become Young's ORTHOGONAL form: diagonal 1/rho, off-diagonal sqrt(1-1/rho^2).

    This is an independent check of the corrected diagonal, because the old
    `h/[rho]_q` sends h -> 0 at q = 1 and collapses the whole diagonal to zero.
    The sweep in `sdp_cross_channel.q_sweep_sdp_atom` does evaluate at q = 1.
    """
    mats = L._build_ysn_matrices(partition, sparse_threshold=1 << 30, q=1.0)
    dim = len(list(L._standard_tableaux(partition)))
    mats = [_dense(M, dim) for M in mats]
    # Every generator is an involution in S_n: sigma^2 = 1 (h = 0 above).
    for k, S in enumerate(mats):
        S2 = _mul(S, S, dim, mp.mpf(0))
        for i in range(dim):
            for j in range(dim):
                assert abs(S2[i][j] - (1 if i == j else 0)) < MPF_TOL, (
                    f"sigma_{k + 1}^2 != I at q=1")
    quad, braid, comm = _relations(mats, dim, mp.mpf(0), mp.mpf(0), mp.mpf(1))
    assert max(braid, comm) < MPF_TOL
    assert any(abs(mats[k][i][i]) > mp.mpf("1e-9")
               for k in range(len(mats)) for i in range(dim)), (
        "the q=1 diagonal collapsed to zero — the `h/[rho]` form is back")


def test_q_int_mp_is_the_mpf_quantum_integer():
    """`q_parameter`'s `_MP` family was missing its `q_int`; this is that gap.

    `q_int` closes over the FLOAT `Q`/`Q_INV`/`HA` and returns a Python float
    at any working precision, so `mpf / q_int(n)` silently caps at ~17 digits
    with nothing in the type to show it.
    """
    from q_parameter import q_int, q_int_mp, Q_MP, Q_INV_MP, HA_MP
    for n in (-3, -2, -1, 1, 2, 3, 4):
        got = q_int_mp(n)
        assert isinstance(got, mp.mpf)
        want = (Q_MP ** n - Q_INV_MP ** n) / HA_MP
        assert abs(got - want) < MPF_TOL
    # The float version really is lossy — if this ever stops being true the
    # alias is redundant and this file should say so rather than imply it.
    assert abs(mp.mpf(q_int(2)) - q_int_mp(2)) > mp.mpf("1e-20")
