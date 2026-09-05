/-
# The isospin-type class at level 4 is a singleton

`content/quantum-observable-universe/mass-theory/mass-coefficient-shadow-price-proof.md`
classifies each partition's scaling function by its content sum
`c(λ) = Σ_{(i,j)∈λ} (j - i)`:

```
c(λ) > 0   volume-type   (A-dependent)
c(λ) = 0   ISOSPIN-type  (T(T+1)/A^p)
c(λ) < 0   charge-type   (Z-dependent)
```

The Wigner energy is T = 0 isoscalar proton-neutron pairing — a **quartet**
correlation, so `n = 4`. This file shows the isospin-type class at that level
contains **exactly one** partition, `(2,2)`, out of the five partitions of 4:

```
(4)         c =  6     volume-type
(3,1)       c =  2     volume-type
(2,2)       c =  0     ISOSPIN-type   <- the only one
(2,1,1)     c = -2     charge-type
(1,1,1,1)   c = -6     charge-type
```

## Why this is worth stating

The QA note on `mass-formula-regime-switching-table1-data` raises the right
objection to this whole family of coefficients:

> "seven coefficients each written as a short product of q-integers drawn from a
> large menu, agreeing with known LDM values at the 1-6 % level, **is the shape a
> fit takes**; nothing in the table or its parent derives which product goes with
> which coefficient"

