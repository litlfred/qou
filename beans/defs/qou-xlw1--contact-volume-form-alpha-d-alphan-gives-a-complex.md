---
# qou-xlw1
title: 'Contact volume form: alpha ^ (d alpha)^n gives a COMPLEX rank-n object; rank 3 forces dim M = 7'
status: completed
type: task
priority: high
tags:
    - reorg-2026-10-04
    - 8f-lean
created_at: 2026-09-04T03:32:39Z
updated_at: 2026-10-10T10:14:21Z
parent: qou-8lxd
---

## Body written 2026-10-10 — this bean was TITLE-ONLY from 2026-09-04

Priority `high`, body empty for five weeks. A title-only bean cannot be claimed,
worked or closed; that is the same organisational defect that kept `qou-6766`
parked for eight. Written up here from the title plus a measurement of what the
corpus actually says.

## The claim in the title

> "Contact volume form: `α ∧ (dα)^n` gives a COMPLEX rank-n object; rank 3
> forces `dim M = 7`."

A contact form `α` on a `(2n+1)`-manifold has `α ∧ (dα)^n` as its volume form.
A **rank-3** contact object — three forms `(α₁, α₂, α₃)` carrying an `SU(2)`
triad — is a quaternionic-contact (qc) structure, and Biquard's qc structures
live on `(4n+3)`-manifolds with `n ≥ 1`, i.e. **`dim M ≥ 7`**.

## 🛑 Where the claim bears, and where it does NOT — measured, because conflating these would be an over-claim

**It bears on the parenthetical, not on "3-Sasakian".** `lem:bring-cone-reeb-quaternionic-twist`
(`folio/quantum-observable-universe/brings-surface/bring-cone-reeb-quaternionic-twist.md:4-6`)
states that the cone's link "carries a **3-Sasakian** *(degenerate
quaternionic-contact)* structure: in place of a single Reeb vector field there is
an `SU(2)` triad of contact forms and dual Reeb fields."

- **Against "3-Sasakian" the dimension argument FAILS.** 3-Sasakian manifolds
  have dimension `4n+3` and `n = 0` is allowed — `S³` is 3-Sasakian. The link is
  3-dimensional (the cone is a complex surface, hence a real 4-manifold, per
  `def:bring-cone-tetraplectic-structure`), so dimension alone excludes nothing.
  **Do not write "dim 3 contradicts 3-Sasakian".**
- **Against non-degenerate quaternionic-contact it holds**, and that is exactly
  what the word *"degenerate"* in the lemma is absorbing: a genuine rank-3
  contact object needs `dim M = 7` at minimum, and the link has 3. So the
  parenthetical is load-bearing rather than parenthetical, and the honest
  statement is that **no non-degenerate qc structure exists on a 3-manifold.**

## The expression is NOWHERE in the corpus — this is an unrecorded constraint, not a located defect

Searched, and saying which surfaces so the next reader does not redo it:
`α ∧ (dα)^n` in any spelling, `4n+3`, and `dim M = 7` over all of
`folio/quantum-observable-universe/**/*.md` — **zero hits each**. `contact`
appears in 7 `brings-surface` blocks; `quaternionic-contact` / `3-Sasakian` in
**4** lines total across 3 files. So "resolve or document" means *write the
constraint down*; there is no existing sentence asserting it to correct.

## It is the THIRD independent argument about ONE sentence — hence the block below

Three separate measurements now bear on that same lemma's prose:

1. **`qou-rydq`** — the link is `UT(Σ₄)`, Seifert Euler number **−6** against
   **−1** for the quaternionic model `ℍ`, with **infinite `π₁`** (`SL̃₂(ℝ)`
   geometry); a 3-Sasakian 3-manifold is a spherical space form `S³/Γ`, so `π₁`
   is finite. Lean landed: `BringConeLinkEulerNumber.lean`, sorry-free.
