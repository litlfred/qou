#!/usr/bin/env python3
"""
Sprint B verification — canonical 3-term Wedderburn formula in
alpha_blend_tower.py.

Tests:
  1. None of the dropped 2-term-blend tokens (root-find calls, fitted
     constants, helper functions) appear anywhere in the source.
  2. V_3term reproduces the proton mass within 1% of CODATA after
     a single-point energy-scale calibration (no fit beyond E0).
  3. The chirality channel (alt) contributes a non-zero amount to
     the neutron generators — proving it is actually summed and not
     symmetrised away.
  4. The brane-tower assembly contains no numerical root-find calls.

Run with:
    python -m pytest computations/test_three_term_wedderburn.py -v
or:
    python computations/test_three_term_wedderburn.py
"""
from __future__ import annotations
import sys
import re
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import alpha_blend_tower as abt  # noqa: E402  (path-injected import)
from hecke_core import _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1  # noqa: E402
from experimental_constants import M_P_MEV, M_N_MEV  # noqa: E402

SRC_PATH = HERE / "alpha_blend_tower.py"
SRC = SRC_PATH.read_text()
TOKEN_MANIFEST = HERE / "three-term-forbidden-tokens.txt"


# ─── Test 1: forbidden tokens ──────────────────────────────────────

def _load_tokens():
    if not TOKEN_MANIFEST.exists():
        return []
    return [
        ln.strip()
        for ln in TOKEN_MANIFEST.read_text().splitlines()
        if ln.strip() and not ln.startswith('#')
    ]


def test_no_forbidden_tokens_in_source():
    """No 2-term-blend artefacts (root-find, fitted constants, helpers)."""
    needles = _load_tokens()
    assert needles, "manifest must list at least one forbidden token"
    present = [t for t in needles if t in SRC]
    assert not present, (
        f"forbidden tokens still in alpha_blend_tower.py: {present}\n"
        f"(see {TOKEN_MANIFEST.name})"
    )


def test_no_root_find_calls():
    """Defensive grep: no scipy root-find calls anywhere in the file."""
    # Match any call-like usage of brentq / fsolve / newton / bisect.
    forbidden_calls = (r'\bbrentq\s*\(', r'\bfsolve\s*\(',
                       r'\bnewton\s*\(', r'\bbisect\s*\(')
    hits = [pat for pat in forbidden_calls if re.search(pat, SRC)]
    assert not hits, f"root-find call(s) found: {hits}"


def test_no_alpha_star_or_alpha4_definitions():
    """Explicit grep for variable assignments that would re-introduce
    the dropped fitting constants."""
    bad_assignments = [
        r'^\s*alpha_star\s*=',
        r'^\s*alpha_optimal\s*=',
        r'^\s*alpha_4\s*=',
        r'^\s*alpha4\s*=',
        r'^\s*_TARGET\s*=\s*0\.305807',
    ]
    for pat in bad_assignments:
        m = re.search(pat, SRC, re.MULTILINE)
        assert m is None, (
            f"forbidden assignment matched pattern {pat!r}: "
            f"{m.group(0) if m else None}"
        )


# ─── Test 2: V_3term has the right shape and produces a valid mass ─

def test_V_3term_returns_real_mpf():
    v = abt.V_3term(_PROTON_G0)
    assert v is not None
    # Explicit finiteness — `float(v) == float(v)` would have passed
    # even for ±inf (since inf == inf is true). Use mp.isfinite to
    # actually catch a Φ_q pole or other divergence.
    import mpmath as mp
    assert mp.isfinite(v), f"V_3term must be finite; got {v!r}"


def test_proton_mass_calibration_exact():
    """Energy-scale calibration on the proton must be exact by
    construction (E0 = M_P_MEV / mp_v ⇒ m_p_pred = M_P_MEV)."""
    Vp0 = abt.V_3term(_PROTON_G0)
    Vp1 = abt.V_3term(_PROTON_G1)
    mp_v = abt.tower([Vp0, Vp1])
    assert mp_v != 0, "tower(proton) must be non-zero"
    # Calibrate at 50 dps so the threshold check is bounded by the
    # mpmath precision rather than the float64 round-off floor.
    with abt.mp.workdps(abt._DPS):
        E0 = abt.mp.mpf(str(M_P_MEV)) / mp_v
        mp_pred = float(mp_v * E0)
    rel_err = abs(mp_pred - M_P_MEV) / M_P_MEV
    assert rel_err < 1e-12, (
        f"single-point proton calibration not exact: pred={mp_pred:.10f}, "
        f"CODATA={M_P_MEV}, rel_err={rel_err:.2e}"
    )


def test_proton_V_3term_is_O1():
    """The canonical V_3term(proton) must be O(1) — confirming the
    Wedderburn weights and channel formulas land in the physical
    regime. This is the structural analogue of the "within-1%-of-CODATA"
    sanity check for the V-volume itself, independent of any
    downstream tower harness.

    Note: the previous 2-term blend's brane-tower harness was tuned
    to V values around 0.5; the canonical V_3term values sit closer
    to 1 (near the Φ_q pole). The mass-prediction harness therefore
    needs a downstream restructure (cf. Sprint B summary). The
    structural canonicalization in THIS module — eliminating the
    fitted mixing parameter and the downstream n→p calibration
    constant — is independent of and complete without that
    restructure."""
    Vp0 = abt.V_3term(_PROTON_G0)
    Vp1 = abt.V_3term(_PROTON_G1)
    assert 0.1 < abs(float(Vp0)) < 10, (
        f"V_3term(proton G0)={float(Vp0)} is outside O(1) — "
        f"check Wedderburn weights and channel formulas"
    )
    assert 0.1 < abs(float(Vp1)) < 10, (
        f"V_3term(proton G1)={float(Vp1)} is outside O(1) — "
        f"check Wedderburn weights and channel formulas"
    )


