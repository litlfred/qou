"""Numerical-regression tests for the Gram matrix and Markov trace.

These tests pin the exact values at the substrate q_0 so any future change
to pyhecke.gram that would alter downstream witnesses is caught immediately.

Baseline values were captured from the pre-inversion hecke_core.py and
round-trip-verified on every committed certificate-*.json.

REPAIRED 2026-08-09 (bean qou-wgta, items 11/15/16). Three of these tests
had been failing since 2026-05-19 and one header claim was wrong:

* The header said q_0 = 1.1099785955541805. That is the MUON pin. The
  module reads `q_parameter.Q`, the PROTON pin 1.1099785827513808 (AGENTS.md
  owner directive 2026-08-07). The two are 11.54 ppb apart, which is 1.5e-10
  on z -- four orders of magnitude past the 1e-14 tolerance the z test used.
* `docs/audits/2026-05-19-trm5-markov-bug.md` corrected TR_M[5] from `z**3`
  to `h*z**2 + z` in the module and updated NEITHER the test asserting
  `z**3` NOR the determinant pin that followed from it (nor the Rust
  mirror -- see tools/hecke-engine/src/gram.rs).

CONVENTION. **MIGRATED TO CONVENTION D** (z = q^3/(q^2+1)) -- the block
that this header previously described as "BLOCKED here" is now lifted.
Every literal that moved is labelled with both values so the change is
auditable from this file alone:

    z        0.4993203341836945 (C)  ->  0.6126880371464652 (D)   +22.70%
    det G   -0.1892052191440367 (C)  ->  0                 (D)   SINGULAR
    G_INV    exists              (C)  ->  does not exist    (D)

The determinant test below was strengthened rather than merely re-pinned:
under D the form is genuinely degenerate, and a float64 determinant
(3.998e-17 on this machine) cannot distinguish "singular" from "very
small". Convention D makes the Gram exactly rational, so the test now
asserts det == 0 EXACTLY over Q, plus rank 5 and G @ RADICAL == 0.
"""

from __future__ import annotations

import pytest

pytest.importorskip("numpy")
numpy = pytest.importorskip("numpy")

try:
    from pyhecke import gram as pyhecke_gram  # needs hecke_core path
except ImportError:  # pragma: no cover
    pytest.skip("pyhecke.gram requires computations on path",
                allow_module_level=True)


def test_z_markov_value():
    """z = q^3/(q^2+1) -- **convention D** -- at the PROTON pin
    q_0 = 1.1099785827513808 (`q_parameter.Q`).

    History of this pin: 0.4993203340335982 (convention C at the MUON
    pin -- wrong pin, failed by 1.5e-10 against a 1e-14 tolerance)
    -> 0.4993203341836945 (convention C at the proton pin)
    -> 0.6126880371464652 (convention D at the proton pin), +22.70%.

    Recomputed from the definition rather than read off the module."""
    q = float(pyhecke_gram.q0)
    assert abs(pyhecke_gram.z - q ** 3 / (q ** 2 + 1)) < 1e-15
    assert abs(pyhecke_gram.z - 0.6126880371464652) < 1e-14
    # Guard the migration directly: this is NOT the convention-C value.
    assert abs(pyhecke_gram.z - 0.4993203341836945) > 0.1


def test_tr_m_weights_shape_and_start():
    """TR_M = [1, z, z, z^2, z^2, h*z^2 + z] on the NF basis.

    The last entry asserted `z**3` until 2026-08-09. `h*z^2 + z` is the
    correct Markov trace of e- = sigma_0 sigma_1 sigma_0 (cyclicity plus
    sigma_0^2 = h*sigma_0 + 1); `z**3` is the bug that
    docs/audits/2026-05-19-trm5-markov-bug.md fixed IN THE MODULE while
    leaving this assertion behind, so the test has been red ever since.
    """
    h = pyhecke_gram.h
    z = pyhecke_gram.z
    assert pyhecke_gram.TR_M.shape == (6,)
    assert abs(pyhecke_gram.TR_M[0] - 1.0) < 1e-15
    assert abs(pyhecke_gram.TR_M[1] - z) < 1e-15
    assert abs(pyhecke_gram.TR_M[3] - z ** 2) < 1e-15
    assert abs(pyhecke_gram.TR_M[5] - (h * z ** 2 + z)) < 1e-15
    # Guard the regression directly: e- is NOT z^3.
    assert abs(pyhecke_gram.TR_M[5] - z ** 3) > 1e-3


