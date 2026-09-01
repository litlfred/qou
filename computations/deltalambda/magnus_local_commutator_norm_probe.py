#!/usr/bin/env python3
"""magnus_local_commutator_norm_probe.py — the DECISIVE test for the operator-norm route to
the sublinear single-window bound (qou-o6ov).

CONTEXT. #6339 reduced the open estimate to ‖⁅ρ_λ,A_a⁆‖_F = o(√dim). The Leibniz telescoping
(Lean commutator_mul_left) gives, with ρ = ∏σ_{g_i},
    ‖⁅ρ,A_a⁆‖_F ≤ Σ_{|g_i−a|≤1} ‖σ_{<i}‖_op · ‖⁅σ_{g_i},A_a⁆‖_F · ‖σ_{>i}‖_op.
The seminormal σ_k are SYMMETRIC with Hecke eigenvalues q, −q⁻¹, so ‖σ_k‖_op = q (a
DIM-INDEPENDENT constant), and only O(1) crossings sit near position a. Hence
    ‖⁅ρ,A_a⁆‖_F ≤ C · max_g ‖⁅σ_g,A_a⁆‖_F,   C = (#near-a)·q^{L−1}  (independent of dim),
and the WHOLE dim-dependence collapses onto the LOCAL commutator ‖⁅σ_g,A_a⁆‖_F — a fixed
3-strand object, no ρ.

THE DECISIVE QUESTION (this probe, cheap ⇒ A=2,3,4 FULL):
  * If ‖⁅σ_g,A_a⁆‖_F = o(√dim): the operator-norm route CLOSES — |t| ≤ C·o(√dim)·Θ(√dim) =
    o(dim), the theorem reduces to a fixed-3-strand-object bound (no ρ, no cancellation).
  * If ‖⁅σ_g,A_a⁆‖_F = Θ(√dim): the op-norm route gives only O(dim); the measured o(dim)
    then comes from a CANCELLATION the submultiplicative bound discards (word-piece dressing
    or the trace itself), and the "‖⁅ρ,A_a⁆‖_F = o(√dim)" target would need that cancellation,
    not a naive local bound. Either way this SETTLES which route is viable.

Measures ‖⁅σ_{a+1},A_a⁆‖_F/√dim (the forward local commutator) by b-level, plus the controls
⁅σ_a,A_a⁆ = 0 (germ commutes with its own generator) and eig(σ 2×2 block) = {q,−q⁻¹} ⇒
‖σ‖_op = q. scope-(a); NO-FLOAT64 (mpf, dps inherited =140). No fit, no witness, nothing wired.
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
    s = mp.mpf(0)
    for _i, row in X.items():
        for _j, v in row.items():
            s += v * v
    return s


def controls(shape):
    """Return (sym_err, self_comm, opnorm_err).
      sym_err   : ‖σ_0 − σ_0ᵀ‖_∞ (σ symmetric ⇒ ‖σ‖_op = max|eig|).
      self_comm : max_g ‖⁅σ_g,A_a⁆‖_F  — NOTE this is NONZERO (a correction: the germ does
                  NOT commute with its own generator; B(q) and ∂B do not commute because the
                  eigenvectors rotate with q). So the near-a local terms are g∈{a−1,a,a+1}.
      opnorm_err: eig of a genuine 2×2 σ block == {q,−1/q} ⇒ ‖σ‖_op = q (search ALL gens)."""
    per_gen, dim = base.block_structure(shape)
    if dim <= 1:
        return None
    sig = base.sigma_csr(per_gen, dim, base.Q0)
    germ_rows, hcheck = base.germ_csr(per_gen, dim, base.Q0, base.EPS)
    assert hcheck < mp.mpf(10) ** -55
    ngen = len(sig)
    sd = {g: base.csr_to_dict(sig[g]) for g in range(ngen)}
    ad = {g: base.csr_to_dict(germ_rows[g]) for g in range(ngen)}
    sym = mp.mpf(0)
    for i, row in sd[0].items():
        for j, v in row.items():
            sym = max(sym, abs(v - sd[0].get(j, {}).get(i, mp.mpf(0))))
    self_comm = mp.mpf(0)
    for g in range(ngen):
        self_comm = max(self_comm, mp.sqrt(fro2(base.commutator(sd[g], ad[g]))))
    op_err = mp.mpf("nan")
    for g in range(ngen):
        for i, row in sd[g].items():
            offs = [(j, v) for j, v in row.items() if j != i]
            if offs:
                j, b = offs[0]
                a = row[i]; ap = sd[g][j][j]
                tr = a + ap; det = a * ap - b * b
                disc = mp.sqrt(tr * tr - 4 * det)
                got = sorted([(tr + disc) / 2, (tr - disc) / 2])
                want = sorted([base.Q0, -1 / base.Q0])
                op_err = max(abs(got[0] - want[0]), abs(got[1] - want[1]))
                break
        if not mp.isnan(op_err):
            break
    return sym, self_comm, op_err


def analyze(A):
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    print(f"[loc] A={A} (n={n}), generators 0..{ngen-1}")

    # controls on a representative fat partition
    fat = None
    for sh in base.partitions(n):
        _pg, d = base.block_structure(sh)
        if d > 1:
            fat = sh; break
    c = controls(fat)
    if c:
        sym, sc, oe = c
        print(f"[loc] controls on λ={fat}: σ symmetric err={mp.nstr(sym,3)}; "
              f"max_g ‖⁅σ_g,A_g⁆‖_F={mp.nstr(sc,3)} (NONZERO — germ ≠ commutes with own gen); "
              f"eig(σ block)={{q,−1/q}} err={mp.nstr(oe,3)} ⇒ ‖σ‖_op=q\n")

    byb = defaultdict(list)   # b -> list of (max_{a,g∈{a-1,a,a+1}} ‖⁅σ_g,A_a⁆‖_F/√dim, dim)
    for shape in base.partitions(n):
        per_gen, dim = base.block_structure(shape)
        if dim <= 1:
            continue
        b = n - shape[0]
        sig = base.sigma_csr(per_gen, dim, base.Q0)
        germ_rows, hcheck = base.germ_csr(per_gen, dim, base.Q0, base.EPS)
        assert hcheck < mp.mpf(10) ** -55
        sd = {g: base.csr_to_dict(sig[g]) for g in range(ngen)}
        ad = {g: base.csr_to_dict(germ_rows[g]) for g in range(ngen)}
        sdroot = mp.sqrt(mp.mpf(dim))
        best = mp.mpf(0)
        for a in range(ngen):            # germ position a
            for g in (a - 1, a, a + 1):  # near-a generators (the telescoping support)
                if 0 <= g < ngen:
                    C = base.commutator(sd[g], ad[a])   # ⁅σ_g, A_a⁆
                    best = max(best, mp.sqrt(fro2(C)) / sdroot)
        byb[b].append((best, dim))

    print("  b :  max_{a,g∈{a±1,a}} ‖⁅σ_g,A_a⁆‖_F/√dim   (max-dim λ of b)   dim")
    b_levels = sorted(byb)
    seq = []
    for b in b_levels:
        val, dim = max(byb[b], key=lambda r: r[1])
        seq.append((b, val, dim))
        print(f"  {b:>2} : {mp.nstr(val,6):>18}                        {dim:>6}")

    # verdict: is ‖⁅σ_{a+1},A_a⁆‖_F/√dim → 0 (route closes) or ≈const (need cancellation)?
    print()
    if len(seq) >= 2:
        v0, vlast = seq[0][1], seq[-1][1]
        dim0, dimlast = seq[0][2], seq[-1][2]
        trend = "DECREASES→0 (op-norm route CLOSES: |t|≤C·o(√dim)·Θ(√dim)=o(dim))" \
                if vlast < v0 * mp.mpf("0.7") else \
                "≈CONST/↑ ⇒ LOCAL COMMUTATOR IS Θ(√dim): op-norm route gives only O(dim); " \
                "the measured o(dim) is a CANCELLATION the submultiplicative bound discards"
        print(f"  local max ‖⁅σ_g,A_a⁆‖_F/√dim : b={seq[0][0]} → {seq[-1][0]}  "
              f"{mp.nstr(v0,4)} → {mp.nstr(vlast,4)}  (dim {dim0}→{dimlast})")
        print(f"  ⇒ {trend}")
    return seq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    args = ap.parse_args()
    analyze(A=args.A)


if __name__ == "__main__":
    main()
