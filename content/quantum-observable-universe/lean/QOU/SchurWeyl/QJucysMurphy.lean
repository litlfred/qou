import QOU.SchurWeyl.HeckeAlgebra
import QOU.SchurWeyl.HoefsmitRep
import Mathlib.Tactic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# `QOU.SchurWeyl.QJucysMurphy` — q-deformed Jucys–Murphy elements (bean SW-10 / qou-ck0g)

The **Murphy elements** (q-deformed Jucys–Murphy family) `L_0, L_1, …, L_n ∈ H_{n+1}(q)`,
defined recursively by conjugation with the Hecke generators:

  `L_0 = 1`,   `L_{k+1} = σ_k · L_k · σ_k`.

In the Hoefsmit seminormal representation `ρ_λ`, the element `L_k` acts diagonally on
the basis vector indexed by a standard Young tableau `T` with eigenvalue
`q^{2·cellContent(T(k))}`, where `T(k)` is the cell of shape `λ` occupied by entry `k`.

## What is delivered here

* **Definition** (`qJM`): the Murphy elements as a recursive σ-conjugation in
  `Hecke K q qi n`, generic over `[CommRing K]` (AGENTS.md §7c). **Sorry-free.**

* **Inverse Murphy elements** (`qJMInv`): the inverse family, built from `σInv`.
  **Sorry-free** (definition only; the inverse proof is a Ref'd gap).

* **Per-cell algebraic identity** (`cosh_eq_sq_bracket_add_two`): for any `a, b`
  with `a·b = 1` (i.e. `a = q^c`, `b = q^{−c}`),
    `a² + b² = (a − b)² + 2`,
  which is the cleared-denominators form of
    `q^{2c} + q^{−2c} = (q − q⁻¹)² · [c]_q² + 2`.
  **Sorry-free.** This identity shows the two candidate bar-even brackets for `g_λ`
  coincide up to a bar-even scalar and a λ-independent shift (see bean `qou-8vt2`).

* **Seminormal eigenvalue** — GAP: `L_k` acts with eigenvalue `q^{2c(k)}` on the
  seminormal basis. Ref: [ram1997] Theorem 4.1; [murphy1983]; [hoefsmit1974].

* **Commutativity** — GAP: the Murphy elements commute pairwise, generating the
  Gelfand–Tsetlin subalgebra. Ref: [murphy1983] §2.

* **Bar-symmetrised sum** (`barSymJMSum`): `Σ_{k=0}^{n} (L_k + L_k⁻¹)`, the bar-even
  central element whose block eigenvalue is `Σ_{c ∈ λ} (q^{2c} + q^{−2c})`.
  **Definition sorry-free; block eigenvalue is a GAP** (follows from the per-element
  eigenvalue GAP).

## Convention

We follow the QOU Hecke–skein convention (AGENTS.md §7a): `σ_i² = (q − q⁻¹)·σ_i + 1`,
with eigenvalues `{q, −q⁻¹}`. The Murphy-element eigenvalue convention is **`q^{2c}`**
(matching Ram 1997, after normalisation to the skein form). **This convention is NOT
`q^c`** — the factor of 2 in the exponent comes from the skein normalisation where
the quadratic has roots `q, −q⁻¹` (not `q, −1`).

**Cite the convention** — it is not stated elsewhere in this corpus, and conventions
differ by `q ↔ q²` and by sign across the literature.

## Refs

- [murphy1983] G. E. Murphy, *The idempotents of the symmetric group and Nakayama's
  conjecture*, J. Algebra 81 (1983), 258–265.
- [ram1997] A. Ram, *Seminormal representations of Weyl groups and Iwahori–Hecke algebras*,
  Proc. LMS (1997), https://doi.org/10.1112/S0024611597000282.
- [hoefsmit1974] P. N. Hoefsmit, PhD thesis, UBC (1974).
- [dipper-james1986] R. Dipper & G. James, *Representations of Hecke algebras of general
  linear groups*, Proc. LMS (1986).
-/

namespace QOU.SchurWeyl

open Hecke

/-! ## The q-deformed Jucys–Murphy elements -/

section QJMDef

variable (K : Type*) [CommRing K] (q qi : K) (n : ℕ)

/-- **The Murphy elements** `L_k ∈ H_{n+1}(q)` (`= Hecke K q qi n`), defined recursively:
  `L_0 = 1`,   `L_{k+1} = σ_k · L_k · σ_k`.

`Hecke K q qi n` has `n` generators `σ_0, …, σ_{n−1}`, corresponding to the Hecke algebra
`H_{n+1}(q)` (the symmetric group `S_{n+1}` has `n` adjacent transpositions).  There are
`n + 1` Murphy elements `L_0, …, L_n`.  For indices beyond `n`, the recursion freezes
(no generator `σ_k` exists); those elements are semantically meaningless.

The recursion `L_{k+1} = σ_k L_k σ_k` is the q-analogue of the classical Jucys–Murphy
recursion in `MonoidAlgebra k (Equiv.Perm (Fin n))` (see `QOU.BraidKnot.jucysMurphy`). -/
noncomputable def qJM : ℕ → Hecke K q qi n
  | 0 => 1
  | k + 1 =>
    if h : k < n then
      σ K q qi n ⟨k, h⟩ * qJM k * σ K q qi n ⟨k, h⟩
    else qJM k

/-- `L_0 = 1` (the identity element of `H_{n+1}(q)`). -/
@[simp]
theorem qJM_zero : qJM K q qi n 0 = (1 : Hecke K q qi n) := rfl

/-- Recursion step: `L_{k+1} = σ_k · L_k · σ_k` for `k < n`. -/
theorem qJM_succ {k : ℕ} (hk : k < n) :
    qJM K q qi n (k + 1) =
      σ K q qi n ⟨k, hk⟩ * qJM K q qi n k * σ K q qi n ⟨k, hk⟩ :=
  dif_pos hk

/-- `L_1 = σ_0²` (when the algebra has at least one generator). -/
theorem qJM_one (hn : 0 < n) :
    qJM K q qi n 1 =
      σ K q qi n ⟨0, hn⟩ * σ K q qi n ⟨0, hn⟩ := by
  rw [qJM_succ K q qi n hn, qJM_zero, mul_one]

/-- `L_1` expanded via the quadratic relation: `σ_0² = (q − qi)·σ_0 + q·qi`. -/
theorem qJM_one_expand (hn : 0 < n) :
    qJM K q qi n 1 =
      (q - qi) • σ K q qi n ⟨0, hn⟩ + (q * qi) • (1 : Hecke K q qi n) := by
  rw [qJM_one K q qi n hn]
  exact σ_quadratic K q qi n ⟨0, hn⟩

end QJMDef

/-! ## Inverse Murphy elements (for bar-symmetrisation)

When `q · qi = 1` each generator `σ_i` is a unit with `σ_i⁻¹ = σInv_i` (see
`Hecke.σ_mul_σInv`).  The Murphy inverse `L_k⁻¹` is defined by the same recursion
with `σ` replaced by `σInv`. -/

section QJMInv

variable (K : Type*) [CommRing K] (q qi : K) (n : ℕ)

/-- **Inverse Murphy elements** `L_k⁻¹ ∈ H_{n+1}(q)`, defined recursively:
  `L_0⁻¹ = 1`,   `L_{k+1}⁻¹ = σInv_k · L_k⁻¹ · σInv_k`. -/
noncomputable def qJMInv : ℕ → Hecke K q qi n
  | 0 => 1
  | k + 1 =>
    if h : k < n then
      σInv K q qi n ⟨k, h⟩ * qJMInv k * σInv K q qi n ⟨k, h⟩
    else qJMInv k

@[simp]
theorem qJMInv_zero : qJMInv K q qi n 0 = (1 : Hecke K q qi n) := rfl

theorem qJMInv_succ {k : ℕ} (hk : k < n) :
    qJMInv K q qi n (k + 1) =
      σInv K q qi n ⟨k, hk⟩ * qJMInv K q qi n k * σInv K q qi n ⟨k, hk⟩ :=
  dif_pos hk

/-- **`qJMInv` is the right inverse of `qJM`** when `q · qi = 1`.

Proof: straightforward induction on `k`. Base: `1 · 1 = 1`. Step: by
associativity `σ L σ · σ⁻¹ L⁻¹ σ⁻¹ = σ · (L L⁻¹) · σ⁻¹ → σ · σ⁻¹ → 1`,
using the inductive hypothesis `L_k · L_k⁻¹ = 1` and `σ_mul_σInv`. -/
theorem qJM_mul_qJMInv (hqi : q * qi = 1) :
    ∀ (k : ℕ), k ≤ n → qJM K q qi n k * qJMInv K q qi n k = 1
  | 0, _ => by simp
  | k + 1, hk => by
    by_cases h : k < n
    · rw [qJM_succ K q qi n h, qJMInv_succ K q qi n h]
      -- Goal: (σ * L * σ) * (σ⁻¹ * L⁻¹ * σ⁻¹) = 1
      have hσσi := σ_mul_σInv K q qi n hqi ⟨k, h⟩
      have ih := qJM_mul_qJMInv hqi k h.le
      -- Reassociate: (σ * L * σ) * (σ⁻¹ * L⁻¹ * σ⁻¹)
      --            = σ * L * (σ * σ⁻¹) * L⁻¹ * σ⁻¹
      --            = σ * L * 1 * L⁻¹ * σ⁻¹
      --            = σ * (L * L⁻¹) * σ⁻¹
      --            = σ * 1 * σ⁻¹ = σ * σ⁻¹ = 1
      calc σ K q qi n ⟨k, h⟩ * qJM K q qi n k * σ K q qi n ⟨k, h⟩ *
             (σInv K q qi n ⟨k, h⟩ * qJMInv K q qi n k * σInv K q qi n ⟨k, h⟩)
          = σ K q qi n ⟨k, h⟩ * qJM K q qi n k *
            (σ K q qi n ⟨k, h⟩ * σInv K q qi n ⟨k, h⟩) *
            qJMInv K q qi n k * σInv K q qi n ⟨k, h⟩ := by simp only [mul_assoc]
        _ = σ K q qi n ⟨k, h⟩ * qJM K q qi n k * 1 *
            qJMInv K q qi n k * σInv K q qi n ⟨k, h⟩ := by rw [hσσi]
        _ = σ K q qi n ⟨k, h⟩ * (qJM K q qi n k * qJMInv K q qi n k) *
            σInv K q qi n ⟨k, h⟩ := by simp only [mul_assoc, one_mul]
        _ = σ K q qi n ⟨k, h⟩ * 1 * σInv K q qi n ⟨k, h⟩ := by rw [ih]
        _ = σ K q qi n ⟨k, h⟩ * σInv K q qi n ⟨k, h⟩ := by simp only [mul_one]
        _ = 1 := hσσi
    · -- k ≥ n: recursion freezes, reduces to the k-th case
      push_neg at h
      have hkn : k + 1 ≤ n := hk
      omega

/-- **`qJMInv` is the left inverse of `qJM`** when `q · qi = 1`. -/
theorem qJMInv_mul_qJM (hqi : q * qi = 1) :
    ∀ (k : ℕ), k ≤ n → qJMInv K q qi n k * qJM K q qi n k = 1
  | 0, _ => by simp
  | k + 1, hk => by
    by_cases h : k < n
    · rw [qJM_succ K q qi n h, qJMInv_succ K q qi n h]
      have hσiσ := σInv_mul_σ K q qi n hqi ⟨k, h⟩
      have ih := qJMInv_mul_qJM hqi k h.le
      -- Symmetric to qJM_mul_qJMInv
      calc σInv K q qi n ⟨k, h⟩ * qJMInv K q qi n k * σInv K q qi n ⟨k, h⟩ *
             (σ K q qi n ⟨k, h⟩ * qJM K q qi n k * σ K q qi n ⟨k, h⟩)
          = σInv K q qi n ⟨k, h⟩ * qJMInv K q qi n k *
            (σInv K q qi n ⟨k, h⟩ * σ K q qi n ⟨k, h⟩) *
            qJM K q qi n k * σ K q qi n ⟨k, h⟩ := by simp only [mul_assoc]
        _ = σInv K q qi n ⟨k, h⟩ * qJMInv K q qi n k * 1 *
            qJM K q qi n k * σ K q qi n ⟨k, h⟩ := by rw [hσiσ]
        _ = σInv K q qi n ⟨k, h⟩ * (qJMInv K q qi n k * qJM K q qi n k) *
            σ K q qi n ⟨k, h⟩ := by simp only [mul_assoc, one_mul]
        _ = σInv K q qi n ⟨k, h⟩ * 1 * σ K q qi n ⟨k, h⟩ := by rw [ih]
        _ = σInv K q qi n ⟨k, h⟩ * σ K q qi n ⟨k, h⟩ := by simp only [mul_one]
        _ = 1 := hσiσ
    · push_neg at h; omega

end QJMInv

/-! ## Algebraic identity: the cosh–bracket relation (sorry-free)

The key identity connecting the "cosh" form `q^{2c} + q^{−2c}` of the bar-symmetrised
JM eigenvalue to the "bracket" form `(q − q⁻¹)² · [c]_q² + 2`.

In cleared-denominators form with `a = q^c`, `b = q^{−c}` (so `a · b = 1`):

  `a² + b² = (a − b)² + 2`.

The two bar-even candidates for the per-mode rate `g_λ` — the cosh sum
`Σ_{c ∈ λ} (q^{2c} + q^{-2c})` and the bracket sum `(q − q⁻¹)² · Σ [c]_q² + 2n` —
therefore differ only by a bar-even overall scalar `(q − q⁻¹)²` and a λ-independent
shift `2n`. The scalar is normalisation; the shift is an overall heat-trace factor.
**Neither is a spectral degree of freedom.** -/

section CoshBracket

/-- **Cleared-denominators cosh–bracket identity** (sorry-free).

For any `a, b ∈ R` with `a · b = 1`:
  `a² + b² = (a − b)² + 2`.

Instantiate with `a := q^c`, `b := q^{−c}` to obtain the per-cell identity
  `q^{2c} + q^{−2c} = (q^c − q^{−c})² + 2 = (q − q⁻¹)² · [c]_q² + 2`,
the last step by `[c]_q = (q^c − q^{−c})/(q − q⁻¹)`. -/
theorem cosh_eq_sq_bracket_add_two {R : Type*} [CommRing R] (a b : R) (hab : a * b = 1) :
    a ^ 2 + b ^ 2 = (a - b) ^ 2 + 2 := by
  have h : (a - b) ^ 2 = a ^ 2 - 2 * (a * b) + b ^ 2 := by ring
  rw [h, hab]; ring

/-- **Symmetry form** of the cosh–bracket identity: `(a − b)² = a² + b² − 2`.

Useful when the LHS (the bracket form) is the primary, and the RHS (cosh minus
constant) is the target. -/
theorem sq_bracket_eq_cosh_sub_two {R : Type*} [CommRing R] (a b : R) (hab : a * b = 1) :
    (a - b) ^ 2 = a ^ 2 + b ^ 2 - 2 := by
  have h := cosh_eq_sq_bracket_add_two a b hab
  linear_combination -h

end CoshBracket

/-! ## Seminormal eigenvalue and commutativity (GAPs — Ref'd `sorry`)

The deep results from the Hoefsmit/Murphy/Ram theory.  These cannot be proved
without the general seminormal representation (itself a GAP in `HoefsmitRep.lean`,
bean SW-4 residual).  They are stated here as `sorry`-gapped theorems with full
citations so that downstream consumers (`qou-8vt2`) can depend on the API. -/

section SeminormalTheory

/-!
### Eigenvalue statement (informal)

In the seminormal representation `ρ_λ : H_{n+1}(q) →ₐ M_{d_λ}`, the Murphy element
`L_k` (`= qJM K q qi n k`) acts **diagonally** on the basis indexed by SYT of shape
`λ`.  The eigenvalue on the basis vector indexed by SYT `T` is

  `q^{2 · cellContent(T(k))}`,

where `T(k)` is the cell `(row, col)` occupied by entry `k` in `T`, and
`cellContent (row, col) = col − row`.

**Convention alert.** The `q^{2c}` (not `q^c`) arises from the QOU/skein
normalisation `σ² = (q − q⁻¹)σ + 1` with eigenvalues `{q, −q⁻¹}`.  In the
Kazhdan–Lusztig normalisation `T² = (q−1)T + q` (eigenvalues `{q, −1}`), the
eigenvalue would be `q^c`.  The factor-of-2 difference is pure convention.

Refs: [ram1997] Theorem 4.1; [murphy1983] Theorem 1.1; [hoefsmit1974] §3.
-/

/-- **[GAP] The Murphy elements commute pairwise** — they generate the commutative
Gelfand–Tsetlin subalgebra `GZ_{n+1} ⊂ H_{n+1}(q)`.

-- Ref: [murphy1983] §2, Lemma 2.1.  Also [ram1997] Corollary 2.4.
-- The classical proof (the `L_k` are simultaneously diagonalised by the
-- seminormal basis) lifts verbatim to the q-deformed setting.
-- Blocked on: the general seminormal rep (bean SW-4 residual). -/
theorem qJM_commute (K : Type*) [CommRing K] (q qi : K) (n : ℕ) (i j : ℕ)
    (hi : i ≤ n) (hj : j ≤ n) :
    qJM K q qi n i * qJM K q qi n j = qJM K q qi n j * qJM K q qi n i := by
  -- Ref: [murphy1983] Lemma 2.1 — the JM elements generate a commutative subalgebra.
  -- GAP: requires the seminormal diagonalisation (bean SW-4 residual).
  sorry

end SeminormalTheory

/-! ## Bar-symmetrised sum

The bar-even central element whose block eigenvalue is `Σ_{c ∈ λ} (q^{2c} + q^{−2c})`
— the "cosh" form that `qou-8vt2` requires for the per-mode rates `μ_λ(q)`. -/

section BarSymSum

variable (K : Type*) [CommRing K] (q qi : K) (n : ℕ)

/-- **The bar-symmetrised Jucys–Murphy sum** `Θ_n := Σ_{k=0}^{n} (L_k + L_k⁻¹)`.

This is the principled bar-even generator for the q-heat kernel: the bar
involution `q ↦ q⁻¹` sends `L_k ↦ L_k⁻¹`, so each summand `L_k + L_k⁻¹`
is bar-invariant, and hence `Θ_n` is bar-even.  Its block eigenvalue on the
irreducible `ρ_λ` is `Σ_{c ∈ λ} (q^{2c} + q^{−2c})`, the cosh form. -/
noncomputable def barSymJMSum : Hecke K q qi n :=
  ∑ k ∈ Finset.range (n + 1), (qJM K q qi n k + qJMInv K q qi n k)

/-- `Θ_0 = L_0 + L_0⁻¹ = 1 + 1 = 2`. -/
theorem barSymJMSum_zero_eq :
    barSymJMSum K q qi 0 = (1 : Hecke K q qi 0) + 1 := by
  simp only [barSymJMSum, Finset.sum_range_succ, Finset.sum_range_zero,
    qJM_zero, qJMInv_zero, zero_add]

/-! ### Block eigenvalue of the bar-symmetrised sum — GAP

On the irreducible seminormal module `ρ_λ`, the element `Θ_n = barSymJMSum`
acts as the scalar `Σ_{c ∈ λ} (q^{2c} + q^{−2c})`, where the sum runs over
the cells of the Young diagram of `λ`, and `c` is `cellContent (row, col) = col − row`.

This follows immediately from the per-element eigenvalue: if `L_k` acts with eigenvalue
`α_k` on a seminormal basis vector, then `L_k + L_k⁻¹` acts with eigenvalue
`α_k + α_k⁻¹`, and the sum over `k` gives `Σ_k (α_k + α_k⁻¹)`.  Since the
seminormal eigenvalue of `L_k` is `q^{2c(k)}` (Ref: [ram1997]), the block eigenvalue
is `Σ_{c ∈ λ} (q^{2c} + q^{−2c})`.

Via `cosh_eq_sq_bracket_add_two`, this equals `(q − q⁻¹)² · Σ_{c ∈ λ} [c]_q² + 2n`,
showing the two candidate bar-even brackets differ only by normalisation and
a λ-independent shift — no spectral degree of freedom remains.

Ref: [ram1997] Theorem 4.1 + the per-cell cosh–bracket identity above.
GAP: requires the per-element eigenvalue (itself gapped on bean SW-4 residual).
The formal statement would quantify over Partition N, SYT, etc.; we leave
it as a docstring-level specification until the general seminormal rep lands. -/

end BarSymSum

end QOU.SchurWeyl
