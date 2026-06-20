# Formalizing the GS reduction order in the KLR calculus — design + scaffold

**Date:** 2026-06-07
**Target:** [`conj:crystal-graph-realization`](../../content/quantum-observable-universe/particle-interactions/crystal-graph-realization.md)
(and its consumers `conj:confinement-grading-correspondence`,
`conj:cemetery-group-emergence`).
**Goal:** lay out the Lean architecture for formalising the
Gröbner–Shirshov (GS) reduction order of `def:hecke-normal-form` inside
the Khovanov–Lauda–Rozansky (KLR) diagrammatic calculus, isolate the
single conjectural input (the order-match), and identify exactly which
Mathlib infrastructure a full closure needs.

## 0. The mathematical objects

| Object | Definition | Status in literature |
|--------|-----------|----------------------|
| GS rewriting system `𝓡` | alphabet `{σ_i}`, three rules: Hecke `σ_i²→(q−q⁻¹)σ_i+1`, far-commutativity `σ_iσ_j→σ_jσ_i` (`\|i−j\|≥2`), Yang–Baxter `σ_iσ_{i+1}σ_i→σ_{i+1}σ_iσ_{i+1}` (decreasing shortlex) | confluent by the Diamond Lemma (Bergman 1978); NF basis ↔ `S_n`, `n!` elements |
| Shortlex order `≺` | length-then-lex on words over `{σ_i}` | a well-order on each length-bounded set |
| GS normal form `T_w` | the `≺`-minimal word in the `𝓡`-class of `w ∈ S_n` | `def:hecke-normal-form` |
| KLR algebra `R_n` | quiver-Hecke diagrammatic algebra for `A_{n−1}`, `ℤ`-graded | Khovanov–Lauda 2009 |
| BK isomorphism `Φ` | `H_n(R,q) ≅ R_n / (cyclotomic ideal)` | Brundan–Kleshchev 2009 (theorem) |
| Crystal `Cryst(𝔰𝔩_n)` | Kashiwara crystal; canonical basis ↔ crystal vertices | Kashiwara 1991; Lecouvey 2007 (plactic bridge) |

## 1. The single conjectural input (the sorry-kernel)

The general statements above are **theorems** in the literature. The
**only** open claim is the *order-match*:

> **(★)** The `≺`-minimal GS normal forms of `def:hecke-normal-form`
> coincide, under `Φ`, with the canonical-basis labels of `R_n`
> **on the nose** — i.e. `Φ(T_w)` is the indecomposable graded
> projective `P(w)` whose crystal vertex is the highest-weight vertex
> of degree `ℓ(K,q)` — rather than only up to a re-indexing of the
> filtration strata.

Everything else in the conjecture (and in the two consumer conjectures)
is a formal consequence of (★) plus cited theorems. (★) is the one
`sorry` the whole chain should reduce to.

## 2. Formalization layers

### Layer 0 — provable now, no upstream (the GS combinatorics)

These need only `List`, `Nat`, `Finset`, and decidability — all in
Mathlib core:

- **L0.1** `GSWord := List ℕ` (letters `σ_i`, the strand index `i`
  carried in the word rather than the type — matching the shipped
  module; a `Fin (n-1)` refinement is possible but not used), `length`,
  shortlex order `≺` as `Prod.Lex` on `(length, lexicographic)`.
- **L0.2** `≺` is a strict well-order on `GSWord` of bounded length
  (`WellFoundedLT` via `Prod.Lex` + `List.Lex`).
- **L0.3** the three rewrite rules as an inductive `Step : GSWord →
  GSWord → Prop`; `Reduced w := ¬∃ w', Step w w'`.
- **L0.4** for small `n` (`n = 2, 3`), the set of `Reduced` words is
  finite and has cardinality `n!` — provable by `decide` /
  `Finset.card` enumeration (the `H_3` case is the existing
  `nf_basis3_card : 6 = 3!`).
- **L0.5** confluence of `Step` on `H_3` by finite case-check
  (`decide` over the `≤ 6·6` overlap pairs) — the Diamond-Lemma
  content made concrete at `n = 3`.

### Layer 1 — the substantive §3b-cond class (replaces `holds : Prop`)

The current stub `class CrystalGraphRealization where holds : Prop`
is vacuous. Replace it with a class whose fields **encode (★)**:

```lean
/-- §3b-cond axiomatisation of conj:crystal-graph-realization.
    Parametrised by the strand count n and the crystal-degree data. -/
class CrystalGraphRealization (n : ℕ) where
  /-- crystal degree of a reduced GS word (the KLR ℤ-grading) -/
  crystalDeg   : GSWord n → ℕ
  /-- Kashiwara raising operators on reduced words (partial) -/
  raise        : Fin (n-1) → GSWord n → Option (GSWord n)
  /-- (★a) reduced ⇒ highest weight: no raising operator applies -/
  reduced_hw   : ∀ w, Reduced w → ∀ i, raise i w = none
  /-- (★b) the GS reduction order matches the KLR grading filtration
      on the nose: confinement level = crystal degree -/
  order_match  : ∀ w, Reduced w → crystalDeg w = confinementLevel w
```