def test_nf_basis_is_canonical_ordering():
    assert pyhecke_gram.NF_BASIS == [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
    assert pyhecke_gram.NF_NAMES == ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]


def test_gram_shape_and_determinant():
    """Under **convention D** the Markov-Gram form is SINGULAR.

    Pin history: -0.36080112 (convention C with the pre-2026-05-19
    `TR_M[5] = z**3` bug -- still what tools/hecke-engine/src/gram.rs
    produces, since the fix was never ported there) -> -0.1892052191440367
    (convention C with the correct `h*z^2 + z`) -> 0 EXACTLY (convention
    D). Degeneracy proved in QOU/QBeta/GramSignature.lean.

    This asserts rank, not a float determinant. `numpy.linalg.det(G)` is
    3.998e-17 here, which is NOT evidence of singularity -- it is what a
    float64 determinant of a singular matrix looks like, and it is also
    what a genuinely tiny nonzero determinant looks like. The exact
    statement is `test_gram_determinant_is_exactly_zero_over_Q` below."""
    G = pyhecke_gram.G
    assert G.shape == (6, 6)
    assert numpy.linalg.matrix_rank(G, tol=1e-12) == 5
    # The null direction is the q-antisymmetriser, in closed form.
    assert numpy.linalg.norm(G @ pyhecke_gram.RADICAL) < 1e-12


def test_gram_determinant_is_exactly_zero_over_Q():
    """det G == 0 EXACTLY in Q, and the nullspace is exactly 1-dimensional.

    This is the test the float64 path cannot express. Convention D makes
    z = q^3/(q^2+1) a rational *function*, so at the rational model
    q = 111/100 every Gram entry is a Fraction and the determinant is an
    exact rational number -- which is 0, not 3.998e-17. Under convention C
    this test could not have been written at all: z was irrational there,
    so the exact path carried a 4-digit truncation of it."""
    from fractions import Fraction

    NF = pyhecke_gram.NF_BASIS
    trm = pyhecke_gram._TR_M_FRAC
    assert all(isinstance(t, Fraction) for t in trm), trm

    # G_ij = tr_M(w_i . w_j), all in Q.
    rows = []
    for i in range(6):
        row = []
        for j in range(6):
            nf = pyhecke_gram.nf_of_word(NF[i] + NF[j], exact=True)
            row.append(sum(nf[k] * trm[k] for k in range(6)))
        rows.append(row)
    assert all(isinstance(x, Fraction) for r in rows for x in r)

    # Exact fraction-free Gaussian elimination -> rank + determinant.
    M = [r[:] for r in rows]
    det = Fraction(1)
    rank = 0
    for col in range(6):
        piv = next((r for r in range(rank, 6) if M[r][col] != 0), None)
        if piv is None:
            det = Fraction(0)
            continue
        if piv != rank:
            M[rank], M[piv] = M[piv], M[rank]
            det = -det
        det *= M[rank][col]
        inv = Fraction(1) / M[rank][col]
        for r in range(rank + 1, 6):
            f = M[r][col] * inv
            if f:
                for c in range(col, 6):
                    M[r][c] -= f * M[rank][c]
        rank += 1
    assert rank == 5, f"expected rank 5, got {rank}"
    assert det == 0, f"expected exactly 0, got {det}"

    # And the closed-form radical really is the null direction, exactly.
    qf = pyhecke_gram._Q_FRAC
    v = [(-1 / qf) ** len(w) for w in NF]
    for i in range(6):
        assert sum(rows[i][j] * v[j] for j in range(6)) == 0, i


