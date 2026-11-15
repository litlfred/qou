#!/usr/bin/env python3
"""gg_decay_probe.py — weak vertex W between two-orientation γγ nucleon candidates (pre-registered, 515ef592b8b).

Bean qou-a1hh, PR #7741. mpmath, convention D, proton q₀. Hypothesis only; nothing adopted, selected or wired.
-- Ref: [manuscript] bean qou-a1hh; bean qou-hlx7; bean qou-qs1x
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

import mpmath as mp
mp.mp.dps = max(mp.mp.dps, 40)  # the h2_one_rule base works at 40 dps; stated here so this
                                # probe does not rely on an import side effect two modules away

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
import h2_gg_atom_probe as ga  # noqa: E402

base, log = ga.base, ga.log
kct = base.kct
ONE, ZERO, H = base.ONE, base.ZERO, base.H
Q = base.Q
from qou_substrate.witness import WitnessBuilder  # noqa: E402

LET = {"V": [(ONE, ZERO, 0), (ONE, -H, 1)], "B": [(ONE, -H, 0), (ONE, ZERO, 1)]}
Q2 = Q + 1 / Q
TOLC = mp.mpf(10) ** -35  # base module works at 40 dps (h2_one_rule), not 70; checks sized to that


def word(p):
    return [t for c in p for t in LET[c]]


def inv(w):
    # tokens are σ_g (c=1,d=0) or σ_g⁻¹ = σ_g − h (c=1,d=−h)
    return [(ONE, ZERO if d != 0 else -H, g) for (c, d, g) in reversed(w)]


def W(g):
    return (2 / (Q * Q2), -H / (Q * Q2), g)


SHAPES = [tuple(l) for l in base.two_row(3)]


def mat(w, lam):
    dim = kct.cols(list(lam))[1]
    I = [[ONE if i == j else ZERO for j in range(dim)] for i in range(dim)]
    return kct.right_apply(I, w, list(lam))


def tau(w):
    return mp.fsum(base.y(lam) * mp.fsum(mat(w, lam)[i][i] for i in range(len(mat(w, lam)))) for lam in SHAPES)


def maxdiff(A, B):
    return max(abs(a - b) for ra, rb in zip(A, B) for a, b in zip(ra, rb))


def main() -> int:
    checks = {}
    # D0
    d0 = []
    for lam in SHAPES:
        for g in (0, 1):
            W2 = mat([W(g), W(g)], lam)
            dim = len(W2)
            target = [[(Q ** -2 if i == j else ZERO) for j in range(dim)] for i in range(dim)]
            d0.append(maxdiff(W2, target))
    checks["D0_W_squared_is_q^-2"] = max(d0) < TOLC
    # D1
    checks["D1_tau_one_is_1"] = abs(tau([]) - 1) < TOLC
    # D2: W built from -σ^{-1} equals -W
    d2 = []
    for lam in SHAPES:
        for g in (0, 1):
            # q⁻¹(2(−σ⁻¹) − h)/[2] = q⁻¹(−2σ + 2h − h)/[2]
            Wi = mat([(-2 / (Q * Q2), H / (Q * Q2), g)], lam)
            Wm = mat([W(g)], lam)
            d2.append(maxdiff(Wi, [[-x for x in r] for r in Wm]))
    checks["D2_iota_W_is_minus_W"] = max(d2) < TOLC
    for k, v in checks.items():
        log(f"[{'PASS' if v else 'FAIL'}] {k}")
    if not all(checks.values()):
        return 1
    N = ["".join(p) for p in itertools.product("VB", repeat=3)] + ["VVVVVV", "BBBBBB"]
    A = {}
    for n, p in itertools.product(N, N):
        for g in (0, 1):
            A[f"{n}->{p};g{g}"] = tau(inv(word(p)) + [W(g)] + word(n))
    asym = {}
    for n, p in itertools.combinations(N, 2):
        for g in (0, 1):
            asym[f"{n}|{p};g{g}"] = abs(A[f"{n}->{p};g{g}"]) - abs(A[f"{p}->{n};g{g}"])
    owner = {f"g{g}": {"V6->V3": mp.nstr(A[f'VVVVVV->VVV;g{g}'], 15), "V3->V6": mp.nstr(A[f'VVV->VVVVVV;g{g}'], 15)}
             for g in (0, 1)}
    nz = sorted(((k, v) for k, v in asym.items() if abs(v) > mp.mpf(10) ** -40), key=lambda kv: -abs(kv[1]))
    log(f"owner assignments: {owner}")
    log(f"{len(nz)} of {len(asym)} unordered pairs (x g) show |A| asymmetry; top: "
        f"{[(k, mp.nstr(v, 6)) for k, v in nz[:10]]}")
    for g in (0, 1):
        log(f"diagonal g{g}: " + ", ".join(f"{n}:{mp.nstr(A[f'{n}->{n};g{g}'], 8)}" for n in N))
    wb = WitnessBuilder("gg-decay", engine="mpmath", output_dir=HERE)
    for k, v in checks.items():
        wb.add_assertion(k, computed="1" if v else "0", expected="1", source="preregistration.md")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "via h2_gg_atom (cf.Q, proton pin)",
             "description": "PROBE (bean qou-a1hh, hypothesis): A(n->p;g)=tau(p^-1 W_g n), convention-D Markov trace "
                            "on H_3, W=q^-1(2sigma-h)/[2], nucleon candidates {V,Vbar}^3 + V^6, Vbar^6. "
                            "Pre-registered. Nothing adopted or wired.",
             "weight_family": "markov_y_lambda_convention_D", "candidates": N,
             "owner_assignments": owner,
             "A": {k: mp.nstr(v, 15) for k, v in A.items()},
             "asymmetry": {k: mp.nstr(v, 15) for k, v in asym.items()}})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
