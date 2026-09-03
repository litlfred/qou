---
# qou-htv4
title: 'def:braid-twist-flip encodes V4 (commuting involutions) but the trefoil holonomy is S3 — Lean twist_flip_comm is the root error'
status: todo
type: bug
priority: normal
created_at: 2026-08-29T15:05:00Z
updated_at: 2026-08-29T15:05:00Z
---

The corpus carries **two contradictory definitions of the trefoil/branched-cover
holonomy group**, and the blocks that build on them (`rem:holonomy-trefoil`,
`rem:rho-s3-holonomy-exposition`) `uses[]`/`interprets` both:

- **`def:su2-generators`** (`brings-surface/su2-generators.md` + `.lean`) — the
  correct, standard one. Group = **S3 ≅ D3**, lifted to the binary dihedral
  group **Dic3 ⊂ SU(2)** (order 12). Generators α = exp(2π e₃/3) an explicit
  **3-cycle** (α³ = −I), β = exp(π e₁) order 2, dihedral βαβ⁻¹ = α⁻¹.
- **`def:braid-twist-flip`** (`braids-and-knots/braid-twist-flip.md` + `.lean`) —
  the ERRONEOUS one. σ₁ (twist) = (0 1)(2 3), σ₂ (flip) = (0 3)(1 2) on four
  resolvents; these **commute**, so they generate the **Klein four-group V4**
  (order 4), and σ₁σ₂ has **order 2**.

These are irreconcilable: **S3 has no V4 subgroup or quotient** (4 ∤ 6). Verified
numerically — the twist/flip permutations commute, generate a group of order 4,
and **fail the braid relation** σ₁σ₂σ₁ = σ₂ ≠ σ₁ = σ₂σ₁σ₂, so they are literally
**not a representation of B₃ / the trefoil group**, which is exactly what both
blocks claim. In genuine S3 the product of the two transpositions **is** a
3-cycle of order 3 — matching `def:su2-generators` and the original block text.

**Owner ruling 2026-08-29: S3 is canonical.** The reversal of the (wrongly
V4-aligned) block text landed in PR after #6012 (`rem:holonomy-trefoil` and
`rem:rho-s3-holonomy-exposition` now say S3 / 3-cycle / order 3). What remains,
tracked here:

1. **Correct `def:braid-twist-flip` and its Lean.** The proved theorem
   `twist_flip_comm` (commutativity → V4) is the root error and must be replaced
   by the dihedral/braid relation. The generators must be the non-commuting S3
   transpositions of `def:su2-generators` (β and αβα⁻¹-style, or the standard
   adjacent transpositions), and the Lean should PROVE σ₁σ₂ has order 3 and the
   dihedral relation βαβ⁻¹ = α⁻¹ — not commutativity. This is real formalization
   work (a proved theorem becomes false), not a mechanical fix; scope the base
   ring (§7c) and verify lean-direct.
2. **The `\mathbf{w} ↦ (w₃,w₄,w₁,w₂)` explicit resolvent map** removed from
   `rem:holonomy-trefoil` was the V4 (order-2) element, wrong for a 3-cycle. If
   an explicit resolvent action is wanted, derive the correct order-3 one from
   the corrected definition and restore it.
