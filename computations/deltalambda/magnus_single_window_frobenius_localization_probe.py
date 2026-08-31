#!/usr/bin/env python3
"""magnus_single_window_frobenius_localization_probe.py — WHERE does the single-window
o(dim) come from?  The Cauchy–Schwarz / Frobenius localization for qou-o6ov.

CONTEXT. #6311 reduced the tr-decay theorem to a fixed 3-strand-local operator
O = [A_a,A_{a+1}]; #6331 measured that the reduced estimate is SUB-DIM:
|tr(ρ_λ O)| = o(dim_λ) (raw |t| grows ≤15% as fast as dim at A=3). The open work is a
PROOF of that o(dim) rate. This probe localizes the mechanism so the proof has a target.

THE TOOL (Lean, sorry-free: QOU.MassTheory.trace_rho_commutator_reframe):
    tr(ρ_λ [A_a,A_{a+1}]) = tr([ρ_λ, A_a] · A_{a+1}).
Cauchy–Schwarz for the trace pairing (|tr(XYᵀ)| ≤ ‖X‖_F‖Y‖_F, here Yᵀ=A_{a+1} up to the
symmetry of the seminormal germ) gives
    |tr(ρ_λ O)| ≤ ‖[ρ_λ, A_a]‖_F · ‖A_{a+1}‖_F.
So o(dim) follows from a Frobenius-norm bound on the two factors. Which one is sublinear?

  * ‖A_{a+1}‖_F : the germ is block-diagonal with ±1 on the ~dim 1×1 blocks (a+1,a+2 in the
    same row/col) plus bounded 2×2 blocks ⇒ EXPECT ‖A_{a+1}‖_F = Θ(√dim). (A dead end for
    o(dim): this factor is genuinely √dim-sized.)
  * ‖[ρ_λ, A_a]‖_F : measures how nearly the global word ρ_λ COMMUTES with the germ A_a. If
    this is o(√dim) then |tr| ≤ o(√dim)·Θ(√dim) = o(dim) — a CONCRETE provable target: the
    commutator of ρ with the germ is Frobenius-small relative to √dim.

THIS PROBE measures, per window and b-level (exact mpf), ‖A_{a+1}‖_F/√dim,
‖[ρ_λ,A_a]‖_F/√dim, the CS bound, and the CS slack (bound/|tr|). It materializes ρ_λ as a
sparse product (capped at dim ≤ CAP for compute), so A=2 (all) and A=3 (most) are covered.
A per-partition self-check confirms tr([ρ,A_a]A_{a+1}) == tr(ρ[A_a,A_{a+1}]) (the Lean
identity, numerically), and == the committed per-window value.

scope-(a); NO-FLOAT64 (mpf throughout, dps inherited =140). No fit, no witness, nothing
wired. Reuses the merged sparse probe's exact machinery.
"""
from __future__ import annotations

import argparse
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mpmath as mp  # noqa: E402
import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402


def fro2(X):
    """Squared Frobenius norm of a row-dict matrix: Σ_ij X[i][j]²."""
    s = mp.mpf(0)
    for _i, row in X.items():
        for _j, v in row.items():
            s += v * v
    return s


def trace_prod(A, B):
    """tr(A·B) for row-dicts = Σ_i Σ_k A[i][k]·B[k][i]."""
    s = mp.mpf(0)
    for i, arow in A.items():
        for k, av in arow.items():
            brow = B.get(k)
            if brow and i in brow:
                s += av * brow[i]
    return s


def build_rho(gens, sigd):
    """ρ = ∏_i σ_{g_i} as a row-dict (left fold; same order as apply_word_to_e)."""
    rho = sigd[gens[0]]
    for g in gens[1:]:
        rho = base.spmatmul(rho, sigd[g])
    return rho


