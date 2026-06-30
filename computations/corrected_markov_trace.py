#!/usr/bin/env python3
"""Canonical Markov trace of the trefoil braid sigma_0 sigma_1 sigma_0 in H_3(q).

Settles the `corrected-markov-trace` cluster: the value is hz^2 + z (NOT z^3).
Computed two independent ways, both via the canonical `pyhecke` formal
Markov-Ocneanu-Wenzl engine (no hand-coded weights):

  1. directly:                tr_M(sigma0 sigma1 sigma0)
  2. via the recursion:       z * tr_M(sigma0^2),  z := tr_M(sigma0)

and checked against the two candidate closed forms hz^2+z and z^3, where
h = q - q^{-1} (q = s^2) is the Hecke parameter inferred from the engine's
own  g^2 = h g + 1  relation.

Emits computations/corrected-markov-trace.witness.json.
"""
from __future__ import annotations
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools", "pyhecke", "python"))

import sympy as sp  # noqa: E402
from pyhecke import trace_formal as tf  # noqa: E402


def main() -> int:
    def tr0(word):
        return sp.simplify(tf.nf_tr_formal(tf.nf_of_word_formal(word)))
    # Use the ENGINE's own symbol s (with its assumptions) so expressions cancel.
    z0 = tr0((0,))
    s = next(iter(z0.free_symbols))  # q = s^2
    h = s**2 - 1 / s**2  # q - q^{-1}, matches engine's inferred Hecke relation

    def tr(word):
        return sp.simplify(tf.nf_tr_formal(tf.nf_of_word_formal(word)))

    z = tr((0,))                 # tr_M(sigma_0)  (the Markov parameter)
    tr_g2 = tr((0, 0))           # tr_M(sigma_0^2)  = h z + 1
    T = tr((0, 1, 0))            # tr_M(sigma_0 sigma_1 sigma_0)

    cand_hz2_z = sp.simplify(h * z**2 + z)
    cand_z3 = sp.simplify(z**3)
    via_recursion = sp.simplify(z * tr_g2)

    eq_hz2_z = sp.cancel(T - cand_hz2_z) == 0
    eq_z3 = sp.cancel(T - cand_z3) == 0
    eq_recursion = sp.cancel(T - via_recursion) == 0
    hecke_ok = sp.cancel(tr_g2 - (h * z + 1)) == 0

    result = {
        "description": "Canonical Markov trace tr_M(sigma0 sigma1 sigma0) in H_3(q)",
        "engine": "pyhecke.trace_formal (formal Markov-Ocneanu-Wenzl, q = s^2)",
        "z_eq_tr_sigma": str(z),
        "tr_sigma_squared": str(tr_g2),
        "tr_trefoil": str(sp.simplify(T)),
        "candidate_hz2_plus_z": str(sp.cancel(cand_hz2_z)),
        "candidate_z3": str(cand_z3),
        "trefoil_equals_hz2_plus_z": bool(eq_hz2_z),
        "trefoil_equals_z3": bool(eq_z3),
        "trefoil_equals_z_times_tr_sigma_squared": bool(eq_recursion),
        "hecke_relation_g2_eq_hg_plus_1": bool(hecke_ok),
        "verdict": "tr_M(sigma0 sigma1 sigma0) = h z^2 + z  (z^3 is the invalid naive product)",
    }

    out = os.path.join(os.path.dirname(__file__), "corrected-markov-trace.witness.json")
    with open(out, "w") as fh:
        json.dump(result, fh, indent=2)
        fh.write("\n")

    for k, v in result.items():
        print(f"{k}: {v}")

    assert eq_hz2_z and eq_recursion and hecke_ok and not eq_z3, "engine disagrees with hz^2+z"
    print("\nOK: engine confirms tr_M = h z^2 + z, NOT z^3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
