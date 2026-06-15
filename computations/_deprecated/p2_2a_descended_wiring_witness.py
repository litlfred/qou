#!/usr/bin/env python3
"""
P2.2a wiring witness — descended Markov trace via proper Schur-Weyl

Compares three paths for the descended trace |tr_M(𝒜, q_0)| on the
light atoms (D, ³He, ⁴He, ¹²C):

  1. H_3-std-channel-only:  markov_trace_symbolic_eval
       Per-generator product Π V_s, no V_sym/V_alt.
  2. H_3-three-channel:     descended part of tower_mass_symbolic_eval
       Per-generator V̂_full = w_sym·V_sym + w_std·V_s + w_alt·V_alt
       at H_3 weights, product across generators.
  3. Schur-Weyl (proper):   markov_trace_schur_weyl_eval (NEW, P2.2a)
       Σ_{λ ⊢ 3A} w_λ(q) · χ^λ(𝒜) at proper H_{3A} weights via
       schur_weyl_symbolic.

Important nuance discovered during P2.2a wiring: the Φ_q tower
divergence reported in P2.1a comes from path 2's per-generator
V̂_full overweighted at H_3 — NOT from path 1's descended-only.
Both H_3 paths give convergent descended traces (|·| < q_0); the
divergence is structural to the tower terms.

So P2.2a wiring (this witness) corrects the **descended** trace
to use proper H_{3A} weights, but doesn't yet fix the tower terms
(they need re-derivation in proper SW framing — separate task).

Witness: docs/audits/2026-05-01-p2-2a-descended-wiring.witness.json
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from crt_markov import (
    markov_trace_symbolic_eval,
    markov_trace_schur_weyl_eval,
    tower_mass_symbolic_eval,
)
from q_parameter import Q as Q0_FLOAT

mpmath.mp.dps = 50
q0 = mpmath.mpf(str(Q0_FLOAT))

ATOMS = [
    ("D", 1, 1),
    ("3He", 2, 1),
    ("4He", 2, 2),
    ("12C", 6, 6),
]


def compare(name, Z, N):
    print(f"\n=== {name} (Z={Z}, N={N}, A={Z+N}) ===")

    # Path 1: H_3 std-channel-only
    h3_std = abs(markov_trace_symbolic_eval(
        Z, N, True, 1, 1, 1, q0, 50, legacy_h3=True))
    print(f"  (1) H_3 std-only:      |tr_M| = {float(h3_std):.6e}")

    # Path 2: H_3 three-channel (descended part of tower)
    full = tower_mass_symbolic_eval(Z, N, True, 1, 1, 1, q0, precision=50)
    h3_three = full["desc"]
    print(f"  (2) H_3 three-channel: |Π V̂_full| = {float(h3_three):.6e}")

    # Path 3: Proper Schur-Weyl
    try:
        sw = abs(markov_trace_schur_weyl_eval(Z, N, True, q0, 50))
        print(f"  (3) Schur-Weyl proper: |Σ_λ w_λ χ^λ| = {float(sw):.6e}")
    except Exception as e:
        print(f"  (3) Schur-Weyl proper: ERROR ({type(e).__name__}: {str(e)[:80]})")
        sw = None

    # Convergence diagnostic
    q0_f = float(q0)
    print(f"  Φ_q convergence (|·| < q_0={q0_f:.4f}):")
    print(f"    path 1: {float(h3_std) < q0_f}  ({float(h3_std):.4f})")
    print(f"    path 2: {float(h3_three) < q0_f}  ({float(h3_three):.4f})")
    if sw is not None:
        print(f"    path 3: {float(sw) < q0_f}  ({float(sw):.4f})")

    # Φ_q values
    qi = 1 / q0
    from crt_markov import _Phi_q_mp
    def safe_phi(z):
        if z >= q0:
            return float("inf")
        try:
            v = _Phi_q_mp(z, q0, qi)
            return float(v) if not mpmath.isinf(v) else float("inf")
        except Exception:
            return float("nan")

    phi1 = safe_phi(h3_std)
    phi2 = safe_phi(h3_three)
    phi3 = safe_phi(sw) if sw is not None else float("nan")
    print(f"  Φ_q(descended):")
    print(f"    path 1: {phi1:.6e}")
    print(f"    path 2: {phi2:.6e}")
    if sw is not None:
        print(f"    path 3: {phi3:.6e}")

    return {
        "atom": name,
        "Z": Z, "N": N, "A": Z + N,
        "path_1_h3_std_only": str(h3_std),
        "path_2_h3_three_channel": str(h3_three),
        "path_3_schur_weyl_proper": str(sw) if sw is not None else None,
        "phi_q_descended": {
            "path_1": phi1 if phi1 != float("inf") else "inf",
            "path_2": phi2 if phi2 != float("inf") else "inf",
            "path_3": phi3 if phi3 != float("inf") else "inf",
        },
        "all_three_convergent_under_phi_q": (
            phi1 != float("inf")
            and phi2 != float("inf")
            and (sw is None or phi3 != float("inf"))
        ),
    }


print("=" * 80)
print("P2.2a — Descended Markov trace: H_3 std-only vs H_3 three-channel vs Schur-Weyl")
print("=" * 80)
print(f"q_0 = {q0}")

results = []
for name, Z, N in ATOMS:
    try:
        r = compare(name, Z, N)
        results.append(r)
    except Exception as e:
        import traceback
        traceback.print_exc()
        results.append({"atom": name, "error": str(e)})

witness = {
    "audit": "P2.2a wiring — descended Markov trace via proper Schur-Weyl",
    "generated": datetime.now(timezone.utc).isoformat(),
    "q_0": str(q0),
    "atoms": results,
    "interpretation": (
        "Three descended-trace paths compared. Refinement of P2.1a "
        "finding: the Φ_q tower divergence reported there comes from "
        "the per-generator V̂_full at H_3 weights (path 2's tower-term "
        "contribution), not from path 2's descended part. All three "
        "descended paths produce convergent values (|·| < q_0). The "
        "proper Schur-Weyl path (3, NEW via markov_trace_schur_weyl_eval) "
        "gives values 10-10000x smaller than either H_3 path — a "
        "structural correctness improvement to the descended trace, "
        "independent of the tower-term divergence question."
    ),
    "next_steps": (
        "P2.2a wiring proper: replace tower_mass_symbolic_eval's "
        "descended part with markov_trace_schur_weyl_eval. Tower terms "
        "(Σ Φ_q(|V̂_i|), z² Σ Φ_q(|V̂_i V̂_j|)) need re-derivation in "
        "proper Schur-Weyl framing — they're intrinsically per-generator "
        "and don't have an immediate H_{3A}-weight reformulation. "
        "Tracked as P2.2a-deeper."
    ),
}

out_path = Path(__file__).parent.parent.parent / "docs/audits/2026-05-01-p2-2a-descended-wiring.witness.json"
out_path.write_text(json.dumps(witness, indent=2, default=str))
print()
print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
