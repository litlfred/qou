/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.Hecke.InteriorMarkovOfBraidedTower

/-!
# Interior bond factors for the `σ`, `σ⁻¹` and symmetric letters

Bean `qou-qqm4`. The bond product (`tr_bondWord_of_braided`, and
`Mass.ProductionChainBondProduct` for the production layout) carries an
**arbitrary** scalar `d` per bond. This file pins `d` for three specific
letters, in the **interior** position a bond actually occupies.

## What is proved

`tr_bond_gen` — the `σ` letter carries `d = 0`: factor `z`. `InteriorMarkov`
restated at the bond; here so the three sit together.

`tr_bond_ginv` — **the content.** The `σ⁻¹` letter carries `d = −h`: factor
`z − h`. The skein relation `σ⁻¹ = σ − h` (`gen_inv_eq_of_quadratic`) fed
through `tr_bond_of_interiorMarkov` at `d = −h`.

`tr_bond_gen_add_ginv` — the unnormalised symmetric letter `σ + σ⁻¹` carries
`2z − h`, i.e. `z − h/2` per letter wherever `2` is invertible. Stated
unnormalised so it needs no `2⁻¹` in `R`.

`bond_factors_of_skein_letters` — the three collected.

All are stated over a `MarkovTrace` carrying `[BraidedTower]`, so
`InteriorMarkov` is **discharged** by `interiorMarkov_of_braided` rather than
assumed: the hypotheses are the tower's defining relations, the Markov axioms,
and the quadratic scalar `h`.

## Why these are not already in the corpus

The corpus has both halves of the `σ⁻¹` fact but never composes them, and it
has the composition only in **right-multiplication** form:

* `MathlibExt.OcneanuTrace.tr_mul_ginv_of_quadratic` — `tr (a * ginv n) =
  (z − h) * tr a`. The `b = 1` case.
* `MathlibExt.DisjointBlockTraceLaw.tr_mul_gen_comb_of_quadratic` — the general
  combination `tr (a * (c • g n + c' • ginv n)) = tr a * ((c+c')·z − c'·h)`.
  Also `b = 1`.
* `mass-theory/interface-knot-markov-z.lean` — over a different structure
  (`MarkovHeckeSkeinAlgebra`), and takes trace-linearity as a *hypothesis*.

A bond carries material on **both** sides, so the bond product needs the
interior form with `b ∈ upper g`. The structural reason it is missing is that
`MarkovInteriorBond` works in `MarkovTower`, which has no `ginv` field at all.

## 🛑 THE `pn` LETTER IS NOT THE SYMMETRIC ONE — corrected before merge

An earlier version of this file, and the first body of its PR, identified the
production `pn` interface with the symmetric letter, i.e. `d_pn = −h/2`. **That
is wrong, and the corpus had already ruled it out on 2026-09-07.** The
production letter is `averaged_weighted`:

    d_pn = −h · (1/2 − δ/4),   δ = (q−1)²(1 − q⁻⁴)/3

carried by `Hecke.ClosedFormInterfaceFactors.bondD`, `MathlibExt.MarkovBondRule.dIface`,
`computations/canonical_braid_crossings.py` and `computations/markov_peel.py`.
`−h/2` is the corpus's **`averaged`** letter — a different `ctype`, and not the
production one.

The two agree through order `ε³` and separate at `ε⁴`:

| | `ε⁰` | `ε¹` | `ε²` | `ε³` | `ε⁴` |
|---|---|---|---|---|---|
| `z − h/2` (symmetric) | `1/2` | `0` | `3/4` | `−3/4` | **`5/8`** |
| `z + d_pn` (production) | `1/2` | `0` | `3/4` | `−3/4` | **`31/24`** |
| measured `pn` bond | `1/2` | `0` | `3/4` | `−3/4` | **`31/24`** |

`computations/probes/bond_pn_kind_order_four_discriminator_probe.py` is the
discriminator, on two objects plus a held-out ³He word. The error is instructive
and is why this block exists: an `ε²` check **passes both**, so agreeing to the
order you happened to expand to is not evidence of identity.

`tr_bond_gen_add_ginv` is therefore a theorem about the `averaged` letter, and
is **not** a statement about the production `pn` interface.

## 🛑 What is NOT proved

1. **The production `pn` letter is not derived here.** Deriving the `δ/4` from
   the colour-tube geometry is `qou-qqm4`'s live open item. Two of the three
   letters are the skein's; the third is not, and nothing here changes that.
2. **`h` is a hypothesis, not a value.** That `h = q − q⁻¹` for `H_n(q)`, and
   that the substrate's `z` is `z_D = q³/(q²+1)`, are elsewhere.
   `BraidedTower.quad` is existential (`∀ m, ∃ h, …`) and cannot supply a
   uniform `h`, which is why it is an explicit argument.
