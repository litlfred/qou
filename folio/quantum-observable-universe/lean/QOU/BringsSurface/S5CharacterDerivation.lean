import QOU.BringsSurface.BringHarmonicTypes
import QOU.BringsSurface.BringReflectionParity

/-!
# The character table of `S₅`, derived from the permutations

Bean `qou-u81q`. `BringHarmonicTypes.lean` proves that the seven harmonic types of Bring's
surface are exhaustive, taking the `S₅` character table as a cited input
(`S5Char.chi*`). This file **derives** that table from the permutations themselves, so the
exhaustiveness rests only on standard theorems of representation theory and not on a quoted
table.

## Construction

Every function below is computed from `g : Perm (Fin 5)`:

* `triv = 1`, `sgn = sign g`;
* `[4,1] = fix₁ − 1`, where `fix₁` counts fixed points (the permutation character on points
  minus the trivial character);
* `[3,2] = fix₂ − fix₁`, where `fix₂` counts fixed 2-subsets (points on 2-subsets
  `= triv + [4,1] + [3,2]`);
* `[3,1,1] = Λ²[4,1] = (χ(g)² − χ(g²)) / 2`;
* `[2,1,1,1] = [4,1] ⊗ sgn` and `[2,2,1] = [3,2] ⊗ sgn`.

Each is an integer combination of permutation characters, their tensor products and an exterior
square, so each is a **virtual character**.

## Results (sums over all 120 permutations, by `decide`)

1. `derived_orthonormal`: `Σ_g χ_r(g) χ_s(g) = 120 δ_rs`. A virtual character of norm `1` with
   positive degree is an irreducible character (Serre, *Linear Representations*, §2.3,
   Thm. 5 and its corollary). So these are seven distinct irreducible characters.
2. `derived_sum_dim_sq`: `Σ_r χ_r(1)² = 120 = |S₅|`. Since `Σ (dim ρ)²` over **all** irreducibles
   is `|G|`, there is no eighth irreducible.
3. `derived_matches_table`, `derived_eq_table_everywhere`: `χ_r(g)` equals the `S5Char` table
   entry of the class of `g`, for every one of the 120 permutations. So the table used in
   `BringHarmonicTypes.lean` is the derived one.
4. `class_sizes_derived`: the invariant `(fix₁ g, fix₁ g²)` separates the seven cycle types, and
   counting it over `S₅` gives the class sizes `1, 10, 15, 20, 20, 30, 24`.

Cited (standard, not formalised): the norm-1 lemma for virtual characters, `Σ dim² = |G|`, and
that conjugacy in `S₅` is cycle type. No empirical value enters.

-- Ref: [serre1977] J.-P. Serre, *Linear Representations of Finite Groups*, §2.3.
-/

namespace QOU.Brings.S5CharacterDerivation

open Equiv QOU.Brings.S5Char QOU.Brings.HarmonicTypes

set_option maxRecDepth 200000

/-- Fixed points. -/
def fix₁ (g : Perm (Fin 5)) : ℤ := ((Finset.univ.filter fun i => g i = i).card : ℤ)

/-- Fixed 2-subsets `{a, b}`, `a < b`. -/
def fix₂ (g : Perm (Fin 5)) : ℤ :=
  ((Finset.univ.filter fun p : Fin 5 × Fin 5 =>
    p.1 < p.2 ∧ ((g p.1 = p.1 ∧ g p.2 = p.2) ∨ (g p.1 = p.2 ∧ g p.2 = p.1))).card : ℤ)

def sgnZ (g : Perm (Fin 5)) : ℤ := ((Perm.sign g : ℤˣ) : ℤ)

def dStd (g : Perm (Fin 5)) : ℤ := fix₁ g - 1
def d32 (g : Perm (Fin 5)) : ℤ := fix₂ g - fix₁ g
def d311 (g : Perm (Fin 5)) : ℤ := (dStd g * dStd g - dStd (g * g)) / 2

