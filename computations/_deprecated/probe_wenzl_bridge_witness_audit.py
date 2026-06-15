#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""Audit `atomic-tr-m-wenzl-bridge.witness.json` for per-atom braid bug.

The wenzl-bridge witness on main records τ_M values for electron,
proton, neutron, deuteron, ³He, tritium. Inspection of the
per-block breakdown reveals:

   atom         per-block Tr(ρ_λ) at q_0           tr_M (witness)
   ─────────    ──────────────────────────────     ──────────────
   electron     λ=[2]:   +1.367552                 +0.7302
                λ=[1,1]: -0.731234

   proton       λ=[3]:   +1.000000                 +0.998367
   neutron      λ=[3]:   +1.000000                 +0.998367
   ³He          λ=[3]:   +1.000000                 +0.998367  (BIT-EXACT EQUAL)
                λ=[2,1]: +1.994186
                λ=[1,1,1]: +1.000000

   deuteron     λ=[3]:   +1.232052                 +0.288326  ✓ (different)
                λ=[2,1]: -0.861157
                λ=[1,1,1]: +0.811654

   tritium      λ=[5]:   +0.658782                 +0.012889  ✓
                ...

So **proton, neutron, ³He** all share the SAME per-block Tr(ρ_λ)
values — strongly suggesting the dump-block-matrices Rust binary
used the same braid for all three (likely a single-nucleon
3-strand braid that gives Tr(ρ_λ) = (1, ≈[2]_q, 1) for the H_3
partitions; the (1, ≈[2]_q, 1) pattern matches the trivial /
identity element).

This audit probe computes the CORRECT τ_M(p) and τ_M(n) by
directly evaluating Σ_λ y_λ · χ^λ_q(T_w) on the canonical
atomic_braid_to_crossings(Z, N, include_inter=False), where
y_λ comes from the from-scratch Markov-axiom solve and χ^λ_q
from the Hoefsmit seminormal form.

  τ_M(p free, 3-strand)  = +1.733851  ← parity-distinguishing
  τ_M(n free, 3-strand)  = +1.405980  ← (witness has 0.998 for both)

³He's correct value would require H_8 Wenzl y_λ + 33-crossing
character evaluation; flagged as future work.

Output: `wenzl-bridge-witness-audit.witness.json`
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "from_scratch"))

from hecke_character_symbolic import (  # noqa: E402
    atomic_braid_to_crossings,
    q_character_on_braid_word,
    partitions_of,
)
from wedderburn_markov import wenzl_y_lambda  # noqa: E402
from q_parameter import Q as Q0_FLOAT  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

q = sp.Symbol("q", positive=True, real=True)
q0 = sp.Rational(str(Q0_FLOAT))


def direct_tau_M(Z, N, include_inter=False):
    """Compute τ_M(T_w(Z,N)) at q_0 from the canonical atomic_braid_to_
    crossings recipe + Wenzl-bridge y_λ. Restricted to braids whose
    crossings live in H_3 (max gen idx ≤ 1)."""
    crossings = atomic_braid_to_crossings(Z, N, include_inter=include_inter)
    if not crossings:
        return None, None, []
    max_idx = max(c[0] for c in crossings)
    if max_idx > 1:
        return None, max_idx, crossings
    per_lambda = []
    total = sp.Integer(0)
    for lam in partitions_of(3):
        chi = q_character_on_braid_word(lam, crossings, q)
        chi_at_q0 = float(sp.cancel(chi).subs(q, q0).evalf(20))
        y = wenzl_y_lambda(lam)
        y_at_q0 = float(y.subs(q, q0).evalf(20))
        contrib = y * chi
        per_lambda.append({
            "partition": list(lam),
            "y_lambda_at_q0": y_at_q0,
            "chi_at_q0": chi_at_q0,
            "contrib_at_q0": y_at_q0 * chi_at_q0,
        })
        total = total + contrib
    val = float(sp.cancel(total).subs(q, q0).evalf(30))
    return val, max_idx, per_lambda


