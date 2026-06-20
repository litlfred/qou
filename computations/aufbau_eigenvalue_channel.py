#!/usr/bin/env python3
"""
Aufbau order from the eigenvalue CHANNEL the angular ℓ couples to — the duality
question (owner, 2026-06-20): is the Frobenius pairing being used correctly, and
can the compact↔noncompact (λ₊↔λ₋) duality supply the right ℓ-grading?

T_γe eigenvalues: λ₊ = q₀ (dominant), λ₋ = −1/q₀ (sub-dominant), λ₊·λ₋ = det = −1
(bar-dual, duality-tracker D1). The angular ℓ can be read on three channels:

  (A) sub-dominant λ₋ via the RATIO (λ₋/λ₊)^ℓ = q^{−2ℓ}   → key K=n−2ℓ, a=−2
      — #2531 (merged). The NON-Perron term.
  (B) dominant λ₊:  λ₊^ℓ = q^{+ℓ}                         → key K=n+ℓ,  a=+1
      — the Perron-leading term of the Markov/Frobenius trace.
  (C) compact loop-trace of V_ℓ:  [2ℓ+1]_q ~ q^{+2ℓ}      → key K=n+2ℓ, a=+2
      — the full Frobenius trace (the capacity object).

The Markov/Frobenius pairing V̂(n) = z(Tⁿ)₁₁+(Tⁿ)₂₁ ~ λ₊ⁿ is **Perron-dominated
by λ₊** (that is exactly why the radial energy is λ₊ⁿ). So the Frobenius-leading
reading of the angular ℓ — ℓ extra Perron (λ₊) transfer steps — is channel (B),
a=+1. This script checks which channel reproduces the empirical **Aufbau fill
order** (4s before 3d, …).

HONEST SCOPE: this tests the fill ORDER (the sequence), not the noble-gas
closure POSITIONS — in the integer key K=n+ℓ the np and (n+1)s subshells are
TIED, so inertness/closure gaps need the actual energies, not K alone. And
"angular ℓ = ℓ λ₊ transfer steps" is the conditional modeling reading (B); the
Perron-dominance makes it the *leading* Frobenius term, but whether ℓ enters as
λ₊-steps (vs the loop-trace C) is the open structural choice the duality must fix.
"""
from __future__ import annotations
import sys
sys.path.insert(0, "substrate"); sys.path.insert(0, ".")
from q_parameter import Q as q0, Q_INV as qi0
q0, qi0 = float(q0), float(qi0)

LET = "spdfghi"
NMAX = 6
ORB = [(n, l) for n in range(1, NMAX + 1) for l in range(n)]


def aufbau_reference():
    """Empirical Madelung/Aufbau order: increasing n+ℓ, ties by increasing n."""
    return sorted(ORB, key=lambda o: (o[0] + o[1], o[0]))


def order_by(key):
    return sorted(ORB, key=lambda o: (key(*o), o[0]))


def fmt(seq, k=12):
    return " ".join(f"{n}{LET[l]}" for n, l in seq[:k])


def main() -> int:
    ref = aufbau_reference()
    print(f"  AUFBAU ORDER FROM THE EIGENVALUE CHANNEL   q₀={q0:.5f}  "
          f"λ₊={0.5*((q0-qi0)+((q0-qi0)**2+4)**.5):.5f}  λ₋={0.5*((q0-qi0)-((q0-qi0)**2+4)**.5):.5f}\n")
    print(f"  empirical Aufbau ref:  {fmt(ref)}\n")
    channels = [
        ("(A) λ₋ sub-dominant via ratio   K=n−2ℓ  a=−2  [#2531, non-Perron]", lambda n, l: n - 2 * l),
        ("(B) λ₊ dominant  λ₊^ℓ           K=n+ℓ   a=+1  [Perron-leading]", lambda n, l: n + l),
        ("(C) compact loop-trace q-dim    K=n+2ℓ  a=+2  [full Frobenius trace]", lambda n, l: n + 2 * l),
    ]
    for label, key in channels:
        seq = order_by(key)
        match = (seq == ref)
        # also report first divergence from Aufbau
        div = next((i for i in range(min(len(seq), len(ref))) if seq[i] != ref[i]), None)
        tag = "MATCHES Aufbau ✓" if match else f"diverges at #{div} ({fmt([seq[div]],1)} vs {fmt([ref[div]],1)})"
        print(f"  {label}")
        print(f"      {fmt(seq)}")
        print(f"      → {tag}\n")
    print("### Reading")
    print("  • Only channel (B) — angular ℓ in the DOMINANT λ₊ (a=+1) — reproduces")
    print("    the empirical Aufbau fill order (4s<3d, 5s<4d, 6s<4f…).")
    print("  • (A) λ₋ sub-dominant (a=−2, #2531) and (C) loop-trace q-dim (a=+2)")
    print("    both diverge: (A) fills high-ℓ first; (C) is ns-dominated.")
    print("  • The Markov/Frobenius trace is PERRON-dominated by λ₊, so (B) is its")
    print("    leading angular term — this is the 'use the Frobenius pairing")
    print("    correctly' answer: the dominant-eigenvalue (noncompact-Perron)")
    print("    reading gives Aufbau; the loop-trace (compact) reading overshoots.")
    print("  • OPEN (honest): (B) reproduces the ORDER, not the noble-gas closure")
    print("    POSITIONS (np/(n+1)s are K-tied; gaps need actual energies). And")
    print("    'ℓ = ℓ λ₊-steps' is the conditional reading the duality must FORCE")
    print("    (vs the loop-trace C); Perron-dominance makes it leading, not proven.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
