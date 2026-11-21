# H8 result: an open categorical trace with a boundary object (2026-11-21)

Pre-registration: `h8_preregistration.md`. Script: `h8_open_trace_probe.py`, output in `.out.txt`.
Exact sympy. q₀ is the proton pin.

## The open trace

For V³:
- the closed trace has `T_p/T_n = q²` exactly (the pivot);
- the boundary trace is `B_p = −q s(q⁶−3q⁴+3q²−3)` and `B_n = s(q⁶−2q⁴+3q²−1)/q⁵`;
- `B` is free of `xy` and proportional to `s = x + y`.

With the boundary inheriting the same λ, the wall's effect beyond the pivot is

  `D(s) = [(T_n + B_n)/(T_p + B_p)] / (T_n/T_p)`.

## Candidates

| | s | corpus status | D at q = 1 | D at q₀ |
|---|---|---|---|---|
| N1 folding | `h = q − q⁻¹` | **conditional**: `conj:type-b-folding-cpt` folds the Cartan datum but does not state the boundary eigenvalues; matching them to the crossing's `{q, −q⁻¹}` is a reading | 1 | 0.93995737184425521828 |
| N2 involutive | 0 | convention; null | 1 | 1 |
| N3 unit Markov | `(q²+1)/q²` | convention chosen here | 5/7 | 0.73098688585601506837 |
| N4 quantum dim | `[2]/q` | convention chosen here (identical to N3) | 5/7 | 0.73098688585601506837 |

## Verdict

**No hit.** No corpus statement fixes `s`.

The structure is clear, though:
- under folding the wall enters at order `h`, vanishes at `q = 1`, and gives a 6 % change at q₀;
- under N3/N4 it gives an order-1 change (5/7 at `q = 1`), as expected for a boundary that carries
  the bulk λ.

So if folding were derived (boundary eigenvalues equal to the crossing's), the wall would be a
q-deformation effect that disappears classically. That is the qualitative shape a small splitting
needs.

`D` is not a mass: the trace-to-MeV map is not derived (B1). So no comparison with CODATA is made.

## What would make N1 a hit

A corpus derivation that the type-B boundary generator obeys the same Hecke relation as a crossing,
`(τ − q)(τ + q⁻¹) = 0`. One route is the standard embedding of type-B braids as symmetric braids on
doubled strands, where `τ` maps to a middle crossing. But the 2×2 `𝒦` used here is not that image: the
folded image acts on a doubled strand. So this needs its own construction.

Caveat: this is `M_QCD` only, for the V³ special pair; the general γγ pair is not swept.
