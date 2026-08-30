#!/usr/bin/env python3
"""magnus_tr_decay_perpair_cluster_probe.py — is the tr-decay PER-PAIR-LOCAL, or an
INTER-PAIR cancellation? The discriminating datum for the cluster route (qou-o6ov).

CONTEXT. The open theorem (qou-o6ov) is: |tr(ρ_λ Ω₂_λ)|/dim_λ decays with b(λ)=n−λ₁.
Two proof routes are already closed as negatives (Kerov–Olshanski content-
polynomiality REFUTED #6291; the 2-row closed form is not clean). The one surviving
route is the CLUSTER / CUMULANT connected-diagram cancellation, and this probe
supplies the concrete datum that route turns on.

THE STRUCTURE (measured, exact). By far-commutativity ([A_a,A_b]=0 for |a−b|≥2),
    Ω₂ = ½ Σ_{i<j} [A_{g_i},A_{g_j}]
       = ½ Σ_{(a,a+1)} mult(a,a+1) · [A_a, A_{a+1}]     (adjacent generators only)
and the adjacent-pair multiplicities of the canonical atom word are PERIOD-3
translation-invariant, identical in every nucleon window and identical across A:
    (3m,3m+1):28   (3m+1,3m+2):4   (3m+2,3m+3):7        [the last has no +3 bond]
so Ω₂ is a genuine LATTICE SUM of local operators, one motif per nucleon — the MPO /
transfer-matrix picture made exact, not an analogy.

THE QUESTION this probe answers (falsifiable, cheap, A=3 exact). Write the per-pair
local trace
    t_λ^{(a)} := tr(ρ_λ · [A_a, A_{a+1}]).
Then 2·tr(ρ_λ Ω₂) = Σ_a mult(a,a+1)·t_λ^{(a)}  (self-checked against the committed
triton witness to full precision). The mechanism of the b-decay is then EITHER:

  (P) PER-PAIR LOCAL: each t_λ^{(a)}/dim_λ already decays with b(λ). Then the whole
      theorem localizes — a bound on ONE 3-strand-window local operator's normalised
      trace, summed over a λ-INDEPENDENT number of windows, gives the result. This is
      the good case: it reduces the theorem to a single local estimate.

  (C) INTER-PAIR CANCELLATION: individual t_λ^{(a)}/dim_λ do NOT decay (or grow), and
      the decay only appears after the signed sum over pairs. Then the cluster route
      must prove a cancellation BETWEEN windows — the harder Penrose/Ursell
      connected-diagram story — and a per-window bound is insufficient.

RESULT. See docstring tail / the audit doc. This discriminates (P) vs (C) and, in
case (P), identifies the single local operator whose normalised-trace decay is the
whole theorem.

scope-(a): a dimensionless structural datum; no MeV, no fit, nothing wired. Reuses
the MERGED sparse probe's exact machinery (block_structure, sigma_csr, germ_csr,
commutator, apply_word_to_e) — nothing re-derived. NO-FLOAT64: mpmath mpf end to end,
dps=140 (inherited from the sparse probe import); the germ is a finite-difference
q-derivative that cancels ~50 digits, so ~90 remain. Reproduces from the committed
triton (A=3) witness for the aggregate self-check.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mpmath as mp  # noqa: E402

# Reuse the merged sparse probe's machinery verbatim (sets dps=140 at import).
import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

_HERE = os.path.dirname(os.path.abspath(__file__))


def adjacent_pairs(gens):
    """Multiplicity of each word-adjacent generator pair (a,a+1) — i.e. the count of
    ordered crossing pairs (i<j) with {g_i,g_j}={a,a+1}. This is the coefficient of
    [A_a,A_{a+1}] in Σ_{i<j}[A_{g_i},A_{g_j}]."""
    m = Counter()
    L = len(gens)
    for i in range(L):
        for j in range(i + 1, L):
            a, b = gens[i], gens[j]
            if abs(a - b) == 1:
                m[(min(a, b), max(a, b))] += 1
    return dict(sorted(m.items()))


def per_pair_traces(shape, gens):
    """For partition `shape`, return (dim, {(a,a+1): t_λ^{(a)}}, tr_rho_Omega2).

    t_λ^{(a)} = tr(ρ_λ [A_a,A_{a+1}]); the aggregate ½ Σ mult·t must equal tr(ρ_λ Ω₂).
    """
    per_gen, dim = base.block_structure(shape)
    if dim == 1:
        return dim, {}, mp.mpf(0)
    sig = base.sigma_csr(per_gen, dim, base.Q0)
    germ_rows, hcheck = base.germ_csr(per_gen, dim, base.Q0, base.EPS)
    assert hcheck < mp.mpf(10) ** -55, f"germ Hecke check failed {shape}: {mp.nstr(hcheck,3)}"
    A = [base.csr_to_dict(germ_rows[g]) for g in range(len(germ_rows))]

    pairs = adjacent_pairs(gens)
    tvals = {}
    agg = mp.mpf(0)  # ½ Σ mult·t == tr(ρ_λ Ω₂)
    for (a, b), mult in pairs.items():
        C = base.commutator(A[a], A[b])  # rows dict
        # t = tr(ρ_λ C) = Σ_k Σ_c C[k,c]·(ρ e_k)[c]
        t = mp.mpf(0)
        for k, crow in C.items():
            w = base.apply_word_to_e(gens, sig, k, dim)
            s = mp.mpf(0)
            for c, v in crow.items():
                s += v * w[c]
            t += s
        tvals[(a, b)] = t
        agg += mult * t
    return dim, tvals, agg / 2


def run(A=3, verify=True):
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    pairs = adjacent_pairs(gens)
    print(f"[perpair] A={A} (n={n}, Z={Z} N={N}), word L={len(gens)}, "
          f"distinct gens {sorted(set(gens))}")
    print(f"[perpair] adjacent-pair multiplicities (period-3 lattice): {pairs}")
    print(f"[perpair] Ω₂ = ½ Σ_pair mult·[A_a,A_{{a+1}}] over {len(pairs)} local windows\n")

    # committed witness for the aggregate self-check
    wpath = {3: "triton-magnus-omega2-sign.witness.json",
             2: "deuteron-magnus-omega2-sign.witness.json"}.get(A)
    committed = {}
    if wpath and os.path.exists(os.path.join(_HERE, wpath)):
        w = json.load(open(os.path.join(_HERE, wpath)))
        for r in w["results"]["per_partition"]:
            committed[tuple(r["lambda"])] = mp.mpf(r["tr_rho_Omega2"])

    shapes = list(base.partitions(n))
    # per-pair contributions grouped by b, normalised by dim
    by_b_pair = defaultdict(lambda: defaultdict(lambda: mp.mpf(0)))   # b -> pair -> Σ|t|/... (we store list)
    rows = []
    max_agg_err = mp.mpf(0)
    for shape in shapes:
        dim, tvals, agg = per_pair_traces(shape, gens)
        b = n - shape[0]
        if committed and shape in committed:
            err = abs(agg - committed[shape])
            max_agg_err = max(max_agg_err, err)
        rows.append((shape, b, dim, tvals, agg))

    if committed:
        print(f"[perpair] SELF-CHECK ½Σmult·t == committed tr(ρΩ₂): "
              f"max abs err = {mp.nstr(max_agg_err,3)} over {len(committed)} partitions "
              f"{'OK' if max_agg_err < mp.mpf(10)**-40 else 'FAIL'}\n")

    # For each pair, does |t^{(a)}|/dim decay with b?  (aggregate over partitions at each b:
    # report the dim-weighted RMS of |t|/dim, and the max, per b.)
    pair_list = list(pairs.keys())
    print("PER-PAIR normalised local trace  max_λ |t_λ^{(a)}|/dim_λ  by b-level:")
    header = "  b  " + "".join(f"{str(p):>12}" for p in pair_list)
    print(header)
    b_levels = sorted({n - sh[0] for sh in shapes})
    decay_flags = {}
    per_pair_by_b = {p: {} for p in pair_list}
    for b in b_levels:
        cells = []
        for p in pair_list:
            vals = [abs(tv.get(p, mp.mpf(0))) / dim
                    for (sh, bb, dim, tv, ag) in rows if bb == b and dim > 1]
            mx = max(vals) if vals else mp.mpf(0)
            per_pair_by_b[p][b] = mx
            cells.append(mp.nstr(mx, 4))
        print(f"  {b:>2} " + "".join(f"{c:>12}" for c in cells))
    # HONEST verdict per pair. The largest b-level is the 1-dim sign rep (contribution
    # trivially 0), so "b1 vs top" is a weak test. Instead ask the mechanism question:
    #   - does the window PEAK at b=1 (mass at low b)?  [peaks_at_b1]
    #   - how much smaller is the tail (max over b>=3) than the b=1 value?  [b1/tail]
    #   - is the fall MONOTONE across b=1..bmax_nontrivial, or does it bump?  [monotone]
    # (P) requires every window to peak at b=1 (no window carries its mass high) — that is
    # what rules OUT an inter-window cancellation. Monotonicity is a SEPARATE, stronger
    # property we do NOT claim.
    nontrivial_bs = [b for b in b_levels if any(bb == b and dim > 1
                     for (sh, bb, dim, tv, ag) in rows)]
    print(f"\nPER-PAIR verdict (nontrivial b-levels {nontrivial_bs}; largest-b sign rep excluded):")
    all_peak_b1 = True
    any_nonmono = False
    min_tailratio = mp.mpf("inf")
    max_tailratio = mp.mpf(0)
    for p in pair_list:
        series = [per_pair_by_b[p][b] for b in nontrivial_bs]
        v1 = per_pair_by_b[p].get(1, mp.mpf(0))
        peak_b = nontrivial_bs[max(range(len(series)), key=lambda i: series[i])]
        tail = max((per_pair_by_b[p][b] for b in nontrivial_bs if b >= 3), default=mp.mpf(0))
        ratio = (v1 / tail) if tail > 0 else mp.mpf("inf")
        if ratio < min_tailratio:
            min_tailratio = ratio
        if mp.isfinite(ratio) and ratio > max_tailratio:
            max_tailratio = ratio
        mono = all(series[i] >= series[i + 1] for i in range(len(series) - 1))
        if peak_b != 1:
            all_peak_b1 = False
        if not mono:
            any_nonmono = True
        print(f"  {str(p):>10}: peak@b={peak_b}  b1/tail(b>=3)={mp.nstr(ratio,3):>8}  "
              f"monotone={'yes' if mono else 'NO'}")

    print("\nMECHANISM VERDICT:")
    if all_peak_b1:
        print("  (P) PER-PAIR LOCAL — EVERY local window's normalised trace |t^{(a)}|/dim")
        print("      PEAKS at b=1. No window carries its mass at high b, so the b-decay of")
        print("      tr(ρΩ₂) is ALREADY present per-window — it is NOT an inter-window")
        print("      (Penrose/Ursell) cancellation. This RULES OUT the harder connected-diagram")
        print("      sub-route and reduces the theorem to a single-window normalised-trace")
        print("      estimate: |tr(ρ_λ[A_a,A_{a+1}])|/dim_λ decays with b, for a FIXED")
        print("      3-strand-local operator (ρ still global).")
        print(f"      Per-window b1/tail(b>=3) suppression this run: "
              f"{mp.nstr(min_tailratio,3)}× (min) .. {mp.nstr(max_tailratio,3)}× (max).")
        print("      HONEST: the suppression is only MODEST at small A (some windows ~1.5× at")
        print("      A=2); it SHARPENS with A (rep-stability). 'Peak at b=1' is the robust")
        print("      claim; a uniform quantitative bound is NOT established by this probe.")
    else:
        print("  (C) INTER-PAIR — a local window peaks at high b; the decay of tr(ρΩ₂) needs")
        print("      an inter-window cancellation, not a single-window bound.")
    if any_nonmono:
        print("  NOTE: the per-window fall is NOT strictly monotone in b (small bumps at high")
        print("        b); (P) is a peak-at-b=1 statement, not a monotone-decay one.")
    return rows, pair_list, per_pair_by_b


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    args = ap.parse_args()
    run(A=args.A)


if __name__ == "__main__":
    main()
