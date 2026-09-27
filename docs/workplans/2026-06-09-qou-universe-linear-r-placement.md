# Workplan — lift `[CommRing R] [Linear R C]` onto the base QOU universe triple

**Status:** queued (owner-approved 2026-06-09, follow-up to merged PR #2022).
**Scope:** whole-`QOU`-lib refactor — own PR, larger blast radius than the
transform-block slice.

## Motivation

`def:quantum-observable-universe` already declares the `(𝐂, A, τ)` triple has
`𝐂` a **k-linear rigid monoidal** category (`𝐂 = 𝐑𝐞𝐩(SU_q(2))`, fibre functor
abstracting `Vect_k`).  PR #2022 *restored* that k-linearity **locally** — each
transform structure (`CategoricalDiracOperator`, `CategoricalLagrangian`) now
carries `[CommRing R] [Preadditive C] [Linear R C]` on its own signature.

This follow-up lifts the assumption to **one source of truth**: the base
universe structures, so every downstream consumer inherits it rather than
re-declaring it.

> **Ground ring is `R` (a commutative ring), NOT a field `k`.**  The narrative
> "k-linear" maps to Mathlib `CategoryTheory.Linear R C` over `[CommRing R]`
> (§7c base-ring convention).  Scalars that need inversion (e.g. `q⁻¹`) are
> carried as explicit elements with a unit hypothesis (`q * qinv = 1`), not by
> assuming a field.

## Additive (`⊕`) is derived, not a new axiom

`[Linear R C]` gives **preadditive** (the `+`/`−`/`0` the formulas need).  The
biproduct `⊕` (Wedderburn / isotypic decomposition, Fourier "direct sum of
`V_j`") follows from **semisimplicity**:

- generic `q`: `Ext¹(V_i, V_j) = 0` ⟹ every object is a biproduct of simples ⟹
  additive, for free (`Preadditive + HasFiniteProducts ⟹ HasFiniteBiproducts`);
- root-of-unity substrate `q₀`: not semisimple — recover additivity in the
  **semisimplified** (negligibles-quotient) category.

So additivity need not be a separate field on the base struct; record it as a
consequence (or a `[HasFiniteBiproducts C]` instance available under the
semisimplicity hypothesis), not an independent axiom.

## Target structures

- `QOU.QuantumUniverse` (`CategoricalFoundations.lean`) — add `[CommRing R]`
  + `[Preadditive C] [Linear R C]` (or carry `R` + the instances as fields).
- `QOU.QuantumObservableUniverse` (`CategoricalFoundations.lean`) — inherits;
  the observation layer (Frobenius pairing / Markov trace) is where the
  semisimplicity ⟹ `⊕` is actually used.

## Blast-radius inventory (to fill in during execution)

Every consumer of `QuantumUniverse` / `QuantumObservableUniverse` must thread
the new `R` + instances. Start from:

```
grep -rln "QuantumUniverse\|QuantumObservableUniverse" folio/quantum-observable-universe/lean/
```

Structures already carrying the instances locally (from #2022 — can drop the
local copy once the base carries it): `CategoricalDiracOperator`,
`CategoricalLagrangian` (+ their `exists`/`unique`).

## Migration order

1. Base structs in `CategoricalFoundations.lean` (add `R` + instances).
2. Direct consumers in the same file, then `GaugeTheory.lean`,
   `Instanton.lean`, `Structures.lean`.
3. Transitive consumers (walk the import graph leaf-ward).
4. Drop the now-redundant local `[Linear R C]` from the #2022 transform blocks.

## Verification

- Per-module `lake build QOU.<Module>` for the touched cone (the heavy
  Manifold/InnerProductSpace cone builds from source; Mathlib release-cache is
  network-blocked in the sandbox).
- `_Scratch` bundles for content-block `.lean` files (outside the lake
  `srcDir`), compiled against the real lib modules.
- `bun run validate quantum-observable-universe` exit 0.

## Risks

- Large mechanical diff; instance-resolution churn (`Linear R C` needs
  `Preadditive C` first).
- Pre-existing broken lib modules unrelated to this change may surface; fix
  inline only if 1-token (cf. the `GaugeTheory:229` fix), else flag + defer.
