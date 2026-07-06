# Iwahori-Hecke algebra in Mathlib — infrastructure plan

**Authored:** 2026-05-30
**Branch:** `claude/phase1-tier-a-and-infra-plan-2026-05-30`
**Tracks:** Phase 2 §2a of
[`docs/workplans/2026-05-30-source-conjecture-closure-plan.md`](2026-05-30-source-conjecture-closure-plan.md)

## Why

The single highest-leverage infrastructure investment for closing
source-node conjectures is **Iwahori-Hecke algebras of type A in
Mathlib**. The closure plan's Phase 2 table:

| infra | unlocks Tier-B conjs | downstream users |
|------|------:|------:|
| **Iwahori-Hecke algebra** | 5 (crystal-graph-realization, gs-graded-markov-trace, hoefsmit-ew-cell-content, reverse-limit-q-to-infinity, hecke-anyonic-substrate) | **18+** |

By comparison the next-best infra unlocks 1-2 conjectures each.
Iwahori-Hecke is the keystone.

This document is the **scoping plan**, not the implementation. It
identifies what Mathlib already has, what's missing, and the
minimum-viable shape of the PR series needed to unblock the QOU
closures.

## Current Mathlib state (snapshot)

As of 2026-05-30 (Mathlib4 latest), Mathlib has:

- ✅ `Mathlib.GroupTheory.Coxeter.*` — full Coxeter group theory
  (Tits cone, root system, length function, exchange property,
  reduced expressions)
- ✅ `Mathlib.GroupTheory.SpecificGroups.Symmetric` — symmetric
  group $S_n$, including Coxeter presentation via adjacent
  transpositions
- ✅ `Mathlib.Combinatorics.Young.YoungDiagram` — Young diagrams,
  hook length, semistandard tableaux
- ✅ `Mathlib.Algebra.Module.LinearMap.*` — linear algebra over
  commutative rings
- ✅ `Mathlib.RingTheory.PolynomialAlgebra` — algebra structures
- ⚠️ **Missing**: the Iwahori-Hecke algebra $H_n(q)$ itself, as a
  unital associative $R$-algebra with the explicit braid + Hecke
  relations
- ⚠️ **Missing**: the type-$A_n$ specialisation
- ⚠️ **Missing**: Markov trace, Hoefsmit basis, Wedderburn
  decomposition (these depend on Iwahori-Hecke existing first)

The Iwahori-Hecke construction is a well-understood algebraic
object; the missing content is engineering, not research.

## Scope of the proposed Mathlib PR series

**Mathlib namespace**: `Mathlib.Algebra.IwahoriHecke.*`.

The series follows the standard Mathlib pattern for new algebraic
objects: definition → basic API → specialisations → corollaries.

### PR series outline (5 PRs)

| # | PR title | scope | est. LOC | est. weeks |
|---|---|---|------:|------:|
| 1 | `feat(IwahoriHecke): Defn + universal property` | `IwahoriHecke W q` for a Coxeter group `W` over a `CommRing R` with `q : R`; quotient of the free algebra on $\{T_s\}_{s \in S}$ by braid + Hecke relations | 500-800 | 3-4 |
| 2 | `feat(IwahoriHecke): Reduced-expression basis` | `IwahoriHecke W q` has a basis indexed by `W` (the $T_w$ basis); independence of reduced expression | 400-600 | 2-3 |
| 3 | `feat(IwahoriHecke): Type A specialisation` | `IwahoriHeckeOfSn n q` defined from `Equiv.Perm (Fin n)`'s Coxeter structure; isomorphism with the abstract `IwahoriHecke (symmetricGroup n) q` | 200-400 | 1-2 |
| 4 | `feat(IwahoriHecke): Markov trace` | `markovTrace : IwahoriHecke W q → R` for type $A$, satisfying Markov's two axioms (trace + braid-closure invariance under stabilisation $T_n$); existence + uniqueness | 600-900 | 3-4 |
| 5 | `feat(IwahoriHecke): Hoefsmit seminormal basis` | Construction of the Hoefsmit basis $\{v_T\}$ indexed by standard tableaux $T \vdash n$; cell-content recurrence; orthogonality | 800-1200 | 4-6 |

**Total estimate**: 2500-3900 LOC, 13-19 weeks (≈ 3-5 months).

### Dependencies between PRs

```
PR 1 (Defn) ──┬─→ PR 2 (Basis)
              └─→ PR 3 (Type A spec)
                     │
PR 2 ────────────────┴─→ PR 4 (Markov trace)
                              │
PR 2 ─────────────────────────┴─→ PR 5 (Hoefsmit)
```

PRs 1-3 form the foundation (linear sequence). PRs 4 + 5 are
independent of each other (parallel after PR 3 lands).

### Smallest viable subset for QOU

If the goal is to unblock just **one** Tier-B conjecture, the
critical path is **PRs 1 + 2 + 3** (foundational $T_w$ basis).
That alone unblocks `conj:hecke-anyonic-substrate` and
`conj:reverse-limit-q-to-infinity`, plus enables the §3b-cond
class instances in `prop:hecke-branching-trace-decomposition` to
go from `placeholder Unit` field to actual `IwahoriHecke`-valued
content.

PR 4 (Markov trace) unblocks `conj:gs-graded-markov-trace-existence`.

PR 5 (Hoefsmit) closes the operator-valued
`A^λ_{μ,ν}(I)` content from
[`prop:hecke-branching-trace-decomposition`](../../content/quantum-observable-universe/mass-endomorphism/hecke-branching-trace-decomposition.md).

## Coordination strategy

### Option A — Author the Mathlib PRs ourselves

