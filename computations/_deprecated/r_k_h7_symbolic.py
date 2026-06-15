#!/usr/bin/env python3
"""Closed-form symbolic r_λ coefficients at H_7 in Q(q^{1/2}).

Same scheme as r_k_h{5,6}_symbolic.py (15 partitions × 15 conjugacy
classes; max SYT dim 35 for (3,2,1,1)). Gauge auto-fallback on
non-hooks where χ_λ((1234567)) = 0.
"""
from __future__ import annotations
import json
import sys
import time
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT  # noqa: E402

import sympy as sp

from sympy import simplify, together
from witness_polynomial import expose_polynomial

q = sp.symbols('q', positive=True)


@lru_cache(maxsize=None)
def standard_young_tableaux(shape):
    n = sum(shape)
    if n == 0:
        return [{}]

    def fill(shape_, used, current):
        if len(used) == n:
            yield dict(current)
            return
        nxt = len(used) + 1
        for r in range(len(shape_)):
            for c in range(shape_[r]):
                if (r, c) in current.values():
                    continue
                if r > 0 and (r - 1, c) not in current.values():
                    continue
                if c > 0 and (r, c - 1) not in current.values():
                    continue
                current[nxt] = (r, c)
                yield from fill(shape_, used | {nxt}, current)
                del current[nxt]

    return list(fill(shape, set(), {}))


@lru_cache(maxsize=None)
def hoefsmit_T_i_symbolic(shape, i):
    """Full Hoefsmit seminormal σ_i over Q(q^{1/2}) with off-diagonal entries.

    For each SYT pair {T, T'} that swap entries (i, i+1) at axial distance ρ:
        σ_i e_T  = a_ρ      e_T  + b   e_{T'}
        σ_i e_{T'} = a_{-ρ} e_{T'} + b e_T
    where a_ρ = h / (1 - q^{-2ρ}), b² = a_ρ a_{-ρ} + 1, h = q - q^{-1}.

    Same-row → eigenvalue +q (1×1 block).
    Same-column → eigenvalue -q^{-1} (1×1 block).
    """
    syts = standard_young_tableaux(shape)
    dim = len(syts)
    M = sp.zeros(dim, dim)
    h = q - q**(-1)
    processed = set()

    # Build a lookup: tableau (frozenset of (entry, cell)) → index
    syt_idx = {tuple(sorted(T.items())): k for k, T in enumerate(syts)}

    for ti, T in enumerate(syts):
        if ti in processed:
            continue
        pos_i = T[i]
        pos_i1 = T[i + 1]
        ri, ci = pos_i
        ri1, ci1 = pos_i1
        # Axial distance: c(i+1) - r(i+1) - (c(i) - r(i))
        rho = (ci1 - ri1) - (ci - ri)
        if ri == ri1:
            # same row → +q
            M[ti, ti] = q
            processed.add(ti)
        elif ci == ci1:
            # same column → -q^{-1}
            M[ti, ti] = -q**(-1)
            processed.add(ti)
        else:
            # Find swap partner
            T_swap = dict(T)
            T_swap[i], T_swap[i + 1] = pos_i1, pos_i
            tj = syt_idx.get(tuple(sorted(T_swap.items())))
            if tj is None or tj == ti:
                # Defensive: should not happen for valid SYTs
                M[ti, ti] = h / (1 - q**(-2 * rho))
                processed.add(ti)
                continue
            a = h / (1 - q**(-2 * rho))
            a_prime = h / (1 - q**(2 * rho))
            b_sq = a * a_prime + 1
            b = sp.sqrt(sp.simplify(b_sq))
            M[ti, ti] = a
            M[tj, tj] = a_prime
            M[ti, tj] = b
            M[tj, ti] = b
            processed.add(ti)
            processed.add(tj)
    return M


def char_value_symbolic(shape, word):
    if not word:
        return sp.S(len(standard_young_tableaux(shape)))
    Ms = [hoefsmit_T_i_symbolic(shape, i) for i in word]
    M = Ms[0]
    for X in Ms[1:]:
        M = M * X
    return sp.cancel(M.trace())


