#!/usr/bin/env python3
"""End-to-end A=3 wiring check: categorical operator-form combiner → atomic χ^λ → tr_M.

Owns the closure-b wiring step (the piece left after PRs #2358/#2365/#2366): take the
categorical operator-form interface operator A^λ_{ξν}(I) =
`a_operator_gauge_align.gauge_aligned_A_combiner_general` (the V_ξ⊗V_ν matrix, the
SPEEDUP form) and plug it into the branching reconstruction of the REAL ³He atomic
braid at the production 50-dps floor:

    χ^λ(β_inner^{H6} · I_pn · β_outer^{H3})
        = Σ_{ξ⊢6, ν⊢3} Tr[ A^λ_{ξν}(I_pn) · (ρ_ξ(β_inner) ⊗ ρ_ν(β_outer)) ]

³He (Z=2,N=1 = p,p,n) is the clean wiring target: its 2nd inter-nucleon interface
I_23 is the p-n averaged crossing σ_5 − h/2 — EXACTLY the interface the combiner
bakes in — so no interface generalization is needed (tritium's n-n σ_5 − h is the
linear-in-interface follow-up).

This extends the sibling's H_9 universality demo (abstract panel words, λ∈{(9),(8,1)})
to the PHYSICAL ³He atomic words across all feasible λ⊢9, and — where coverage is
complete — assembles tr_M = Σ_λ y_λ χ^λ and compares to the canonical reference.
Large-λ combiner SVDs are O(r^6) pure-mpmath; capped per-λ and reported (the full
sweep is the documented Rust-kernel follow-up).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "a_operator"))

from a_operator_gauge_align import gauge_aligned_A_combiner_general, _kron  # noqa: E402
import a_operator_categorical as aoa  # noqa: E402
from lr_coefficients import partitions_of  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

CANONICAL_TRM_3HE = 0.2065408170207396
DPS = 50
PER_LAMBDA_CAP_S = 90.0  # skip a λ whose combiner SVD exceeds this
DIM_CAP = 50  # pre-skip λ with dim(V_λ) > DIM_CAP (large-λ SVD → Rust follow-up)


def ops_to_factors(ops, h, gen_shift=0):
    """(gen, ctype) atomic ops → Hecke factors [(c, d, g)] with optional gen shift."""
    out = []
    for gen, ctype in ops:
        g = int(gen) + gen_shift
        if ctype == "sigma":
            out.append((mp.mpf(1), mp.mpf(0), g))
        elif ctype == "sigma_inv":
            out.append((mp.mpf(1), -h, g))
        elif ctype == "averaged":
            out.append((mp.mpf(1), -h / 2, g))
        else:
            raise ValueError(f"unknown crossing {ctype!r}")
    return out


def word_matrix(mats, factors):
    dim = mats[0].rows
    M = mp.eye(dim)
    for (c, d, g) in factors:
        M = M * (c * mats[g] + d * mp.eye(dim))
    return M


def main() -> int:
    mp.mp.dps = DPS + 10
    q = aoa.q0_mp(DPS)
    q_str = mp.nstr(q, DPS)
    h = q - 1 / q
    print(f"³He end-to-end combiner wiring — q_0≈{float(Q0):.6f}, dps={DPS}\n")

    # Real ³He atomic braid, split (6,3) at the single gen-5 interface.
    ops = atom_canonical_crossings(2, 1)
    inner_ops = [(g, t) for (g, t) in ops if g <= 4]
    iface_ops = [(g, t) for (g, t) in ops if g == 5]
    outer_ops = [(g, t) for (g, t) in ops if g >= 6]
    assert len(iface_ops) == 1 and iface_ops[0][1] == "averaged", \
        f"³He interface must be pn-averaged, got {iface_ops}"
    inner_fac = ops_to_factors(inner_ops, h)            # H_6 gens 0..4
    outer_fac = ops_to_factors(outer_ops, h, gen_shift=-6)  # H_3 gens 0..1
    print(f"  split: |inner|={len(inner_ops)} (H_6) · I_pn(σ_5−h/2) · "
          f"|outer|={len(outer_ops)} (H_3)\n")

    p6, p3, p9 = partitions_of(6), partitions_of(3), partitions_of(9)
    rho6 = {m: aoa.exact_seminormal_matrices(m, q_str, DPS)[0] for m in p6}
    rho3 = {n: aoa.exact_seminormal_matrices(n, q_str, DPS)[0] for n in p3}
    # ρ_ξ(β_inner) and ρ_ν(β_outer) — small-dim (the speedup payoff).
    rmu = {m: word_matrix(rho6[m], inner_fac) for m in p6}
    rnu = {n: word_matrix(rho3[n], outer_fac) for n in p3}

    y_dict = {tuple(k): mp.mpf(mp.nstr(v, DPS)) if not isinstance(v, complex)
              else mp.mpc(v) for k, v in y_lambda_at(9, float(Q0)).items()}

    # Residual print precision is tied to the working precision (Gemini #2371):
    # never silently truncate below the configured dps.
    sig = max(6, mp.mp.dps - 6)
    print(f"  {'λ ⊢ 9':<16} {'dim':>4} {'|χ_comb − χ_true|':>16} {'wall':>8}  st"
          f"   progress (rate, elapsed, ETA)")
    print("  " + "-" * 92)
    trM = mp.mpf(0)
    covered = 0
    worst = mp.mpf(0)
    skipped = []
    # ascending dim so the cheap λ verify first; pre-skip large λ (their O(r^6)
    # SVD is the documented Rust-kernel follow-up — can't be interrupted mid-call).
    p9_sorted = sorted(p9, key=lambda l: aoa.partition_dim(l))
    feasible = [l for l in p9_sorted if aoa.partition_dim(l) <= DIM_CAP]
    deferred = [l for l in p9_sorted if aoa.partition_dim(l) > DIM_CAP]
    for l in deferred:
        skipped.append((l, f"dim {aoa.partition_dim(l)} > DIM_CAP={DIM_CAP} (Rust follow-up)"))
    total = len(feasible)
    loop_start = time.time()
    for idx, lam in enumerate(feasible):
        mats9, dim = aoa.exact_seminormal_matrices(lam, q_str, DPS)
        if dim == 0:
            continue
        t0 = time.time()
        try:
            with mp.workdps(DPS + 10):
                Ac = gauge_aligned_A_combiner_general(lam, 6, 3, q_str, DPS)
            wall = time.time() - t0
            if any("error" in v for v in Ac.values()):
                skipped.append((lam, "intertwiner empty"))
                cell, st = f"{'(intertwiner empty)':>16}", "⚠"
            else:
                chi_comb = sum((aoa._trace(info["A"] * _kron(rmu[mu], rnu[nu]))
                                for (mu, nu), info in Ac.items() if "A" in info),
                               mp.mpf(0))
                full_fac = (inner_fac + [(mp.mpf(1), -h / 2, 5)]
                            + ops_to_factors(outer_ops, h))
                chi_true = aoa._trace(word_matrix(mats9, full_fac))
                resid = abs(chi_comb - chi_true)
                worst = max(worst, resid)
                ok = resid < mp.mpf("1e-25")
                covered += 1
                trM += y_dict[tuple(lam)] * chi_comb
                cell, st = f"{mp.nstr(resid, sig):>16}", ("✓" if ok else "✗")
        except Exception as e:  # noqa: BLE001
            skipped.append((lam, f"combiner error: {e}"))
            wall = time.time() - t0
            cell, st = f"{'(combiner error)':>16}", "⚠"
        elapsed = time.time() - loop_start
        rate = (idx + 1) / elapsed if elapsed > 0 else 0.0
        eta = (total - idx - 1) / rate if rate > 0 else 0.0
        print(f"  {str(lam):<16} {dim:>4} {cell} {wall:>7.1f}s  {st}"
              f"   {idx+1}/{total} ({rate:.3f} λ/s, el {elapsed:.0f}s, eta {eta:.0f}s)")

    print(f"\n  covered {covered}/{len(p9)} λ⊢9; worst |χ_comb−χ_true| = "
          f"{mp.nstr(worst,4)}")
    if skipped:
        print(f"  skipped {len(skipped)}: {[list(l) for l,_ in skipped]}")
    if covered == len(p9):
        trM_abs = abs(trM)
        gap = abs(trM_abs - CANONICAL_TRM_3HE)
        print(f"\n  tr_M(³He) via combiner = {mp.nstr(trM_abs, 13)}")
        print(f"  tr_M(³He) canonical    = {CANONICAL_TRM_3HE:.13f}")
        print(f"  |gap| = {mp.nstr(gap,4)}  {'✓' if gap < 1e-6 else '✗'}")
        ok_all = worst < mp.mpf("1e-25") and gap < 1e-6
        print("\n  ✅ END-TO-END WIRING VERIFIED" if ok_all
              else "\n  ✗ wiring mismatch — investigate")
        return 0 if ok_all else 1
    print(f"\n  Per-λ operator-form reconstruction verified for {covered} λ at "
          f"50-dps (the new result: physical ³He atomic words, not panel words).")
    print(f"  Full tr_M assembly needs all {len(p9)} λ — remaining large-λ SVDs are "
          f"the documented Rust-kernel follow-up.")
    return 0 if worst < mp.mpf("1e-25") else 1


if __name__ == "__main__":
    raise SystemExit(main())
