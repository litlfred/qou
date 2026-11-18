---
# cnd4
title: §3b-cond rule 4 is violated by 19 blocks — and obeying it collides with the detangler
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T13:20:00Z
updated_at: 2026-10-04T15:25:43Z
parent: qou-5p7n
---

Found while working `fwr11` (PR #4921). An adversarial reader flagged one
instance on `prop:transfer-matrix-level-independence`; the corpus scan says it
is a class of **19 blocks / 31 undeclared edges**.

## The rule

AGENTS.md §3b-cond, the conditional-class exception, rule 4 (STRICT):

> **`uses[]` includes the conjecture explicitly.** The conditional dependency is
> auditable from the manifest.

A block may keep a provable kind (`theorem`/`proposition`/…) while sitting
downstream of a conjecture *only if* all five conditions hold, and rule 4 is one
of them. A conditional banner in the `.md` is **part of the theorem statement**
(§4d keeps it in prose deliberately, unlike author-tracking notes), so the block
itself asserts the dependency in the strongest available form.

## The measurement

Blocks whose `.md` opens `**Kind (conditional on [conj:…])**`:

| | blocks |
|---|---|
| declare the conjecture in `uses[]` (compliant) | 14 |
| **do not** (rule-4 violation) | **19** |

31 conjecture edges are asserted in prose and absent from the manifest. Note the
banner is often multi-line and names **several** conjectures — `core-levi-form`
names four — so a single-conjecture regex undercounts this by roughly half.

## The collision

Splitting the 31 by reading order:

| | edges |
|---|---|
| backward — free to declare | **11** |
| forward — declaring adds a forward reference | **19** |
| target unpositioned (`conj:s5-so3-fiber-action`) | 1 |

So for 19 edges, **§3b-cond rule 4 and the `detangler-no-forward-ref` axis pull
in opposite directions.** Obeying the rule costs forward references the whole
`fwr1`–`fwr9` arc existed to remove.

The distances are not marginal:

| source | conjecture | forward by |
|---|---|---|
| `prop:magic-A-binding-formula` | `conj:magic-numbers-bring` | **1008** |
| `prop:hecke-1d-irrep-closed-form-character` | `conj:borromean-quark` | 846 |
| `prop:hoefsmit-V21-cos-symmetrization` | `conj:borromean-quark` | 844 |
| `conj:hoefsmit-scattering-pipeline` | `conj:hyperbolic-volume-transcendence` | 657 |
| `prop:wigner-coefficient-derivation` | `conj:q-integer-mass-formula` | 202 |
| `prop:shell-structure-eigenvalues` | `conj:borromean-quark` | 127 |
| the three `fluid-dynamics` blocks | four NS conjectures | 7–32 each |

## Reading: the edges are right, the ordering is wrong

A proposition conditional on a conjecture should come **after** it — a reader
cannot evaluate "this holds if X" without having met X. So a 1008-position
forward reference is not an argument against declaring the edge; it is evidence
that `conj:magic-numbers-bring` sits ~1000 blocks later than the results
depending on it. That is the `fwr` arc's own category: *the ordering is wrong,
not the edge*.

The three `fluid-dynamics` blocks are the mild case (7–32 forward) and look like
a local ordering slip. `conj:borromean-quark` and `conj:q-integer-mass-formula`
are the systemic ones: each is the declared hypothesis of several results
scattered hundreds of positions ahead of it.

## Disposition

- **The 11 backward edges: declare them.** Rule-mandated, zero ordering cost.
  Landed on PR #4921.
- **The 19 forward edges: not landed.** Declaring them satisfies one STRICT rule
  by violating another axis, and choosing between two of the author's rules is
  not an agent's call. The honest options:
  1. Declare anyway — rule 4 is STRICT and correctness beats tidiness; accept 19
     new forward references and record why.
  2. Move the conjectures earlier — fixes both, and is what the reading above
     actually implies. Largest mover is `conj:magic-numbers-bring`.
  3. Re-scope the banners — if a block is *not* genuinely conditional, the
     banner is the defect and should go.
- **`conj:s5-so3-fiber-action` is unpositioned** — not in any chapter manifest,
  so it is invisible to the detangler either way. That is the `fwr8` parser
  class, and a separate defect.

## The same collision, from the other direction (added 2026-08-10)

`prn1` tranche 1 hit this independently. Of 21 pruned edges restored after
adversarial review, **5 point forward** and turned three blocks red on
`detangler-no-forward-ref`:

| source | target | forward by |
|---|---|---|
| `prf:phi-q-categorical-truncation` | `prop:unified-curvature-rank-mass-formula` | +248 |
| `rem:hecke-charge-mass-duality` | `def:vertex-operator` | +244 |
| `prf:quantum-dilogarithm-stratified` | `prop:curvature-rank-gb-stratification` | +222 |
| `prf:phi-q-categorical-truncation` | `prop:spectral-sequence-collapse` | +221 |
| `prf:phi-q-categorical-truncation` | `prop:curvature-rank-gb-stratification` | +216 |

Held for the same reason as the 19 above, and the reading is the same: an
adversarial reader confirmed each of these as load-bearing, so *the edge is
right and the ordering is wrong.* Two proofs cannot legitimately depend on a
proposition stated ~220 blocks after them.

That makes **24 edges across two independent defects** blocked on one decision:
whether a correct dependency may be declared when declaring it costs a forward
reference. `prop:curvature-rank-gb-stratification` alone is depended on by two
proofs that precede it — see also `msc1` §2, which finds that those same proofs
attribute to it a claim it does not contain. Its position and its content are
both in question.

## Not to be confused with

This is **not** the `prn1` prune damage. These edges were never pruned — the
scan compares each block's own conditional banner against its manifest. Two
independent defects on the same field.

## Round 88 Formalization (`litlfred/qou#8471`)
- Formalized in `QOU.Foundations.BraidPlaceholderResweepArchimedeanMarkerPartitionConditionalEdgeCollisionBaseOrderPivotExtensionInstanceProjectionAudit` (`folio/quantum-observable-universe/lean/QOU/Foundations/BraidPlaceholderResweepArchimedeanMarkerPartitionConditionalEdgeCollisionBaseOrderPivotExtensionInstanceProjectionAudit.lean`).
- 80-dps `mpmath` probe & 2-commit witness (`e47fb91c9186e83c35ba5f8afe823fc02682f7fa` -> `eb5a105f27408ec654ee82cac266aca18e9361f3`, `scriptHash = scriptSha256 = 76b0a54b7612529d0460197f1a503d128d9ca3acb85f7c16e201490dd4b263d6`).
- PR: https://github.com/litlfred/qou/pull/8471
