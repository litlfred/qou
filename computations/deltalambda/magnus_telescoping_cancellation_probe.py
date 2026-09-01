#!/usr/bin/env python3
"""magnus_telescoping_cancellation_probe.py — HOW do the O(1) telescoping terms of ⁅ρ,A_a⁆
cancel?  Quantify the cancellation the surviving (sign-tracking) proof route must capture.

CONTEXT. #6349 established: the operator-norm route to |tr(ρ_λ O)| = o(dim_λ) is a DEAD END —
the local commutator ‖⁅σ_g,A_a⁆‖_F is Θ(√dim), so submultiplicativity gives only O(dim). The
measured o(dim) is a CANCELLATION. By the Leibniz telescoping (Lean commutator_mul_left),
    ⁅ρ,A_a⁆ = Σ_{i: |g_i−a|≤1} T_i,   T_i = (∏_{j<i} σ_{g_j})·⁅σ_{g_i},A_a⁆·(∏_{j>i} σ_{g_j}),
a sum of O(1) terms EACH of Frobenius norm Θ(√dim), yet ‖⁅ρ,A_a⁆‖_F/√dim DECREASES with b.
So the terms cancel. This probe measures the cancellation quantitatively:
    κ(λ,a) = ‖Σ_i T_i‖_F / Σ_i ‖T_i‖_F   ∈ (0,1]   (1 = no cancellation; →0 = total).
and its b-trend, and reports the per-term norms so any STRUCTURE (pairwise cancellation, a
dominant surviving term, phase alignment) is visible. This is what the connected-diagram /
cumulant proof has to explain.

Cross-check: Σ_i T_i must equal ⁅ρ,A_a⁆ (built directly) to full precision.

scope-(a); NO-FLOAT64 (mpf, dps inherited =140). No fit, no witness, nothing wired. Reuses
the merged sparse machinery. ρ-materialization ⇒ capped at dim ≤ CAP (A=2 all, A=3 most).
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

IDENT = object()


def fro2(X):
    s = mp.mpf(0)
    for _i, row in X.items():
        for _j, v in row.items():
            s += v * v
    return s


def add_into(acc, X, sign=1):
    for i, row in X.items():
        arow = acc.setdefault(i, {})
        for j, v in row.items():
            arow[j] = arow.get(j, mp.mpf(0)) + (v if sign > 0 else -v)


def diff_norm(A, B):
    """‖A − B‖_F for row-dicts."""
    s = mp.mpf(0)
    keys = set(A) | set(B)
    for i in keys:
        ar = A.get(i, {}); br = B.get(i, {})
        for j in set(ar) | set(br):
            d = ar.get(j, mp.mpf(0)) - br.get(j, mp.mpf(0))
            s += d * d
    return mp.sqrt(s)


def telescoping_terms(shape, gens, a):
    """Return (terms, comm_direct) for germ position a: the per-crossing T_i (only i with
    |g_i−a|≤1) and ⁅ρ,A_a⁆ built directly, as row-dicts."""
    per_gen, dim = base.block_structure(shape)
    if dim <= 1:
        return None
    sig = base.sigma_csr(per_gen, dim, base.Q0)
    germ_rows, hcheck = base.germ_csr(per_gen, dim, base.Q0, base.EPS)
    assert hcheck < mp.mpf(10) ** -55
    ngen = len(sig)
    sd = {g: base.csr_to_dict(sig[g]) for g in range(ngen)}
    Aa = base.csr_to_dict(germ_rows[a])
    L = len(gens)
    # prefixes: pre[i] = σ_{g_0}...σ_{g_{i-1}} ; pre[0] = I
    ident = {k: {k: mp.mpf(1)} for k in range(dim)}
    pre = [ident]
    for i in range(L):
        pre.append(base.spmatmul(pre[-1], sd[gens[i]]))
    # suffixes: suf[i] = σ_{g_{i+1}}...σ_{g_{L-1}} ; suf[L-1] = I
    suf = [None] * L
    acc = ident
    for i in range(L - 1, -1, -1):
        suf[i] = acc
        acc = base.spmatmul(sd[gens[i]], acc)
    rho = pre[L]  # full word
    comm_direct = base.commutator(rho, Aa)   # ⁅ρ,A_a⁆
    terms = []
    for i in range(L):
        if abs(gens[i] - a) > 1:
            continue
        C = base.commutator(sd[gens[i]], Aa)   # ⁅σ_{g_i}, A_a⁆
        if not C:
            continue
        T = base.spmatmul(base.spmatmul(pre[i], C), suf[i])
        terms.append((i, gens[i], T))
    return terms, comm_direct, dim


def analyze(A, cap=200):
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    a_star = ngen // 2   # a representative interior germ position
    print(f"[cancel] A={A} (n={n}), germ position a={a_star} (interior), dim cap={cap}")
    print(f"[cancel] κ = ‖Σ_i T_i‖_F / Σ_i ‖T_i‖_F  (1=no cancellation, →0=total)\n")

    byb = defaultdict(list)
    max_recon = mp.mpf(0)
    for shape in base.partitions(n):
        _pg, dim = base.block_structure(shape)
        if dim <= 1 or dim > cap:
            continue
        b = n - shape[0]
        res = telescoping_terms(shape, gens, a_star)
        if res is None:
            continue
        terms, comm_direct, dim = res
        if not terms:
            continue
        # Σ T_i and reconstruction check
        S = {}
        sum_norms = mp.mpf(0)
        for _i, _g, T in terms:
            add_into(S, T)
            sum_norms += mp.sqrt(fro2(T))
        recon = diff_norm(S, comm_direct)
        max_recon = max(max_recon, recon)
        S_norm = mp.sqrt(fro2(S))
        kappa = S_norm / sum_norms if sum_norms > 0 else mp.mpf(0)
        byb[b].append((kappa, len(terms), S_norm / mp.sqrt(mp.mpf(dim)), dim))

    print(f"[cancel] reconstruction check max‖ΣT_i − ⁅ρ,A_a⁆‖_F = {mp.nstr(max_recon,3)} "
          f"{'OK' if max_recon < mp.mpf(10)**-40 else 'FAIL'}\n")

    print("  b :   κ (cancellation)   #terms   ‖⁅ρ,A_a⁆‖_F/√dim   dim")
    b_levels = sorted(byb)
    seq = []
    for b in b_levels:
        kappa, nt, comm_norm, dim = max(byb[b], key=lambda r: r[3])
        seq.append((b, kappa, comm_norm))
        print(f"  {b:>2} : {mp.nstr(kappa,5):>16}   {nt:>4}    {mp.nstr(comm_norm,5):>14}   {dim}")

    print()
    if len(seq) >= 2:
        k0, klast = seq[0][1], seq[-1][1]
        trend = "DECREASES with b (cancellation SHARPENS as the diagram fattens)" \
                if klast < k0 else "≈const/↑"
        print(f"  κ: b={seq[0][0]}→{seq[-1][0]}  {mp.nstr(k0,4)}→{mp.nstr(klast,4)}  ⇒ {trend}")
        print("  Reading: κ→0 with b IS the cancellation the sign-tracking (cumulant/")
        print("  connected-diagram) proof must capture; κ≈const would mean the decay is")
        print("  instead in the CS/trace step, not the telescoping sum.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    ap.add_argument("--cap", type=int, default=200)
    args = ap.parse_args()
    analyze(A=args.A, cap=args.cap)


if __name__ == "__main__":
    main()
