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

CONVENTION. Every value below is **convention C** (z = 1/(q^1/2+q^-1/2)),
because pyhecke.gram is still on C: the C -> D migration is BLOCKED here,
see the note at pyhecke/gram.py's `z`. When that unblocks, every literal
in this file moves; they are labelled so a grep for the convention finds
them.
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
    """z = 1/(q^{1/2}+q^{-1/2}) -- **convention C** -- at the PROTON pin
    q_0 = 1.1099785827513808 (`q_parameter.Q`).

    Was pinned to 0.4993203340335982, the value at the MUON pin
    1.1099785955541805, and had been failing by 1.5e-10 against a 1e-14
    tolerance. Under convention D this becomes 0.6126880371464652.
    """
    assert abs(pyhecke_gram.z - 0.4993203341836945) < 1e-14


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
    """det G at the proton pin, convention C, with the corrected TR_M[5].

    Was pinned to -0.36080112. That is the determinant you get with the
    pre-2026-05-19 `TR_M[5] = z**3` -- it is still what
    tools/hecke-engine/src/gram.rs produces, because the fix was never
    ported there. With the module's actual (correct) `h*z^2 + z` the value
    is -0.1892052191440367.

    Under convention D this determinant is ZERO -- the Markov-Gram form is
    degenerate, proved in QOU/QBeta/GramSignature.lean. That is why the
    C -> D switch is blocked here; see pyhecke/gram.py.
    """
    G = pyhecke_gram.G
    assert G.shape == (6, 6)
    det = numpy.linalg.det(G)
    assert abs(det - (-0.1892052191440367)) < 1e-9


def test_gram_inverse_identity():
    G = pyhecke_gram.G
    GI = pyhecke_gram.G_INV
    prod = G @ GI
    assert numpy.allclose(prod, numpy.eye(6), atol=1e-10)


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
    assert hecke_core.G_INV is pyhecke_gram.G_INV
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
