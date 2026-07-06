#!/usr/bin/env python3
"""
Phase-1 regression tests for the Markov-axiom recursive ascent
(`markov_peel.py`).

Cross-checks the symbolic `tr_M_atomic(Z, N)` evaluated at q₀
against the production Hoefsmit + Wenzl-bridge witness in
`atomic-tr-m-mpfr-50dps.witness.json`.

The Hoefsmit path materialises dim-up-to-462 matrices per partition;
the Markov-peel path materialises **none**.  Agreement to ~1e-12
at the canonical q₀ confirms the axiomatic-ascent algorithm
reproduces the production trace.

Tracked in #508; A ≥ 3 cases may fall back to the Ocneanu path
until Phase 2 completes the Gröbner–Shirshov rewrite system.

Run with:
    python -m pytest computations/test_markov_peel.py -v
or:
    python computations/test_markov_peel.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from markov_peel import tr_M_atomic, crossing_element  # noqa: E402
from hecke_symbolic import (  # noqa: E402
    SymbolicHeckeElement, q as q_sym, HA, z_markov,
)
from q_parameter import Q as Q0  # noqa: E402


WITNESS = HERE / "atomic-tr-m-mpfr-50dps.witness.json"
PEEL_WITNESS = HERE / "markov-peel-atomic-tr-m.witness.json"


def _load_witness_tr_m(atom: str) -> float:
    """Load `tr_M(q₀)` for the named atom from the production witness."""
    data = json.loads(WITNESS.read_text())
    for entry in data["results"]:
        if entry["atom"] == atom:
            return float(entry["tr_M_at_q0_50dps"])
    raise KeyError(f"atom {atom!r} not in {WITNESS.name}")


def _load_peel_witness(atom: str) -> float:
    """Load `tr_M(q₀)` from the Markov-peel production witness."""
    data = json.loads(PEEL_WITNESS.read_text())
    for row in data["data"]["results"]:
        if row.get("atom") == atom:
            return float(row["tr_M_at_q0"])
    raise KeyError(f"atom {atom!r} not in {PEEL_WITNESS.name}")


def _eval_at_q0(expr) -> float:
    """Numerical evaluation at the canonical q₀ to ~30-digit precision."""
    return float(sp.sympify(expr).subs(q_sym, Q0).evalf(30))


# ── Test 1: crossing_element matches the (c, d) convention ─────────

def test_crossing_element_sigma():
    e = crossing_element(0, "sigma")
    assert e.terms == {(0,): sp.Integer(1)}


def test_crossing_element_sigma_inv():
    # σ⁻¹ = σ − h
    e = crossing_element(2, "sigma_inv")
    assert e.terms[(2,)] == sp.Integer(1)
    assert sp.simplify(e.terms[()] - (-HA)) == 0


def test_crossing_element_averaged():
    # ½(σ + σ⁻¹) = σ − h/2
    e = crossing_element(1, "averaged")
    assert e.terms[(1,)] == sp.Integer(1)
    assert sp.simplify(e.terms[()] - (-HA / 2)) == 0


def test_crossing_element_unknown_raises():
    import pytest
    with pytest.raises(ValueError):
        crossing_element(0, "garbage")


# ── Test 2: trivial / base-case identities ──────────────────────────

def test_tr_M_identity_is_one():
    """tr_M^{(n)}(1) = 1 for any n."""
    from markov_trace_canonical import tr_M_element
    elem = SymbolicHeckeElement.identity()
    assert sp.simplify(tr_M_element(elem, n=3) - 1) == 0
    assert sp.simplify(tr_M_element(elem, n=6) - 1) == 0


def test_tr_M_single_sigma_is_z():
    """tr_M(σ_0) = z (canonical Markov axiom, base case M2)."""
    from markov_trace_canonical import tr_M_element
    elem = SymbolicHeckeElement({(0,): sp.Integer(1)})
    result = tr_M_element(elem, n=3)
    assert sp.simplify(result - z_markov) == 0


def test_tr_M_sigma_pair_is_z_squared():
    """tr_M(σ_0 σ_1) = z² (prop:markov-pair-z2)."""
    from markov_trace_canonical import tr_M_element
    elem = SymbolicHeckeElement({(0, 1): sp.Integer(1)})
    result = tr_M_element(elem, n=3)
    assert sp.simplify(result - z_markov ** 2) == 0


# ── Test 3: cross-check against production witnesses ───────────────

def test_tr_M_atomic_proton_matches_witness():
    """Z=1 N=0: Markov-peel must agree with Hoefsmit+Wenzl bridge."""
    expected = _load_witness_tr_m("proton")
    got_sym = tr_M_atomic(Z=1, N=0)
    got = _eval_at_q0(got_sym)
    assert abs(got - expected) < 1e-12, (
        f"proton tr_M mismatch: peel={got!r}  witness={expected!r}"
    )


def test_tr_M_atomic_neutron_matches_witness():
    """Z=0 N=1: Markov-peel must agree with Hoefsmit+Wenzl bridge."""
    expected = _load_witness_tr_m("neutron")
    got_sym = tr_M_atomic(Z=0, N=1)
    got = _eval_at_q0(got_sym)
    assert abs(got - expected) < 1e-12, (
        f"neutron tr_M mismatch: peel={got!r}  witness={expected!r}"
    )


def test_tr_M_atomic_deuteron_matches_witness():
    """Z=1 N=1: A=2 cross-check, n_strands=6, word length 23."""
    expected = _load_witness_tr_m("deuteron")
    got_sym = tr_M_atomic(Z=1, N=1)
    got = _eval_at_q0(got_sym)
    assert abs(got - expected) < 1e-12, (
        f"deuteron tr_M mismatch: peel={got!r}  witness={expected!r}"
    )


# ── Test 4: production atoms — ³He, tritium, ⁴He ────────────────────

import pytest  # noqa: E402


@pytest.mark.slow
def test_tr_M_atomic_tritium_matches_witness():
    """Z=1 N=2: A=3, n_strands=9, word length 35.

    Phase-2 part 1 (#508 commit 80eafe8b) unblocked this via
    incremental Gröbner–Shirshov reduction — the unreduced product
    used to explode to ~9000 terms before reduction; interleaving
    keeps the intermediate count bounded (~256 terms).  Trace
    recursion takes ~2 minutes; marked `slow` for selective skip.
    """
    expected = _load_witness_tr_m("tritium")
    got_sym = tr_M_atomic(Z=1, N=2)
    got = _eval_at_q0(got_sym)
    assert abs(got - expected) < 1e-10, (
        f"tritium tr_M mismatch: peel={got!r} witness={expected!r}"
    )


@pytest.mark.slow
def test_tr_M_atomic_helium3_matches_witness():
    """Z=2 N=1: A=3, n_strands=9, word length 35.

    Phase-2 part 2 (#508 commit 2834792d) unblocked this by skipping
    the `sp.simplify` step in `tr_M_element` — aggregation is 60 ms
    but the simplify on the ~5000-op total exceeded 30 min.  Total
    runtime now ~5 s (reduce 4.8s + agg 0.06s + evalf 0.06s).
    """
    expected = _load_witness_tr_m("helium-3")
    got_sym = tr_M_atomic(Z=2, N=1)
    got = _eval_at_q0(got_sym)
    assert abs(got - expected) < 1e-10, (
        f"helium-3 tr_M mismatch: peel={got!r} witness={expected!r}"
    )


@pytest.mark.slow
def test_tr_M_atomic_helium4_matches_peel_witness():
    """Z=2 N=2 — the headline target of #508 (A=4, n_strands=12).

    The Hoefsmit + Wenzl-bridge witness file (`atomic-tr-m-mpfr-50dps`)
    has no ⁴He entry — the historical compute path is infeasible at
    A=4 (~30+ min per atom).  This test cross-checks against
    `markov-peel-atomic-tr-m.witness.json`, the production witness
    generated by `markov_peel_atomic_witness.py` from the same
    recursive-ascent path that #508 / PR #516 added.

    A drift in this value either signals a regression in the
    Markov-peel pipeline or that the witness file is stale (re-run
    the generator).  When/if a third independent path computes ⁴He
    (e.g. via a future Lean MarkovPeel formalization with `decide`,
    or a Hoefsmit run on a beefier machine), promote this to a
    three-way cross-check.
    """
    expected = _load_peel_witness("helium-4")
    got_sym = tr_M_atomic(Z=2, N=2)
    got = _eval_at_q0(got_sym)
    assert abs(got - expected) < 1e-12, (
        f"helium-4 tr_M mismatch: peel={got!r} witness={expected!r}"
    )


# ── Manual run ──────────────────────────────────────────────────────

if __name__ == "__main__":
    import traceback
    tests = [
        ("crossing_element σ",     test_crossing_element_sigma),
        ("crossing_element σ⁻¹",   test_crossing_element_sigma_inv),
        ("crossing_element ½σ+½σ⁻¹", test_crossing_element_averaged),
        ("tr_M(1) = 1",            test_tr_M_identity_is_one),
        ("tr_M(σ_0) = z",          test_tr_M_single_sigma_is_z),
        ("tr_M(σ_0 σ_1) = z²",     test_tr_M_sigma_pair_is_z_squared),
        ("proton vs witness",      test_tr_M_atomic_proton_matches_witness),
        ("neutron vs witness",     test_tr_M_atomic_neutron_matches_witness),
        ("deuteron vs witness",    test_tr_M_atomic_deuteron_matches_witness),
    ]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
        except Exception:  # noqa: BLE001
            failed += 1
            print(f"  FAIL  {name}")
            traceback.print_exc()
    sys.exit(1 if failed else 0)
