# H₄(q) NF tables + the H₃ ↪ H₄ Markov stabilization rung, Lean-grade (2026-07-19)

**Bean:** `qou-h4st` (categorical tranche, gap-closing run).
**Preflight (provenance):** [`computations/probes/hecke_h4_nf_table_preflight.py`](../../computations/probes/hecke_h4_nf_table_preflight.py)
→ `hecke-h4-nf-table-preflight.witness.json` — 5/5 PASS, symbolic-exact over ℚ(z,h).
**Lean:** [`QOU/Machinery/HeckeH4StabilizationRung.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/HeckeH4StabilizationRung.lean)
— sorry-free, `lean`-direct exit 0. §7c-generic (`[CommRing R]`).

## The closed item

`MarkovTraceOnHecke` §"Extending past H₃" recorded: *"the n = 4 case is
numerically confirmed … the Lean-grade proof still awaits ingredient (1)
[the H₄ NF basis + table]"*, with the caveat that a naive local-rewriting
reducer is not confluent for H₄. Both ingredients are now delivered:

1. **The table** (ingredient 1) — the 24-word S₄ GB-NF basis (H₃ Lean basis
   as its prefix) with generator right-actions by the **exact Iwahori–Hecke
   length rule** `T_w·T_s = T_{ws}` (length up) / `h·T_w + T_{ws}` (length
   down) — the permutation-indexed recursion, not local rewriting, so no
   confluence issue. The preflight verifies over ℚ(z,h): Hecke quadratic ×3,
   both adjacent braid relations, far commutation, and that the emitted
   Lean formulas match the matrices entry-for-entry. The 24 trace weights
   are **uniquely derived** (cyclicity + Markov-σ₂ reduction + tr(1)=1) —
   data, not choices; the longest-element weight is
   `h³z³ + h²z² + 2hz³ + z²`.
2. **The rung** (ingredient 2) — Lean-grade, sorry-free:
   - `trM4_iota34_stabilizes` : `tr₄(ι x) = tr₃ x` — the H₃ ↪ H₄ Markov
     stabilization (previously numerically-confirmed only);
   - `trM4_markov_σ₂` : `tr₄((ι x)·σ₂) = z·tr₃ x` — the (M3) reduction at
     the new rung;
   - `iota34_mulσ₀/σ₁` — the inclusion intertwines the level-3 generators;
   - quadratic ×3, braid ×2, and **`far_commute_σ₀σ₂`** — the F1
     monoidal-interchange shadow, **non-vacuous for the first time**
     (n ≤ 3 has no non-adjacent pair); until now it existed only as a
     class field.

## Honesty

The general-n `MarkovStabilization` class instance stays OPEN (its
`HeckeBraidedPresentation` binders quantify the H_∞ generator family — no
finite-level instance is possible, per the merged `HeckeH3AlgebraLaws`
analysis). This closes the concrete `3 → 4` rung and realizes all three
presentation-law *kinds* (quadratic, braid, far-commutation) as theorems.
Nothing wired; `1/(8π)` stays phase-4.

## Tower state

```
n=2:  quadratic (scaffold) + H₂ algebra + trM₂            proved
n=3:  full algebra object + Ring/Algebra + MarkovTrace     proved + instantiated
2→3:  stabilization rung                                   proved (merged)
n=4:  σ-action tables + presentation laws (incl. far-comm) proved (this)
3→4:  stabilization rung + M3 reduction                    proved (this)
n→∞:  MarkovStabilization / HeckeBraidedPresentation       OPEN (the general-n gap)
```
