/-
  Crossing parity of composite nuclear knots: n_K(A(Z,N)) ≡ Z (mod 2).

  The composite crossing number n_K = A² + 7A + 5Z from the crossing
  budget (8A nucleon internal + A(A-1) inter-nucleon + 3Z electron +
  2Z electron binding).  Since A(A+1) is always even, the parity
  reduces to Z mod 2.
-/
import Mathlib.Data.Nat.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace QOU.Information

/-- **Composite crossing number** of an atom A(Z, N) with mass number A = Z + N.
    n_K = A² + 7A + 5Z from the crossing budget:
    - 8A (nucleon internal: 6 Borromean + 2 Hopf per nucleon)
    - A(A-1) (inter-nucleon Hopf links: 2 per pair × C(A,2))
    - 3Z (electron trefoils)
    - 2Z (electron-nucleus Hopf binding)
    Label: conj:composite-crossing-parity -/
def compositeCrossingNumber (Z N : ℕ) : ℕ :=
  let A := Z + N
  A * A + 7 * A + 5 * Z

/-- The crossing budget decomposes into four contributions. -/
theorem crossingBudget (Z N : ℕ) :
    compositeCrossingNumber Z N =
    8 * (Z + N) + (Z + N) * (Z + N - 1) + 3 * Z + 2 * Z := by
  -- `show` forces the explicit form (defeq to the `let`), so the truncated
  -- `A - 1` and the products are visible. Identity: A²+7A+5Z = 8A+A(A-1)+5Z.
  show (Z + N) * (Z + N) + 7 * (Z + N) + 5 * Z
      = 8 * (Z + N) + (Z + N) * (Z + N - 1) + 3 * Z + 2 * Z
  rcases Nat.eq_zero_or_pos (Z + N) with h | h
  · rw [h]; ring
  · obtain ⟨b, hb⟩ : ∃ b, Z + N = b + 1 := ⟨(Z + N) - 1, by omega⟩
    rw [hb]; simp only [Nat.add_sub_cancel]; ring

/-- **Main theorem**: the composite crossing number has the same parity
    as the atomic number Z.

    n_K(A(Z,N)) ≡ Z  (mod 2)

    Proof: n_K = A² + 7A + 5Z.  Since A² + 7A = A(A+7) and
    A(A+7) ≡ A(A+1) + 6A ≡ 0 + 0 ≡ 0 (mod 2) (because A(A+1) is the
    product of consecutive integers, always even, and 6A is always even),
    we get n_K ≡ 5Z ≡ Z (mod 2). -/
theorem crossing_parity_eq_Z (Z N : ℕ) :
    compositeCrossingNumber Z N % 2 = Z % 2 := by
  -- `show` forces the explicit form (defeq to the `let`) so `omega` sees the
  -- product `(Z+N)*(Z+N)` rather than treating the whole body as one atom.
  show ((Z + N) * (Z + N) + 7 * (Z + N) + 5 * Z) % 2 = Z % 2
  -- The only nonlinear term is A²; a square preserves parity (`m² ≡ m mod 2`),
  -- so the rest is linear parity arithmetic that `omega` discharges.
  have key : ∀ m : ℕ, m * m % 2 = m % 2 := by
    intro m
    rcases Nat.mod_two_eq_zero_or_one m with h | h <;> simp [Nat.mul_mod, h]
  have h := key (Z + N)
  omega

/-- Atoms with even atomic number have even crossing number. -/
theorem even_Z_even_crossing (Z N : ℕ) (hZ : Z % 2 = 0) :
    compositeCrossingNumber Z N % 2 = 0 := by
  rw [crossing_parity_eq_Z]; exact hZ

/-- Atoms with odd atomic number have odd crossing number. -/
theorem odd_Z_odd_crossing (Z N : ℕ) (hZ : Z % 2 = 1) :
    compositeCrossingNumber Z N % 2 = 1 := by
  rw [crossing_parity_eq_Z]; exact hZ

/-- **Hydrogen** (Z = 1, N = 0): crossing number n_K = 13, which is odd. -/
theorem hydrogen_crossing : compositeCrossingNumber 1 0 = 13 := by
  unfold compositeCrossingNumber; norm_num

/-- **Hydrogen has odd crossing number** (Z = 1 is odd). -/
theorem hydrogen_odd : compositeCrossingNumber 1 0 % 2 = 1 := by
  rw [hydrogen_crossing]

/-- **Helium** (Z = 2, N = 2): crossing number n_K = A²+7A+5Z = 16+28+10 = 54,
    which is even. -/
theorem helium_crossing : compositeCrossingNumber 2 2 = 54 := by
  unfold compositeCrossingNumber; norm_num

/-- **Helium has even crossing number** (Z = 2 is even). -/
theorem helium_even : compositeCrossingNumber 2 2 % 2 = 0 := by
  rw [helium_crossing]

/-- **Nitrogen** (Z = 7, N = 7): odd crossing number. -/
theorem nitrogen_odd : compositeCrossingNumber 7 7 % 2 = 1 := by
  rw [crossing_parity_eq_Z]

/-- **Arsenic** (Z = 33, N = 42): odd crossing number. -/
theorem arsenic_odd : compositeCrossingNumber 33 42 % 2 = 1 := by
  rw [crossing_parity_eq_Z]

/-- **Iron** (Z = 26, N = 30): even crossing number. -/
theorem iron_even : compositeCrossingNumber 26 30 % 2 = 0 := by
  rw [crossing_parity_eq_Z]

/-- **Iodine** (Z = 53, N = 74): odd crossing number. -/
theorem iodine_odd : compositeCrossingNumber 53 74 % 2 = 1 := by
  rw [crossing_parity_eq_Z]

end QOU.Information