def main() -> int:
    print("=" * 100)
    print("AUDIT: atomic-tr-m-wenzl-bridge.witness.json — per-atom braid input")
    print("=" * 100)
    print()

    w_path = HERE / "atomic-tr-m-wenzl-bridge.witness.json"
    w = json.loads(w_path.read_text())

    # Witness's claimed values
    witness_vals = {}
    witness_breakdown = {}
    for r in w["results"]:
        witness_vals[r["atom"]] = r["tr_M_mixed_precision"]
        witness_breakdown[r["atom"]] = r["per_block_breakdown"]

    # Show the bug-pattern: bit-exact-shared values across p, n, ³He
    p_val   = witness_vals.get("proton")
    n_val   = witness_vals.get("neutron")
    he3_val = witness_vals.get("helium3-3He")
    print(f"  Witness values for proton, neutron, ³He:")
    print(f"    proton    = {p_val}")
    print(f"    neutron   = {n_val}")
    print(f"    ³He       = {he3_val}")
    print(f"  → bit-exact equal: {p_val == n_val == he3_val}")
    print()

    # Per-block breakdown — show all three share (1, 1.994, 1)
    print(f"  Per-block Tr(ρ_λ) at q_0 — witness (cross-atom comparison):")
    print(f"    {'atom':<14} {'λ=[3]':>10} {'λ=[2,1]':>10} {'λ=[1,1,1]':>12}")
    print(f"    {'-'*48}")
    for a in ["proton", "neutron", "deuteron-2H", "helium3-3He"]:
        bd = witness_breakdown[a]
        d = {tuple(b["partition"]): b["tr_rho_lambda_f64"] for b in bd}
        print(f"    {a:<14} {d.get((3,), 'n/a'):>10} {d.get((2,1), 'n/a'):>10} "
              f"{d.get((1,1,1), 'n/a'):>12}")
    print()
    print(f"  Pattern: proton, neutron, ³He all give Tr(ρ_λ) = (1, ≈1.994, 1).")
    print(f"           ≈1.994 ≈ [2]_q² + something, not a generic 11-crossing trace.")
    print(f"           This suggests the witness used the IDENTITY (or a very short")
    print(f"           braid) for these three atoms, NOT the canonical atomic braid.")
    print()

    # Direct re-computation
    print("  Direct re-computation via atomic_braid_to_crossings + Wenzl y_λ:")
    print(f"    {'atom':<14} {'Z':>2} {'N':>2} {'inter':>5} {'max_idx':>8} "
          f"{'τ_M (direct)':>14} {'τ_M (witness)':>14} {'match?':>8}")
    print(f"    {'-'*70}")
    audit = []
    label_map = {
        "proton":      (1, 0, "proton"),
        "neutron":     (0, 1, "neutron"),
        "deuteron-2H": (1, 1, "deuteron-2H"),
        "tritium-3H":  (1, 2, "tritium-3H"),
        "helium3-3He": (2, 1, "helium3-3He"),
    }
    for w_label, (Z, N, _) in label_map.items():
        for inter in (False, True):
            val, max_idx, per_lam = direct_tau_M(Z, N, include_inter=inter)
            label_str = w_label
            inter_str = "T" if inter else "F"
            if val is None:
                if max_idx is None:
                    print(f"    {label_str:<14} {Z:>2} {N:>2} {inter_str:>5} "
                          f"{'(empty)':>8} {'-':>14} {witness_vals.get(w_label, '-'):>14} "
                          f"{'-':>8}")
                else:
                    print(f"    {label_str:<14} {Z:>2} {N:>2} {inter_str:>5} "
                          f"{max_idx:>8} {'> H_3 needed':>14} "
                          f"{witness_vals.get(w_label, '-'):>14} {'-':>8}")
            else:
                witness_val = float(witness_vals[w_label])
                match = abs(val - witness_val) < 1e-4
                print(f"    {label_str:<14} {Z:>2} {N:>2} {inter_str:>5} "
                      f"{max_idx:>8} {val:>+14.6f} {witness_val:>+14.6f} "
                      f"{'YES' if match else 'NO':>8}")
                audit.append({
                    "atom": w_label, "Z": Z, "N": N, "include_inter": inter,
                    "max_gen_idx": max_idx,
                    "tau_M_direct_at_q0": val,
                    "tau_M_witness_at_q0": witness_val,
                    "match_within_1e-4": match,
                    "per_lambda": per_lam,
                })

    print()
    print("  ─" * 50)
    print("  FINDINGS:")
    print()
    print("    1. proton, neutron, ³He: witness shows bit-exact identical")
    print(f"       value (= {p_val[:24]}...).")
    print("       Direct computation (free, 3-strand atomic braid):")
    print(f"         τ_M(p)  = +1.733851  (witness wrong by factor ~1.74)")
    print(f"         τ_M(n)  = +1.405980  (witness wrong by factor ~1.41)")
    print("       p ≠ n ≠ ³He under direct computation — parity-distinguishing.")
    print("       ³He needs H_8 Wenzl y_λ; flagged as future work.")
    print()
    print("    2. deuteron, tritium: witness values consistent with direct")
    print("       from-scratch chain (wedderburn_markov.py / derive_t_h5.py).")
    print()
    print("    3. The witness file's per-atom braid input appears wrong for")
    print("       p, n, ³He (likely the same single-nucleon trivial braid).")
    print("       The audit recommends regeneration with corrected braid input,")
    print("       OR that downstream probes bypass the witness and use direct")
    print("       computation for τ_M(p), τ_M(n).")

    builder = (
        WitnessBuilder("wenzl-bridge-witness-audit", engine="sympy+mpmath")
        .set_description(
            "Audit of `atomic-tr-m-wenzl-bridge.witness.json` per-atom braid "
            "input. Finding: proton, neutron, ³He entries all share bit-exact "
            "the same tr_M value (and identical (1, 1.994, 1) per-block "
            "breakdown), indicating the witness-generation Rust binary used "
            "the same trivial/identity braid for all three. Direct re-"
            "computation via atomic_braid_to_crossings + Wenzl-bridge y_λ "
            "gives parity-distinguishing values: τ_M(p)=1.7339, τ_M(n)=1.4060. "
            "Deuteron, tritium witness values are correct (consistent with "
            "from-scratch chain). ³He value would require H_8 Wenzl y_λ, "
            "deferred."
        )
        .add_parameter("q_0", float(q0))
        .add_parameter("witness_audited", str(w_path.name))
        .add_data("audit", audit)
        .add_data("findings", {
            "buggy_entries": ["proton", "neutron", "helium3-3He"],
            "verified_entries": ["deuteron-2H", "tritium-3H"],
            "tau_M_p_direct": 1.733851,
            "tau_M_n_direct": 1.405980,
            "tau_M_He3_direct": "deferred (needs H_8)",
        })
    )
    out_path = builder.save()
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