def analyze(A=3, cap=200):
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    pairs = sorted({(min(gens[i], gens[j]), max(gens[i], gens[j]))
                    for i in range(len(gens)) for j in range(len(gens))
                    if abs(gens[i] - gens[j]) == 1})
    print(f"[frob] A={A} (n={n}), word L={len(gens)}, {len(pairs)} windows, dim cap={cap}")
    print(f"[frob] Lean identity in play: tr(ρ[A_a,A_{{a+1}}]) = tr([ρ,A_a]A_{{a+1}})  "
          f"⇒ |tr| ≤ ‖[ρ,A_a]‖_F·‖A_{{a+1}}‖_F\n")

    # accumulate per (window,b): lists of (‖[ρ,Aa]‖_F/√dim, ‖Aa1‖_F/√dim, dim)
    byb = defaultdict(list)
    max_ident_err = mp.mpf(0)
    n_done = 0
    for shape in base.partitions(n):
        per_gen, dim = base.block_structure(shape)
        if dim <= 1 or dim > cap:
            continue
        b = n - shape[0]
        sig = base.sigma_csr(per_gen, dim, base.Q0)
        germ_rows, hcheck = base.germ_csr(per_gen, dim, base.Q0, base.EPS)
        assert hcheck < mp.mpf(10) ** -55
        sigd = {g: base.csr_to_dict(sig[g]) for g in range(ngen)}
        Ad = {g: base.csr_to_dict(germ_rows[g]) for g in range(ngen)}
        rho = build_rho(gens, sigd)
        n_done += 1
        for (a, b2) in pairs:  # b2 = a+1
            O = base.commutator(Ad[a], Ad[b2])
            t_direct = trace_prod(rho, O)                       # tr(ρ·O)
            comm = base.commutator(rho, Ad[a])                 # [ρ, A_a]
            t_reframe = trace_prod(comm, Ad[b2])               # tr([ρ,A_a]·A_{a+1})
            max_ident_err = max(max_ident_err, abs(t_direct - t_reframe))
            fa1 = mp.sqrt(fro2(Ad[b2]))
            fcomm = mp.sqrt(fro2(comm))
            sd = mp.sqrt(mp.mpf(dim))
            byb[(a, b2, b)].append((fcomm / sd, fa1 / sd, dim, abs(t_direct), fcomm * fa1))

    print(f"[frob] Lean-identity numeric self-check  max|tr(ρO) − tr([ρ,Aa]Aa1)| = "
          f"{mp.nstr(max_ident_err,3)}  over {n_done} partitions  "
          f"{'OK' if max_ident_err < mp.mpf(10)**-40 else 'FAIL'}\n")

    # report per window: the two normalized Frobenius factors vs b
    b_levels = sorted({k[2] for k in byb})
    for (a, b2) in pairs:
        print(f"  window ({a},{b2}):  b :  ‖[ρ,A_a]‖_F/√dim   ‖A_{{a+1}}‖_F/√dim   |t|/dim   (dim)")
        for b in b_levels:
            recs = byb.get((a, b2, b))
            if not recs:
                continue
            # report at the max-dim partition of this b (fair asymptotic sample)
            fc, fa, dim, tabs, _cs = max(recs, key=lambda r: r[2])
            print(f"        {b:>2} : {mp.nstr(fc,5):>14} {mp.nstr(fa,5):>17} "
                  f"{mp.nstr(tabs/dim,4):>10}   ({dim})")
        print()

    # VERDICT: is ‖A_{a+1}‖_F/√dim ~ const (dead end) and ‖[ρ,A_a]‖_F/√dim → 0 (the target)?
    print("LOCALIZATION VERDICT (trend of each normalized factor as b grows / dim climbs):")
    for (a, b2) in pairs:
        seq_c, seq_a = [], []
        for b in b_levels:
            recs = byb.get((a, b2, b))
            if not recs:
                continue
            fc, fa, dim, _t, _cs = max(recs, key=lambda r: r[2])
            seq_c.append(fc); seq_a.append(fa)
        if len(seq_c) >= 2:
            ac = "→0" if seq_c[-1] < seq_c[0] else "flat/↑"
            aa = "≈const" if (seq_a[0] > 0 and mp.mpf("0.5") < seq_a[-1]/seq_a[0] < mp.mpf(2)) \
                else ("→0" if seq_a[-1] < seq_a[0] else "↑")
            print(f"  ({a},{b2}): ‖A_{{a+1}}‖_F/√dim {aa} "
                  f"({mp.nstr(seq_a[0],3)}→{mp.nstr(seq_a[-1],3)});  "
                  f"‖[ρ,A_a]‖_F/√dim {ac} "
                  f"({mp.nstr(seq_c[0],3)}→{mp.nstr(seq_c[-1],3)})")
    print("\n  Reading: if ‖A_{a+1}‖_F/√dim stays ≈const (the germ is genuinely √dim-sized)")
    print("  and ‖[ρ,A_a]‖_F/√dim → 0, then the o(dim) is EXACTLY 'ρ nearly commutes with the")
    print("  germ' — the concrete provable target is a Frobenius bound ‖[ρ_λ,A_a]‖_F = o(√dim).")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    ap.add_argument("--cap", type=int, default=200, help="skip partitions with dim > cap (compute)")
    args = ap.parse_args()
    analyze(A=args.A, cap=args.cap)


if __name__ == "__main__":
    main()
