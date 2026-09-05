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

end QOU.Hecke.IsospinClassSingleton
