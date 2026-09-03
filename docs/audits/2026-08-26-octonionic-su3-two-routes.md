# Two octonionic routes to `SU(3)`, and why only one can work

**Date:** 2026-08-26
**Branch:** `claude/8-fold-way-qou-k4e8ch` (PR #5819)
**Bean:** `qou-8pl3`, Route B
**Lean:** [`QOU/Eightfold/OctonionicSu3RankObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/Eightfold/OctonionicSu3RankObstruction.lean)

## What this is, and what it is not

**Not a new finding.** The 2026-08-25 upload triage
([`2026-08-25-octonion-division-algebra-upload-triage.md`](2026-08-25-octonion-division-algebra-upload-triage.md))
already recorded both obstructions below, in prose, on two of the eight papers:

> maps eight `su(3)` generators onto seven octonion imaginaries by reusing `e₃`,
> which is not injective and not a Lie-algebra map

> `λ₈ ∝ λ₃` collapses the Cartan to rank 1, destroying `A₂`

This document does not rediscover that. It records two things the triage did not
do: the observations are now **machine-checked**, and they are stated as a
**class exclusion** rather than as a defect of two particular papers. A third
paper doing the same thing is now excluded without being read.

## The two routes are not variants

| | Route B as the chapter uses it | Generator identification |
|---|---|---|
| Construction | `SU(3) ⊂ G₂ = Aut(𝕆)` as the stabiliser of one imaginary unit | `λ_a ↔ e_a`, Gell-Mann matrices onto imaginary units |
| `SU(3)` acts | **on** `Im(𝕆)` | **as** `Im(𝕆)` |
| Real dimensions | `Im(𝕆) = ℝ ⊕ ℂ³`, and `1 + 2·3 = 7` ✓ | `dim su(3) = 8` into `dim Im(𝕆) = 7` ✗ |
| Cartan rank | 2, carried by the stabiliser's own torus | collapses to 1 |
| Source | Günaydin–Gürsey 1973 (`gunaydin-gursey1973`) | `arxiv-1107.1559v1`, `arxiv-1205.4617v1` |

The dimension column is the whole story. The stabiliser route never needs a
slot for each generator, because the generators do not have to *be* anything in
`Im(𝕆)` — they act on it. The identification route does, and there are not
enough of them.

## The two obstructions, as theorems

`no_faithful_generator_identification` — **dimension.** `su(3)` has dimension 8
as a real Lie algebra; `Im(𝕆)` has dimension 7. Any linear map from an
8-dimensional space to a 7-dimensional one has a kernel, so no identification of
the eight generators with the seven units is faithful. Stated over a generic
division ring (nothing archimedean is used, per the §7c base-ring convention);
the hypothesis is load-bearing, since swapping the two dimensions makes the
statement false.

`cartan_not_independent_on_one_unit` — **rank.** `su(3)` has rank 2: it needs two
independent commuting generators, conventionally `I₃` and the hypercharge `Y`.
If both are carried onto multiples of a single imaginary unit, they are linearly
dependent. No nonvanishing side condition is required — if both multipliers
vanish the pair is `(0, 0)`, which is not independent either.

These are independent obstructions. The dimension count could conceivably be
dodged by an identification that is not linear; the rank count could not, because
it is about what the images actually are.

## The worked instance, and its self-contradiction

`arxiv-1107.1559v1` (Pushpa, Bisht, Li, Negi, *Quaternion-Octonion SU(3) Flavor
Symmetry*) is worth recording in detail, because the collapse is visible in the
paper's own equations rather than needing to be reconstructed.

Its eq. (29)–(30) set

$$\lambda_a = -\mathrm{i}\,e_a k_a \quad (a = 1,\dots,7), \qquad
  \lambda_8 = -\mathrm{i}\,k_8 e_3, \quad k_8 = \tfrac{8}{\sqrt 3}.$$

Seven units, eight generators — so `λ₃` and `λ₈` both land in `span{e₃}`, which
is the kernel element `k₈λ₃ − k₃λ₈`, explicitly.

Its eq. (31)–(32) then give all four Cartan-related quantities:

$$I_3 = \tfrac{\mathrm{i}e_3}{2},\quad
  V_3 = \tfrac{\mathrm{i}e_3}{4}\Bigl(\tfrac{8}{\sqrt3}+1\Bigr),\quad
  U_3 = \tfrac{\mathrm{i}e_3}{4}\Bigl(\tfrac{8}{\sqrt3}-1\Bigr),\quad
  Y = -\tfrac{8\,\mathrm{i}e_3}{\sqrt3}.$$

Every one is a real multiple of `i e₃`. They span a line. The text on the same
page states:

> `U₃`, `V₃`, `I₃` and `Y` are linearly independent generators and are
> simultaneously diagonalized.

Four multiples of one element cannot be linearly independent, so the paper
contradicts itself on its own equations. This is `cartan_not_independent_on_one_unit`
applied with `u = i e₃`.

A second, smaller arithmetic inconsistency in the same place: eq. (32) writes
`Y = λ₈/√3 = −8 i e₃/√3`, but substituting eq. (30) gives `λ₈/√3 = −i(8/3)e₃`.
And the parenthetical labels in eq. (31) are swapped — the line defining
`V₁ = λ₄/2`, `V₂ = λ₅/2` (which is `V`-spin, connecting `u` and `s`, as the
paper's own preceding sentence says) is labelled `(U − Spin)`, and vice versa.

Recorded not to pile on, but because a future agent grepping `SU(3) flavor
octonion` will land on this paper first: its **title** is exactly the open
question of gap (ii), and it does not answer it.

## What this does and does not settle for `qou-8pl3`

**Settled.** Route B must go through the `G₂` stabiliser. The generator-
identification route-class is a **scope-(b) structural exclusion**, with the
justifying invariants named and machine-checked: dimension (`8 > 7`) and rank
(`2 > 1`).

**Not settled — gap (i).** The Günaydin–Gürsey decomposition `Im(𝕆) ≅ ℝ ⊕ ℂ³`
with `SU(3)` acting on the `ℂ³` in its standard fundamental remains a
**citation**, now properly registered as `gunaydin-gursey1973` with the
decomposition spelled out in its note. Nothing here derives it. What the chain
gives, once it is granted: the triple has triality 1, hence is not self-dual
(`fundamental_not_selfDual`), hence is complex type, hence passes the `Sym²`
gate — and `gate_forces_complex_of_dim_three` says complex type is the only way
anything reaches dimension 3 through that gate.

**Not settled — gap (ii).** Whether an octonionic `SU(3)` can serve as flavour
rather than colour is untouched. `arxiv-1107.1559v1` claims flavour in its title
and argues strong interactions in its conclusion, which is the conflation gap
(ii) warns about, not a resolution of it. The two obvious invariants are already
known blind to the distinction: the `ℤ/3` grading
(`identification_invisible_to_selection_rule`) and the `Sym²` gate
(`gate_does_not_separate_two_triples`).

## Verification

- `lean`-direct **exit 0** against the real import cone (3403 Mathlib oleans
  present; no stub).
- `#print axioms` on all four declarations: `[propext, Classical.choice,
  Quot.sound]` — no `sorryAx`.
- Zero `sorry`, zero `axiom`, no `native_decide`.