def test_gram_inverse_is_gone_and_pseudoinverse_is_the_quotient_inverse():
    """`G_INV` does not exist under convention D -- the form is singular,
    so there is no 6x6 inverse. `G_PINV` is the inverse on the quotient
    H_3(q)/rad, which is what downstream consumers actually need."""
    G = pyhecke_gram.G
    assert not hasattr(pyhecke_gram, "G_INV"), \
        "G_INV must not be resurrected: the form is singular under D"
    with pytest.raises(NotImplementedError):
        pyhecke_gram.gram_inverse()

    GP = pyhecke_gram.G_PINV
    # Moore-Penrose defining identity (the one that survives singularity).
    assert numpy.allclose(G @ GP @ G, G, atol=1e-10)
    assert numpy.allclose(GP @ G @ GP, GP, atol=1e-10)
    # G_PINV annihilates the radical -- i.e. it IS the quotient inverse,
    # not a numerically-regularised stand-in for a 6x6 inverse.
    assert numpy.linalg.norm(GP @ pyhecke_gram.RADICAL) < 1e-10
    assert pyhecke_gram.gram_quotient_inverse() is GP


def test_wedderburn_weights_sum_and_individual():
    # W_SYM + W_STD + W_ALT = 1 (unit measure on Wedderburn components)
    s = pyhecke_gram.W_SYM + pyhecke_gram.W_STD + pyhecke_gram.W_ALT
    assert abs(s - 1.0) < 1e-12


def test_hm_identity_action():
    """hm(1, 0, 1, 0) applied to γ gives σ_0."""
    nf = [1.0, 0, 0, 0, 0, 0]  # γ
    out = pyhecke_gram.hm(nf, 1.0, 0.0, 0)
    assert abs(out[1] - 1.0) < 1e-12
    for i in (0, 2, 3, 4, 5):
        assert abs(out[i]) < 1e-12


def test_hm_exact_returns_fractions():
    from fractions import Fraction
    nf = [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0)]
    out = pyhecke_gram.hm_exact(nf, Fraction(1), Fraction(0), 0)
    assert out[1] == Fraction(1)
    assert all(isinstance(x, Fraction) for x in out)


def test_hecke_core_reexports_match_pyhecke():
    """After inversion, hecke_core.G must BE pyhecke.gram.G (not a copy)."""
    import hecke_core  # type: ignore[import-not-found]
    assert hecke_core.G is pyhecke_gram.G
    # G_INV is gone under D; the re-export must follow, not shim it back.
    assert not hasattr(hecke_core, "G_INV")
    assert hecke_core.G_PINV is pyhecke_gram.G_PINV
    assert hecke_core.RADICAL is pyhecke_gram.RADICAL
    assert hecke_core.z is pyhecke_gram.z
    assert hecke_core.NF_BASIS is pyhecke_gram.NF_BASIS
    assert hecke_core.TR_M is pyhecke_gram.TR_M
    assert hecke_core.hm is pyhecke_gram.hm
    assert hecke_core.hm_exact is pyhecke_gram.hm_exact


def test_pyhecke_gram_build_atom_nf_matches_hecke_core():
    """pyhecke.gram.build_atom_nf dispatches to native-or-legacy and
    agrees byte-for-byte with hecke_core.build_atom_nf."""
    import hecke_core  # type: ignore[import-not-found]
    for Z, N in [(1, 0), (2, 2), (6, 6)]:
        nf_dispatched = pyhecke_gram.build_atom_nf(Z, N)
        nf_legacy = hecke_core.build_atom_nf(Z, N)
        diff = numpy.max(numpy.abs(
            numpy.array(nf_dispatched) - numpy.array(nf_legacy)
        ))
        assert diff < 1e-12, f"Z={Z} N={N}: diff {diff}"


def test_pyhecke_gram_atom_per_generator_volumes_matches_hecke_core():
    import hecke_core  # type: ignore[import-not-found]
    py = hecke_core.atom_per_generator_volumes(6, 6)
    ds = pyhecke_gram.atom_per_generator_volumes(6, 6)
    assert len(py) == len(ds)
    max_diff = max(
        abs(p[k] - d[k]) for p, d in zip(py, ds) for k in ("sym", "std", "alt", "full")
    )
    assert max_diff < 1e-12


def test_pyhecke_gram_has_native_exported():
    assert callable(pyhecke_gram.has_native)
    assert isinstance(pyhecke_gram.has_native(), bool)


