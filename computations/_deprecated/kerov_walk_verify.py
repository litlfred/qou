#!/usr/bin/env python3
"""
Verify Σ_λ 1/d_λ = 5/2 at n=3 via Young-lattice walks, and explore
what kind of walk naturally produces this sum.

Candidate walks on Young lattice (n=3 → 3 shapes: (3), (2,1), (1,1,1)):

  1. Uniform-step walk: at each step pick uniformly among add-a-box
     choices.  Ends at (λ) with probability P_us(λ).

  2. Plancherel walk: P(λ → μ added-box) = d_μ/d_λ · 1/(n+1).
     Stationary distribution π_λ = d_λ²/n!

  3. Uniform-endpoint weighting: P(λ) = 1/k (k = # partitions).

  4. Reciprocal-dim weighting: P(λ) = (1/d_λ) / Σ_μ 1/d_μ.

Which of these naturally equals 5/2 (as a sum, not a probability)?

The "sum over endpoints weighted by inverse number-of-paths" gives
exactly Σ 1/d_λ — i.e., if each path contributes 1/(d_λ at its
endpoint) and we sum over ALL paths, we get Σ_λ d_λ · (1/d_λ) = k.

For the 5/2 itself to emerge as a Plancherel-like quantity, we need
a DIFFERENT operation: e.g., "inverse path count" summed over
endpoints = Σ 1/d_λ.  That's just the definition.

This script verifies:
  (a) the hook-length sum Σ 1/d_λ = 5/2 for n=3 (cross-check)
  (b) numerical simulation of uniform-step walk gives (1/4, 1/2, 1/4)
  (c) numerical simulation of Plancherel walk gives (1/6, 4/6, 1/6)
  (d) Σ 1/d_λ emerges from the sum Σ_paths 1/d_λ (= k = # partitions)
      NOT from probability sums under either walk

Conclusion: Σ_λ 1/d_λ = 5/2 is not a STATIONARY distribution of any
natural Kerov walk.  It's the sum of "reciprocal path counts"
summed over endpoints, which equals the number of partitions k only
when we don't weight by d_λ.  For n=3: k=3 (different from 5/2).
Only Σ 1/d_λ gives 5/2, with no natural walk interpretation found.
"""
from __future__ import annotations

import sys, json
from fractions import Fraction
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))

from hecke_characters import partitions_of, young_hooks


def classical_dim(shape):
    n = sum(shape); hooks = young_hooks(shape)
    f = 1
    for k in range(2, n + 1): f *= k
    hp = 1
    for h in hooks: hp *= h
    return f // hp


def add_box_options(shape):
    """All shapes obtainable by adding one box to given shape."""
    shape = list(shape)
    options = []
    # Can add box at end of any existing row if strictly shorter than
    # the previous row (preserves partition order).
    for i in range(len(shape)):
        if i == 0 or shape[i] < shape[i - 1]:
            new = list(shape)
            new[i] += 1
            options.append(tuple(new))
    # Or start a new row at the bottom (adding a (1) row)
    if shape:
        if shape[-1] > 1 or True:
            new = shape + [1]
            options.append(tuple(new))
    else:
        options.append((1,))
    # Dedupe (order-agnostic)
    return list(dict.fromkeys(options))


def uniform_step_walk(n=3):
    """Compute uniform-step end-distribution at level n."""
    # State: dict {shape: prob}
    state = {(): Fraction(1)}
    for step in range(n):
        new_state = {}
        for shape, p in state.items():
            opts = add_box_options(shape)
            w = Fraction(1, len(opts))
            for opt in opts:
                new_state[opt] = new_state.get(opt, Fraction(0)) + p * w
        state = new_state
    return state


def plancherel_walk(n=3):
    """Plancherel growth: P(λ → μ ⊃ λ) = d_μ/((n+1)·d_λ).
    Stationary distribution at level n is d_λ²/n!."""
    state = {(): Fraction(1)}
    for step in range(n):
        new_state = {}
        for shape, p in state.items():
            d_shape = classical_dim(shape) if shape else 1
            opts = add_box_options(shape)
            for opt in opts:
                d_opt = classical_dim(opt)
                # P(shape → opt) = d_opt / ((step+1) · d_shape)
                w = Fraction(d_opt, (step + 1) * d_shape)
                new_state[opt] = new_state.get(opt, Fraction(0)) + p * w
        state = new_state
    return state


