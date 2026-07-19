# α_EM F-construction T5, first brick — the target is now parameter-free (2026-07-19)

**Bean:** `qou-1st5` (T5 brick) of milestone `qou-a46k`.
**Lean:** [`QOU/Archimedean/TauFunctorAssembly.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/TauFunctorAssembly.lean)
— sorry-free, `lean`-direct exit 0 (dep-cone oleans built lean-direct:
`TauRhoHodgeLiftInterface`, `LiftFromReality`, `MarkovWeightValueTransport`,
`TauFunctorTargetSpec`).

**Scope guard (STRICT):** per the target spec's own
`interface_alone_is_trivially_inhabitable`, interface inhabitation carries no
weight and the `assembled` instance is labeled a PACKAGING, never progress on
the wall. Nothing wired; `1/(8π)` stays phase-4.

## What this brick adds

Before this file, `ArchimedeanTauRealization g w` had a **free parameter**:
the prescribed channel weight `w` (any real value trivially inhabitable). The
T1–T4 legs make it derivable:

- **`channelWeight_derived`** — `3·y₂(1) + 1·y₁₁(1) = 5/2`, the pairing of
  the T1 Chevalley–Weil dims (3 moving, 1 invariant) with the T4 canonical
  weight values (¾, ¼), both taken from merged modules. The weight is a
  theorem, not a choice.
- **`assembled : ArchimedeanTauRealization 4 (5/2)`** — the T1-structured
  operator (block-scalar ¾ on the moving block, ¼ on the invariant line,
  conjugate blocks equal per the shape T3 forces, off-blocks zero) packages
  into the target type at the derived weight, via the `swap_conj_blocks`
  machinery of `LiftFromReality`.
- **`assembled_equal_split`** — the spec's `discharge_equal_split` at the
  derived weight: the conjugate block also carries 5/2 (the ½ of `½·a₀`,
  instantiated).

## What this changes about T5

The T5 obligation sharpens from "construct F and inhabit the interface for
some w" to:

> **supply functorial provenance for the specific parameter-free target
> `ArchimedeanTauRealization 4 (5/2)` with the T1-structured (3,1) operator**
> — i.e. show the framework's τ (F1–F5 of `TauFunctorReduction`) assigns
> exactly this operator to the canonical Markov weight.

No free parameter remains anywhere in the α_EM target spec. The wall itself
(functorial provenance — naturality in the categorical data) is untouched
and remains open.

## Plan state (milestone `qou-a46k`)

```
T1 cover structure                     MERGED #4039
T2 local monodromy = H₂(i) module      MERGED #4040
T3 ρ-equivariance (deck reality)       MERGED
T4 weight-value transport (¾,¼)        MERGED #4045
T5 assembly: parameter-free target     THIS (first brick)
T5 residual: functorial provenance     OPEN — THE wall
```