/-- The seven derived characters, in the order `triv, sgn, [4,1], [2,1,1,1], [3,2], [2,2,1],
[3,1,1]`. -/
def dchi (r : Fin 7) (g : Perm (Fin 5)) : ℤ :=
  match r with
  | 0 => 1
  | 1 => sgnZ g
  | 2 => dStd g
  | 3 => dStd g * sgnZ g
  | 4 => d32 g
  | 5 => d32 g * sgnZ g
  | 6 => d311 g

/-- `Λ²` is integral: `χ(g)² − χ(g²)` is even. -/
theorem d311_even : ∀ g : Perm (Fin 5), 2 ∣ dStd g * dStd g - dStd (g * g) := by decide

/-- The class invariant `(fix₁ g, fix₁ g²)`. -/
def sig (g : Perm (Fin 5)) : ℤ × ℤ := (fix₁ g, fix₁ (g * g))

/-- The derived characters agree with the cited table on the class representatives. -/
theorem derived_matches_table :
    ∀ r i : Fin 7, dchi r (QOU.Brings.ReflectionParity.rep i) = irr r i := by decide

/-- The invariant separates the seven representatives. -/
theorem sig_separates :
    ∀ i j : Fin 7, sig (QOU.Brings.ReflectionParity.rep i) =
      sig (QOU.Brings.ReflectionParity.rep j) → i = j := by decide

/-- **Class sizes, counted.** -/
theorem class_sizes_derived :
    ∀ i : Fin 7, ((Finset.univ.filter fun g : Perm (Fin 5) =>
      sig g = sig (QOU.Brings.ReflectionParity.rep i)).card : ℤ) = classSize i := by decide

/-- Every permutation has the invariant of some representative (the classes cover `S₅`). -/
theorem sig_covers :
    ∀ g : Perm (Fin 5), ∃ i : Fin 7, sig g = sig (QOU.Brings.ReflectionParity.rep i) := by decide

/-- The class of `g`: the representative with the same invariant. -/
def classOf (g : Perm (Fin 5)) : Fin 7 :=
  ((List.finRange 7).find? fun i => sig g = sig (QOU.Brings.ReflectionParity.rep i)).getD 0

/-- **The derived characters are the table, on every permutation**, one type at a time:
`χ_r(g) = table(r, class g)` for all 120 elements. -/
theorem table_everywhere_0 : ∀ g : Perm (Fin 5), dchi 0 g = irr 0 (classOf g) := by decide +kernel
theorem table_everywhere_1 : ∀ g : Perm (Fin 5), dchi 1 g = irr 1 (classOf g) := by decide +kernel
theorem table_everywhere_2 : ∀ g : Perm (Fin 5), dchi 2 g = irr 2 (classOf g) := by decide +kernel
theorem table_everywhere_3 : ∀ g : Perm (Fin 5), dchi 3 g = irr 3 (classOf g) := by decide +kernel
theorem table_everywhere_4 : ∀ g : Perm (Fin 5), dchi 4 g = irr 4 (classOf g) := by decide +kernel
theorem table_everywhere_5 : ∀ g : Perm (Fin 5), dchi 5 g = irr 5 (classOf g) := by decide +kernel
theorem table_everywhere_6 : ∀ g : Perm (Fin 5), dchi 6 g = irr 6 (classOf g) := by decide +kernel

theorem derived_eq_table_everywhere : ∀ g : Perm (Fin 5), ∀ r : Fin 7,
    dchi r g = irr r (classOf g) := by
  intro g r
  fin_cases r
  exacts [table_everywhere_0 g, table_everywhere_1 g, table_everywhere_2 g, table_everywhere_3 g,
    table_everywhere_4 g, table_everywhere_5 g, table_everywhere_6 g]

/-- `Σ_g χ_r(g) χ_s(g)` over all of `S₅`. -/
def gram (r s : Fin 7) : ℤ := ∑ g : Perm (Fin 5), dchi r g * dchi s g

/-- **Orthonormality over the whole group.** -/
theorem derived_orthonormal : ∀ r s : Fin 7, gram r s = if r = s then 120 else 0 := by decide

/-- **`Σ dim² = |S₅|`**: no eighth irreducible. -/
theorem derived_sum_dim_sq :
    ((List.finRange 7).map (fun r => dchi r 1 * dchi r 1)).sum = 120 := by decide

end QOU.Brings.S5CharacterDerivation
