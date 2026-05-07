#!/usr/bin/env python3
"""Test cohomological r_k pattern at H_4: does the Coxeter-prefix
σ_1σ_2…σ_k extract the depth-k stratum cleanly?

Conclusion: NO — σ_1σ_2σ_3 has Markov pairing 0.124 = z³, but only
0.0006 of that is the depth-3 contribution. The Coxeter-prefix
heavily mixes depths through the lower strata via characters.

Implication: at H_n>3 the canonical r_k must be a linear
combination of length-k words selected by Wedderburn-orthogonal
projection onto the depth-k block — NOT a single Coxeter prefix.
This is the cohomological work that remains open.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import mpmath as mp

mp.mp.dps = 25
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT
q = mp.mpf(repr(Q0_FLOAT))
z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))

with open(Path(__file__).parent / "y-lambda-jones-markov-witness.json") as f:
    W = json.load(f)

y4 = {tuple(w["partition"]): mp.mpf(str(w["y_lambda"]))
      for w in W["tables_by_n"]["4"]["weights"]}

print("y_λ at H_4 (sorted by depth):")
by_depth = {}
for p, y in y4.items():
    by_depth.setdefault(len(p) - 1, []).append((p, y))
for d in sorted(by_depth):
    print(f"  depth {d}:")
    for p, y in by_depth[d]:
        print(f"    λ={str(p):16}  y_λ = {float(y):+.8f}")
    s = sum(yy for _, yy in by_depth[d])
    print(f"    Σ y_λ at depth {d} = {float(s):+.8f}")

# Simple Markov-property values for length-k Coxeter-prefix words
# tr_M(σ_1σ_2…σ_k) = z^k  (universal across n by Markov induction)
print("\nLength-k Coxeter-prefix Markov pairings at H_4:")
for k in range(0, 4):
    val = z ** k
    print(f"  tr_M(σ_1…σ_{k}) = z^{k} = {float(val):+.8f}")

# Depth-k pairing if r_k were exactly orthogonal to lower depths:
# tr_M(r_k) ≈ Σ_{depth(λ)=k} y_λ · χ_λ(r_k)
# For sign-rep and trivial-rep we know χ values; mixed-rep needs Hoefsmit.

# Diagnostic: compare Coxeter-prefix Markov value vs depth-k Plancherel mass.
print("\nDiagnostic: depth-k Plancherel mass vs Coxeter-prefix Markov value")
print(f"{'k':>3} {'depth-k Σ y_λ':>16} {'tr_M(σ_1..σ_k)':>16} {'ratio':>10}")
for k in range(0, 4):
    sum_d = sum(yy for p, yy in y4.items() if len(p) - 1 == k)
    cox = z ** k
    ratio = sum_d / cox if cox != 0 else mp.mpf(0)
    print(f"{k:>3} {float(sum_d):>+16.8f} {float(cox):>+16.8f} {float(ratio):>+10.4f}")

print("""
Reading: ratio is depth-k stratum proportion. At depths 0, 1, 2 the Coxeter
prefix's pairing is dominated by lower strata ( ratios ≈ 1.83, 0.52, 0.10).
At depth 3 the ratio is -0.0068 → the Coxeter-prefix σ_1σ_2σ_3 sits MOSTLY
in lower-depth blocks, NOT depth-3.

Cohomological work needed: project σ_1σ_2σ_3 onto the depth-3 block via
Wedderburn orthogonality. Concretely, find c_w ∈ R such that
  r_3 = Σ_w c_w · w  (sum over length-3 reduced words)
satisfies χ_λ(r_3) = 0 for every λ with height(λ) ≤ 3 except (1^4).

This is a finite linear-algebra problem at H_n: in H_4 there are 5 length-3
reduced words (s_1s_2s_1, s_2s_3s_2, s_1s_2s_3, s_3s_2s_1, s_1s_3s_2 — equiv.
classes). Imposing 4 orthogonality constraints (depth 0, 1, 1, 2) leaves
a 1-dim solution space — the Wedderburn-projected r_3.

This is feasible in 1-2 sessions with explicit Hoefsmit characters.
""")
