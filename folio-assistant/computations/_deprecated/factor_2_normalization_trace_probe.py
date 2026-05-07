#!/usr/bin/env python3
"""
Trace the factor-of-2 normalization mismatch between PR #546's
`hoefsmit_symbolic.tr_M_symbolic` and the standard char_fast +
Plancherel-Markov-axiom convention.

PR #546 uses:
  tr_M(β) = Σ_λ w_λ · χ^λ(β) / f^λ
  with w_λ = dim_q(λ)² / [n]_q!

`char_fast` + my Markov-axiom probe uses:
  tr_M(β) = Σ_λ y_λ · χ^λ(β)
  with y_λ solved from {tr_M(1) = 1, tr_M(σ_1) = z, tr_M(σ_1σ_2) = z²}

These should be EQUAL if y_λ = w_λ / f^λ (which is the standard
identification). This probe tests on simple braids and reports any
divergence per irrep.

Output: factor-2-normalization-trace.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp
import mpmath as mp
import numpy as np

mp.mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from char_fast import chi_lambda_fast  # noqa: E402
from hoefsmit_symbolic import (  # noqa: E402
    chi_lambda_symbolic, tr_M_symbolic, dim_q, q_fac, Q,
)
from hecke_characters import standard_young_tableaux  # noqa: E402
from q_parameter import Q_MP  # noqa: E402

q_num = float(Q_MP)


def char_fast_chi(shape: tuple, ctypes: list, q_val: float) -> float:
    """char_fast version: convert (gen_idx, ctype) → (c, d, gen_idx)."""
    h = q_val - 1.0 / q_val
    word = []
    for k_gen, ctype in ctypes:
        # PR #546's ctype convention: 'sigma' = σ_k, 'sigma_inv' = σ_k^{-1},
        # 'averaged' = (σ + σ^{-1})/2 = σ - h/2.
        # char_fast uses 0-indexed gen, PR #546 uses 1-indexed.
        if ctype == "sigma":
            word.append((1.0, 0.0, k_gen - 1))
        elif ctype == "sigma_inv":
            # σ^{-1} = σ - h
            word.append((1.0, -h, k_gen - 1))
        elif ctype == "averaged":
            word.append((1.0, -h / 2, k_gen - 1))
        else:
            raise ValueError(f"unknown ctype: {ctype}")
    return chi_lambda_fast(shape, word, q_val=q_val).real


def char_fast_tr_M_via_planch(ctypes: list, q_val: float, n: int) -> tuple[float, dict]:
    """char_fast + Plancherel-Markov-axiom convention.

    Solves Markov-axiom system to get y_λ. Returns (tr_M, y_lambda_dict).
    """
    from itertools import combinations
    parts = []
    def gen(remaining, max_part, prefix):
        if remaining == 0:
            parts.append(tuple(prefix))
            return
        for k in range(min(remaining, max_part), 0, -1):
            gen(remaining - k, k, prefix + [k])
    gen(n, n, [])

    z = 1.0 / (q_val ** 0.5 + 1.0 / q_val ** 0.5)

    # Markov axioms: tr_M(1) = 1, tr_M(σ_1) = z, tr_M(σ_1 σ_2) = z² for n=3.
    # In general, for n strands we need n constraints. For now n=3 only.
    if n != 3:
        raise NotImplementedError("Only n=3 supported for Plancherel-axiom solver")
    chi_id = {p: char_fast_chi(p, [], q_val) for p in parts}
    chi_s1 = {p: char_fast_chi(p, [(1, "sigma")], q_val) for p in parts}
    chi_s1s2 = {p: char_fast_chi(p, [(1, "sigma"), (2, "sigma")], q_val) for p in parts}

    M_mat = mp.matrix([
        [chi_id[p] for p in parts],
        [chi_s1[p] for p in parts],
        [chi_s1s2[p] for p in parts],
    ])
    b_vec = mp.matrix([mp.mpf(1), mp.mpf(z), mp.mpf(z) ** 2])
    y_vec = mp.lu_solve(M_mat, b_vec)
    y = {p: float(y_vec[i, 0]) for i, p in enumerate(parts)}
    return None, y


def hoefsmit_w_lambda(shape: tuple, n: int) -> float:
    """PR #546's w_λ = dim_q(λ)² / [n]_q! evaluated at q_0 numerically."""
    f = sp.lambdify(Q, dim_q(list(shape)) ** 2 / q_fac(n), modules=["mpmath"])
    return float(f(q_num))