def main() -> int:
    print("=" * 100)
    print("KEROV WALK VERIFICATION: Σ_λ 1/d_λ = 5/2 at n=3?")
    print("=" * 100)
    # (a) hook-length cross-check
    s = Fraction(0)
    for shape in partitions_of(3):
        d = classical_dim(shape)
        print(f"  λ = {shape}:  d_λ = {d},  1/d_λ = {Fraction(1,d)}")
        s += Fraction(1, d)
    print(f"  Σ 1/d_λ = {s} = {float(s):.6f}")
    print()

    # (b) uniform-step walk
    print("(b) UNIFORM-STEP walk end-distribution at n=3:")
    us = uniform_step_walk(3)
    for shape, p in sorted(us.items(), key=lambda kv: (-max(kv[0]), kv[0])):
        print(f"    P({shape}) = {p} = {float(p):.6f}")
    print(f"    Σ P = {sum(us.values())} = {float(sum(us.values())):.6f}")
    print()

    # (c) Plancherel walk
    print("(c) PLANCHEREL walk end-distribution at n=3:")
    pw = plancherel_walk(3)
    for shape, p in sorted(pw.items(), key=lambda kv: (-max(kv[0]), kv[0])):
        d = classical_dim(shape)
        expected = Fraction(d * d, 6)    # n! = 6 for n=3
        print(f"    P({shape}) = {p} = {float(p):.6f}  "
              f"(Plancherel π_λ = d_λ²/n! = {expected})")
    print(f"    Σ P = {sum(pw.values())} = {float(sum(pw.values())):.6f}")
    print()

    # (d) Relationship to Σ 1/d_λ
    print("(d) Σ_λ 1/d_λ vs natural walk sums:")
    print(f"    Σ 1/d_λ                         = {s} = {float(s):.6f}")
    print(f"    Σ 1 (= number of partitions k)  = {sum(1 for _ in partitions_of(3))}")
    print(f"    Σ d_λ                           = {sum(classical_dim(sh) for sh in partitions_of(3))}")
    print(f"    Σ d_λ²                           = n! = {sum(classical_dim(sh)**2 for sh in partitions_of(3))}")
    print()

    # Uniform over endpoints × path count
    print("(e) Uniform-endpoint weighting P_uni(λ) = 1/k:")
    k = sum(1 for _ in partitions_of(3))
    for shape in partitions_of(3):
        d = classical_dim(shape)
        print(f"    λ = {shape}:  P_uni = 1/{k} = {Fraction(1,k)},  "
              f"P_uni·d_λ = {Fraction(d,k)},  1/d_λ = {Fraction(1,d)}")
    print()

    # Normalized reciprocal-dim as probability
    print("(f) Reciprocal-dim probability P_rd(λ) = (1/d_λ) / Σ 1/d_μ:")
    for shape in partitions_of(3):
        d = classical_dim(shape)
        P_rd = Fraction(1, d) / s
        print(f"    λ = {shape}:  P_rd = {Fraction(1,d)} / {s} = {P_rd} = {float(P_rd):.6f}")
    print()

    print("CONCLUSION: Σ_λ 1/d_λ = 5/2 is not a stationary distribution "
          "of any natural Kerov walk.")
    print("  - Uniform-step walk:        (1/4, 1/2, 1/4)")
    print("  - Plancherel walk:          (1/6, 4/6, 1/6)")
    print("  - Reciprocal-dim prob:      (2/5, 1/5, 2/5) after normalization")
    print()
    print("5/2 arises from SUMMING 1/d_λ without normalization — it's a "
          "Plancherel-dual quantity:")
    print("  Σ 1/d_λ · d_λ² = Σ d_λ       (first moment of Plancherel)")
    print("  Σ 1/d_λ        = Σ_λ 1/d_λ   (our sum)")
    print()
    # Recompute via character orthogonality
    # Σ 1/d_λ = Σ_λ (χ_λ(e)/|S_n|) · (|S_n|/d_λ²) = (1/n!) · Σ |S_n|/d_λ
    # = Σ 1/d_λ (trivially)
    # More useful: Σ 1/d_λ = (1/n!) · Σ_λ (n!/d_λ) = (1/n!) · Σ h(λ)
    # where h(λ) = product of hook lengths.
    h_sum = sum(Fraction(1) * Fraction(6, classical_dim(sh)) for sh in partitions_of(3))
    h_sum_direct = 0
    for shape in partitions_of(3):
        hooks = young_hooks(shape)
        h = 1
        for x in hooks: h *= x
        h_sum_direct += h
    print(f"(g) Hook-length product sum Σ h(λ) over partitions of n=3:")
    for shape in partitions_of(3):
        hooks = young_hooks(shape)
        h = 1
        for x in hooks: h *= x
        print(f"    λ = {shape}: hooks = {hooks}, h(λ) = {h}")
    print(f"    Σ h(λ) = {h_sum_direct}")
    print(f"    Σ h(λ) / n! = {h_sum_direct}/6 = {Fraction(h_sum_direct, 6)}")
    print()
    print("  → Σ_λ 1/d_λ = (Σ h(λ)) / n!  (by d_λ = n!/h(λ))")

    witness = {
        "computation": "kerov-walk-verify",
        "description": (
            "Verify Σ_λ 1/d_λ = 5/2 at n=3 and explore whether it arises "
            "from a natural Kerov walk.  Finds: the uniform-step and "
            "Plancherel walks give different distributions; Σ 1/d_λ is a "
            "Plancherel-dual quantity equal to Σ h(λ)/n! where h(λ) is the "
            "hook-length product.  No natural walk interpretation found."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "sum_inv_d_n3": str(s),
        "sum_h_n3": h_sum_direct,
        "n_factorial_n3": 6,
        "uniform_step_dist": {str(k): str(v) for k, v in us.items()},
        "plancherel_dist": {str(k): str(v) for k, v in pw.items()},
    }
    out = Path(__file__).parent / "kerov-walk-verify.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