def main():
    t_total = time.time()

    classes = [
        ("e",                       ()),
        ("(12)",                    (1,)),
        ("(12)(34)",                (1, 3)),
        ("(12)(34)(56)",            (1, 3, 5)),
        ("(123)",                   (1, 2)),
        ("(123)(45)",               (1, 2, 4)),
        ("(123)(45)(67)",           (1, 2, 4, 6)),
        ("(123)(456)",              (1, 2, 4, 5)),
        ("(1234)",                  (1, 2, 3)),
        ("(1234)(56)",              (1, 2, 3, 5)),
        ("(1234)(567)",             (1, 2, 3, 5, 6)),
        ("(12345)",                 (1, 2, 3, 4)),
        ("(12345)(67)",             (1, 2, 3, 4, 6)),
        ("(123456)",                (1, 2, 3, 4, 5)),
        ("(1234567)",               (1, 2, 3, 4, 5, 6)),
    ]
    partitions = [
        (7,), (6, 1), (5, 2), (5, 1, 1), (4, 3),
        (4, 2, 1), (4, 1, 1, 1), (3, 3, 1), (3, 2, 2),
        (3, 2, 1, 1), (3, 1, 1, 1, 1), (2, 2, 2, 1),
        (2, 2, 1, 1, 1), (2, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1),
    ]
    p_n = len(partitions)
    print(f"Building symbolic Hoefsmit character matrix at H_7 "
          f"({p_n} partitions × {len(classes)} classes)...\n", flush=True)

    chi = {}
    t_chi = time.time()
    for label, word in classes:
        for p in partitions:
            t0 = time.time()
            val = char_value_symbolic(p, word)
            chi[(p, word)] = val
            print(f"  χ_{p}({label}) ... {time.time()-t0:.1f}s", flush=True)
    print(f"Character table assembled ({time.time()-t_chi:.1f}s).\n", flush=True)

    # Numerical sanity check at q_0
    q0_rational = sp.Rational(str(Q0_FLOAT))  # centralized via q_parameter
    print("Numerical sanity (entries at q_0):")
    for label, word in classes:
        row = []
        for p in partitions:
            try:
                v = float(chi[(p, word)].subs(q, q0_rational))
                row.append(f"{v:+7.3f}")
            except Exception:
                row.append("  ?  ")
        print(f"  {label:>10}: {' '.join(row)}")
    print()

    # Solve the symbolic linear system per partition.
    # Strategy: use sympy.linsolve on the (p_n-1)-equation gauge-fixed
    # system rather than M.nullspace() + simplify (which is O(p(n)^2 ·
    # determinant-cost) and explodes at H_5). For each gauge index k,
    # set c[k]=1 and solve for the remaining p_n-1 coefficients.
    print("=" * 72)
    print("Closed-form r_λ coefficients in Q(q^{1/2}):")
    print("=" * 72)

    # H_7 gauge selection: hooks have non-zero χ_λ((1234567)), so gauge_k=14
    # (the last class, the n-cycle) works. Non-hooks have χ_λ=0 there, so
    # we fall back. Best heuristic: try gauge_k descending from p_n-1 and
    # pick the first that gives a clean solve.
    GAUGE_HINT = {
        (7,):                  14,
        (6, 1):                14,
        (5, 2):                13,   # non-hook
        (5, 1, 1):             14,
        (4, 3):                13,   # non-hook
        (4, 2, 1):             13,   # non-hook
        (4, 1, 1, 1):          14,
        (3, 3, 1):             13,   # non-hook
        (3, 2, 2):             13,   # non-hook
        (3, 2, 1, 1):          13,   # non-hook
        (3, 1, 1, 1, 1):       14,
        (2, 2, 2, 1):          13,   # non-hook
        (2, 2, 1, 1, 1):       13,   # non-hook
        (2, 1, 1, 1, 1, 1):    14,
        (1, 1, 1, 1, 1, 1, 1): 14,
    }

    results = {}
    for target in partitions:
        constraints = [p for p in partitions if p != target]
        # Build per-target equations once; substitute different gauges per attempt.
        c_syms = [sp.Symbol(f"c_{j}") for j in range(p_n)]
        equations = []
        for i, p in enumerate(constraints):
            row = sum(chi[(p, classes[j][1])] * c_syms[j] for j in range(p_n))
            equations.append(row)

        # Try gauges in this order: hint first, then descend from p_n-1.
        # Multiple non-hooks at H_7 have several zero columns, so a single
        # gauge index isn't enough. Iterate and accept the first that solves.
        hinted = GAUGE_HINT.get(target, p_n - 1)
        gauge_order = [hinted] + [k for k in range(p_n - 1, -1, -1) if k != hinted]
        sol = None
        gauge_idx = None
        t_solve_total = 0.0
        for k_try in gauge_order:
            equations_subst = [eq.subs(c_syms[k_try], 1) for eq in equations]
            unknowns = [c_syms[j] for j in range(p_n) if j != k_try]
            t0 = time.time()
            try:
                cand = sp.solve(equations_subst, unknowns, rational=True)
            except Exception as e:
                t_solve_total += time.time() - t0
                continue
            t_solve_total += time.time() - t0
            if cand:
                sol = cand
                gauge_idx = k_try
                break
        if sol is None:
            print(f"\n  λ = {target}: no gauge solved (tried all {p_n})")
            results[str(target)] = {"error": "no gauge solved"}
            continue
        t_solve = t_solve_total
        # Reassemble full c vector (gauge_idx → 1)
        c_full = []
        for j in range(p_n):
            if j == gauge_idx:
                c_full.append(sp.S(1))
            else:
                c_full.append(sol.get(c_syms[j], sp.S(0)))
        c_simplified = []
        for ci in c_full:
            try:
                c_simplified.append(sp.cancel(ci))
            except Exception:
                c_simplified.append(ci)
        z_sym = sp.S(1) / (sp.sqrt(q) + 1 / sp.sqrt(q))
        tr_M = sum(c_simplified[j] * z_sym**len(word)
                   for j, (_, word) in enumerate(classes))
        try:
            tr_M_simp = sp.cancel(tr_M)
        except Exception:
            tr_M_simp = tr_M
        try:
            val_num = float(tr_M.subs(q, q0_rational))
        except Exception:
            val_num = None
        print(f"\n  λ = {target}: gauge = c[{gauge_idx}], "
              f"solve {t_solve:.1f}s")
        for (label, _), ci in zip(classes, c_simplified):
            s = str(ci)
            if len(s) > 100:
                s = s[:97] + "..."
            print(f"    c_{label:10}  =  {s}", flush=True)
        if val_num is not None:
            print(f"    tr_M(r_λ) at q_0 = {val_num:+.10f}", flush=True)
        results[str(target)] = {
            "gauge_idx": gauge_idx,
            "closed_form_c": [str(ci) for ci in c_simplified],
            "tr_M_symbolic": str(tr_M_simp)[:1000],
            "tr_M_polynomial": expose_polynomial(tr_M_simp, q, simplify=False),
            "tr_M_at_q0_numerical": val_num,
            "solve_time_s": t_solve,
        }

        # Incremental witness write (so we don't lose progress on crash)
        out_partial = {
            "computation": "r-k-h7-symbolic",
            "description": (
                "Symbolic closed-form r_λ coefficients at H_7 in Q(q^{1/2}) "
                "via sympy.solve on the gauge-fixed linear system (faster "
                "than nullspace+simplify on full Q(q) matrices). Full "
                "Hoefsmit construction with off-diagonal b·e_T' entries. "
                "Gauge per partition follows the H_4 closed-form prop "
                "convention: c[last]=1 for hooks, adaptive for non-hooks."
            ),
            "engine": "sympy",
            "computedAt": datetime.now(timezone.utc).isoformat(),
            "q_0_rational": "11099785955541805/10000000000000000",
            "results": results,
            "partial": True,
        }
        out_path_partial = Path(__file__).parent / "r-k-h7-symbolic.witness.json"
        with open(out_path_partial, "w") as fp:
            json.dump(out_partial, fp, indent=2, default=str)

    out = {
        "computation": "r-k-h7-symbolic",
        "description": (
            "Symbolic closed-form r_λ coefficients at H_7 in Q(q^{1/2}) via "
            "sympy.solve on the gauge-fixed linear system (faster than "
            "nullspace+simplify on full Q(q) matrices). Full Hoefsmit "
            "construction with off-diagonal b·e_{T'} entries (fixes the "
            "H_4 script's bug). Gauge per partition follows the H_4 "
            "closed-form prop convention: c[last]=1 for hooks, adaptive "
            "(c[k] for k=13 chosen) for non-hooks at H_7."
        ),
        "engine": "sympy",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q_0_rational": "11099785955541805/10000000000000000",
        "results": results,
        "wall_time_s": time.time() - t_total,
        "partial": False,
    }
    out_path = Path(__file__).parent / "r-k-h7-symbolic.witness.json"
    with open(out_path, "w") as fp:
        json.dump(out, fp, indent=2, default=str)
    print(f"\nWitness: {out_path} ({time.time()-t_total:.1f}s total)")


if __name__ == "__main__":
    main()