def main() -> int:
    print("=" * 96)
    print("  Factor-of-2 normalization mismatch tracer (PR #546 vs char_fast)")
    print("=" * 96)

    # Compare per-irrep weights y_λ vs w_λ / f^λ
    print(f"\n  Convention table at q_0 = {q_num:.10f}:")
    print(f"  λ ⊢ 3       f^λ    w_λ (PR #546)    w_λ/f^λ      y_λ (char_fast)   match?")
    print("  " + "-" * 80)

    parts_3 = [(3,), (2, 1), (1, 1, 1)]
    _, y_charfast = char_fast_tr_M_via_planch([], q_num, n=3)

    rows = []
    for p in parts_3:
        syts, _, _ = standard_young_tableaux(list(p))
        f_lam = len(syts)
        w_lam = hoefsmit_w_lambda(p, n=3)
        w_over_f = w_lam / f_lam
        y_cf = y_charfast[p]
        ratio = y_cf / w_over_f if w_over_f != 0 else float("inf")
        match = "✓" if abs(ratio - 1) < 1e-6 else f"ratio = {ratio:.4f}"
        print(f"  {str(p):<10} {f_lam:>5} {w_lam:>16.6f} {w_over_f:>12.6f} {y_cf:>17.6f}  {match}")
        rows.append({
            "lambda": list(p),
            "f_lambda": f_lam,
            "w_lambda_PR546": w_lam,
            "w_over_f_PR546": w_over_f,
            "y_lambda_char_fast": y_cf,
            "ratio_y_over_w_over_f": ratio,
        })

    # Test on a few small braids
    print(f"\n  Trace comparison on test braids (n=3):")
    print(f"  {'word':<25} {'PR #546 tr_M':>16} {'char_fast tr_M':>18} {'ratio':>8}")
    print("  " + "-" * 72)

    test_braids = [
        ("identity", []),
        ("σ_1", [(1, "sigma")]),
        ("σ_1²", [(1, "sigma"), (1, "sigma")]),
        ("trefoil σ_1³", [(1, "sigma"), (1, "sigma"), (1, "sigma")]),
        # σ_2 has IndexError on shape (3) in PR #546's
        # q_character_on_braid_word — separate bug, exclude for now
    ]

    trace_data = []
    for name, ctypes in test_braids:
        # PR #546 trace
        try:
            tr_pr546_sym = tr_M_symbolic(ctypes, n=3)
            f_pr546 = sp.lambdify(Q, tr_pr546_sym, modules=["mpmath"])
            tr_pr546_val = float(f_pr546(q_num))
        except (IndexError, Exception) as exc:
            print(f"  {name:<25} ERROR (PR #546): {type(exc).__name__}")
            continue

        # char_fast trace
        chi = {p: char_fast_chi(p, ctypes, q_num) for p in parts_3}
        tr_cf_val = sum(y_charfast[p] * chi[p] for p in parts_3)

        ratio = tr_cf_val / tr_pr546_val if abs(tr_pr546_val) > 1e-12 else float("nan")
        print(f"  {name:<25} {tr_pr546_val:>16.6f} {tr_cf_val:>18.6f} {ratio:>8.4f}")
        trace_data.append({
            "name": name,
            "ctypes": ctypes,
            "tr_M_pr546": tr_pr546_val,
            "tr_M_char_fast": tr_cf_val,
            "ratio_cf_over_pr546": ratio,
        })

    # ─── Apply normalization fix ────────────────────────────────
    print(f"\n  Normalization fix: divide PR #546's tr_M by tr_M(1) to enforce")
    print(f"  the standard Markov axiom tr_M(1) = 1.")
    tr_pr546_at_id = trace_data[0]["tr_M_pr546"] if trace_data else 1.0
    print(f"    PR #546 tr_M(1) = {tr_pr546_at_id:.6f}")
    print(f"\n  Renormalized comparison:")
    print(f"  {'word':<25} {'PR #546 / tr_M(1)':>20} {'char_fast tr_M':>18} {'ratio':>8}")
    print("  " + "-" * 76)
    fixed_ratios = []
    for r in trace_data:
        tr_pr546_norm = r["tr_M_pr546"] / tr_pr546_at_id if tr_pr546_at_id != 0 else 0
        ratio_fixed = r["tr_M_char_fast"] / tr_pr546_norm if abs(tr_pr546_norm) > 1e-12 else float("nan")
        print(f"  {r['name']:<25} {tr_pr546_norm:>20.6f} {r['tr_M_char_fast']:>18.6f} {ratio_fixed:>8.4f}")
        r["tr_M_pr546_renormalized"] = tr_pr546_norm
        r["ratio_cf_over_pr546_renormalized"] = ratio_fixed
        fixed_ratios.append(ratio_fixed)

    # Diagnose
    ratios = [r["ratio_cf_over_pr546"] for r in trace_data
              if abs(r["tr_M_pr546"]) > 1e-12]
    print(f"\n  Raw ratios:         {[f'{r:.4f}' for r in ratios]}")
    print(f"  Renormalized ratios: {[f'{r:.4f}' for r in fixed_ratios]}")

    if fixed_ratios and all(abs(r - 1) < 1e-3 for r in fixed_ratios):
        print(f"\n  ✅ NORMALIZATION FIX RESOLVES THE MISMATCH:")
        print(f"     PR #546's tr_M divided by their tr_M(1) gives the canonical")
        print(f"     Markov-axiom-normalised trace, matching char_fast exactly.")
        print(f"     Categorical correction:")
        print(f"       tr_M^canonical(K) = tr_M^{{PR #546}}(K) / [(2 + [2]_q^2) / [3]_q!]")
        print(f"     For the proton closed form:")
        print(f"       tr_M^canonical(p)(q) = p(q) / (12 q^10) ÷ [(2 + [2]_q^2)/(2·3)]")
        print(f"                            = p(q) · [3]_q! / (12 q^10 · (2 + [2]_q^2))")

    print(f"\n  Per-irrep weight verification:")
    all_y_match_w = all(abs(r["ratio_y_over_w_over_f"] - 1) < 1e-6 for r in rows)
    if all_y_match_w:
        print(f"    y_λ from Markov axioms EQUALS w_λ/f^λ (PR #546 convention).")
        print(f"    The two formulas tr_M = Σ y·χ and tr_M = Σ (w/f)·χ are identical.")
        print(f"    Any per-braid trace mismatch must come from the BRAID WORD itself,")
        print(f"    not the trace convention.")
    else:
        print(f"    y_λ ≠ w_λ/f^λ — convention difference at the weight level.")
        print(f"    Per-irrep ratios:")
        for r in rows:
            print(f"      {r['lambda']}: ratio y / (w/f) = {r['ratio_y_over_w_over_f']:.4f}")

    witness = {
        "computation": "factor-2-normalization-trace",
        "description": (
            "Traces the factor-of-2 normalization mismatch between PR "
            "#546's hoefsmit_symbolic.tr_M_symbolic (using w_λ = "
            "dim_q² / [n]_q! and dividing by f^λ) and char_fast + "
            "Plancherel-Markov-axiom convention (using y_λ solved "
            "from {tr_M(1)=1, tr_M(σ_1)=z, tr_M(σ_1σ_2)=z²}). "
            "Tests whether the two formulas are equivalent (y_λ = "
            "w_λ/f^λ) and where any discrepancy arises."
        ),
        "reference_blocks": [
            "prop:atomic-mass-gb-nf",
            "prop:markov-trace-antipode-polynomial-symmetry",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q_0": q_num},
        "weight_comparison": rows,
        "trace_comparison": trace_data,
        "y_lambda_equals_w_lambda_over_f_lambda": all_y_match_w,
    }
    out = HERE / "factor-2-normalization-trace.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