# ──────────────────────────────────────────────────────────────────
# Native (Rust) dispatch — convergence self-check (qou-m7py RESOLVED)
# ──────────────────────────────────────────────────────────────────
# The crate + every language binding are on convention D as of the
# qou-m7py port (2026-08-15): trace_weights ends h*z^2 + z, Q_0 is the
# proton pin, gram_inverse -> gram_quotient_inverse + gram_radical. So a
# freshly-built wheel is ENABLED by default. The only residual risk is an
# OLD wheel (build date unknowable), which `_native_ok()` catches with a
# runtime convergence self-check against TR_M/G at q0 and refuses loudly.
# QOU_DISABLE_NATIVE=1 is the explicit opt-out. These tests pin that.

def test_native_ok_false_when_wheel_absent():
    """No wheel -> no dispatch, and no exception either."""
    if pyhecke_gram.has_native():
        pytest.skip("wheel installed; see the self-check tests below")
    assert pyhecke_gram._native_ok() is False


def test_native_dispatch_enabled_when_convergent(monkeypatch):
    """A wheel that passes the convention-D self-check is ENABLED.

    Post-qou-m7py the crate matches this module, so the self-check passes and
    `_native_ok()` returns True (the ~100x native path). We stub the check to
    True to keep this test independent of whether a real wheel is installed in
    this environment."""
    monkeypatch.setattr(pyhecke_gram, "_HAS_NATIVE", True)
    monkeypatch.setattr(pyhecke_gram, "_NATIVE_VERIFIED", True)
    monkeypatch.delenv("QOU_DISABLE_NATIVE", raising=False)
    assert pyhecke_gram._native_ok() is True


def test_native_can_be_disabled_explicitly(monkeypatch):
    """QOU_DISABLE_NATIVE=1 forces the pure-Python path even when a
    convergent wheel is installed."""
    monkeypatch.setattr(pyhecke_gram, "_HAS_NATIVE", True)
    monkeypatch.setattr(pyhecke_gram, "_NATIVE_VERIFIED", True)
    monkeypatch.setenv("QOU_DISABLE_NATIVE", "1")
    assert pyhecke_gram._native_ok() is False


def test_native_dispatch_refuses_a_divergent_wheel(monkeypatch):
    """An OLD/divergent wheel (self-check fails) is refused loudly, never
    silently returning divergent numbers."""
    monkeypatch.setattr(pyhecke_gram, "_HAS_NATIVE", True)
    monkeypatch.setattr(pyhecke_gram, "_NATIVE_VERIFIED", False)
    monkeypatch.delenv("QOU_DISABLE_NATIVE", raising=False)
    assert pyhecke_gram._native_ok() is False


# ──────────────────────────────────────────────────────────────────
# safe_inverse — the guard numpy does not give you
# ──────────────────────────────────────────────────────────────────

def test_numpy_inv_silently_returns_garbage_on_the_d_gram():
    """The premise `safe_inverse` exists for. If numpy ever starts raising
    here, this test fails and the guard can be reconsidered -- so the
    justification is pinned, not just asserted in a docstring."""
    G = pyhecke_gram.G
    bad = numpy.linalg.inv(G)          # no exception -- that IS the problem
    assert numpy.abs(bad).max() > 1e10, numpy.abs(bad).max()
    assert numpy.linalg.norm(G @ bad - numpy.eye(6)) > 1.0


def test_safe_inverse_raises_on_the_singular_gram():
    with pytest.raises(numpy.linalg.LinAlgError, match="singular"):
        pyhecke_gram.safe_inverse(pyhecke_gram.G, what="Markov Gram")


def test_safe_inverse_message_names_the_replacement():
    """A guard that only says 'no' costs the caller a research detour."""
    try:
        pyhecke_gram.safe_inverse(pyhecke_gram.G)
    except numpy.linalg.LinAlgError as e:
        msg = str(e)
    assert "gram_quotient_inverse" in msg
    assert "rank 5 of 6" in msg
    # It must also say the replacement is a DIFFERENT object, or a caller
    # will just swap it under the old witness key.
    assert "DIFFERENT witness key" in msg


