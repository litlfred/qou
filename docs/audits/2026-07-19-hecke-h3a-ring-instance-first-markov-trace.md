# H₃(q) packaged as `Ring`/`Algebra` + the FIRST `MarkovTrace` instance (2026-07-19)

**Bean:** `qou-qh55` (categorical tranche, continuation of the merged
algebra-object laws).
**Lean:** [`QOU/Machinery/HeckeH3AlgebraInstance.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/HeckeH3AlgebraInstance.lean)
— sorry-free, `lean`-direct exit 0. §7c-generic (`[CommRing R]`, no ℝ).

**Scope guard (STRICT):** `MarkovTrace` is an interface with real laws —
instantiating it is proved content, not a conjecture-class discharge. The
OPEN items are unchanged: general-n `HeckeBraidedPresentation` /
`MarkovStabilization` (H_∞ binders), and the `TauRhoHodgeLift` wall.
Nothing wired; `1/(8π)` stays phase-4.

## What landed

- **`H3A R h`** — wrapper type for the H₃(q) NF module with `AddCommGroup`,
  `Module R`, **`Ring`** (mul = the proved `mulNF`, unit = γ, all laws
  discharged by the merged `HeckeH3AlgebraLaws`), and **`Algebra R`**
  (via `Algebra.ofModule` on the proved homogeneity laws).
- **`markovTrace_H3A`** — the **first instance of the `MarkovTrace` class**
  in the corpus (the class had no instance anywhere): cyclicity from
  `trM_cyclic`, additivity from `trM_add`, homogeneity from `trM_smul`.

## What it unlocks

`TauFunctorReduction.observationFrame_cyclic` — previously usable only by
*threading* `[MarkovTrace …]` as a hypothesis — now applies
**unconditionally** to `H3A`: the observation frame `τ_∞ = ev ∘ tr_M` at
n=3 is cyclic at the typeclass level. The F3 slice of the τ-functor's five
laws is realized end-to-end at the concrete rung: algebra object (laws
file) → typeclass instances (this file) → derived frame properties
(reduction file), with zero hypotheses.

## Plan state

```
Source category (F1/F2): n=3 algebra object certified + INSTANTIATED (this)
                          general-n presentation / stabilization   OPEN
F3 (trace):               n=3 realized unconditionally (this)
                          general-n Markov trace                   OPEN
TauRhoHodgeLift:          OPEN — THE wall
Next mechanical step:     H₄ NF table via the confluent gb_nf_reducer.rs
                          route (per MarkovTraceOnHecke §Extending past H₃)
```