**Pro**: Full control; matches QOU's specific conventions.
**Con**: 3-5 months of effort; Mathlib review cycle adds 2-4
weeks per PR; the Mathlib maintainers may push back on
QOU-specific shapes.

### Option B — Stub in QOU's `qou` Lake package, contribute upstream later

**Pro**: Immediate unblock (1-2 weeks per Tier-B closure); QOU
internal correctness; upstream contribution is a separable
follow-up.
**Con**: Duplicates effort (will need to merge with upstream
Iwahori-Hecke if/when it lands); the `qou` package's
`QOU.IwahoriHecke.*` namespace is opaque to other Mathlib
consumers.

### Option C — Hybrid: stub in `qou`, mirror Mathlib's expected API

**Pro**: Best of both — immediate unblock + ready-to-merge
upstream when Mathlib accepts; the `qou` definitions become
direct imports once Mathlib accepts.
**Con**: Slightly higher upfront cost (write to Mathlib style)
but the differential is small.

**Recommendation: Option C.**

## Concrete next-action sequence (Option C)

1. **Sprint 1 (1-2 weeks)** — `qou:QOU.IwahoriHecke.Defn`:
   - `IwahoriHecke (W : Type*) [CoxeterSystem W] (q : R)` —
     quotient construction
   - Universal property API
   - Smoke test: verify `IwahoriHecke (symmetricGroup 3) q`
     has finite dimension 6 (= |S_3|)
   - Discharges: nothing yet (no Tier-B conjecture closed)
   - Unblocks: PRs 2-3 in this plan

2. **Sprint 2 (1-2 weeks)** — `qou:QOU.IwahoriHecke.Basis`:
   - `Tw : W → IwahoriHecke W q` (reduced-expression-based)
   - `IsBasis (Set.range Tw)`
   - **Closes**: `conj:hecke-anyonic-substrate` (anyonic-substrate
     content reduces to "the $T_w$ basis spans"). Conditional or
     unconditional depending on the conjecture's exact statement
     — see the closure-plan §3b-cond preference.

3. **Sprint 3 (1-2 weeks)** — `qou:QOU.IwahoriHecke.TypeA`:
   - `IwahoriHeckeOfSn (n : ℕ) (q : R)` = `IwahoriHecke
     (symmetricGroup n) q`
   - Concrete-strand API: `σi : Fin (n-1) → IwahoriHeckeOfSn n q`
   - **Closes**: `conj:reverse-limit-q-to-infinity` (the
     limiting behaviour follows from `σi` arithmetic).

4. **Sprint 4 (2-3 weeks)** — `qou:QOU.IwahoriHecke.MarkovTrace`:
   - `markovTrace : IwahoriHeckeOfSn n q →+ R` via
     stabilisation axioms
   - **Closes**: `conj:gs-graded-markov-trace-existence`.

5. **Sprint 5 (3-4 weeks)** — `qou:QOU.IwahoriHecke.Hoefsmit`:
   - Hoefsmit basis indexed by SYT λ
   - **Closes**: `conj:hoefsmit-ew-cell-content`.
   - **Closes**: §3b-cond placeholder in
     `prop:hecke-branching-trace-decomposition` —
     `branchCoefficient` field upgrades from `Unit` to the
     actual operator-valued coefficient.
   - **Closes**: `conj:crystal-graph-realization` if combined
     with the Brundan-Kleshchev iso (separate KLR algebra
     infra; out of this plan's scope).

**Total Sprint 1-5**: 8-13 weeks (≈ 2-3 months).

## Risk register

| risk | mitigation |
|------|------------|
| Mathlib already has partial Iwahori-Hecke content not picked up by initial survey | Re-search `lean_local_search "Iwahori"` + `lean_loogle "IwahoriHecke"` before Sprint 1 begins; abandon Option C in favour of "direct Mathlib import" if so |
| QOU's `Wenzl positivity` (q^{1/2} + q^{-1/2} > 2) requires specific real-valued q, not generic ring element — type-class friction | Use `[CommRing R]` parameter with `q : R` and supply an `[LinearOrderedField R]` specialisation for the positivity regime; keeps Wenzl out of the generic API |
| Hoefsmit basis at `n ≥ 9` is computationally expensive | Define abstractly via cell-content recurrence; defer explicit numerical computation to the existing `hecke-engine` Rust crate (out of Lean) |
| Mathlib upstream PR rejects the shape | The `qou` stubs continue to serve QOU; upstream contribution becomes a separate effort |
| Type-class blow-up (Coxeter + CommRing + LinearOrderedField + …) | Keep the `IwahoriHecke` constructor as `[CommRing R]` only; layer additional constraints via downstream lemmas, not the core definition |

## Out of scope for this plan

- **KLR algebras** (needed for `conj:crystal-graph-realization`'s
  Brundan-Kleshchev iso). Separate Mathlib infrastructure track.
- **Hoefsmit at general Coxeter type B/D** — only type A is in
  scope.
- **Affine Hecke algebras** — only finite Hecke is in scope.
- **Quantum group $U_q(\mathfrak{sl}_n)$** — separate dependency
  track; not needed for the QOU Tier-B closures.

## Linkage

- Parent plan: [`docs/workplans/2026-05-30-source-conjecture-closure-plan.md`](2026-05-30-source-conjecture-closure-plan.md)
- §3b-cond reference: [`AGENTS.md` §3b-cond](../../AGENTS.md)
- Existing QOU §3b-cond placeholder using Iwahori-Hecke:
  [`prop:hecke-branching-trace-decomposition`](../../content/quantum-observable-universe/mass-endomorphism/hecke-branching-trace-decomposition.md)
- Existing computational stack (Rust): `tools/hecke-engine/`
  + `tools/pyhecke-native/`. The Lean infra targets correctness;
  the Rust stack targets performance.
