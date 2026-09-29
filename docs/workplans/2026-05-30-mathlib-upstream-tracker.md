# Mathlib upstream dependency tracker

**Authored:** 2026-05-30
**Branch:** `claude/option-e-explore-and-mathlib-tracker-2026-05-30`
**Companion to:** [`docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md`](2026-05-30-iwahori-hecke-mathlib-infra-plan.md)
+ [`docs/workplans/2026-05-30-source-conjecture-closure-plan.md`](2026-05-30-source-conjecture-closure-plan.md)

## Purpose

This document tracks Mathlib upstream APIs that the QOU project
needs but does not yet have. Each entry lists:

- What we need
- What currently exists in Mathlib (if anything)
- What QOU conjecture(s) it unblocks
- Status (e.g. "in flux", "PR open upstream", "missing entirely")

When an upstream API lands, the corresponding QOU follow-up sprint
becomes actionable. This tracker is the central audit point for
"what is currently blocked on upstream".

## Active dependencies

### `CoxeterSystem` per-pair order accessor

**Need:** A function `m : S → S → ℕ` returning the Coxeter order
`m_{s,t}` for each pair of simple reflections `s, t ∈ S` in a
Coxeter system `(W, S)`.

**Current Mathlib state:** `Mathlib.GroupTheory.Coxeter.Matrix`
exposes `CoxeterMatrix.M : B → B → ℕ` (the Coxeter matrix), and
`CoxeterSystem` carries an associated matrix. The accessor is
**in flux** as of 2026-05; the precise API for reading
`m_{s,t}` from a `CoxeterSystem` instance is not yet stable.

**QOU follow-ups gated on this:**

- [`QOU.IwahoriHecke.Quotient`](../../folio/quantum-observable-universe/lean/QOU/IwahoriHecke/Quotient.lean)
  Sprint 2 follow-up: add **braid relations** to `heckeIdeal`.
  Currently the ideal includes only Hecke quadratic relations;
  braid relations require reading `m_{s,t}` to construct the
  alternating-product polynomial of length `m_{s,t}`.
- [`QOU.IwahoriHecke.Tw`](../../folio/quantum-observable-universe/lean/QOU/IwahoriHecke/Tw.lean)
  Sprint 2 follow-up: **Matsumoto's well-definedness** of
  `Tw : W → IwahoriHeckeQuot R q S`. The proof requires the
  braid-relation invariance from the ideal extension above.

**Status:** awaiting Mathlib API stabilisation. Track
`Mathlib.GroupTheory.Coxeter.*` changes; no upstream PR known
to be in progress.

### `CoxeterSystem.reducedExpression` API

**Need:** Given `w : W` and a `CoxeterSystem M W`, an enumeration
of all reduced expressions for `w`, plus the standard predicate
`IsReduced : List S → W → Prop` and witnesses.

**Current Mathlib state:** `Mathlib.GroupTheory.Coxeter.Length`
defines the length function `ℓ : W → ℕ`. The reduced-expression
API is incomplete; lifting a length-`k` word to `W` and verifying
reducedness is not yet a one-step Mathlib operation.

**QOU follow-ups gated on this:**

- `QOU.IwahoriHecke.Tw.wordProduct` already exists; the full
  `Tw : W → IwahoriHeckeQuot R q S` basis lift via Matsumoto
  requires the reduced-expression API.

**Status:** related to the order-accessor work above; likely lands
together.

### Specht modules + Hoefsmit basis

**Need:** Concrete Specht-module construction over a generic
commutative ring, plus the Hoefsmit seminormal basis indexed by
standard Young tableaux with the cell-content recurrence.

**Current Mathlib state:** `Mathlib.RepresentationTheory.*` has
representation theory primitives. Specht modules over a generic
ring are partially present; the Hoefsmit basis is **missing**.

**QOU follow-ups gated on this:**

- [`QOU.IwahoriHecke.Hoefsmit`](../../folio/quantum-observable-universe/lean/QOU/IwahoriHecke/Hoefsmit.lean)
  Sprint 5 follow-up: **concrete cell-content recurrence** for
  `T_{s_i} · v_T = α · v_T + β · v_{s_i T}`. Currently the file
  has `qBracket` + `alphaCoefficient` signatures; the recurrence
  proof needs Specht-module machinery.
- `prop:hecke-branching-trace-decomposition` §3b-cond placeholder
  upgrade: `branchCoefficient : Unit` → operator-valued
  `End(V_μ ⊗ V_ν)^⊕ c^λ_{μν}`. Requires Hoefsmit basis on `V_μ`,
  `V_ν`.