3. **No `c_k`, no binding coefficient, no absolute trace.** The bond model is
   about the *ratio* `tr(atom)/tr(free)`.
4. **Nothing here reaches the production Ocneanu trace.** The only
   `MarkovTrace` on the presented tower factors through a rank-2 quotient;
   `qou-0fmb` is the bridge.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [manuscript] beans qou-qqm4, qou-0fmb; prop:interface-knot-markov-z.
-/

namespace QOU.Hecke.BondLetterIdentification

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.HeckeSandwichReduces
open QOU.Hecke.MarkovInteriorBond QOU.Hecke.InteriorMarkovOfBraidedTower

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (S : MarkovTrace R A) [BraidedTower S]

/-- **The `σ` letter carries `d = 0`**, so a positive-crossing interface's bond
factor is `z` itself. Immediate from `InteriorMarkov`; stated so the three
letters sit together. -/
theorem tr_bond_gen {g : ℕ} {a b : A}
    (ha : a ∈ S.H g) (hb : b ∈ upper (toTowerB S) g) :
    S.tr (a * S.g g * b) = S.z * S.tr (a * b) :=
  interiorMarkov_of_braided S g a ha b hb

/-- **The `σ⁻¹` letter carries `d = −h`**, so a negative-crossing interface's
bond factor is `z − h`.

This is the **interior** counterpart of
`MathlibExt.OcneanuTrace.tr_mul_ginv_of_quadratic`, which is the `b = 1` case.
A bond has material above it as well as below, and the bond product needs that
form; `MarkovTower` has no `ginv` field, which is why the composition lives
here in the `MarkovTrace` vocabulary. -/
theorem tr_bond_ginv {g : ℕ} (h : R)
    (hq : S.g g * S.g g = h • S.g g + 1) {a b : A}
    (ha : a ∈ S.H g) (hb : b ∈ upper (toTowerB S) g) :
    S.tr (a * S.ginv g * b) = (S.z - h) * S.tr (a * b) := by
  have hgi : S.ginv g = S.g g + (-h) • (1 : A) := by
    rw [S.gen_inv_eq_of_quadratic g h hq, neg_smul, ← sub_eq_add_neg]
  rw [hgi]
  have := tr_bond_of_interiorMarkov (toTowerB S) (interiorMarkov_of_braided S)
    (g := g) (a := a) (b := b) ha hb (-h)
  simpa [sub_eq_add_neg] using this

/-- **The unnormalised symmetric letter `σ + σ⁻¹` carries the factor `2z − h`**,
i.e. `z − h/2` per letter wherever `2` is invertible. Stated unnormalised so the
statement needs no `2⁻¹` in `R`.

🛑 This is the corpus's **`averaged`** letter, **not** the production `pn`
interface, which is `averaged_weighted` with `d = −h(1/2 − δ/4)`. The two agree
through `ε³` and separate at `ε⁴` (`5/8` against the measured `31/24`). See the
module docstring. -/
theorem tr_bond_gen_add_ginv {g : ℕ} (h : R)
    (hq : S.g g * S.g g = h • S.g g + 1) {a b : A}
    (ha : a ∈ S.H g) (hb : b ∈ upper (toTowerB S) g) :
    S.tr (a * (S.g g + S.ginv g) * b) = (2 * S.z - h) * S.tr (a * b) := by
  have hsplit : a * (S.g g + S.ginv g) * b = a * S.g g * b + a * S.ginv g * b := by
    rw [mul_add, add_mul]
  rw [hsplit, map_add, tr_bond_gen S ha hb, tr_bond_ginv S h hq ha hb]
  ring

/-- **The three skein letters' interior bond factors, collected.** Given the
quadratic relation's scalar `h`, the `σ`, `σ⁻¹` and symmetric letters carry
`d = 0`, `d = −h` and (after halving) `d = −h/2`. None is measured.

🛑 The *production* `pn` interface is **not** among these — it is
`averaged_weighted`, `d = −h(1/2 − δ/4)`, and deriving that remains open. The
name says `skein_letters` for exactly this reason. -/
theorem bond_factors_of_skein_letters {g : ℕ} (h : R)
    (hq : S.g g * S.g g = h • S.g g + 1) {a b : A}
    (ha : a ∈ S.H g) (hb : b ∈ upper (toTowerB S) g) :
    S.tr (a * S.g g * b) = (S.z + 0) * S.tr (a * b)
      ∧ S.tr (a * S.ginv g * b) = (S.z + -h) * S.tr (a * b)
      ∧ S.tr (a * (S.g g + S.ginv g) * b) = (2 * S.z - h) * S.tr (a * b) := by
  refine ⟨?_, ?_, tr_bond_gen_add_ginv S h hq ha hb⟩
  · simpa using tr_bond_gen S ha hb
  · simpa [sub_eq_add_neg] using tr_bond_ginv S h hq ha hb

end QOU.Hecke.BondLetterIdentification
