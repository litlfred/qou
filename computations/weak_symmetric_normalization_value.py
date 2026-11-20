#!/usr/bin/env python3
"""Evaluate prop:weak-symmetric-normalization's closed form.

    N_sym(q) = (q^4 + q^6 + q^8) / 3 = q^4 (1 + q^2 + q^4) / 3

The block states this polynomial and its factored form as unconditional
algebra. This producer checks the factorisation exactly (sympy) and
evaluates the polynomial at the proton-pinned q_0 (experimental anchor,
AGENTS.md owner directive 2026-08-07) in mpmath, end to end.

It does NOT compute the G_F-back-solved target 213.11; that lives in
`n_sym_numerical_anchor.py` and is a different quantity (see the
block's .md and `conj:g-action-on-substrate`). No number here is
compared to experiment.

# Ref: folio/quantum-observable-universe/mass-theory/weak-symmetric-normalization.md
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at  # noqa: E402  (proton pin)
from witness_base import WitnessBuilder  # noqa: E402


def symbolic_check() -> bool:
    """Exact check that (q^4+q^6+q^8)/3 == q^4(1+q^2+q^4)/3."""
    q = sp.symbols("q")
    lhs = (q**4 + q**6 + q**8) / 3
    rhs = q**4 * (1 + q**2 + q**4) / 3
    return sp.simplify(lhs - rhs) == 0


def n_sym(q: mp.mpf) -> mp.mpf:
    return (q**4 + q**6 + q**8) / 3


def main() -> int:
    set_compute_dps(70)
    q0 = mp.mpf(q_at(70))
    val = n_sym(q0)
    factored = q0**4 * (1 + q0**2 + q0**4) / 3
    resid = abs(val - factored)
    sym_ok = symbolic_check()

    print(f"q_0 (proton pin) = {mp.nstr(q0, 30)}")
    print(f"N_sym(q_0) = (q^4+q^6+q^8)/3 = {mp.nstr(val, 30)}")
    print(f"factored-form residual = {mp.nstr(resid, 5)}")
    print(f"symbolic factorisation exact: {sym_ok}")

    wb = WitnessBuilder("weak-symmetric-normalization-value", engine="mpmath")
    wb.data["block"] = "prop:weak-symmetric-normalization"
    wb.data["q0_anchor"] = "proton"
    wb.data["q0"] = fmt(q0)
    wb.data["formula"] = "(q^4 + q^6 + q^8)/3"
    wb.data["n_sym_at_q0"] = fmt(val)
    wb.data["factored_form_residual"] = fmt(resid)
    wb.data["symbolic_factorisation_exact"] = sym_ok
    wb.data["scope"] = (
        "Evaluates the stated polynomial only. Its reading as the electroweak "
        "symmetric-channel weight rests on open premises "
        "(prop:weak-spectral-completeness, conj:electroweak-higgs-torus-link-triplet). "
        "Not the G_F-back-solved 213.11 of n_sym_numerical_anchor.py.")
    wb.add_assertion("symbolic_factorisation_exact",
                     computed=1 if sym_ok else 0, expected=1, tolerance=0)
    wb.add_assertion("factored_form_agrees_at_q0",
                     computed=1 if resid < mp.mpf(10) ** -60 else 0,
                     expected=1, tolerance=0)
    wb.save()
    return 0 if sym_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
