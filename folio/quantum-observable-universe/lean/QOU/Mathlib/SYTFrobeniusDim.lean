import QOU.Mathlib.SYTEnumeration

/-!
# QOU.Mathlib.SYTFrobeniusDim — the manifestly-integer (Frobenius/Aitken) form of `dimHLF`

The two-row hook dimension is the ballot number `C(a+b,b) − C(a+b,b−1)` (`SYTDimHLFPair.dimHLF_pair`),
a manifest `ℤ` with no floor-division — that is what made the two-row corner-removal recursion (A)
provable by Pascal's rule.  For `m ≥ 3` there is **no** single-binomial closed form; the manifestly-
integer generalisation is the **Frobenius/Aitken determinant in signed-multinomial form**:

    dimHLF λ  =  Σ_{σ ∈ S_m}  sgn(σ) · multinomial(n ; (λ_i − i + σ(i))_i)

(`n!·det(1/(λ_i − i + j)!)` with the determinant expanded over `S_m`).  Each term is an integer
multinomial — the indices sum to `n` since `Σ(λ_i − i + σ(i)) = Σλ_i = n` — and terms with a negative
index vanish.  Integrality of `#SYT` is therefore **global** (the signed sum), not entry-wise.

This file is **step 2a** of closing the general-`n` hook-length formula (bean `sy7b`): it pins the
formula in Lean and `decide`-verifies `dimHLF = frobeniusDim` for `n ≤ 5` — the regression backstop
for the general identity `dimHLF = frobeniusDim` (step 2b, via `Matrix.det_vandermonde` + the
sorry-free hook side).  The two-row specialisation is exactly `C(n,b) − C(n,b−1)`; `(3,2,1)` gives
`60 − 20 − 30 + 6 = 16`.  Pure ℕ/ℤ combinatorics; nothing archimedean.
-/

namespace QOU.Mathlib.SYTEnum

open QOU.BraidKnot.IdentityI (dimHLF sz)

/-- Inversion count of a permutation presented as a list (structurally recursive, kernel-reducible). -/
def inversions : List ℕ → ℕ
  | [] => 0
  | x :: xs => (xs.filter (· < x)).length + inversions xs

/-- The sign `(−1)^{inv σ}` of a permutation-as-list. -/
def signZ (σ : List ℕ) : ℤ := if inversions σ % 2 = 0 then 1 else -1

/-- The shifted indices `λ_i − i + σ(i)` (over `ℤ`, so the negative ones are visible). -/
def frobIdx (l σ : List ℕ) : List ℤ :=
  (List.range l.length).map (fun i => (l.getD i 0 : ℤ) - (i : ℤ) + (σ.getD i 0 : ℤ))

/-- The integer multinomial `n!/∏ k_i!` when the indices are valid (all `≥ 0`, sum `n`), else `0`. -/
def multinomZ (n : ℕ) (ks : List ℤ) : ℤ :=
  if (ks.all (fun k => 0 ≤ k)) && (ks.sum == (n : ℤ)) then
    (n.factorial : ℤ) / (ks.map (fun k => (k.toNat.factorial : ℤ))).prod
  else 0

/-- **Frobenius/Aitken signed-multinomial dimension** — the manifestly-integer form of `dimHLF`. -/
def frobeniusDim (l : List ℕ) : ℤ :=
  ((allPerms (List.range l.length)).map
    (fun σ => signZ σ * multinomZ (sz l) (frobIdx l σ))).sum

/-- **`dimHLF = frobeniusDim`, `decide`-verified for every shape of `n ≤ 4` (sorry-free).** -/
theorem dimHLF_eq_frobeniusDim_le4 :
    ∀ l ∈ shapesLE4, (dimHLF l : ℤ) = frobeniusDim l := by decide

set_option maxRecDepth 20000 in
/-- **`dimHLF = frobeniusDim`, `decide`-verified for every shape of `n = 5` (sorry-free).** -/
theorem dimHLF_eq_frobeniusDim_5 :
    ∀ l ∈ shapes5, (dimHLF l : ℤ) = frobeniusDim l := by decide

end QOU.Mathlib.SYTEnum