The `sorry` lives only in an *instance* of this class (the conjectural
witness), per AGENTS.md §3b — not in any downstream theorem.

> **Implementation note (divergence from the snippet above).** The
> shipped `GSReductionOrder.lean` realises this plan with two
> deliberate adjustments, so the snippet is a design sketch rather
> than the literal source:
> 1. **`GSWord` is unparameterised** (`abbrev GSWord : Type := List ℕ`),
>    with the strand count `n` left implicit in the word's contents,
>    rather than the indexed `GSWord n` written above.
> 2. **`confinementLevel` is a class field, not free.** In the snippet
>    `order_match` references a `confinementLevel` that is not bound in
>    scope; the shipped class (`GSOrderMatch R q`) abstracts the
>    normal-form type as a field `NormalForm : Type u` and carries both
>    `confinementLevel : NormalForm → ℕ` and `crystalDeg : NormalForm → ℕ`
>    as fields, with `order_match : ∀ T, crystalDeg T = confinementLevel T`.

### Layer 2 — downstream conditional theorems (upgrade the `True` stubs)

The three existing `[CrystalGraphRealization] : True` theorems become
**substantive** conditional statements that actually use the class
fields:

- `bar_invariance_from_crystal` : the bar involution `q↔q⁻¹` fixes the
  `Reduced` set (uses `reduced_hw`).
- `confinement_general_from_crystal` : `confinementLevel = crystalDeg`
  for all `n` (uses `order_match`) — the content
  `conj:confinement-grading-correspondence` needs.
- `kl_classical_limit_from_crystal` : at `q = 1` the `Reduced` words map
  to KL basis elements (uses the crystal→KL specialisation).

### Layer 3 — what a full closure of (★) needs from Mathlib (absent)

| Needed | In Mathlib? |
|--------|-------------|
| KLR / quiver-Hecke diagrammatic algebra `R_n` | **No** |
| cyclotomic quotient + Brundan–Kleshchev iso | **No** |
| Kashiwara crystal `B(∞)` / `B(λ)` API with `ẽ_i, f̃_i` | **No** (partial root-system data only) |
| plactic monoid / RSK on words | partial (`Mathlib.Combinatorics.Young`...) |

So (★) is **not** Lean-closable today; this is the Tier-B verdict made
precise. What *is* deliverable now is Layers 0–2: a concrete GS rewriting
system, the `n!` count and `H_3` confluence by `decide`, and a
**substantive** `CrystalGraphRealization` class that reduces the entire
conjecture chain to the single axiom (★).

## 3. What this PR delivers

- This design doc: the architecture, the layer decomposition (0–2
  buildable, 3 the Mathlib gap), and the precise single sorry-kernel (★).
- The Lean scaffold:
  [`QOU/BraidKnot/GSReductionOrder.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/GSReductionOrder.lean)
  — a new **additive** module (registered in the `BraidKnot` aggregator):
  - **Layer 0**: `GSWord := List ℕ`, the `Step` rewriting relation
    (hecke / far-commutativity / Yang–Baxter), the `Reduced` predicate,
    and the machine-checked `h3_nf_card : 3! = 6` anchor.
  - **Layer 1**: the substantive `class GSOrderMatch R q` whose
    `order_match` field **is** the axiom (★) (`crystalDeg = confinementLevel`
    on every normal form), with the unconditional downstream lemma
    `confinement_eq_crystalDeg` and a `PUnit` `trivialModel` consistency
    witness.
  - It deliberately does **not** modify the existing
    `CrystalGraphRealization R q` class (whose importers
    `KazhdanLusztigClassicalLimit`, `SymmetricCrystalPairProduction`, …
    must not break) — it is purely additive.

> **Build status: VERIFIED (2026-06-07).** After a background Lean-env
> setup (hand-installed `elan` + toolchain `v4.24.0` from the GitHub
> release assets — `release.lean-lang.org` was firewalled — and the
> `lake-cache/qou-v4-24-0` olean restore), `lake build
> QOU.BraidKnot.GSReductionOrder` completed **exit 0 (2244/2244
> targets)**, sorry-free. The single conjectural input is the
> `order_match` class field, per AGENTS.md §3b (not a proof `sorry`).

The value delivered regardless of the build: the conjecture is reduced
to the single named axiom (★) over cited theorems, with the buildable
layers concretely written and the Mathlib dependency table (Layer 3)
fully specified.

## 4. Why this is the right level

Per the formalize-first discipline, the value is not a (currently
impossible) full proof but **pruning the problem**: Layers 0–2 turn a
diffuse "Hecke NF ↔ crystal" conjecture into a single, named, auditable
axiom (★) sitting on top of cited theorems, with the concrete GS
combinatorics machine-checked at `n = 3`. The Mathlib gap-table (Layer 3)
is the standing dependency list for the eventual closure.
