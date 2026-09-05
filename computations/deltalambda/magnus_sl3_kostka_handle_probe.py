#!/usr/bin/env python3
"""magnus_sl3_kostka_handle_probe.py — a THIRD handle: every λ with ≤ 3 rows, via U_q(sl_3)
Schur–Weyl weight sectors and Kostka inversion. (qou-o6ov)

WHY A THIRD HANDLE IS NEEDED, and why my last stated plan was wrong. I said the next move was to
bound the envelope max_{b(λ)=b} tr_λ(X*X)/dim_λ from the two closed forms already in hand. That
premise is FALSE and the data to see it was already measured: at A=3 the envelope is not attained on
a hook or a two-row at large b —

    b=6:  (3,3,3)       211.56   vs hook (3,1⁶)  14.319    →  15x
    b=7:  (2,2,2,2,1)    31.56   vs hook (2,1⁷)   0.4354   →  72x

At large b the hook is near the MINIMUM of its level, not the maximum. So the hook and two-row
closed forms cannot bound the envelope; a handle that reaches the FAT shapes is required.

THE PRINCIPLED GENERALISATION, which subsumes both existing handles. Hooks came from exterior powers
of the (n−1)-dim reflection rep; two-rows from weight sectors of (ℂ²)^⊗n under U_q(sl_2) Schur–Weyl
(#6525). The general statement is (ℂ^k)^⊗n = ⊕_λ S^λ(ℂ^k) ⊗ M^λ, with the Hecke algebra acting only
on M^λ. The μ-weight space of S^λ(ℂ^k) has dimension K_{λμ} (a Kostka number), so for every algebra
element g:

    tr_{W_μ}(g) = Σ_λ K_{λμ} · χ_λ(g),          λ ⊢ n with at most k rows                    (K)

K is unitriangular in dominance order (K_{λλ} = 1, K_{λμ} = 0 unless λ ⊵ μ), so (K) INVERTS: every
χ_λ with ≤ k rows is recoverable from weight-sector traces. k=2 reproduces #6525's difference
formula tr_(n−k,k) = tr_W_k − tr_W_(k−1) exactly — that is the k=2 case of this inversion, not a
separate trick.

At k=3, n=9 this adds (6,2,1), (5,3,1), (5,2,2), (4,4,1), (4,3,2) and (3,3,3) — including the b=6
envelope shape, and five shapes no probe in this arc has ever evaluated. Ř still acts on adjacent
pairs, so #6710's sparse column-wise kernel carries over with only the local rule changed.

THE GATES. n=6 is a COMPLETE gate: all 7 of its ≤3-row shapes are checkable three independent ways —
the direct seminormal trace (dim ≤ 16), the reduced-Burau closed form on hooks, and the sl_2 sector
difference on two-rows. Nothing about k=3 is reported until all three agree. Separately the Kostka
matrix itself is checked combinatorially against multinomial(n; μ) = Σ_λ K_{λμ}·f^λ, which is
dim W_μ counted two ways and involves no trace at all — so a bug in K cannot hide behind a bug in
the kernel.

scope-(a); NO-FLOAT64 (mpf; dps asserted at every compute entry). No fit, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import math
import os
import sys
from itertools import permutations

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_gauge_hook_closed_form_probe import reflection_generators  # noqa: E402
from magnus_hook_majorant_closed_form_probe import burau_closed_form  # noqa: E402
from magnus_frobenius_is_positive_trace_probe import build  # noqa: E402
# Module-level by necessity: these pin mp.mp.dps at import, so a deferred import would re-set the
# precision of a run in progress. That trap cost a silent no-op --dps flag in #6710; see _assert_dps.
from magnus_tworow_majorant_sector_probe import sector_majorant as _sl2_sector  # noqa: E402

_WANT_DPS = None
DIM_CAP = 50


def _assert_dps(where):
    """Fail loudly if global precision is not what this run asked for (the #6710 trap)."""
    if _WANT_DPS is not None and mp.mp.dps != _WANT_DPS:
        raise RuntimeError(f"mp.mp.dps is {mp.mp.dps}, expected {_WANT_DPS}, at {where}")


# ---------------------------------------------------------------- partitions / Kostka

def partitions_maxlen(n, maxlen):
    out = []

    def rec(rem, mx, cur):
        if rem == 0:
            out.append(tuple(cur))
            return
        if len(cur) >= maxlen:
            return
        for p in range(min(rem, mx), 0, -1):
            rec(rem - p, p, cur + [p])
    rec(n, n, [])
    return out


def pad(lam, ln):
    return tuple(lam) + (0,) * (ln - len(lam))


def horizontal_strips(lam, size):
    """All ν ⊆ λ with λ/ν a horizontal strip of the given size (interlacing λ_i ≥ ν_i ≥ λ_{i+1})."""
    ln = len(lam)
    res = []

    def rec(i, cur, rem):
        if i == ln:
            if rem == 0:
                res.append(tuple(x for x in cur if x > 0))
            return
        lo = lam[i + 1] if i + 1 < ln else 0
        for v in range(lo, lam[i] + 1):
            take = lam[i] - v
            if take <= rem:
                rec(i + 1, cur + [v], rem - take)
    rec(0, [], size)
    return res


def kostka(lam, mu):
    """K_{λμ} = #SSYT of shape λ, content μ, by peeling the horizontal strip of the largest entry."""
    lam = tuple(x for x in lam if x > 0)
    mu = tuple(x for x in mu if x > 0)
    if sum(lam) != sum(mu):
        return 0
    if not mu:
        return 1 if not lam else 0
    total = 0
    for nu in horizontal_strips(lam, mu[-1]):
        total += kostka(nu, mu[:-1])
    return total


def n_syt(lam):
    """f^λ by the hook-length formula — the Hecke irrep dimension."""
    lam = tuple(x for x in lam if x > 0)
    n = sum(lam)
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    prod = 1
    for i, r in enumerate(lam):
        for j in range(r):
            prod *= (r - j) + (conj[j] - i) - 1
    return math.factorial(n) // prod


# ---------------------------------------------------------------- sl_k sparse sector kernel

def weight_states(n, mu):
    """Distinct words in {0..k−1}^n with letter multiplicities mu (as tuples)."""
    letters = []
    for a, m in enumerate(mu):
        letters += [a] * m
    states = sorted(set(permutations(letters, n)))
    return states, {s: i for i, s in enumerate(states)}


def sparse_gen_k(n, i, q, states, index):
    """Ř on strands (i, i+1) for U_q(sl_k), restricted to a weight sector, by column.

    Local rule (the k=2 case is exactly #6525's): with a = w[i], b = w[i+1],
        a == b : q·|w⟩
        a <  b : (q − q⁻¹)·|w⟩ + |w with i,i+1 swapped⟩
        a >  b : |w with i,i+1 swapped⟩
    At most two entries per column, which is what makes the column-wise route affordable.
    """
    qi = 1 / q
    cols = []
    one = mp.mpf(1)
    for w in states:
        a, b = w[i], w[i + 1]
        if a == b:
            cols.append(((index[w], q),))
        else:
            t = list(w)
            t[i], t[i + 1] = b, a
            t = tuple(t)
            if a < b:
                cols.append(((index[w], q - qi), (index[t], one)))
            else:
                cols.append(((index[t], one),))
    return cols


def apply_gen(cols, v, D):
    w = [mp.mpf(0)] * D
    for col in range(D):
        x = v[col]
        if x:
            for row, c in cols[col]:
                w[row] += c * x
    return w


def sector_majorant_k(n, mu, gens, q):
    """tr_{W_μ}(X* X) = ‖X|_{W_μ}‖_F² for X = ρ·Ω₂^P, column by column (Ř symmetric — gated below)."""
    _assert_dps(f"sector_majorant_k(mu={mu})")
    states, index = weight_states(n, mu)
    D = len(states)
    ngen = max(gens) + 1
    G = [sparse_gen_k(n, i, q, states, index) for i in range(ngen)]
    c = 4 / (q + 1 / q) ** 2
    rev = list(reversed(gens))
    total = mp.mpf(0)
    for j in range(D):
        e = [mp.mpf(0)] * D
        e[j] = mp.mpf(1)
        acc = [mp.mpf(0)] * D
        for a in range(ngen - 1):
            u = apply_gen(G[a], apply_gen(G[a + 1], e, D), D)
            z = apply_gen(G[a + 1], apply_gen(G[a], e, D), D)
            for r in range(D):
                acc[r] += u[r] - z[r]
        v = [c * x for x in acc]
        for g in rev:
            v = apply_gen(G[g], v, D)
        for x in v:
            if x:
                total += x * x
    return total, D


def chi_by_kostka(n, k, gens, q, verbose=False):
    """Every χ_λ(X*X) with ≤ k rows, by inverting tr_{W_μ} = Σ_λ K_{λμ}·χ_λ in dominance order."""
    shapes = partitions_maxlen(n, k)                       # both the λ and the μ index set
    order = sorted(shapes, key=lambda s: pad(s, k), reverse=True)   # dominance-compatible
    K = {(l, m): kostka(l, m) for l in order for m in order}
    tr = {}
    for m in order:
        val, D = sector_majorant_k(n, m, gens, q)
        tr[m] = val
        if verbose:
            print(f"      tr_W{m} done (dim {D})", flush=True)
    chi = {}
    for m in order:                                        # λ ⊵ μ ⇒ solve in this order
        s = tr[m]
        for l in order:
            if l != m and K[(l, m)]:
                s -= K[(l, m)] * chi[l]
        chi[m] = s / K[(m, m)]
    return chi, K, order


# ---------------------------------------------------------------- gates

def kostka_dimension_check(n, k):
    """multinomial(n; μ) = Σ_λ K_{λμ}·f^λ — dim W_μ counted two ways, no trace involved.

    Deliberately independent of the sector kernel: a bug in K cannot hide behind a bug in the
    kernel (or vice versa) if one of the checks never touches the other's code.
    """
    shapes = partitions_maxlen(n, k)
    worst = 0
    for m in shapes:
        lhs = math.factorial(n)
        for p in m:
            lhs //= math.factorial(p)
        rhs = sum(kostka(l, m) * n_syt(l) for l in shapes)
        worst = max(worst, abs(lhs - rhs))
    return worst


def gate(A, k, q):
    """n=6 is a COMPLETE gate: every ≤3-row shape checkable 3 ways. Returns (worst_rel, rows)."""
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    L = len(gens)
    sV, _ = reflection_generators(n, ngen, q)
    chi, _K, order = chi_by_kostka(n, k, gens, q)
    worst = mp.mpf(0)
    rows = []
    for lam in order:
        refs = {}
        _pg, d = base.block_structure(lam)
        if d <= DIM_CAP:
            X, Xs, dim, _a = build(lam, gens, q, ngen)
            P = Xs * X
            refs["seminormal"] = mp.re(sum(P[i, i] for i in range(dim)))
        if len(lam) == 1 or all(p == 1 for p in lam[1:]):          # hook
            refs["burau"] = burau_closed_form(len(lam) - 1, gens, q, ngen, sV, L)
        if len(lam) <= 2:                                           # two-row
            kk = lam[1] if len(lam) > 1 else 0
            hi, _dW, _as = _sl2_sector(n, kk, gens, q)
            lo = (_sl2_sector(n, kk - 1, gens, q)[0] if kk > 0 else mp.mpf(0))
            refs["sl2"] = mp.re(hi) - mp.re(lo)
        got = chi[lam]
        for nm, ref in refs.items():
            den = abs(ref) if abs(ref) > mp.mpf(10) ** -40 else mp.mpf(1)
            worst = max(worst, abs(got - ref) / den)
        rows.append((lam, d, got, sorted(refs)))
    return worst, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[3])
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--dps", type=int, default=65)
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()
    global _WANT_DPS
    _WANT_DPS = args.dps
    mp.mp.dps = args.dps
    q = base.Q0

    print(f"[sl{args.k}] third handle: every λ with ≤ {args.k} rows, via weight sectors + Kostka "
          f"inversion (mp.dps = {args.dps})")

    # --- gate 1: the Kostka matrix alone, no traces involved ---
    for n in (6, 9, 12):
        w = kostka_dimension_check(n, args.k)
        print(f"  [K] n={n}: multinomial(n;μ) == Σ_λ K_λμ·f^λ for every μ?  "
              f"{'YES ✓' if w == 0 else f'NO ✗ (worst |Δ| = {w})'}")
        if w:
            print("  ⇒ the Kostka matrix is wrong; nothing downstream is reportable. Stopping.")
            return

    # --- gate 2: n=6, every shape three independent ways ---
    print(f"\n  [gate] A=2 (n=6): every ≤{args.k}-row shape vs seminormal / Burau / sl_2")
    worst, rows = gate(2, args.k, q)
    for lam, d, got, refs in rows:
        print(f"    {str(lam):<12} dim {d:>3}  χ_λ(X*X) = {mp.nstr(got,10):>16}   checked vs {refs}")
    ok = worst < mp.mpf(10) ** -(args.dps // 2)
    print(f"  worst |Δ_rel| over every shape and every reference = {mp.nstr(worst,3)}   "
          f"{'✓' if ok else '✗'}")
    if not ok:
        print("\n  ⇒ GATE FAILED. The k=3 inversion does not reproduce the known values, so no new")
        print("    shape is reportable. Report the mismatch; do not tune the Kostka order to fit.")
        return
    print("  ⇒ gate passed on ALL 7 shapes — the k=2 difference formula is the k=2 case of this\n"
          "    inversion, and the hooks agree with the Burau form independently.\n")

    for A in args.A:
        n = 3 * A
        Z, N = A // 2, A - A // 2
        gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
        print(f"[sl{args.k}] A={A} (n={n}) — every λ with ≤ {args.k} rows")
        chi, _K, order = chi_by_kostka(n, args.k, gens, q, verbose=args.verbose)
        print("     λ                dim    b(λ)   χ_λ(X*X)          per-dim        new?")
        for lam in sorted(order, key=lambda s: sum(s) - s[0]):
            _pg, d = base.block_structure(lam)
            b = sum(lam) - lam[0]
            hook_or_2row = (len(lam) <= 2) or all(p == 1 for p in lam[1:])
            new = "" if (hook_or_2row or d <= DIM_CAP) else "NEW — no prior handle"
            print(f"    {str(lam):<16} {d:>4}   {b:>4}   {mp.nstr(chi[lam],10):>16}  "
                  f"{mp.nstr(chi[lam]/d,8):>13}   {new}")

        # ---- LEVEL COMPLETENESS AND THE ENVELOPE ----
        # The envelope max_{b(λ)=b} per-dim is the one global monotone form that survived #6587,
        # and every prior measurement of it was over a DIM-CAPPED subset of each level — which can
        # only understate a maximum. Adding the ≤3-row shapes to the hooks completes some levels
        # outright. A level's envelope is reported ONLY when the level is complete: a max over a
        # subset is a lower bound on the max, not the max, and printing it as one is how a capped
        # measurement gets quoted as a fact.
        ngen_h = max(gens) + 1
        sV_h, _ = reflection_generators(n, ngen_h, q)
        L_h = len(gens)
        known = dict(chi)
        for bb in range(n):                                   # hooks, via the Burau closed form
            hk = tuple([n - bb] + [1] * bb)
            known.setdefault(hk, burau_closed_form(bb, gens, q, ngen_h, sV_h, L_h))
        all_shapes = {}
        for lam in partitions_maxlen(n, n):
            all_shapes.setdefault(sum(lam) - lam[0], []).append(lam)
        print("\n     b   level size   known   COMPLETE?   envelope max per-dim   attained by")
        env = []
        for bb in sorted(all_shapes):
            lv = all_shapes[bb]
            have = [l for l in lv if l in known]
            complete = len(have) == len(lv)
            if have:
                best = max(have, key=lambda l: known[l] / base.block_structure(l)[1])
                bv = known[best] / base.block_structure(best)[1]
            miss = [l for l in lv if l not in known]
            if complete and have and bv > 0:
                env.append((bb, bv))
                print(f"    {bb:>2}   {len(lv):>10}   {len(have):>5}   YES         "
                      f"{mp.nstr(bv,8):>18}   {best}")
            elif complete:
                # COMPLETE but excluded from the envelope: Ω₂^P vanishes identically on a 1-dim
                # rep, so b=0 and b=n−1 are exact zeros. Say that, rather than printing "no" under
                # COMPLETE? beside "missing 0", which reads as a coverage gap that does not exist.
                print(f"    {bb:>2}   {len(lv):>10}   {len(have):>5}   YES         "
                      f"{'(exact zero)':>18}   endpoint — Ω₂^P ≡ 0 on a 1-dim rep; excluded")
            else:
                print(f"    {bb:>2}   {len(lv):>10}   {len(have):>5}   no          "
                      f"{'(not reported)':>18}   missing {len(miss)}: {miss[:3]}"
                      f"{' …' if len(miss) > 3 else ''}")
        mono = all(env[i + 1][1] < env[i][1] for i in range(len(env) - 1))
        if len(env) > 1:
            print(f"\n  envelope over the {len(env)} COMPLETE level(s) b = "
                  f"{[b for b, _ in env]} strictly decreasing?  {'YES ✓' if mono else 'NO'}")
            print("      " + " > ".join(mp.nstr(v, 7) for _b, v in env))
            print("  These are the first complete levels in this arc — every earlier envelope was a")
            print("  max over a dim-capped subset, which can only UNDERSTATE a level maximum.")
        print()


if __name__ == "__main__":
    main()