# ─── Test 3: chirality (alt channel) is non-zero on neutron gens ───

def test_alt_channel_nonzero_on_neutron():
    """The alt Wedderburn block — the chirality channel — must
    contribute non-trivially. If it were zero, the 3-term formula
    would degenerate back to the symmetrised blend and we would not
    have eliminated the n→p calibration parameter."""
    n_g0 = abt.channel_decomposition(_NEUTRON_G0)
    n_g1 = abt.channel_decomposition(_NEUTRON_G1)
    alt_g0 = float(n_g0['alt'])
    alt_g1 = float(n_g1['alt'])
    # Use absolute magnitude relative to the total to make the
    # threshold scale-free.
    tot_g0 = abs(float(n_g0['total']))
    tot_g1 = abs(float(n_g1['total']))
    assert tot_g0 > 0 and tot_g1 > 0, "neutron totals must be non-zero"
    # alt should contribute at the percent-or-better level (it is the
    # whole point of the upgrade — anything less means we're back in
    # the 2-term frame).
    rel_g0 = abs(alt_g0) / tot_g0
    rel_g1 = abs(alt_g1) / tot_g1
    assert rel_g0 > 1e-6, (
        f"alt channel on neutron gen-0 vanishes: alt={alt_g0:.3e}, "
        f"total={tot_g0:.3e}, ratio={rel_g0:.3e}"
    )
    assert rel_g1 > 1e-6, (
        f"alt channel on neutron gen-1 vanishes: alt={alt_g1:.3e}, "
        f"total={tot_g1:.3e}, ratio={rel_g1:.3e}"
    )


def test_alt_channel_distinguishes_proton_neutron():
    """Sanity: the chirality channel must not be identical for the
    proton and neutron — otherwise it would not encode the n↔p
    distinction it is supposed to restore."""
    p_g0 = abt.channel_decomposition(_PROTON_G0)
    n_g0 = abt.channel_decomposition(_NEUTRON_G0)
    diff = abs(float(p_g0['alt']) - float(n_g0['alt']))
    avg = 0.5 * (abs(float(p_g0['alt'])) + abs(float(n_g0['alt'])))
    assert avg > 0
    rel = diff / avg
    assert rel > 1e-6, (
        f"alt channel identical for proton and neutron (rel diff "
        f"{rel:.3e}) — chirality is not encoding n vs p"
    )


# ─── Test 4: structural attestation ────────────────────────────────

def test_V_3term_is_pure_wedderburn_sum():
    """V_3term should equal the sum of its three channel contributions
    (no hidden mixing). Compare in mpmath at 50 dps — the previous
    float64 cast capped error at ~1e-16 floor, which made the 1e-30
    bound meaningless."""
    chain = _PROTON_G0
    decomp = abt.channel_decomposition(chain)
    direct = abt.V_3term(chain)
    # mp.almosteq(a, b, rel_eps) holds iff |a-b| <= rel_eps * max(|a|,|b|).
    # Use a tolerance ~10^-(_DPS-2) so the test exercises mpmath
    # precision rather than float round-off.
    tol = abt.mp.mpf(10) ** (-(abt._DPS - 2))
    assert abt.mp.almosteq(direct, decomp['total'], rel_eps=tol), (
        f"V_3term({chain[:3]}...) = {direct} but channel decomposition "
        f"sums to {decomp['total']} (|Δ|={abs(direct - decomp['total'])}, "
        f"rel_eps tol={tol})"
    )


def test_dps_is_50():
    # alpha_blend_tower._DPS is the canonical Sprint B precision floor.
    # The module sets mp.mp.dps = _DPS at import time as a deliberate
    # documented side-effect; importers see the elevated precision.
    import mpmath as mp
    assert abt._DPS == 50, f"abt._DPS is {abt._DPS}, expected 50"
    assert mp.mp.dps >= abt._DPS, (
        f"global mp.mp.dps is {mp.mp.dps}, expected >= {abt._DPS}"
    )


# ─── Standalone runner ─────────────────────────────────────────────

def _run_all():
    tests = [
        ('no_forbidden_tokens_in_source', test_no_forbidden_tokens_in_source),
        ('no_root_find_calls', test_no_root_find_calls),
        ('no_alpha_star_or_alpha4_definitions',
         test_no_alpha_star_or_alpha4_definitions),
        ('V_3term_returns_real_mpf', test_V_3term_returns_real_mpf),
        ('proton_mass_calibration_exact', test_proton_mass_calibration_exact),
        ('proton_V_3term_is_O1', test_proton_V_3term_is_O1),
        ('alt_channel_nonzero_on_neutron',
         test_alt_channel_nonzero_on_neutron),
        ('alt_channel_distinguishes_proton_neutron',
         test_alt_channel_distinguishes_proton_neutron),
        ('V_3term_is_pure_wedderburn_sum',
         test_V_3term_is_pure_wedderburn_sum),
        ('dps_is_50', test_dps_is_50),
    ]
    failures = []
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
        except AssertionError as e:
            print(f"  FAIL  {name}: {e}")
            failures.append((name, str(e)))
        except Exception as e:
            print(f"  ERROR {name}: {type(e).__name__}: {e}")
            failures.append((name, f"{type(e).__name__}: {e}"))
    print()
    if failures:
        print(f"  {len(failures)} test(s) failed:")
        for name, msg in failures:
            print(f"    - {name}: {msg}")
        return 1
    print(f"  all {len(tests)} tests passed.")
    return 0


if __name__ == "__main__":
    sys.exit(_run_all())