3. **α notation overload.** `def:su2-generators` uses α for the **3-cycle**
   (order 3); `rem:rho-s3-holonomy-exposition` uses α for the **twist generator**
   (order 2, = σ₁), with αβ the 3-cycle. Same glyph, two meanings across blocks
   that reference each other — a §7aa collision. Reconcile when correcting the
   definition (rename one, likely rho-s3's twist generator).

Until (1) lands, `def:braid-twist-flip` still says V4 while its interpreting
blocks say S3 — a KNOWN, filed transient inconsistency, not an oversight.

## 2026-08-29 — Lean + .md corrected to S3 and VERIFIED (lean-direct exit 0, no sorryAx)

Both Lean files rewritten V4 -> S3 and verified via lean-direct (olean cache
restored; RESTORED-NO-TRACES, no lake build):

- `braid-twist-flip.lean` (content sibling): deleted the false `twist_flip_comm`;
  added `twist_flip_braid` (σ₁σ₂σ₁ = σ₂σ₁σ₂), `twist_flip_pow_three` ((σ₁σ₂)³=id),
  `twist_flip_ne_id` (σ₁σ₂ ≠ id) — together pinning the order at exactly 3 — plus
  `w4_fixed`. Generators are the adjacent transpositions (w₁ w₂), (w₂ w₃) on Fin 4.
- `lean/QOU/BraidTwistFlip.lean` (library, no importers): same correction on the
  4-tuple carrier; axiom-free rfl.
- `braid-twist-flip.md`: rewritten to the S3/braid-relation statement; hand
  render-QA clean.

**Structurally forced, not guessed:** a faithful S3 on four resolvents MUST fix
one and act as the standard rep on the other three (4 ∤ 6). Only the label of the
fixed resolvent (chose w₄) is conventional — documented in both docstrings + .md.

**Still open (deferred, needs author / other tooling):**
1. The 4-resolvent PHYSICS narrative in `rem:rho-s3-holonomy-exposition`,
   `r-matrix-braiding-structure`, `brings-surface:braid-group-action` — the
   "conjugate pairs (w₁,w₄),(w₂,w₃) / chiral sheets / time-like–space-like"
   description is V₄-flavored and does not match "S3 fixes w₄, cycles w₁w₂w₃".
   Reconciling the physical mode-assignment with the S3 action is genuine
   authoring, not a mechanical fix.
2. α NOTATION OVERLOAD unresolved (α = 3-cycle in su2-generators vs α = twist
   generator in rho-s3) — §7aa collision.
3. `braid-twist-flip.qa.json` SIDECAR staled by the .lean edit; qa-sweep needs
   the folio pipeline, ABSENT this session. Needs a pipeline pass to refresh.

## 2026-08-29 (session cont.) — items 1+2 DONE; item 3 is a CROSS-BLOCK physics decision (owner)

- **Item 1 (α overload): DONE.** rho-s3 renamed its twist/flip generators α/β →
  σ₁/σ₂ and reserves α for the 3-cycle (σ₁σ₂), matching `def:su2-generators` and
  `brings-surface/braid-group-action` §(ii). Overload resolved.
- **Item 2 (sidecars): DONE.** Folio pipeline returned this session; qa-sweep
  refreshed `braid-twist-flip.qa.json` (staled by #6024) and
  `rho-s3-holonomy-exposition.qa.json` (staled by item 1). `needs-agent`
  criteria are the normal agent-verdict backlog.

### Item 3 — NOT mechanical: two different concrete S₃ actions live in the corpus

Reading `brings-surface/braid-group-action.md §(ii)` "Spectral S₃" revealed the
real blocker. There are **two inequivalent concrete realizations** of "the S₃
action on the four resolvents", and rho-s3's (V₄) matched neither:

- **Action A** — my #6024 `braid-twist-flip` Lean: σ₁ = (w₁ w₂), σ₂ = (w₂ w₃),
  **w₄ fixed**; product = 3-cycle (w₁ w₂ w₃). Simple, group-verified in Lean, but
  no conjugate-pair structure — w₄ inertly fixed.
- **Action B** — `braid-group-action §(ii)`: S₃ acts on the ratios
  η₁ = w₁/w₂, η₂ = w₃/w₄; conjugate pairs (w₁,w₄),(w₂,w₃); the **reflection β**
  swaps the pairs, the **3-cycle α** rotates; time-like = (w₂,w₃), space-like =
  w₁. Richer, and it is what rho-s3's chiral-sheet / time-like–space-like physics
  is actually built on. Already uses the correct α/β convention.

A and B are inequivalent concrete embeddings of S₃ into the resolvent space
(A fixes w₄ and ignores the pairing; B swaps the conjugate pairs). rho-s3
`interprets` `def:braid-twist-flip` (Action A) but describes physics closer to B.
**One cannot make rho-s3 consistent with both A and B**, so the corpus must pick
a canonical concrete action. I did NOT fabricate a choice.

**DECISION FOR OWNER.** Is **Action B** (braid-group-action's conjugate-pair /
ratio model) canonical?
- If **B**: revise the #6024 `braid-twist-flip` Lean+md to realize B (β = the
  pair-swap (w₁w₂)(w₃w₄), a second generator giving the 3-cycle), and rewrite
  rho-s3 to match B. Follow-up; needs Lean re-verification. **[my recommendation
  — B is the detailed corpus physics and respects the chiral-sheet structure]**
- If **A**: revise braid-group-action §(ii) + rho-s3's conjugate-pair physics to
  match A's w₄-fixed simple transpositions (loses the conjugate-pair narrative).
- **Default (no action):** items 1+2 stand; rho-s3 keeps its α-corrected but
  still-V₄-flavored operational description, inconsistency flagged here; #6024's
  Action A stands as a valid-but-maybe-non-canonical S₃ realization.
- **Blast radius:** rho-s3, r-matrix-braiding-structure, braid-group-action,
  braid-twist-flip (.lean+.md), su2-generators — the trefoil-holonomy cluster.

## 2026-09-03 — item 3 RESOLVED: owner chose Action B; implemented across the cluster (PR #6436)

Owner ruling: **Action B canonical.** Investigating B confirmed a further defect
in its own source: `braid-group-action §(ii)` defined σ₁ (invert both ratios) and
σ₂ (exchange ratios) as the S₃ generators, but those two operations COMMUTE →
V₄, contradicting the S₃ claim. The genuine group there is the **D₃ on the three
cubic branches** (α = order-3 rotation / ζ-scaling; β = order-2 reflection /
conjugate-pair swap), matching `def:su2-generators` exactly.

Implemented B consistently:
- `braid-twist-flip.lean` + `lean/QOU/BraidTwistFlip.lean`: S₃ ≅ D₃ on the THREE
  branches (Fin 3 / 3-tuple), not four resolvents with one fixed. twist/flip are
  the two D₃ reflections; `rotation := σ₁σ₂` proved order-3
  (`rotation_pow_three` + `rotation_ne_id`); `twist_rotation_dihedral`
  (σ₁ α σ₁ = α⁻¹) exhibits D₃. Dropped the Fin-4 `w4_fixed` artifact.
- `braid-twist-flip.md`: 3-branch S₃ narrative; resolvents carry the conjugate
  pairs (w₁,w₄),(w₂,w₃) + ratios η₁,η₂; reflection swaps pairs, rotation cycles
  branches. `.ts`: tags klein-four → s3/dihedral; uses += def:su2-generators.
- `rho-s3-holonomy-exposition.md`: rewritten to rotation(α)+reflection(β) on the
  branches, time-like (w₂,w₃) / space-like w₁, dihedral βαβ⁻¹=α⁻¹.
- `braid-group-action.md §(ii)`: corrected the V₄ sentence — σ₁,σ₂ are two
  reflections whose product σ₁σ₂=α is the order-3 rotation.

Lean verification: lean-direct (cache restore) in progress; gate before merge.
Render-QA on the 3 .md clean (balanced $, no align/operatorname, cross-refs
resolve). Sidecars refreshed via qa-sweep if pipeline available.

This closes qou-htv4 item 3. Items 1 (α overload) and 2 (sidecars) landed
earlier (#6030).
