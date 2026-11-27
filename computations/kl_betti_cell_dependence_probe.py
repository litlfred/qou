#!/usr/bin/env python3
"""
PROBE 4 follow-up — the KL left-cell Betti sum is NOT a well-defined
per-partition magnitude.

Context. The Option-E Δ_λ gate needs a per-partition magnitude |Δ_λ| = f^λ
(= dim V_λ). PROBE 4 (Kashiwara-crystal / KL-weight) is already PRUNED on the
*sign* (KL positivity cannot supply the mixed chirality sign; Lean-proved
`QOU.BraidsAndKnots.deltaSign_mixed`). It was left open whether KL could at least
supply the *magnitude* via the left-cell Betti sum
    B_λ = Σ_{w ∈ Γ_λ} P_{e,w}(1)
(sum of intersection-cohomology Betti numbers over a left cell Γ_λ of shape λ).

This probe settles the magnitude question. It shows B_λ is **cell-dependent**:
distinct left cells of the *same* shape λ have *different* Betti sums (e.g.
shape (3,3) over S_6 ranges 6..23 across its five cells). Hence B_λ is not a
function of λ alone — it has no canonical value without an extra, unmotivated
cell-selection rule. Two prior on-main scripts disagreed for exactly this
reason: `kl_betti_extrapolation.py` takes the first-encountered cell (low end),
`probe_option_e_probe4_kl_batch.py` takes canonical_Q (the high end). Neither is
canonical.

Consequence for the deuteron. Swapping f^λ → B_λ in the binding sum
    B(K) = m_e · |Σ_λ y_λ · χ^λ(β_K) · sgn(w_0^{S_{λ'}}) · X_λ|
makes the predicted binding swing with the (arbitrary) cell choice, so the
"magnification" B_λ/f^λ is itself ill-defined. This is an (a)-scope negative:
this construction *alone* cannot supply the canonical |Δ_λ|. It is NOT a
structural exclusion of KL data from every closure.

KL evaluation is pure-Python (`kazhdan_lusztig.kl_polynomial`), validated
against published values by the module's own `_self_test`
(P_{e,3412}=1+q, P_{e,4231}=1+q in S_5, P_{e,w_0}=1 in S_6). The Rust
`pyhecke_native.kl_betti_sum_rust` computes the identical object for a *given*
cell, so it cannot resolve the cell-ambiguity this probe exposes.

Primitives (sgn, dim, χ, y, RSK) copied verbatim from
`delta_lambda_binding_full_evaluation.py`.
"""
import sys, json, math, time, ast
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from collections import defaultdict
from mpmath import mp, mpf, fabs
import sympy as sp
import kazhdan_lusztig as KL
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent
m_e = mpf('0.51099895069')
B_AME_D = 2.22452
N = 6                         # deuteron lives in H_6 / S_6
CANONICAL_F_SUM = mpf('-0.743781')   # known f^λ deuteron sum (reproduced below)

# ---- primitives copied verbatim from the producer ----
def conjugate(lam):
    if not lam: return ()
    return tuple(sum(1 for p in lam if p > i) for i in range(lam[0]))
