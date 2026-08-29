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