For the **Wigner row specifically that objection does not bite**, because the
menu is a singleton. Say "isospin-type" (the corpus's own `c(λ) = 0` rule) and
"quartet" (`n = 4`) and the partition is forced — `(2,2)` — with no freedom left
to fit. That is one row of seven; the objection stands for the other six, and
nothing here touches them.

## What is proved here, and what is not

Proved by `decide`: the five content sums, and that `(2,2)` is the unique
member of the list with `c = 0` (`isospin_class_of_four_is_singleton`).

**Not proved here:** that the list is *all* partitions of 4. That is the standard
`p(4) = 5`, verified by enumeration in
`computations/qbeta/qbeta_isospin_class_singleton_probe.py` rather than in Lean —
formalising partition enumeration over `Nat.Partition` is disproportionate to the
claim. The division is stated so nobody reads the `decide` as more than it is.

Also **not** offered here: the numerical agreement. `pn-bond-cannot-be-extremal.md`
records `Δ_{(2,2)} = m_e [3]_q [2]_q² = 6.2894 MeV` against an empirically
extracted `Δ_W ≈ 6.3 MeV` (Satuła–Nazarewicz 1997); recomputed at `q₀` it is
`6.289300` MeV, 0.17 % off. **That is reported with the fit-shape caveat
attached, not as evidence** — the caveat is the point of the paragraph above,
and a 0.17 % agreement drawn from a menu proves nothing on its own. What the
singleton adds is that this particular number was not drawn from a menu.

Companion to `QOU/Hecke/SelfConjugateRowCap.lean`, which shows the row cap
empties the `c = 0 ∧ ℓ ≤ 2` class at every `n ≥ 5`. Bean `qou-ld2a`.
-/

import Mathlib.Tactic

namespace QOU.Hecke.IsospinClassSingleton

/-- Content of one row: row `i` of length `len` contributes
`Σ_{j < len} (j - i) = len(len-1)/2 - i·len`. -/
def rowContent (i len : ℕ) : ℤ :=
  (len : ℤ) * ((len : ℤ) - 1) / 2 - (i : ℤ) * (len : ℤ)

/-- Content sum from row index `i` downward. -/
def contentFrom : ℕ → List ℕ → ℤ
  | _, [] => 0
  | i, len :: rest => rowContent i len + contentFrom (i + 1) rest

/-- `c(λ) = Σ_{(i,j)∈λ} (j - i)`. -/
def contentSum (l : List ℕ) : ℤ := contentFrom 0 l

/-- The five partitions of 4, in dominance order. Completeness (`p(4) = 5`) is
the standard fact, checked in the probe rather than here. -/
def partitionsOfFour : List (List ℕ) :=
  [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]

/-- The content sums, computed. `(2,2)` is the only zero. -/
theorem contentSums_of_four :
    partitionsOfFour.map contentSum = [6, 2, 0, -2, -6] := by decide

/-- **The isospin-type class at level 4 is a singleton.** Among the partitions
of 4, `c(λ) = 0` holds for `(2,2)` and nothing else — so "isospin-type at the
quartet level" forces the partition with no freedom left to fit. -/
theorem isospin_class_of_four_is_singleton :
    partitionsOfFour.filter (fun p => contentSum p = 0) = [[2, 2]] := by decide

/-- The volume-type members at level 4. -/
theorem volume_class_of_four :
    partitionsOfFour.filter (fun p => 0 < contentSum p) = [[4], [3, 1]] := by decide

/-- The charge-type members at level 4. -/
theorem charge_class_of_four :
    partitionsOfFour.filter (fun p => contentSum p < 0) = [[2, 1, 1], [1, 1, 1, 1]] := by
  decide

/-- `(2,2)` also has at most two rows, so it survives convention D's row cap —
the one self-conjugate shadow price `QOU/Hecke/SelfConjugateRowCap.lean` leaves
standing. -/
theorem two_two_survives_row_cap : ([2, 2] : List ℕ).length ≤ 2 := by decide

/-! ## The charge-type class under the row cap is also a singleton

The same question for `c(λ) < 0`. For a two-row shape `(a,b)` with `b ≤ a`,
summing contents row by row gives `2·c(a,b) = a(a-1) + b(b-3)`, and that is
negative for exactly one pair.

`(1,1)` at `n = 2` is therefore the **unique** charge-type shape the row cap
admits — so "charge-type at its level" forces a partition just as "isospin-type
at the quartet level" does. The selection principle transfers.

**What does not transfer is the number.** `m_e·H_q((1,1)) = m_e[2]_q = 1.0276`
MeV against `a_C ≈ 0.711` — 44 % off — while the corpus uses
`λ_C = h[6]_q·m_e = 0.68244` (−4 %), which is not `m_e·H_q(λ)` for any partition
with `n ≤ 14`. Measured in
`computations/qbeta/qbeta_charge_class_singleton_probe.py`, where the same sweep
finds that **six of the seven coefficients** in
`mass-formula-regime-switching-table1-data` are not hook products at all: they
carry integer prefactors, a bare `h = q - 1/q`, or a quotient, none of which a
product of `[h]_q` yields. Only `δ_S = [2]_q²[3]_q = H_q((2,2))` matches.

That is worth stating carefully. `unified-iterative-correction-proof.md` asserts
`C_λ = m_e·H_q(λ)` as "the universal constant determined by the partition
algebra", without restriction to a family — yet its own `(2,1) ⊢ 3` clause says
the volume/surface/Coulomb coefficients arise "through their image under the
Wedderburn embedding", an unspecified transformation. So the two cannot both be
read at face value, and **the bridge between them is unspecified rather than
contradicted**. Recorded as a gap, not a refutation. Bean `qou-orjl`.
-/

/-- Twice the content sum of the two-row shape `(a, b)`, kept doubled so the
statement stays in `ℤ` with no division: `2·c(a,b) = a(a-1) + b(b-3)`. -/
def contentDoubled (a b : ℕ) : ℤ := (a : ℤ) * ((a : ℤ) - 1) + (b : ℤ) * ((b : ℤ) - 3)

/-- `b(b-3) ≥ -2` for every natural `b`, since `(b-1)(b-2) ≥ 0` over the
integers. This is what stops the second row from ever dragging the content sum
below `-2`. -/
theorem two_le_row_two_content (b : ℕ) : (-2 : ℤ) ≤ (b : ℤ) * ((b : ℤ) - 3) := by
  rcases le_or_gt (b : ℤ) 1 with h | h
  · nlinarith [Int.natCast_nonneg b]
  · have : (2 : ℤ) ≤ (b : ℤ) := by omega
    nlinarith

/-- With two or more columns in the first row the content sum is already
nonnegative, because `a(a-1) ≥ 2` outweighs the second row's floor of `-2`. -/
theorem contentDoubled_nonneg_of_two_le {a b : ℕ} (ha : 2 ≤ a) :
    0 ≤ contentDoubled a b := by
  have h1 : (2 : ℤ) ≤ (a : ℤ) := by exact_mod_cast ha
  have h2 := two_le_row_two_content b
  have h3 : (2 : ℤ) ≤ (a : ℤ) * ((a : ℤ) - 1) := by nlinarith
  simp only [contentDoubled]
  linarith

/-- **The charge-type class the row cap admits is the singleton `{(1,1)}`.**
Among two-row shapes, `c(λ) < 0` holds for `(1,1)` and nothing else. -/
theorem contentDoubled_neg_iff {a b : ℕ} (hab : b ≤ a) :
    contentDoubled a b < 0 ↔ (a = 1 ∧ b = 1) := by
  constructor
  · intro h
    have ha : a < 2 := by
      by_contra hc
      exact absurd h (not_lt.mpr (contentDoubled_nonneg_of_two_le (by omega)))
    interval_cases a <;> interval_cases b <;> simp_all [contentDoubled]
  · rintro ⟨rfl, rfl⟩
    norm_num [contentDoubled]

end QOU.Hecke.IsospinClassSingleton
