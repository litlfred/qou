#!/usr/bin/env python3
"""d1a_functional_arm — the #7876 elements read with the D1 = A functional (bean qou-ggls).

NOT pre-registered. A diagnostic arm written 2026-11-21 to reconcile PR #7876 with the owner
ruling D1 = A (2026-11-20, bean qou-99qc): the scored Q_β is |ε_flavour(V³)|·E₀^tower, where

    ε_flavour(X_p, X_n) = ( q⁻¹·tr_{W_n}(X_n) − q·tr_{W_p}(X_p) ) / [2]³

is the T³ weight split of the z_D trace Tr(K^{⊗3}·)/[2]³ (docs/audits/2026-11-20-qbeta-flavour-
weight-split.md). #7876 scored its elements CORE·TAIL_x·Vᵏ with a different functional, the
Markov-trace difference |τ_zD(X_n) − τ_zD(X_p)|·E₀. This script evaluates the same four elements
with ε_flavour, so the two readings sit side by side. Nothing is selected and nothing is scored.

Representation: the 3-dim weight spaces of NucleonWeightSpaceTraces.lean, copied from
probes/qbeta_flavour_weight_split (σ₀ ↦ A1, σ₁ ↦ A2 on W_p; σ₀ ↦ A2, σ₁ ↦ A1 on W_n). A letter
(c, d, g) of gg_gluon_segment_probe is c·σ_g + d (σ⁻¹ = σ − h, averaged letter = σ − h/2).

Calibration (must pass before any other line is read): X_p = X_n = V³ reproduces the scorecard's
D1 = A cell `data.qbeta_ruled_base.Q_beta_MeV` to 1e-25.

Exact sympy over Q(q); proton q₀ as an exact rational; mpmath 70 dps for display. E₀ =
qbeta_e0.canonical() (tower-summed). Writes no witness.
"""
from __future__ import annotations

import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
for _p in ("computations", "computations/qbeta", "computations/substrate", "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

import qbeta_e0  # noqa: E402
from codata_constants import Q_BETA_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 70
q = sp.symbols("q", positive=True)
h = q - 1 / q
D2 = q + 1 / q
Q0 = sp.Rational(Q_50_DIGIT_STR)

A1 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])
A2 = sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])
GEN = {"p": {0: A1, 1: A2}, "n": {0: A2, 1: A1}}

U = lambda g: (1, 0, g)
Dn = lambda g: (1, -h, g)
UD = lambda g: (1, -h / 2, g)
V = [U(0), Dn(1)]
CORE = V * 3
TAIL = {"p": [U(0), UD(0), UD(1)], "n": [UD(0), UD(0), Dn(1)]}


def trW(x, letters):
    M = sp.eye(3)
    for c, d, g in letters:
        M = M * (c * GEN[x][g] + d * sp.eye(3))
    return sp.together(M.trace())


def eps_flavour(Xp, Xn):
    return sp.factor(sp.together((trW("n", Xn) / q - q * trW("p", Xp)) / D2 ** 3))


def at_q0(e):
    v = sp.Rational(sp.simplify(sp.sympify(e).subs(q, Q0)))
    return mp.mpf(int(v.p)) / mp.mpf(int(v.q))


def main() -> int:
    E0 = qbeta_e0.canonical()
    codata = mp.mpf(str(Q_BETA_MEV))
    with open(os.path.join(ROOT, "computations/per-observable-100x-status.witness.json")) as fh:
        ref = mp.mpf(str(json.load(fh)["data"]["qbeta_ruled_base"]["Q_beta_MeV"]))
    cal = abs(at_q0(eps_flavour(V * 3, V * 3))) * E0
    ok = abs(cal - ref) < mp.mpf("1e-25")
    print(f"[{'PASS' if ok else 'FAIL'}] calibration: |eps_flavour(V^3)|*E0 = {mp.nstr(cal, 15)}"
          f" vs scorecard {mp.nstr(ref, 15)}")
    if not ok:
        return 1
    print("\n| element | eps_flavour at q0 | Q_beta (MeV) | vs CODATA | same element for p and n |")
    print("|---|---|---|---|---|")
    rows = [("V^3 (D1 = A scored)", V * 3, V * 3)]
    rows += [(f"CORE.TAIL.V^{k}", CORE + TAIL["p"] + V * k, CORE + TAIL["n"] + V * k) for k in range(4)]
    for name, Xp, Xn in rows:
        e = at_q0(eps_flavour(Xp, Xn))
        qb = abs(e) * E0
        pct = (qb - codata) / codata * 100
        print(f"| {name} | {mp.nstr(e, 12)} | {mp.nstr(qb, 12)} | {mp.nstr(pct, 8)} % | {Xp == Xn} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