def test_safe_inverse_passes_through_invertible_matrices():
    M = numpy.array([[2.0, 1.0], [1.0, 3.0]])
    assert numpy.allclose(pyhecke_gram.safe_inverse(M) @ M, numpy.eye(2))


# ══════════════════════════════════════════════════════════════════
# mpmath mirror — convention lockstep with the float64 originals
# ══════════════════════════════════════════════════════════════════
# WHY THESE EXIST (bean qou-h4ab). The 2026-08-15 migration moved the f64
# `z` to convention D and this file pinned it — `test_z_value` even asserts
# it is NOT the C value. But nothing here touched `z_mp`, `tr_m_mp` or
# `gram_matrix_mp`, so the 50-dps mirror silently stayed on C for two days:
#
#     z        = 0.6126880371464652   (D)
#     z_mp()   = 0.4993203341836945   (C)      18.5 % apart
#
# and `gram_matrix_mp` — which inlines its own weights rather than calling
# `tr_m_mp`, despite a docstring saying otherwise — disagreed with the f64
# `G` by 3.36e-01 where its own docstring promised ~1e-15.
#
# The mirror is the path the NO-FLOAT64 precision discipline steers careful
# callers onto, so the superseded convention was reaching exactly the code
# that had tried hardest to be right. Pinning the f64 original while leaving
# its high-precision twin unguarded is the hole; these close it.
#
# Written as LOCKSTEP invariants, not as value pins: a future convention
# migration should have to change one number in this file, not four, and
# should fail loudly here if it forgets the mirror again.

def test_z_mp_is_in_lockstep_with_float64_z():
    """z_mp() must equal the f64 `z` to mpmath precision, not 18 % off."""
    import mpmath as mp
    from pyhecke import gram as pyhecke_gram
    with mp.workdps(50):
        zf = mp.mpf(repr(pyhecke_gram.z))
        zm = pyhecke_gram.z_mp()
        rel = abs(zm - zf) / zf
        assert rel < mp.mpf("1e-15"), (
            f"z_mp() is not in lockstep with z: rel={mp.nstr(rel, 6)}. "
            f"z={mp.nstr(zf, 20)}  z_mp={mp.nstr(zm, 20)}. "
            f"A convention migration probably moved one and not the other."
        )
        # and it is D, not C
        assert abs(zm - mp.mpf("0.4993203341836945")) > mp.mpf("0.1"), \
            "z_mp() is back on convention C"


def test_tr_m_mp_is_in_lockstep_with_float64_TR_M():
    import mpmath as mp
    from pyhecke import gram as pyhecke_gram
    with mp.workdps(50):
        for i, (a, b) in enumerate(zip(pyhecke_gram.TR_M,
                                       pyhecke_gram.tr_m_mp())):
            af = mp.mpf(repr(float(a)))
            rel = abs(b - af) / max(abs(af), mp.mpf("1e-30"))
            assert rel < mp.mpf("1e-14"), (
                f"tr_m_mp()[{i}] diverges from TR_M[{i}]: "
                f"rel={mp.nstr(rel, 6)} ({mp.nstr(af, 18)} vs {mp.nstr(b, 18)})"
            )


def test_gram_matrix_mp_agrees_with_float64_G():
    """The ~1e-15 agreement `gram_matrix_mp`'s docstring promises.

    This is the assertion that was false: it read 3.36e-01. Note that fixing
    `z_mp` and `tr_m_mp` alone does NOT fix it — `gram_matrix_mp` inlines its
    own Markov weights — so this test is not redundant with the two above.
    """
    import mpmath as mp
    from pyhecke import gram as pyhecke_gram
    with mp.workdps(50):
        Gm = pyhecke_gram.gram_matrix_mp()
        G = pyhecke_gram.G
        worst = mp.mpf(0)
        for i in range(6):
            for j in range(6):
                af = mp.mpf(repr(float(G[i][j])))
                rel = abs(Gm[i][j] - af) / max(abs(af), mp.mpf("1e-30"))
                worst = max(worst, rel)
        assert worst < mp.mpf("1e-14"), (
            f"gram_matrix_mp disagrees with G by {mp.nstr(worst, 6)}; its "
            f"docstring promises ~1e-15"
        )
