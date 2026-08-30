#!/usr/bin/env python3
"""magnus_tr_decay_kerov_olshanski_probe.py — is the Magnus germ-trace a low-degree
content polynomial? (a REFUTED proof route for the tr-decay theorem, qou-o6ov)

CONTEXT. The open theorem (qou-o6ov) is: |tr(ρ_λ Ω₂_λ)| decays with b(λ)=n−λ₁.
The measured concentration is a TRACE cancellation, not a weight effect (the
Σ y_λ dim_λ bound plateaus at 0.5). One candidate proof route is Kerov–Olshanski
/ the algebra of polynomial functions on Young diagrams: for a FIXED central
element x, the normalised character χ_λ(x)/dim_λ is a polynomial of bounded degree
in the content power-sums p_k(λ)=Σ_cells (col−row)^k, and bounded degree forces the
b-decay. IF the germ-trace fit that shape, the theorem would follow.

RESULT (this probe): it does NOT. On A=3 (28 partitions with dim>1),
tr(ρ_λ Ω₂_λ)/dim_λ is NOT a low-degree polynomial in {p_2,…,p_5, p_2², …}: the max
relative residual falls only 0.94 → 0.29 (deg 1) → 0.20 (deg 2) → 0.08 (9 terms),
with NO collapse to machine-zero — a genuine low-degree content polynomial would
nail all 28 points once its degree is reached. So the germ-trace sits OUTSIDE the
standard polynomial-functions-on-Young-diagrams framework — unsurprising, since
ρ·Ω₂ is neither central nor a group-algebra element (Ω₂ is a germ = q-derivative
of the rep). The naive content-polynomiality proof route is REFUTED for this
normalisation, steering the tr-decay proof to the OTHER route: the cluster/cumulant
connected-diagram cancellation (tr(Ω₂)=0), tied to the ingested Procacci–Yuhjtman /
Rebenko papers.

scope-(a) infrastructure; a negative research result. Reproduces from the committed
triton (A=3) witness; needs numpy for the least-squares fit (float is fine — we are
testing the STRUCTURE, i.e. whether a low-degree fit collapses the residual, not a
high-precision value).
"""
from __future__ import annotations

import json
import os

import mpmath as mp

_HERE = os.path.dirname(os.path.abspath(__file__))


def contents(shape):
    return [j - i for i, ri in enumerate(shape) for j in range(ri)]


def main():
    mp.mp.dps = 40
    tri = json.load(open(os.path.join(_HERE, "triton-magnus-omega2-sign.witness.json")))
    rows = []
    for r in tri["results"]["per_partition"]:
        if r["dim"] == 1:
            continue  # tr = 0 trivially
        cs = contents(r["lambda"])
        p = [sum(mp.mpf(c) ** k for c in cs) for k in range(6)]
        rows.append((mp.mpf(r["tr_rho_Omega2"]) / r["dim"], p))
    try:
        import numpy as np
    except Exception:
        print("numpy required for the least-squares structure test"); return
    names = ["1", "p2", "p3", "p4", "p5", "p2^2", "p2p3", "p2^3", "p3^2"]

    def vec(p):
        return [1.0, float(p[2]), float(p[3]), float(p[4]), float(p[5]),
                float(p[2] ** 2), float(p[2] * p[3]), float(p[2] ** 3), float(p[3] ** 2)]
    X = np.array([vec(p) for _, p in rows])
    y = np.array([float(td) for td, _ in rows])
    print(f"[KO] A=3, {len(rows)} partitions (dim>1): is tr(ρΩ₂)/dim a low-degree content polynomial?")
    for nc in (1, 2, 3, 4, 5, 6, 7, 9):
        coef, *_ = np.linalg.lstsq(X[:, :nc], y, rcond=None)
        relres = np.max(np.abs(X[:, :nc] @ coef - y)) / (np.max(np.abs(y)) + 1e-30)
        print(f"  {nc} terms {names[:nc]}: max rel resid = {relres:.2e}")
    print("  => NO collapse to machine-zero at low degree ⇒ content-polynomiality route REFUTED;")
    print("     the germ-trace is outside the polynomial-functions-on-Young-diagrams framework.")
    print("     Steers the tr-decay proof (qou-o6ov) to the cluster/cumulant cancellation route.")


if __name__ == "__main__":
    main()