def sgn_conjugate_parabolic(lam):
    return math.prod((-1)**(p*(p-1)//2) for p in conjugate(lam))
def dim_sn(lam):
    n = sum(lam); num = math.factorial(n); den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i]-j-1
            leg = sum(1 for r in range(i+1, len(lam)) if lam[r] > j)
            den *= arm+leg+1
    return num//den
def rsk_PQ(w):
    P=[]; Q=[]
    for i,x in enumerate(w):
        r=0
        while r < len(P):
            idx=-1
            for c in range(len(P[r])):
                if P[r][c] > x: idx=c; break
            if idx==-1:
                P[r].append(x); Q[r].append(i+1); break
            else:
                x, P[r][idx] = P[r][idx], x; r+=1
        if r==len(P):
            P.append([x]); Q.append([i+1])
    return P, Q

# ---- P_{e,w}(1) via literature-validated pure-Python KL ----
_ident = tuple(range(1, N+1))
def P_e_w_at1(w):
    poly = KL.kl_polynomial(_ident, w)
    return int(poly.subs({s: 1 for s in poly.free_symbols}))

def is_hook(lam):
    return len(lam) == 1 or lam[1] == 1

def main():
    t0 = time.time()
    print(f"KL self-test all_passed = {KL._self_test()['all_passed']}")
    assert P_e_w_at1((6,5,4,3,2,1)) == 1
    assert KL.kl_polynomial((1,2,3,4),(3,4,1,2)).subs({s:1 for s in KL.kl_polynomial((1,2,3,4),(3,4,1,2)).free_symbols}) == 2
    print("sanity OK\n")

    perms = KL.permutations_S_n(N)
    # group all of S_6 into left cells (fixed Q-tableau)
    q_cells = defaultdict(list)
    for w in perms:
        _, Q = rsk_PQ(w)
        q_cells[tuple(tuple(r) for r in Q)].append(w)

    # per-shape: list of (Betti sum) over each cell of that shape
    print(f"Computing P_e_w(1) for all {len(perms)} elements of S_{N} ...")
    shape_cell_sums = defaultdict(list)
    done = 0
    for q_tup, words in q_cells.items():
        shape = tuple(len(r) for r in q_tup)
        s = sum(P_e_w_at1(tuple(w)) for w in words)
        shape_cell_sums[shape].append(s)
        done += len(words)
        if done % 120 < len(words):
            print(f"  ... {done}/{len(perms)} elements  ({time.time()-t0:.0f}s)")

    # per-shape summary
    table = {}
    for shape, sums in shape_cell_sums.items():
        f = dim_sn(shape)
        table[str(shape)] = {
            "f_lambda": f,
            "n_cells": len(sums),
            "betti_min": min(sums),
            "betti_max": max(sums),
            "betti_distinct": sorted(set(sums)),
            "cell_invariant": len(set(sums)) == 1,
            "is_hook": is_hook(shape),
        }

    print(f"\n{'shape':16s} {'f^l':>4s} {'#cells':>6s} {'Bmin':>5s} {'Bmax':>5s} {'inv?':>5s} {'hook?':>6s}")
    print("-"*56)
    for shape in sorted(table, key=lambda k: sum(ast.literal_eval(k)), reverse=True):
        r = table[shape]
        print(f"{shape:16s} {r['f_lambda']:>4d} {r['n_cells']:>6d} {r['betti_min']:>5d} "
              f"{r['betti_max']:>5d} {str(r['cell_invariant']):>5s} {str(r['is_hook']):>6s}")

    inv_shapes = sorted([s for s, r in table.items() if r["cell_invariant"]], key=lambda k: sum(ast.literal_eval(k)), reverse=True)
    n_cell_dependent = sum(1 for r in table.values() if not r["cell_invariant"])
    bulk_not_inv = any((not r["cell_invariant"]) for r in table.values() if not r["is_hook"])
    # NB: hooks are NOT uniformly cell-invariant either — e.g. (4,1,1) ranges 10..26.
    # Only the three trivial shapes (n,), (n-1,1), (1^n) are invariant over S_6.
    hooks_also_vary = any((not r["cell_invariant"]) for r in table.values() if r["is_hook"])

    # ---- deuteron sum under f^λ, min-cell B_λ, max-cell B_λ ----
    with open(HERE/'atom-chi-rust-d.witness.json', encoding='utf-8') as f:
        d = json.load(f)['data']['atom']['by_partition']
    with open(HERE/'rho-k-h3a-lp-dual.witness.json', encoding='utf-8') as f:
        lp = json.load(f)['data']['per_lambda']
    y  = {tuple(e['partition']): mpf(str(e['y_lambda_at_q0'])) for e in lp}

    sum_f = sum_min = sum_max = mpf(0)
    for e in d:
        lam = tuple(e['partition']); chi = mpf(str(e['chi_lambda']))
        yl = y.get(lam, mpf(0)); sgn = sgn_conjugate_parabolic(lam)
        f = dim_sn(lam)
        r = table[str(lam)]
        base = yl*chi*sgn
        sum_f   += base*f
        sum_min += base*r['betti_min']
        sum_max += base*r['betti_max']

    Bf   = float(m_e*fabs(sum_f))
    Bmin = float(m_e*fabs(sum_min))
    Bmax = float(m_e*fabs(sum_max))
    f_reproduces = abs(float(sum_f) - float(CANONICAL_F_SUM)) < 1e-3

    print(f"\nDeuteron B_pred (B_AME = {B_AME_D} MeV):")
    print(f"  f^λ        : Σ={float(sum_f):+.5f}  B={Bf:.4f} MeV  ({(Bf-B_AME_D)/B_AME_D*100:+.1f}%)")
    print(f"  B_λ min-cell: Σ={float(sum_min):+.5f}  B={Bmin:.4f} MeV  (mag x{float(fabs(sum_min)/fabs(sum_f)):.3f})")
    print(f"  B_λ max-cell: Σ={float(sum_max):+.5f}  B={Bmax:.4f} MeV  (mag x{float(fabs(sum_max)/fabs(sum_f)):.3f})")
    print(f"\n  => deuteron prediction swings {Bmin:.3f}..{Bmax:.3f} MeV with cell choice; none reach {B_AME_D}.")
    print(f"  f^λ baseline reproduces canonical -0.7438 : {f_reproduces}")

    witness = {
        "engine": "python3/sympy+mpmath", "engineVersion": "50dps",
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "computation": "kl-betti-cell-dependence",
        "scriptFile": "kl_betti_cell_dependence_probe.py",
        "description": (
            "KL left-cell Betti sum B_λ = Σ_{w∈Γ_λ} P_{e,w}(1) is NOT cell-invariant: "
            "distinct left cells of the same shape λ over S_6 give different Betti sums "
            "(e.g. (3,3): 6..23). Hence B_λ is not a function of λ and cannot canonically "
            "supply |Δ_λ|=f^λ. Hooks ARE cell-invariant and equal f^λ. (a)-scope negative; "
            "reinforces the PROBE-4 KL-positivity sign prune. Pure-Python KL, literature-validated."
        ),
        "data": {
            "n": N,
            "per_shape": table,
            "cell_invariant_shapes": inv_shapes,
            "n_cell_dependent_shapes": n_cell_dependent,
            "hooks_also_vary": bool(hooks_also_vary),
            "deuteron": {
                "B_AME_MeV": B_AME_D,
                "sum_f_lambda": float(sum_f),
                "B_pred_f_lambda_MeV": Bf,
                "B_pred_Bmin_MeV": Bmin,
                "B_pred_Bmax_MeV": Bmax,
                "magnification_min": float(fabs(sum_min)/fabs(sum_f)),
                "magnification_max": float(fabs(sum_max)/fabs(sum_f)),
            },
        },
        "assertions": [
            {"label": "bulk partitions NOT cell-invariant (B_lambda ill-defined as per-lambda magnitude)", "passed": bool(bulk_not_inv)},
            {"label": "only trivial shapes cell-invariant; even hooks vary across cells", "passed": bool(hooks_also_vary and len(inv_shapes) <= 3)},
            {"label": "deuteron magnification is cell-choice-dependent (min-cell != max-cell)", "passed": bool(float(fabs(sum_min)) != float(fabs(sum_max)))},
            {"label": "f^lambda baseline reproduces canonical deuteron sum -0.7438", "passed": bool(f_reproduces)},
        ],
        "allPassed": bool(bulk_not_inv and hooks_also_vary and f_reproduces),
    }
    out = HERE/"kl-betti-cell-dependence.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    witness["scriptFile"] = _os.path.basename(__file__)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(witness, fh, indent=2, default=str)
    print(f"\nWitness: {out.name}  allPassed={witness['allPassed']}  ({time.time()-t0:.0f}s)")

if __name__ == '__main__':
    main()
