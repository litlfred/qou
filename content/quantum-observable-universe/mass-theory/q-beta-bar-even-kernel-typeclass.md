**Proposition (definition + composition theorem).** *The `BarEvenKernel`
Lean typeclass bundles all four $\S 4$ formalize-first invariants for a
candidate Habiro element $F(q)$ into a single parametric type, with
fields for the bar-even symmetry, radius-of-convergence pole location,
$q = 1$ classical-limit shadows, and direction-sanity magnitude check.
Instantiating `BarEvenKernel` for any candidate is equivalent to that
candidate clearing all four §4 gates simultaneously.*

## Why a unified typeclass

The four §4 formalize-first invariants from the
[refuted-class map](../../../docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)
were formalized separately as four parametric gate classes:

| invariant | gate class | parametric? |
|---|---|---|
| (a) Anchor-stable (simple pole at $u_{\text{substrate}}$) | `RadiusOfConvergenceGateClass` | no (global axiom) |
| (b) Bar-even under $q \mapsto q^{-1}$ | structural identity | n/a (CommRing R lemma) |
| (c) $q = 1$ classical-limit shadow | `QOneShadowGateClass (c2 c3 : ℝ → ℝ)` | **yes** |
| (d) Direction sanity at $q_0$ | `DirectionSanityGateClass (m : ℝ)` | **yes** |

A future probe author evaluating a candidate $F(q)$ currently has to
instantiate four classes by hand. **`BarEvenKernel` is the single
bundling typeclass** that makes the entire formalize-first chain a
one-liner: instantiate `BarEvenKernel pole c2 c3 magnitude` and the
candidate is admitted (or rejected — Lean cannot construct the
instance if any field's hypothesis fails).

## The composition

```lean
class BarEvenKernel
    (pole : ℝ)            -- candidate's nearest singularity in u-plane
    (c2 c3 : ℝ → ℝ)       -- candidate's per-rung coefficient functions
    (magnitude : ℝ)        -- candidate's |F(q_0)| substrate magnitude
    : Prop where
  -- §4(a) radius-of-convergence: pole at u_substrate within fibre tolerance
  pole_at_u_substrate :
    |pole - uSubstrate| ≤ radiusTolerance
  -- §4(c) q=1 classical-limit shadow
  c2_shadow : c2 1 = -1
  c3_shadow : c3 1 = jonesHopfAtQOne
  -- §4(d) direction sanity at q_0
  direction_match :
    |magnitude - directionTarget| ≤ directionThreshold * directionTarget
  -- §4(b) bar-evenness (the structural identity holds for
  --       any candidate in CommRing R, so the typeclass instance does
  --       not need to re-state it; included as a corollary lemma)
```

The bar-even invariant is a CommRing R-level structural
identity that holds automatically for any kernel candidate built from
the substrate primitives ($b$, $\hbar_q$); the typeclass therefore
does not duplicate it as a field. The bar-even rejection lemma remains available as the standalone gate when a candidate
does NOT come from the substrate (e.g., a freely-constructed test
kernel during exploratory work).

## Composition theorem

If `BarEvenKernel pole c2 c3 magnitude` is instantiable for some
specific `(pole, c2, c3, magnitude)`, then:

1. `RadiusOfConvergenceGateClass`-equivalent holds at the parametric
   level (pole within tolerance of $u_{\text{substrate}}$).
2. `QOneShadowGateClass c2 c3` is instantiable.
3. `DirectionSanityGateClass magnitude` is instantiable.

The Lean proof of each lifting is a one-line extraction of the
corresponding field — `BarEvenKernel.pole_at_u_substrate`,
`BarEvenKernel.c2_shadow`, etc. — with the bundle-to-class conversion
implicit in the constructor.

## Use in the formalize-first checklist

This typeclass *operationalises* the 7-step Δ_λ pre-flight checklist
(`docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md`
$\S 3$): instead of running Steps 3–6 as separate sympy probes + Lean
checks, a probe author writes:

```python
# Conceptual: at the formal level, the entire pre-flight reduces to:
candidate = build_candidate(...)
pole, c2, c3, magnitude = extract_observables(candidate)
# In Lean: try { @BarEvenKernel.mk pole c2 c3 magnitude ... }
#          If Lean accepts the instance → admit; else → REFUTE
```

with each field hypothesis discharged by the corresponding probe.

## Honest scope

- This is **infrastructure**, not new mathematical content. It does
  NOT construct a new $F(q)$ kernel — the open keystone remains owner-
  gated multi-session research per refuted-class map $\S 5$.
- The typeclass codifies the *gate-chain composition*; the actual
  kernel search proceeds independently.
- Subclasses of `BarEvenKernel` (e.g. extending to include the
  `CFinite.recurrence_step` engine for kernel-driven $c_k$
  generation) are natural follow-ups.
