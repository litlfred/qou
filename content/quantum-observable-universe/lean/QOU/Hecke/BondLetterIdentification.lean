/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.Hecke.InteriorMarkovOfBraidedTower

/-!
# The production bond letters are DERIVED, not three measured numbers

Bean `qou-qqm4`. `computations/probes/bond_factors_are_z_plus_d_probe.py` records
the three production interface letters and their bond factors as **measured**, by
turning one interface on at `A = 3`:

| interface | letter | measured bond factor, `ε`-series at `q = 1+ε` |
|---|---|---|
| `pp` | `σ` | `1/2, 1, 1/4` |
| `pn` | `averaged_weighted` | `1/2, 0, 3/4` |
| `nn` | `σ⁻¹` | `1/2, −1, 5/4` |

Those three series are, respectively, `z_D`, `z_D − h/2` and `z_D − h` at
`z_D = q³/(q²+1)`, `h = q − q⁻¹` — coefficient for coefficient. This file proves
the underlying algebra, so the three numbers stop being three independent
measurements and become **one scalar `h` and a choice of letter**.

## What is proved

`tr_bond_gen` — the `σ` letter carries `d = 0`: the factor is `z`. This is
`InteriorMarkov` restated at the bond, and is included only so the three sit
together.

`tr_bond_ginv` — **the `σ⁻¹` letter carries `d = −h`**: the factor is `z − h`.
The whole content is the skein relation `σ⁻¹ = σ − h` (`gen_inv_eq_of_quadratic`)
fed through `tr_bond_of_interiorMarkov` at `d = −h`.

`tr_bond_gen_add_ginv` — the unnormalised symmetric letter `σ + σ⁻¹` carries the
factor `2z − h`, so the *average* letter carries `z − h/2` wherever `2` is
invertible. Stated unnormalised to avoid needing `2⁻¹` in `R`.

`bond_letters_determined` — the three collected: the `d` of the production
letters are `0`, `−h`, `−h/2`, all fixed by the single scalar `h` of the
quadratic relation.

Everything is stated over a `MarkovTrace` carrying `[BraidedTower]`, so
`InteriorMarkov` is discharged by `interiorMarkov_of_braided` rather than
assumed: the only hypotheses are the tower's own defining relations, the Markov
axioms, and the quadratic scalar `h`.

## Why this is not already in the corpus

`MathlibExt.OcneanuTrace.tr_mul_ginv_of_quadratic` proves the **stabilisation**
form `tr (a * ginv n) = (z − h) * tr a` — the case `b = 1`, nothing above the
generator. A *bond* has material on both sides, so the bond product needs the
**interior** form with `b ∈ upper g`, which is what `tr_bond_ginv` supplies. The
two proofs share the `ginv = g − h•1` rewrite and differ in what they push it
through: `markov` there, `InteriorMarkov` here.

## 🛑 What is NOT proved

1. **The `pn` letter is still a modelling choice.** `tr_bond_gen_add_ginv` says
   what the symmetric letter's factor *is*; it does not say the `pn` interface
   *should* be the symmetric letter. That the unlike-pair interface is the
   average of the like-pair ones is the producer's `averaged_weighted`
   convention, and this file does not derive it — it only shows that **granting
   it, the value follows**. So the letter set reduces from three free numbers to
   **one convention**, not to zero.
2. **`h` is a hypothesis, not a value.** Every statement takes the quadratic
   relation's scalar as an explicit argument. That `h = q − q⁻¹` for `H_n(q)`,
   and that the substrate's `z` is `z_D = q³/(q²+1)`, are elsewhere.
3. **No `c_k`, no binding coefficient, no absolute trace.** The bond model is
   about the *ratio* `tr(atom)/tr(free)`; the free half is a separate object.
4. **`BraidedTower.quad` is existential** (`∀ m, ∃ h, …`), so it cannot supply a
   uniform `h`. Taking `h` explicitly is what keeps these statements honest
   about that, and matches `gen_inv_eq_of_quadratic`'s own signature.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [manuscript] beans qou-qqm4; computations/probes/bond_factors_are_z_plus_d_probe.py
-/

namespace QOU.Hecke.BondLetterIdentification

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.HeckeSandwichReduces
open QOU.Hecke.MarkovInteriorBond QOU.Hecke.InteriorMarkovOfBraidedTower

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (S : MarkovTrace R A) [BraidedTower S]

/-- **The `σ` letter carries `d = 0`.** The `pp` interface's bond factor is `z`
itself. Immediate from `InteriorMarkov`; stated so the three letters sit
together. -/
theorem tr_bond_gen {g : ℕ} {a b : A}
    (ha : a ∈ S.H g) (hb : b ∈ upper (toTowerB S) g) :
    S.tr (a * S.g g * b) = S.z * S.tr (a * b) :=
  interiorMarkov_of_braided S g a ha b hb

/-- **The `σ⁻¹` letter carries `d = −h`**, so the `nn` interface's bond factor is
`z − h`.

This is the interior counterpart of
`MathlibExt.OcneanuTrace.tr_mul_ginv_of_quadratic`, which is the `b = 1` case.
A bond has material above it as well as below, and the bond product needs that
form. -/
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

/-- **The unnormalised symmetric letter `σ + σ⁻¹` carries the factor `2z − h`.**

Dividing by `2` — legitimate wherever `2` is invertible in `R` — gives the
average letter's factor `z − h/2`, which is the measured `pn` bond factor.
Stated unnormalised so the statement needs no `2⁻¹`. -/
theorem tr_bond_gen_add_ginv {g : ℕ} (h : R)
    (hq : S.g g * S.g g = h • S.g g + 1) {a b : A}
    (ha : a ∈ S.H g) (hb : b ∈ upper (toTowerB S) g) :
    S.tr (a * (S.g g + S.ginv g) * b) = (2 * S.z - h) * S.tr (a * b) := by
  have hsplit : a * (S.g g + S.ginv g) * b = a * S.g g * b + a * S.ginv g * b := by
    rw [mul_add, add_mul]
  rw [hsplit, map_add, tr_bond_gen S ha hb, tr_bond_ginv S h hq ha hb]
  ring

/-- **The three production bond letters are fixed by the single scalar `h`.**

Collecting the above: the `d` of `σ` is `0`, the `d` of `σ⁻¹` is `−h`, and the
unnormalised symmetric letter contributes `2z − h`, i.e. `d = −h/2` per letter
after halving. Nothing here is measured — given the quadratic relation's `h`,
all three follow.

🛑 This does **not** derive that the `pn` interface *is* the symmetric letter;
that remains the producer's `averaged_weighted` convention. See the module
docstring. -/
theorem bond_letters_determined {g : ℕ} (h : R)
    (hq : S.g g * S.g g = h • S.g g + 1) {a b : A}
    (ha : a ∈ S.H g) (hb : b ∈ upper (toTowerB S) g) :
    S.tr (a * S.g g * b) = (S.z + 0) * S.tr (a * b)
      ∧ S.tr (a * S.ginv g * b) = (S.z + -h) * S.tr (a * b)
      ∧ S.tr (a * (S.g g + S.ginv g) * b) = (2 * S.z - h) * S.tr (a * b) := by
  refine ⟨?_, ?_, tr_bond_gen_add_ginv S h hq ha hb⟩
  · simpa using tr_bond_gen S ha hb
  · simpa [sub_eq_add_neg] using tr_bond_ginv S h hq ha hb

end QOU.Hecke.BondLetterIdentification
