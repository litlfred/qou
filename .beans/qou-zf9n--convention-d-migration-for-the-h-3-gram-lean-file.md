---
# qou-zf9n
title: Convention-D migration for the H_3 Gram Lean file and its spectrahedral-phase-collapse consumer
status: todo
type: task
priority: normal
created_at: 2026-08-23T19:27:04Z
updated_at: 2026-08-23T19:27:34Z
---

Found while dispositioning `qou-bm4i` block 5/12 (`prop:gram-matrix-h3-symbolic`).
Branch: claude/rag-document-ingestion-options-orasrw.

## What already landed (do not redo)

`GramMatrixH3Symbolic.lean` now carries BOTH frames, `lean`-direct exit 0, all
eight new declarations sorry-free (`[propext, Classical.choice, Quot.sound]`):

- `markovWeightD`, `markovWeightD_root` — `(q²+1)·z_D − q³ = 0`, the vanishing
  determinant factor, stated in Lean so a later relabel cannot silence it.
- `gramEntryD` / `gramMatrixD` — the 36 canonical entries, rational in `q`.
- `gramEntryD_zero_one` — `G[0,1] = z`, a machine-checkable convention anchor.
- `gramMatrixD_isSymm`, `gramMatrixD_top_left` — the two C results that transfer.
- `gramRadicalD`, `gramRadicalD_ne_zero`, `gramMatrixD_mulVec_radical`,
  `gramMatrixD_det_eq_zero`, `gramMatrixD_not_posDef`.

The C declarations are untouched and now scoped in their docstrings. The
regression guard compares D against D and passes at 2.27e-16; the C−D gap is
retained in the witness as `data`. Derivation + six cross-checks:
`computations/probes/gram_h3_convention_frame_probe.py`.

## What is LEFT, and why it was not done here

### 1. Make `gramMatrix` mean D (the rename)

`lean.ref` on the block still points at `qou:...GramMatrixH3Symbolic.gramMatrix`,
which is the C matrix. The canonical end state is `gramMatrix` = D with the C
one renamed `gramMatrixC`, but that renames ~15 declarations and breaks the one
downstream importer, so it belongs with item 2 rather than half-done here.

### 2. `prop:spectrahedral-phase-collapse` — the claim does not survive D

`QOU/Archimedean/spectrahedral_phase_collapse.lean` is the only Lean importer.
It proves `(gramMatrix u).det = 0` at the supergolden threshold `u³ + u − 1 = 0`
via `detFactor3`, and the block reads that as a *phase transition*: "the Gram
matrix develops a kernel and drops rank at `u = 1/ψ` ... collapses the formal
solution space onto a strictly lower-dimensional face of the Hecke spectrahedron."

Under D the determinant is **identically zero for every `q`**
(`gramMatrixD_det_eq_zero`). So the theorem stays true and becomes **empty**: a
vanishing that holds everywhere singles out no threshold, and there is no
collapse *at* `1/ψ` because there is nowhere it fails to collapse. The physics
reading is what breaks, not the Lean.

This is a scope-(b) structural exclusion and the invariant is the determinant
factorisation, but it is a **claim in a second content block** — deciding what
that block should say instead is authoring, not migration, so it is not done
unilaterally. The honest options look like: retire the block; or re-derive
whether some *other* D-frame object (the Gram on the radical quotient, which
`gram-matrix-dual.witness.json` already carries as `gram_quotient_inverse`)
has a supergolden rank drop, which would be a real result rather than a
relabel.

### 3. Is the supergolden root a C artefact?

Worth settling while in here. `u³ + u − 1` is a factor of the **C**
determinant. Over `ℚ(q,z)` the determinant factors as
`−(z−q)⁵(qz+1)⁵((q²+1)z − q³)(q³z + qz + 1)/q⁸`, so every C-frame "special
value of `u`" is a root of one of those factors *after* substituting
`z = √q/(q+1)`. Whether `1/ψ` is intrinsic or an artefact of that substitution
is answerable directly from the generic form.

## Two cautions for whoever takes this

- **The C results are not wrong and must not be deleted.** They are correct
  theorems about a non-canonical frame; per AGENTS.md a Lean-proved piece is a
  permanent contribution. Scope them, do not remove them.
- **Do not "tidy" the entries.** Splicing the D entries in, a regex that looked
  purely cosmetic stripped numerator parentheses — `(q^7 + q^3) / d` became
  `q^7 + q^3 / d`, a different expression. Six `mulVec` rows went red and Lean
  caught it. Any transformation of these 36 lines needs a re-verify, not an eye.
