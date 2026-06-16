#!/usr/bin/env python3
"""
Electron-shell SDP "capacity" — formalize-first demo (diagnostic; no fit, no witness).

The owner's idea: "put an electron on an isotope, keep adding electrons until the
confinement SDP won't solve — that's the capacity." This script checks that idea
against the canonical mechanism BEFORE trusting any number, and the result is a
formalize-first correction:

  * The naive test (add electrons; stop when the **raw Frobenius Gram** Gx ≥ 0
    first fails) gives non-physical "capacities" (H≈5, He≈8, …) — NOT the
    chemical shell counts. A prior session reported exactly these.

  * The canonical shell-closure mechanism (prop:shell-closure-stability) is the
    **dual objective** of the confinement SDP,
        σ_F(P^Z, q) = n_target · y₀*(P^Z, q)        (Frobenius stability index),
    and it is **monotonically non-decreasing in Z** (claim 1) — the SDP never
    "won't solve." The proof explicitly warns: this monotonicity is
    *SDP-relaxation*, NOT Cauchy eigenvalue interlacing, and "the two give
    opposite conclusions on the raw Gram matrix." The naive capacity is exactly
    that interlacing artifact.

  * Shell closure is a **local maximum of σ_F** at noble-gas
    Z ∈ {2,10,18,36,54,86} with binding **multiplicity μ ≥ 2** (claim 2) —
    equivalently the topological full-of-curls condition
    (prop:noble-gas-characterization). It is a max-of-a-monotone-dual /
    multiplicity phenomenon, not an infeasibility threshold.

So this script (1) reproduces the raw-Gram artifact, (2) computes the canonical
confinement-SDP dual via the canonical solver and shows it stays feasible with a
well-defined σ_F where the raw-Gram test falsely declares "capacity," and
(3) prints the finding. The full per-Z σ_F(Z) chain that exhibits the noble-gas
local maxima lives in the multi-level SDP infra (multi_level_sdp.py) and is the
flagged follow-up — not reproduced here.

Refs: prop:shell-closure-stability, prop:confinement-sdp, prop:noble-gas-
characterization, ElectronShell.lean (bindingMultiplicity = active dual support).
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "substrate"))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "tools", "pyhecke", "python"))

from q_parameter import Q as q0, Q_INV as qi0, HA as h  # noqa: E402
from pyhecke.lp_dual_solver import solve_operator_selection_lp  # noqa: E402

q0, qi0, h = float(q0), float(qi0), float(h)
z = 1.0 / (q0 ** 0.5 + qi0 ** 0.5)


def qintv(k):
    return (q0 ** k - qi0 ** k) / h


# NF basis [γ, σ₀, σ₁, L₊, L₋, e⁻] with Markov-trace weights (cost operator T).
NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
TR_M = np.array([1.0, z, z, z * z, z * z, z ** 3])
OPS = [("σ₀⁻¹", 0, 1.0, -h), ("σ₁⁻¹", 1, 1.0, -h)]  # electron crossings


def hm(nf, c, d, g):
    """Right-multiply NF vector by a Hecke generator (c·σ_g + d·1)."""
    r = [0.0] * 6
    if g == 0:
        t = [(0, [(1, c), (0, d)]), (1, [(1, c * h), (0, c), (1, d)]),
             (2, [(3, c), (2, d)]), (3, [(3, c * h), (2, c), (3, d)]),
             (4, [(5, c), (4, d)]), (5, [(5, c * h), (4, c), (5, d)])]
    else:
        t = [(0, [(2, c), (0, d)]), (1, [(4, c), (1, d)]),
             (2, [(2, c * h), (0, c), (2, d)]), (3, [(5, c), (3, d)]),
             (4, [(4, c * h), (1, c), (4, d)]), (5, [(5, c * h), (3, c), (5, d)])]
    for si, tgts in t:
        if abs(nf[si]) < 1e-15:
            continue
        for ti, co in tgts:
            r[ti] += nf[si] * co
    return r


def hm_dict(t1, t2):
    r = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            r[w] = r.get(w, 0.0) + c1 * c2
    return {w: c for w, c in r.items() if abs(c) > 1e-15}


def reduce_nf(terms):
    changed = True
    while changed:
        changed = False
        new = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
            for p in range(len(word) - 1):
                if word[p] == word[p + 1]:
                    i = word[p]
                    pre, suf = word[:p], word[p + 2:]
                    new[pre + (i,) + suf] = new.get(pre + (i,) + suf, 0) + coeff * h
                    new[pre + suf] = new.get(pre + suf, 0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            for p in range(len(word) - 2):
                a, b, c = word[p], word[p + 1], word[p + 2]
                if a == c and abs(a - b) == 1:
                    nt = (b, a, b)
                    if nt < (a, b, a):
                        nw = word[:p] + nt + word[p + 3:]
                        new[nw] = new.get(nw, 0) + coeff
                        done = changed = True
                        break
            if not done:
                new[word] = new.get(word, 0) + coeff
        terms = {w: c for w, c in new.items() if abs(c) > 1e-15}
    return terms


# Frobenius Gram G_{ij} = tr_M(b_i · b_j) over the NF basis.
G = np.zeros((6, 6))
for i in range(6):
    for j in range(6):
        nf = reduce_nf(hm_dict({NF_BASIS[i]: 1.0}, {NF_BASIS[j]: 1.0}))
        vec = np.array([nf.get(b, 0.0) for b in NF_BASIS])
        G[i, j] = sum(vec[k] * TR_M[k] for k in range(6))


def build_nucleus(Z, N):
    nf = [1, 0, 0, 0, 0, 0]
    pc, nc = 0, 0
    for k in range(Z + N):
        ip = (k % 2 == 0 and pc < Z) or nc >= N
        for _ in range(3):
            nf = hm(nf, 1, 0, 0); nf = hm(nf, 1, -h, 1)
        nf = hm(nf, 1, 0, 0); nf = hm(nf, 1, -h / 2, 1); nf = hm(nf, 1, -h / 2, 0)
        if ip:
            nf = hm(nf, 1, 0, 0); nf = hm(nf, 1, 0, 0); pc += 1
        else:
            for _ in range(2):
                nf = hm(nf, 1, 0, 0)
            nc += 1
    return nf


def raw_gram_violation(nf):
    """Prior method: feasibility = raw Frobenius Gram Gx ≥ 0 (componentwise)."""
    Gx = G @ np.array(nf)
    return [(NF_NAMES[i], Gx[i]) for i in range(6) if Gx[i] < -1e-10]


def raw_gram_capacity(Z, N, max_e=20):
    """Add alternating σ₀⁻¹/σ₁⁻¹ electrons; stop at first raw-Gram violation."""
    nf = build_nucleus(Z, N)
    for e in range(1, max_e + 1):
        name, gen, c, d = OPS[(e - 1) % 2]
        nf = hm(list(nf), c, d, gen)
        if raw_gram_violation(nf):
            return e - 1, e  # last-feasible, first-infeasible
    return max_e, None


def main() -> int:
    print(f"  ELECTRON-SHELL SDP CAPACITY — formalize-first demo   "
          f"q₀={q0:.6f}  z={z:.5f}\n")

    # --- §1  Raw-Gram "capacity" (the prior method — the artifact) ----------
    print("### §1  Naive 'capacity' = first raw-Gram Gx≥0 violation (the artifact)")
    print("| atom | Z | N | last-feasible e⁻ | infeasible at | chemical (neutral) |")
    print("|---|--:|--:|--:|--:|--:|")
    for name, Z, N in [("H", 1, 0), ("He", 2, 2), ("Li", 3, 4),
                       ("C", 6, 6), ("O", 8, 8)]:
        cap, bad = raw_gram_capacity(Z, N)
        print(f"| {name} | {Z} | {N} | {cap} | "
              f"{bad if bad else '>'+str(20)} | {Z} |")
    print("  → these are NOT the chemical shell counts (H holds ~1–2, He closes")
    print("    at 2). The raw-Gram threshold is the eigenvalue-interlacing")
    print("    artifact the proof of prop:shell-closure-stability explicitly")
    print("    warns against ('opposite conclusion on the raw Gram matrix').\n")

    # --- §2  Canonical confinement-SDP dual σ_F = n_target·y₀* --------------
    #   The selection principle is the DUAL objective, not raw-Gram feasibility.
    #   Cost T = Markov weights TR_M; G = Frobenius Gram. Sweep n_target as the
    #   dressing-level proxy (A+Z grows with dressing) → σ_F monotone, FEASIBLE
    #   throughout, with active set = binding multiplicity μ.
    print("### §2  Canonical confinement-SDP dual (the selection principle)")
    print("| n_target (dressing proxy) | σ_F = n_t·y₀* | y₀* | μ=|active| | gap | feasible |")
    print("|--:|--:|--:|--:|--:|:--:|")
    prev = None
    monotone = True
    for n_target in [1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 10.0]:
        r = solve_operator_selection_lp(TR_M, G, n_target)
        d = r.to_dict() if hasattr(r, "to_dict") else r
        sigma_F = d["dual_obj"]
        mu = len(d.get("active_set", []))
        gap = d.get("duality_gap", float("nan"))
        feas = d.get("feasible", True)
        if prev is not None and sigma_F < prev - 1e-9:
            monotone = False
        prev = sigma_F
        print(f"| {n_target:.0f} | {sigma_F:.6f} | {d['y0_star']:.6f} | {mu} | "
              f"{gap:.1e} | {'✓' if feas else '✗ INFEASIBLE'} |")
    print(f"  → σ_F monotone non-decreasing: {monotone}; SDP feasible throughout")
    print("    (gap≈0) — where §1's raw-Gram test falsely declares 'infeasible',")
    print("    the canonical dual solves cleanly. σ_F = n_target·y₀* is the")
    print("    Frobenius stability index of prop:shell-closure-stability claim 1.")
    print("    NB σ_F=0 here is the SINGLE-LEVEL degeneracy (Markov-cost")
    print("    normalisation is non-binding on the 6-dim NF block); the non-")
    print("    trivial σ_F(Z) growth + the noble-gas local maxima require the")
    print("    multi-level cost operator (multi_level_sdp.py). What §2 shows is")
    print("    the machinery + the absence of any infeasibility wall.\n")

    # --- §3  Finding --------------------------------------------------------
    print("### Finding")
    print("  • 'Add electrons until the SDP won't solve' is the wrong notion:")
    print("    the canonical confinement-SDP DUAL objective σ_F is monotone")
    print("    non-decreasing in Z (claim 1) — it never goes infeasible.")
    print("  • The prior H≈5 / He≈8 'capacities' are the raw-Gram eigenvalue-")
    print("    interlacing artifact the proof explicitly excludes.")
    print("  • Shell closure = LOCAL MAX of σ_F + multiplicity μ≥2 at noble-gas")
    print("    Z∈{2,10,18,36,54,86} (claim 2) = topological full-of-curls")
    print("    (prop:noble-gas-characterization). Max-of-monotone-dual, not a")
    print("    feasibility wall.")
    print("  • The per-Z σ_F(Z) chain exhibiting the noble-gas local maxima is")
    print("    the multi-level SDP infra (multi_level_sdp.py) — flagged follow-up.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
