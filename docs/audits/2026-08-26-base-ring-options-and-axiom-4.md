# What the base ring can be — and why the stated one fails axiom 4

**Date:** 2026-08-26 · **Branch:** `claude/8-fold-way-qou-k4e8ch` (PR #5819)
**Beans:** `qou-y7vg` (T3g base question)
**Trigger:** owner question — *"give the options of what it can be. I want it as
close to the commutative ring as possible. If we need to add in q and its inverse
that's okay… what's needed downstream as a consumer?"*

## The constraint, from the corpus's own axioms

`def:quantum-universe` axiom 4 requires, per block `λ`:

> a Frobenius weight `∫_A p_λ` **invertible in `R`**, and a quantum dimension
> `dim_q(λ)` **invertible in `R`**

and `quantum-universe-axiom-motivation.md` fixes the reading, deliberately:

> Over a field this is just non-vanishing; over a ring it is the stronger demand,
> **and it is the stronger one that is meant.**

So this is not a technicality to be relaxed. It is the binding constraint, and
everything below follows from it.

## The blocking fact

**The units of `ℤ[q, q⁻¹]` are exactly `{±q^k}`** — it is a Laurent polynomial
ring over a domain. But `dim_q(λ)` is a product of quantum integers, and in the
balanced convention the corpus uses (`[2]_q = q + q⁻¹`, §7c):

| bracket | factorisation | polynomial part |
|---|---|---|
| `[2]_q` | `q⁻¹ (q² + 1)` | degree 2 |
| `[3]_q` | `q⁻² (q²−q+1)(q²+q+1)` | degree 4 |
| `[4]_q` | `q⁻³ (q²+1)(q⁴+1)` | degree 6 |
| `[5]_q` | `q⁻⁴ (q⁴−q³+q²−q+1)(q⁴+q³+q²+q+1)` | degree 8 |

Each is a monomial times a polynomial of positive degree, which is never `±1`.

**So no `[m]_q` with `m ≥ 2` is a unit, and `ℤ[q, q⁻¹]` fails axiom 4 for every
block beyond the trivial one.** The ground ring the corpus names for itself does
not satisfy the corpus's own axiom.

## A bonus: convention D is free

`q · [2]_q = q² + 1`. Since `q` is already a unit, **convention D's denominator
`(q² + 1)` costs nothing beyond `[2]_q`.** Inverting the brackets covers the
Markov parameter `z = q³/(q²+1)` automatically; it is not a separate demand.

## The options, weakest first

| # | Ring | Axiom 4 | Field? | Notes |
|---|---|---|---|---|
| 0 | `ℤ[q, q⁻¹]` | ✗ | no | the stated one; units `±q^k` only |
| 1 | `ℤ[q, q⁻¹][ [2]_q⁻¹, …, [N]_q⁻¹ ]` | ✓ | **no** | minimal repair; `N = 18` measured |
| 2 | `ℤ[q, q⁻¹][ Φ_d(q)⁻¹ : d ≥ 2 ]` | ✓ | **no** | "`q` generic"; no `N` to track |
| 3 | Habiro `\widehat{ℤ[q]}` | ✗ | no | see below |
| 4 | `ℚ(q)` | ✓ | yes | works, but abandons the ring character |

**Option 1 is the recommendation.** It is a localisation of the stated ring — the
smallest change that makes the axioms true — stays a commutative ring, stays
non-local and non-field, and keeps `ℤ` coefficients. `N = 18` because hook
lengths for `λ ⊢ n` are `≤ n` and the corpus reaches `H_18`.

**Option 2** is the same idea stated without a cutoff: `[m]_q` factors into
cyclotomics, so inverting all `Φ_d(q)` for `d ≥ 2` covers every rank at once. It
is cleaner to state and strictly larger; prefer it if tracking `N` is annoying.

**Option 3 fails, and the reason is worth stating** because the Habiro ring looks
like the natural home — the corpus already defines it (`def:habiro-ring`,
`def:z-habiro-ring`) and Ch 12 builds on it. But `\widehat{ℤ[q]}` surjects onto
`ℤ[ζ]` at **every** root of unity, and the brackets vanish at exactly those
points. A ring that admits such a specialisation cannot make `[m]_q` a unit. The
Habiro ring is the right home for *elements* (`q`-series with root-of-unity
evaluations); it is the wrong base for a category whose axioms demand invertible
quantum dimensions.

## The tension this exposes

Axiom 4 in its intended strong form says: **`q` may not be a root of unity of
order `≤ N` in any specialisation of `R`.** That is precisely what a localisation
at the brackets enforces — it deletes those points from `Spec R`.

But open problem 5 names **root-of-unity truncation** as the candidate mechanism
for the observable-scale cutoff, and Ch 12's Habiro machinery exists to evaluate
at roots of unity.

**These pull in opposite directions, and the corpus does not record it.** The
resolution has to be that truncation lives *after* a base change out of `R` —
`R → R/Φ_d` or `R → ℤ[ζ_d]` — and not inside the base the category is linear
over. Otherwise axiom 4 and the truncation mechanism cannot both hold.

## Downstream consumers, measured

- **Lean:** of 2215 `QOU/**.lean`, **394** carry `[CommRing R]`, **185** `[Field R]`,
  5 `[DivisionRing]`, 4 `[GroupWithZero]`, 0 `[LinearOrderedField]`; **684** touch
  `ℝ` (the archimedean wall). The `[Field R]` files are where a weaker base would
  have to be re-examined; the `CommRing` majority is already compatible with
  options 1–2.
- **Rank:** `H_18` is the deepest Hecke algebra the corpus reaches, fixing `N = 18`
  for option 1.
- **Half-powers of `q`: not needed.** The only live `sqrt(q)` is
  `computations/all-elements-knot-table.py:19`, `math.sqrt(q)` — a float64
  archimedean evaluation, not a base-ring demand. Every other hit is under
  `_deprecated/` and is convention-C residue. **No `ℤ[q^{±1/2}]` is required.**
- **Archimedean specialisation survives.** Options 1 and 2 admit the ring map
  `R → ℝ`, `q ↦ q₀ ≈ 1.10998`: at real `q₀ > 1` every balanced bracket is
  strictly positive, so nothing that was inverted is sent to zero.

## Follow-on measured: is `[Field R]` real field dependence?

The 185 `[Field R]` files looked like the main obstacle to a non-field base.
Measured, they are mostly not.

**Only 4 of 185 declare `[Field R]` and never divide at all** — outright
gratuitous, and directly downgradeable to `[CommRing R]`:
`MathlibExt/SDPEmptyConstraints`, `BraidKnot/DepthStratifiedFrobeniusReciprocityVariance`,
`BraidKnot/HeckeFullTwistProduct`, `BraidKnot/HeckeJucysMurphyReduction`.

The other 181 do divide — but by **what** is the decision-relevant question, and
the answer is lopsided. Counting every inverse across those files:

| denominator | occurrences |
|---|---:|
| `q` | **1597** |
| local variables (`D`, `v`, `x`, `s`, `a^2`, `L_k`, `t`, `G`, `u`, `B`, …) | ~205 |
| `q^n`, `q^2`, `q + q⁻¹` | ~21 |
| `(2 : ℂ)` | 17 |

**About 88 % of all field usage is literally `q⁻¹`**, which `ℤ[q, q⁻¹]` already
supplies — no field needed, and no localisation either. The next tier
(`q^n`, `q²`, `q + q⁻¹`) is exactly what options 1 and 2 invert. The `(2 : ℂ)⁻¹`
hits are archimedean-side, past the wall, and say nothing about the base.

So `[Field R]` here is overwhelmingly a **convenience for writing `q⁻¹`** without
carrying an `Invertible q` instance, not a structural demand. The 185 count is
not evidence of deep field dependence, and it should not be read as an argument
against options 1–2.

**Scope of this measurement, stated honestly.** It counts the *syntactic shape*
of denominators, not their semantics. The ~205 local-variable inverses need
per-file inspection to tell a generic nonzero (which genuinely wants a field)
from a name bound to a `q`-expression (which does not). That residue is the only
part of the `[Field R]` surface still unmeasured, and it is where a migration
would actually have to do work.

## What is not settled here

This answers *which ring makes the axioms true*. It does **not** answer the T3g
question of which **base scheme** the gerbe lives over — `Spec R` for whichever
`R` is chosen, versus the Reeb spectral base `Spec(ξ_q)`. Fixing `R` is a
prerequisite for that, not a substitute.