2. **The corpus already carries a countervailing note**, unprompted, at
   `folio/quantum-observable-universe/mass-theory/torus-chain-pages-on-bring.md:26-29`:
   *"a genus-4 unit tangent bundle has `SL̃₂` geometry and admits no 3-Sasakian
   structure, so which real form is intended there is a question for that
   lemma"* — the frame there is the **split** `sl₂(ℝ)`, the triad is the
   **compact** `su(2)`. Audit cited:
   `docs/audits/2026-09-03-bring-cone-link-is-the-unit-tangent-bundle.md`.
3. **This bean** — the dimension count, which is the only one of the three that
   attacks the *qc* half rather than the *3-Sasakian* half.

Enacting them separately would mean three edits to one paragraph, with three
chances to disagree with each other. **Blocked on `qou-rydq`** so the owner's
single pick there covers this; add the dimension sentence to whichever of
`rydq`'s options (1)/(2)/(3) is chosen.

## What does NOT change either way

`QOU/Brings/BringCone.lean`'s `reeb_twist_ij/jk/ki` is a **correct, sorry-free
quaternion identity** — `[M_x, M_y] = 2 M_{x·y}`, the `su(2)` relations with
structure constant `+2`. Nothing in this bean touches it, and nothing in the
mass / binding / `Q_β` chain consumes the tetraplectic material (measured in
`qou-rydq`).

## Options

1. **Fold into `qou-rydq`'s option (2)+(3)** — one paragraph stating: link =
   `UT(Σ₄)`, Euler number −6, `S¹`-action only, and *no non-degenerate qc
   structure since that needs `dim ≥ 7`*; triad scoped as a local/frame
   statement on the smooth model `ℍ = ℂ²`. Cost: a few sentences in one block,
   as part of an edit that is happening anyway. **Recommended** (agent
   judgement) — it is the only option that does not re-open the same paragraph
   twice.
2. **Separate sentence in the lemma, independent of `rydq`.** Cost: a second
   edit to the same prose; risk: it may contradict whatever `rydq` resolves to.
3. **Record in the notation / conventions layer only** (that rank-3 contact
   requires `dim = 4n+3`, `n ≥ 1`) and leave the lemma to `rydq`. Cheapest,
   and loses the connection to the block that needs it.
4. **Nothing.** The constraint stays unwritten and the word "degenerate" keeps
   carrying it silently.

**Default if unanswered: (4).** No number moves; the risk is that a later agent
reads "quaternionic-contact" as a non-degenerate structure and builds on it.

**Blast radius:** `lem:bring-cone-reeb-quaternionic-twist` (+ its `-proof`
sibling), `rem:tetraplectic-su2-gauge-reading`,
`def:bring-cone-tetraplectic-structure`. Lean importers of `BringCone`:
`QuaternionicElectroweak.lean`, `BringConeSplit.lean`,
`Brings/CategoricalLagrangianDMCubic.lean`. No compute, no witness.


## ENACTED 2026-10-10 — folded into `qou-rydq`'s option (2)+(3), as recommended

The owner took option (2)+(3) on `qou-rydq`, and this bean's argument went into
the same paragraph rather than a second edit to the same prose — which was the
whole reason it was `blocked-by` that bean.

What landed, as argument **(iii)** of the restated lemma: a non-degenerate
quaternionic-contact structure is a rank-3 contact object (three forms `α_a`,
each with `α_a ∧ (dα_a)^n` a volume form) and lives on a `(4n+3)`-manifold with
`n ≥ 1`, i.e. **dimension ≥ 7**; the link has dimension 3, so no non-degenerate
quaternionic-contact structure exists on it.

**The half-correction this bean made to its own title is in the block too**, and
it is the part worth keeping: the block says explicitly that dimension alone
excludes *nothing* about 3-Sasakian structures, since `4n+3` allows `n = 0` and
`S³` is 3-Sasakian. It is the infinite-`π₁` / asphericity argument (ii), not a
dimension count, that excludes that reading. Nobody should now write "dim 3
contradicts 3-Sasakian" from this bean's title.

The measured absence stands and is unchanged: `α ∧ (dα)^n` in any spelling,
`4n+3`, and `dim M = 7` all returned **zero** hits corpus-wide before this, so
the constraint was genuinely unrecorded rather than merely mis-stated.