**Status:** missing entirely. Substantial Mathlib contribution
required (likely 6+ months of focused upstream work, OR a QOU
internal stub via `qou:QOU.IwahoriHecke.Hoefsmit` until upstream
catches up).

### KLR algebra (Khovanov-Lauda-Rouquier)

**Need:** The cyclotomic KLR algebra `R^Λ_α` and the
Brundan-Kleshchev isomorphism `H_n(q) ≅ R^Λ_α`.

**Current Mathlib state:** Missing entirely. KLR algebras have not
been formalised in Mathlib as of 2026-05.

**QOU conjectures gated on this:**

- `conj:crystal-graph-realization` (currently 10 downstream users
   — high-leverage Tier B closure)

**Status:** missing entirely. Substantial contribution required;
no upstream activity known.

### Tauberian theorem + branch-cut control on principal-branch dilogarithm

**Need:** A uniform Tauberian theorem suitable for `q → 1` limits
of q-Pochhammer partial products, plus branch-cut control on the
principal-branch `Li_2`.

**Current Mathlib state:** Real-analysis primitives present;
specific Tauberian + branch-cut lemmas missing.

**QOU conjectures gated on this:**

- `conj:dilogarithm-archimedean-limit` (3 downstream users —
   Tier B; was originally Tier A in the closure plan but
   re-classified after closer inspection).

**Status:** missing entirely.

### Pachner moves + Pentagon identity for 3-manifolds

**Need:** Pachner 2–3 moves on ideal-tetrahedron decompositions
of 3-manifolds, plus the Pentagon identity for the q-dilogarithm
`Φ_q` at the state-sum level (Turaev–Viro / Reshetikhin–Turaev).

**Current Mathlib state:** Manifold topology has some content;
specific Pachner moves + Pentagon for `Φ_q` missing.

**QOU conjectures gated on this:**

- `conj:pachner-pentagon-borromean` (1 downstream user)

**Status:** missing entirely.

## Summary table

| upstream dep | what's there | what's missing | QOU follow-ups gated | est. timeline |
|---|---|---|---:|---|
| `CoxeterSystem` order accessor | matrix | per-pair accessor | Sprint 2 follow-up (2 files) | weeks-months (API stabilisation) |
| `CoxeterSystem.reducedExpression` | length function | enumeration + IsReduced | `Tw` basis Matsumoto | weeks-months (likely with above) |
| Specht modules | partial | Hoefsmit basis | Sprint 5 follow-up + `branchCoefficient` upgrade | 6+ months |
| KLR algebra | none | full algebra | `conj:crystal-graph-realization` (10 users) | 12+ months |
| Tauberian + branch-cut | base real analysis | specific lemmas | `conj:dilogarithm-archimedean-limit` (3 users) | months |
| Pachner moves + Pentagon | partial manifold | specific Pachner | `conj:pachner-pentagon-borromean` | months |

## Process

1. **Quarterly check** — once per quarter, re-survey Mathlib's
   `Mathlib.GroupTheory.Coxeter.*`, `Mathlib.RepresentationTheory.*`,
   and `Mathlib.Topology.*` for changes affecting this list.
2. **On Mathlib release**: when a new Mathlib version pins lands
   in the QOU `lake-manifest.json`, audit this list against the
   new APIs.
3. **Upstream contribution**: for high-leverage items (KLR algebra,
   Hoefsmit basis), consider opening Mathlib PRs ourselves. The
   `qou` Lake package serves as a development sandbox per the
   "Option C — hybrid" strategy in the Iwahori-Hecke infra plan.

## Saga progress summary (PRs across this session-train)

| PR | what landed |
|---|---|
| #1506 | Pontryagin Tier-A closure (Mathlib-only) |
| #1510 | Averaging-resonance Tier-A closure + IwahoriHecke.Defn skeleton |
| #1512 | IwahoriHecke.Quotient construction |
| #1518 | TypeA + MarkovTrace + 2 Tier-B closures |
| #1525 | Hoefsmit + Tw + 2 Tier-B closures |
| #1529 | Sprint follow-up extensions |
| #1533 | L2 100× shared-root structural recording |
| this | Option E exploration scaffold + Mathlib upstream tracker |

**Total: 8 PRs, 6 conjecture closures, 5 Phase-2 sprints with
content, 2 structural-recording / scaffolding PRs.**

The remaining ~50 source-node conjectures are gated on the
upstream Mathlib dependencies listed above OR are research-grade
(Tier C-research, e.g. Yang-Mills mass gap, Kashaev volume
conjecture — open in mathematics).
