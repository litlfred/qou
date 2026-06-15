#!/usr/bin/env python3
"""Closed-form symbolic r_λ coefficients at H_5 in Q(q^{1/2}).

Solves the gauge-fixed Hoefsmit linear system per partition and
emits closed-form r_λ coefficients with their α_λ evaluated at q_0.
Uses the full Hoefsmit seminormal form (off-diagonal b·e_{T'}
entries on 2×2 blocks).
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
        ("e",         ()),
        ("(12)",      (1,)),
        ("(12)(34)",  (1, 3)),
        ("(123)",     (1, 2)),
        ("(123)(45)", (1, 2, 4)),
        ("(1234)",    (1, 2, 3)),
        ("(12345)",   (1, 2, 3, 4)),
    ]
    partitions = [
        (5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1),
        (2, 1, 1, 1), (1, 1, 1, 1, 1),
    ]
    p_n = len(partitions)
    print(f"Building symbolic Hoefsmit character matrix at H_5 "
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

    # Pick gauge per partition based on numerical run (already validated)
    GAUGE_HINT = {
        (5,):              6,
        (4, 1):            6,
        (3, 2):            5,   # non-hook, c[(12345)] = 0
        (3, 1, 1):         6,
        (2, 2, 1):         5,   # non-hook
        (2, 1, 1, 1):      6,
        (1, 1, 1, 1, 1):   6,
    }

    results = {}
    for target in partitions:
        constraints = [p for p in partitions if p != target]
        gauge_idx = GAUGE_HINT.get(target, p_n - 1)
        # Set up (p_n - 1) linear equations Σ_j A[i,j] c[j] = 0
        # with the gauge c[gauge_idx] = 1.
        c_syms = [sp.Symbol(f"c_{j}") for j in range(p_n)]
        equations = []
        for i, p in enumerate(constraints):
            row = sum(chi[(p, classes[j][1])] * c_syms[j] for j in range(p_n))
            equations.append(row)
        # Substitute the gauge
        equations_subst = [eq.subs(c_syms[gauge_idx], 1) for eq in equations]
        unknowns = [c_syms[j] for j in range(p_n) if j != gauge_idx]
        t0 = time.time()
        try:
            sol = sp.solve(equations_subst, unknowns, rational=True)
        except Exception as e:
            print(f"\n  λ = {target}: solve FAILED ({e})")
            results[str(target)] = {"error": f"solve: {e}"}
            continue
        t_solve = time.time() - t0
        if not sol:
            print(f"\n  λ = {target}: no solution")
            results[str(target)] = {"error": "no solution"}
            continue
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
            "computation": "r-k-h5-symbolic",
            "description": (
                "Symbolic closed-form r_λ coefficients at H_5 in Q(q^{1/2}) "
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
        out_path_partial = Path(__file__).parent / "r-k-h5-symbolic.witness.json"
        with open(out_path_partial, "w") as fp:
            json.dump(out_partial, fp, indent=2, default=str)

    out = {
        "computation": "r-k-h5-symbolic",
        "description": (
            "Symbolic closed-form r_λ coefficients at H_5 in Q(q^{1/2}) via "
            "sympy.solve on the gauge-fixed linear system (faster than "
            "nullspace+simplify on full Q(q) matrices). Full Hoefsmit "
            "construction with off-diagonal b·e_{T'} entries (fixes the "
            "H_4 script's bug). Gauge per partition follows the H_4 "
            "closed-form prop convention: c[last]=1 for hooks, adaptive "
            "for non-hooks ((3,2), (2,2,1) at H_5)."
        ),
        "engine": "sympy",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q_0_rational": "11099785955541805/10000000000000000",
        "results": results,
        "wall_time_s": time.time() - t_total,
        "partial": False,
    }
    out_path = Path(__file__).parent / "r-k-h5-symbolic.witness.json"
    with open(out_path, "w") as fp:
        json.dump(out, fp, indent=2, default=str)
    print(f"\nWitness: {out_path} ({time.time()-t_total:.1f}s total)")


if __name__ == "__main__":
    main()
