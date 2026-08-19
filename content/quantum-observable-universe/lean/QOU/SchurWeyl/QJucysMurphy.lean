import QOU.SchurWeyl.HeckeAlgebra
import QOU.SchurWeyl.HoefsmitRep
import QOU.SchurWeyl.TableauCells
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
  seminormal basis. Ref: [ram1997] Theorem 4.1; [murphy1992]; [hoefsmit1974].

* **Commutativity** — the Murphy elements commute pairwise, generating the
  Gelfand–Tsetlin subalgebra. **Proved** (`qJM_commute`, via `qJM_commute_proved`)
  from the braid and far-commutation relations alone.
  Ref: [murphy1992] §2; [murphy1981] for the q = 1 case.

* **Bar-symmetrised sum** (`barSymJMSum`): `Σ_{k=0}^{n} (L_k + L_k⁻¹)`, the bar-even
  central element whose block eigenvalue is `Σ_{c ∈ λ} (q^{2c} + q^{−2c})`.
  **Definition sorry-free; centrality proved** given `q · qi = 1`
  (`barSymJMSum_central`); **the block eigenvalue is the one remaining GAP** in this
  file, and it is stated at generic `q` (`0 < q`, `q ≠ 1`) — see its docstring for
  why the roots-of-unity regime is excluded rather than deferred.

## Convention

We follow the QOU Hecke–skein convention (AGENTS.md §7a): `σ_i² = (q − q⁻¹)·σ_i + 1`,
with eigenvalues `{q, −q⁻¹}`. The Murphy-element eigenvalue convention is **`q^{2c}`**
(matching Ram 1997, after normalisation to the skein form). **This convention is NOT
`q^c`** — the factor of 2 in the exponent comes from the skein normalisation where
the quadratic has roots `q, −q⁻¹` (not `q, −1`).

**Cite the convention** — it is not stated elsewhere in this corpus, and conventions
differ by `q ↔ q²` and by sign across the literature.

## Refs

- [murphy1992] G. E. Murphy, *On the representation theory of the symmetric groups and
  associated Hecke algebras*, J. Algebra 152 (1992), 492–513 — the q-deformed Murphy operators.
- [murphy1981] G. E. Murphy, *A new construction of Young's seminormal representation of the
  symmetric groups*, J. Algebra 69 (1981), 287–297.
- [ram1997] A. Ram, *Seminormal representations of Weyl groups and Iwahori–Hecke algebras*,
  Proc. LMS (1997), https://doi.org/10.1112/S0024611597000282.
- [hoefsmit1974] P. N. Hoefsmit, PhD thesis, UBC (1974).
- [dipper-james1986] R. Dipper & G. James, *Representations of Hecke algebras of general
  linear groups*, Proc. LMS (1986).

NB: earlier drafts cited a non-existent `[murphy1983]` key (broken `-- Ref:` per AGENTS.md §1);
the correct in-corpus keys are `[murphy1992]` (Hecke Murphy operators) and `[murphy1981]`
(seminormal construction). **That note was added and the three live citations below were
left on the broken key anyway** — fixed 2026-08-16. A note recording a defect is not a
fix, and this one sat directly above the uses it described.
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
            qJMInv K q qi n k * σInv K q qi n ⟨k, h⟩ := by noncomm_ring
        _ = σ K q qi n ⟨k, h⟩ * qJM K q qi n k * 1 *
            qJMInv K q qi n k * σInv K q qi n ⟨k, h⟩ := by rw [hσσi]
        _ = σ K q qi n ⟨k, h⟩ * (qJM K q qi n k * qJMInv K q qi n k) *
            σInv K q qi n ⟨k, h⟩ := by noncomm_ring
        _ = σ K q qi n ⟨k, h⟩ * 1 * σInv K q qi n ⟨k, h⟩ := by rw [ih]
        _ = σ K q qi n ⟨k, h⟩ * σInv K q qi n ⟨k, h⟩ := by noncomm_ring
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
            qJM K q qi n k * σ K q qi n ⟨k, h⟩ := by noncomm_ring
        _ = σInv K q qi n ⟨k, h⟩ * qJMInv K q qi n k * 1 *
            qJM K q qi n k * σ K q qi n ⟨k, h⟩ := by rw [hσiσ]
        _ = σInv K q qi n ⟨k, h⟩ * (qJMInv K q qi n k * qJM K q qi n k) *
            σ K q qi n ⟨k, h⟩ := by noncomm_ring
        _ = σInv K q qi n ⟨k, h⟩ * 1 * σ K q qi n ⟨k, h⟩ := by rw [ih]
        _ = σInv K q qi n ⟨k, h⟩ * σ K q qi n ⟨k, h⟩ := by noncomm_ring
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

Refs: [ram1997] Theorem 4.1; [murphy1992] Theorem 1.1; [hoefsmit1974] §3.
-/

section AdjacentReduction

variable (K : Type*) [CommRing K] (q qi : K) (n : ℕ)

/-! ### Reducing commutativity to the adjacent case

`qJM_commute` below is commented *"Blocked on: the general seminormal rep"*.
It is not. `qJM` is the multiplicative recursion `L_{k+1} = σ_k L_k σ_k`, and
commutativity from that recursion is an induction on the **Hecke relations** —
no representation is involved. The two results here carry it as far as it goes
without new mathematics, and isolate exactly what is left.

**What is left is the adjacent case** `L_k L_{k+1} = L_{k+1} L_k`, and it is not
a base case that falls out: the general case *reduces to* it rather than around
it, because peeling `σ_{j-1}` off `L_j` needs `i + 1 ≤ j - 1`, which fails
precisely when `i = j - 1`. -/

/-- `σ_m` commutes with `L_k` whenever `k + 1 ≤ m`. -/
theorem qJM_comm_sigma (m : Fin n) :
    ∀ k : ℕ, k + 1 ≤ (m : ℕ) →
      σ K q qi n m * qJM K q qi n k = qJM K q qi n k * σ K q qi n m := by
  intro k
  induction k with
  | zero => intro _; rw [qJM_zero]; rw [mul_one, one_mul]
  | succ k ih =>
    intro hm
    by_cases hk : k < n
    · rw [qJM_succ K q qi n hk]
      have hfar : (⟨k, hk⟩ : Fin n).val + 2 ≤ (m : ℕ) := by simpa using hm
      have h1 : σ K q qi n m * σ K q qi n ⟨k, hk⟩
              = σ K q qi n ⟨k, hk⟩ * σ K q qi n m := σ_commute K q qi n m ⟨k, hk⟩ hfar
      have h2 := ih (by omega)
      calc σ K q qi n m * (σ K q qi n ⟨k, hk⟩ * qJM K q qi n k * σ K q qi n ⟨k, hk⟩)
          = (σ K q qi n m * σ K q qi n ⟨k, hk⟩) * qJM K q qi n k * σ K q qi n ⟨k, hk⟩ := by
            simp only [mul_assoc]
        _ = (σ K q qi n ⟨k, hk⟩ * σ K q qi n m) * qJM K q qi n k * σ K q qi n ⟨k, hk⟩ := by
            rw [h1]
        _ = σ K q qi n ⟨k, hk⟩ * (σ K q qi n m * qJM K q qi n k) * σ K q qi n ⟨k, hk⟩ := by
            simp only [mul_assoc]
        _ = σ K q qi n ⟨k, hk⟩ * (qJM K q qi n k * σ K q qi n m) * σ K q qi n ⟨k, hk⟩ := by
            rw [h2]
        _ = σ K q qi n ⟨k, hk⟩ * qJM K q qi n k * (σ K q qi n m * σ K q qi n ⟨k, hk⟩) := by
            simp only [mul_assoc]
        _ = σ K q qi n ⟨k, hk⟩ * qJM K q qi n k * (σ K q qi n ⟨k, hk⟩ * σ K q qi n m) := by
            rw [h1]
        _ = σ K q qi n ⟨k, hk⟩ * qJM K q qi n k * σ K q qi n ⟨k, hk⟩ * σ K q qi n m := by
            simp only [mul_assoc]
    · have : qJM K q qi n (k + 1) = qJM K q qi n k := dif_neg hk
      rw [this]; exact ih (by omega)

/-- **Full commutativity follows from the adjacent case alone.**

Everything except `L_k L_{k+1} = L_{k+1} L_k` is bookkeeping: `σ_{j-1}` commutes
with `L_i` as soon as `i + 1 ≤ j - 1` (`qJM_comm_sigma`), which peels one step
off `L_j = σ_{j-1} L_{j-1} σ_{j-1}` and hands the rest to the induction. -/
theorem qJM_commute_of_adjacent
    (hadj : ∀ k : ℕ, qJM K q qi n k * qJM K q qi n (k + 1)
                   = qJM K q qi n (k + 1) * qJM K q qi n k) :
    ∀ j i : ℕ, i ≤ j →
      qJM K q qi n i * qJM K q qi n j = qJM K q qi n j * qJM K q qi n i := by
  intro j
  induction j with
  | zero => intro i hi; interval_cases i; rfl
  | succ j ih =>
    intro i hi
    rcases Nat.lt_or_ge i (j + 1) with hlt | hge
    · -- i ≤ j
      have hij : i ≤ j := Nat.lt_succ_iff.mp hlt
      rcases Nat.eq_or_lt_of_le hij with rfl | hij'
      · -- i = j : the adjacent case, supplied as a hypothesis
        exact hadj i
      · -- i < j : peel sigma off L_{j+1} and use the induction hypothesis
        by_cases hk : j < n
        · have hsig : i + 1 <= (⟨j, hk⟩ : Fin n).val := by simpa using hij'
          have hs := qJM_comm_sigma K q qi n ⟨j, hk⟩ i hsig
          have hL := ih i (le_of_lt hij')
          rw [qJM_succ K q qi n hk]
          calc qJM K q qi n i * (σ K q qi n ⟨j, hk⟩ * qJM K q qi n j * σ K q qi n ⟨j, hk⟩)
              = (qJM K q qi n i * σ K q qi n ⟨j, hk⟩) * qJM K q qi n j * σ K q qi n ⟨j, hk⟩ := by
                simp only [mul_assoc]
            _ = (σ K q qi n ⟨j, hk⟩ * qJM K q qi n i) * qJM K q qi n j * σ K q qi n ⟨j, hk⟩ := by
                rw [← hs]
            _ = σ K q qi n ⟨j, hk⟩ * (qJM K q qi n i * qJM K q qi n j) * σ K q qi n ⟨j, hk⟩ := by
                simp only [mul_assoc]
            _ = σ K q qi n ⟨j, hk⟩ * (qJM K q qi n j * qJM K q qi n i) * σ K q qi n ⟨j, hk⟩ := by
                rw [hL]
            _ = σ K q qi n ⟨j, hk⟩ * qJM K q qi n j * (qJM K q qi n i * σ K q qi n ⟨j, hk⟩) := by
                simp only [mul_assoc]
            _ = σ K q qi n ⟨j, hk⟩ * qJM K q qi n j * (σ K q qi n ⟨j, hk⟩ * qJM K q qi n i) := by
                rw [hs]
            _ = σ K q qi n ⟨j, hk⟩ * qJM K q qi n j * σ K q qi n ⟨j, hk⟩ * qJM K q qi n i := by
                simp only [mul_assoc]
        · have hfrz : qJM K q qi n (j + 1) = qJM K q qi n j := dif_neg hk
          rw [hfrz]; exact ih i (le_of_lt hij')
    · -- i = j + 1
      have : i = j + 1 := le_antisymm hi hge
      rw [this]


/-! ### How far braid + far-commutation reach, and where they stop

`adjacent_reduce` collapses both sides of `L_k L_{k+1} = L_{k+1} L_k` to one
word conjugated by `s`, using **only** the braid relation and `σ_k B = B σ_k`.
So the adjacent case is equivalent to `s` commuting with
`X = σ_{k-1} σ_k L_{k-1} σ_{k-1} σ_k L_{k-1} σ_{k-1}`.

At `k = 1` that closes: `B = L_0 = 1`, `X = (ts)²t`, and the residual is
`(ts)³ = (st)³` — `braid_pow_three`, braid alone. Hence
`qJM_one_two_commute`, unconditional.

**It does not close for general `k`, and the hypotheses above are why.** After
cancelling, the residual asks for `B · t s B t s = t · B t s B t`: the left word
begins with `B`, the right with `t`. Deriving one from the other requires moving
`B` past `t`, and `s * B = B * s` gives no such permission — `B` and `t` do not
commute (`L_{k-1}` is built from `σ_{k-1}` among others). So any proof of the
general adjacent case must use something the reduction deliberately avoids:
either `σ_quadratic`, or structure of `L_{k-1}` beyond commuting with `σ_k`.

That is a statement about *these* hypotheses, not a claim that the adjacent case
is hard in general — the `k = 1` instance shows the shape can close. -/

/-- **The adjacent case, reduced.** Both sides of `L_k L_{k+1} = L_{k+1} L_k`
collapse — using *only* the braid relation and `σ_k`-commutation — to one word
conjugated by `s`. Here `t = σ_{k-1}`, `s = σ_k`, `B = L_{k-1}`, `A = t B t`. -/
theorem adjacent_reduce {R : Type*} [Ring R] (t s B : R)
    (hbraid : t * s * t = s * t * s) (hcomm : s * B = B * s) :
    (t*B*t) * s * (t*B*t) * s = (t*s*B*t*s*B*t) * s
  ∧ s * ((t*B*t) * s * (t*B*t)) = s * (t*s*B*t*s*B*t) := by
  constructor
  · calc (t*B*t) * s * (t*B*t) * s
        = t*B*(t*s*t)*B*t*s := by simp only [mul_assoc]
      _ = t*B*(s*t*s)*B*t*s := by rw [hbraid]
      _ = t*(B*s)*t*s*B*t*s := by simp only [mul_assoc]
      _ = t*(s*B)*t*s*B*t*s := by rw [hcomm]
      _ = (t*s*B*t*s*B*t) * s := by simp only [mul_assoc]
  · calc s * ((t*B*t) * s * (t*B*t))
        = s*t*B*(t*s*t)*B*t := by simp only [mul_assoc]
      _ = s*t*B*(s*t*s)*B*t := by rw [hbraid]
      _ = s*t*(B*s)*t*s*B*t := by simp only [mul_assoc]
      _ = s*t*(s*B)*t*s*B*t := by rw [hcomm]
      _ = s * (t*s*B*t*s*B*t) := by simp only [mul_assoc]

/-- The residual commutation at `B = 1`, i.e. `(ts)³ = (st)³`. Braid alone. -/
theorem braid_pow_three {R : Type*} [Ring R] (t s : R)
    (hbraid : t * s * t = s * t * s) :
    (t*s*t*s*t) * s = s * (t*s*t*s*t) := by
  calc (t*s*t*s*t) * s = (t*s*t)*(s*t*s) := by simp only [mul_assoc]
    _ = (s*t*s)*(t*s*t) := by rw [hbraid]
    _ = s * (t*s*t*s*t) := by simp only [mul_assoc]

/-- **`L_1` and `L_2` commute — unconditionally, from the braid relation alone.**
The `k = 1` instance of the adjacent case, where `B = L_0 = 1`. -/
theorem qJM_one_two_commute (h1 : 1 < n) :
    qJM K q qi n 1 * qJM K q qi n 2 = qJM K q qi n 2 * qJM K q qi n 1 := by
  have h0 : 0 < n := by omega
  set t := σ K q qi n ⟨0, h0⟩ with ht
  set s := σ K q qi n ⟨1, h1⟩ with hs
  have hbraid : t * s * t = s * t * s := by
    have := σ_braid K q qi n ⟨0, h0⟩ (by simpa using h1)
    simpa [ht, hs] using this
  have hL1 : qJM K q qi n 1 = t * (1 : Hecke K q qi n) * t := by
    rw [qJM_one K q qi n h0]; simp [ht]
  have hL2 : qJM K q qi n 2 = s * qJM K q qi n 1 * s := by
    have := qJM_succ K q qi n (k := 1) h1
    simpa [hs] using this
  rw [hL2, hL1]
  obtain ⟨e1, e2⟩ := adjacent_reduce (R := Hecke K q qi n) t s 1 hbraid (by simp)
  calc t * 1 * t * (s * (t * 1 * t) * s)
      = (t*1*t) * s * (t*1*t) * s := by simp only [mul_assoc]
    _ = (t*s*1*t*s*1*t) * s := e1
    _ = (t*s*t*s*t) * s := by simp
    _ = s * (t*s*t*s*t) := braid_pow_three t s hbraid
    _ = s * (t*s*1*t*s*1*t) := by simp
    _ = s * ((t*1*t) * s * (t*1*t)) := e2.symm
    _ = s * (t * 1 * t) * s * (t * 1 * t) := by simp only [mul_assoc]

/-- **The adjacent case at `k` follows from the adjacent case at `k-1`.**
No invertibility, no quadratic relation — braid, `s`-commutation, and the
previous adjacent instance. -/
theorem adjacent_step {R : Type*} [Ring R] (t s B : R)
    (hbraid : t * s * t = s * t * s) (hcomm : s * B = B * s)
    (hprev : B * (t*B*t) = (t*B*t) * B) :
    (t*B*t) * s * ((t*B*t) * s) = s * ((t*B*t) * (s * (t*B*t))) := by
  have hprev' : B*t*B*t = t*B*t*B := by
    have := hprev; simp only [mul_assoc] at this ⊢; exact this
  -- the shared six-letter core
  have core : B*t*s*B*t*s = t*B*t*s*B*t := by
    calc B*t*s*B*t*s = B*t*(s*B)*t*s := by simp only [mul_assoc]
      _ = B*t*(B*s)*t*s := by rw [hcomm]
      _ = B*t*B*(s*t*s) := by simp only [mul_assoc]
      _ = B*t*B*(t*s*t) := by rw [← hbraid]
      _ = (B*t*B*t)*(s*t) := by simp only [mul_assoc]
      _ = (t*B*t*B)*(s*t) := by rw [hprev']
      _ = t*B*t*(B*s)*t := by simp only [mul_assoc]
      _ = t*B*t*(s*B)*t := by rw [← hcomm]
      _ = t*B*t*s*B*t := by simp only [mul_assoc]
  calc (t*B*t) * s * ((t*B*t) * s)
      = t*B*(t*s*t)*B*t*s := by simp only [mul_assoc]
    _ = t*B*(s*t*s)*B*t*s := by rw [hbraid]
    _ = t*(B*s)*t*s*B*t*s := by simp only [mul_assoc]
    _ = t*(s*B)*t*s*B*t*s := by rw [hcomm]
    _ = (t*s)*(B*t*s*B*t*s) := by simp only [mul_assoc]
    _ = (t*s)*(t*B*t*s*B*t) := by rw [core]
    _ = (t*s*t)*(B*t*s*B*t) := by simp only [mul_assoc]
    _ = (s*t*s)*(B*t*s*B*t) := by rw [hbraid]
    _ = s*t*(s*B)*t*s*B*t := by simp only [mul_assoc]
    _ = s*t*(B*s)*t*s*B*t := by rw [hcomm]
    _ = s*t*B*(s*t*s)*B*t := by simp only [mul_assoc]
    _ = s*t*B*(t*s*t)*B*t := by rw [← hbraid]
    _ = s * ((t*B*t) * (s * (t*B*t))) := by simp only [mul_assoc]

/-! ### The induction closes

`adjacent_step` above is the whole content: the adjacent case at `k` follows
from the adjacent case at `k-1`, using braid, `σ_k`-commutation, and **nothing
else** — no invertibility, no quadratic relation. With `L_0 = 1` as the base,
that is a complete induction, and `qJM_commute_of_adjacent` turns it into the
full pairwise statement. -/

theorem qJM_adjacent : ∀ k : ℕ, k < n →
    qJM K q qi n k * qJM K q qi n (k + 1)
      = qJM K q qi n (k + 1) * qJM K q qi n k := by
  intro k
  induction k with
  | zero => intro _; rw [qJM_zero, one_mul, mul_one]
  | succ k ih =>
    intro hk1
    have hk : k < n := by omega
    have hL1 : qJM K q qi n (k + 1)
        = σ K q qi n ⟨k, hk⟩ * qJM K q qi n k * σ K q qi n ⟨k, hk⟩ :=
      qJM_succ K q qi n hk
    have hL2 : qJM K q qi n (k + 1 + 1)
        = σ K q qi n ⟨k+1, hk1⟩ * qJM K q qi n (k+1) * σ K q qi n ⟨k+1, hk1⟩ :=
      qJM_succ K q qi n hk1
    have hbraid : σ K q qi n ⟨k, hk⟩ * σ K q qi n ⟨k+1, hk1⟩ * σ K q qi n ⟨k, hk⟩
        = σ K q qi n ⟨k+1, hk1⟩ * σ K q qi n ⟨k, hk⟩ * σ K q qi n ⟨k+1, hk1⟩ := by
      have := σ_braid K q qi n ⟨k, hk⟩ (by simpa using hk1)
      simpa using this
    have hcomm : σ K q qi n ⟨k+1, hk1⟩ * qJM K q qi n k
        = qJM K q qi n k * σ K q qi n ⟨k+1, hk1⟩ :=
      qJM_comm_sigma K q qi n ⟨k+1, hk1⟩ k (by simp)
    have hprev : qJM K q qi n k * (σ K q qi n ⟨k, hk⟩ * qJM K q qi n k * σ K q qi n ⟨k, hk⟩)
        = (σ K q qi n ⟨k, hk⟩ * qJM K q qi n k * σ K q qi n ⟨k, hk⟩) * qJM K q qi n k := by
      rw [← hL1]; exact ih hk
    have key := adjacent_step (σ K q qi n ⟨k, hk⟩) (σ K q qi n ⟨k+1, hk1⟩)
      (qJM K q qi n k) hbraid hcomm hprev
    rw [hL2, hL1]
    simp only [mul_assoc] at key ⊢
    exact key

/-- **The Murphy elements commute pairwise — unconditionally.** -/
theorem qJM_commute_proved (i j : ℕ) :
    qJM K q qi n i * qJM K q qi n j = qJM K q qi n j * qJM K q qi n i := by
  have hadj : ∀ k : ℕ, qJM K q qi n k * qJM K q qi n (k + 1)
      = qJM K q qi n (k + 1) * qJM K q qi n k := by
    intro k
    by_cases hkn : k < n
    · exact qJM_adjacent K q qi n k hkn
    · have h1 : qJM K q qi n (k + 1) = qJM K q qi n k := dif_neg hkn
      rw [h1]
  rcases le_total i j with h | h
  · exact qJM_commute_of_adjacent K q qi n hadj j i h
  · exact (qJM_commute_of_adjacent K q qi n hadj i j h).symm


/-! ### Towards `barSymJMSum_central`: the pair that saves it

`barSymJMSum_central`'s GAP note used to say it needs *"`qJM_commute` plus the
σ_i–L_k commutation relations"*. `qJM_commute` is now proved — but it is about
**L–L** commutation and does not bear on centrality, which is a **σ–L** question.
The three things centrality actually needs, for a fixed `i`:

| terms | status |
|---|---|
| `L_k`, `k ≤ i-1` | **have it** — `qJM_comm_sigma` |
| `L_i + L_{i+1}` | **have it now** — `qJM_pair_comm` below, needs `q·qi = 1` |
| `L_k`, `k ≥ i+2` | **have it** — `qJM_comm_sigma_high` |

The middle row is the interesting one and the reason a *sum* is central when its
summands are not: `L_{i+1} = σ_i L_i σ_i`, so those two terms are `A + s A s`,
and `pair_comm` shows `s` commutes with that as soon as the quadratic relation
has constant term `1`. Neither `L_i` nor `L_{i+1}` commutes with `σ_i` alone.

The `q·qi = 1` hypothesis is not incidental: the computation leaves a residue
`(1 − q·qi)(sA − As)`, so it is exactly the standard Hecke normalisation that
makes the pair work. `Hecke.σUnit` carries the same hypothesis.

The third row is **not** far commutation — `L_k` for `k ≥ i+2` is built from
`σ_{k-1}, …` which *includes* `σ_i`, and at `k = i+2` the outer generator
`σ_{i+1}` is adjacent to `σ_i`. `qJM_comm_sigma_high` handles it by running the
base case `k = i+2` on the **braid relation** (the two `σ_{i+1}` conjugations
absorb the adjacency) and the step on far commutation. It needs no quadratic
relation — unlike the pair row, which does.

**What was left for `barSymJMSum_central`** was therefore never a missing
commutation: it was (a) the `Finset` assembly splitting `range (n+1)` into
`{i, i+1}` and its complement, and (b) the **inverse family** `L_k⁻¹`, which
needs the same three rows run against `qJMInv` / `σ⁻¹`. Both are done below;
the theorem is sorry-free given `q · qi = 1`. -/

theorem pair_comm {K' R : Type*} [CommRing K'] [Ring R] [Algebra K' R]
    (s A : R) (d : K') (hquad : s * s = d • s + (1 : R)) :
    s * (A + s * A * s) = (A + s * A * s) * s := by
  have hL : s * (A + s * A * s) = s * A + (s * s) * (A * s) := by
    simp only [mul_add, mul_assoc]
  have hR : (A + s * A * s) * s = A * s + (s * A) * (s * s) := by
    simp only [add_mul, mul_assoc]
  rw [hL, hR, hquad]
  simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, one_mul, mul_one,
    mul_assoc]
  abel

/-- **`σ_i` commutes with `L_i + L_{i+1}`** when `q · qi = 1`. Neither summand
is `σ_i`-invariant; the pair is. -/
theorem qJM_pair_comm (hqi : q * qi = 1) (i : ℕ) (hi : i < n) :
    σ K q qi n ⟨i, hi⟩ * (qJM K q qi n i + qJM K q qi n (i + 1))
      = (qJM K q qi n i + qJM K q qi n (i + 1)) * σ K q qi n ⟨i, hi⟩ := by
  have hquad : σ K q qi n ⟨i, hi⟩ * σ K q qi n ⟨i, hi⟩
      = (q - qi) • σ K q qi n ⟨i, hi⟩ + (1 : Hecke K q qi n) := by
    have := σ_quadratic K q qi n ⟨i, hi⟩
    rw [hqi] at this; simpa using this
  rw [qJM_succ K q qi n hi]
  exact pair_comm _ _ _ hquad

/-- **`σ_i` commutes with `L_k` for every `k ≥ i + 2`.** The third and last row
needed for centrality. Not far commutation: at `k = i+2` the outer generator
`σ_{i+1}` is adjacent to `σ_i`, and the base case runs on the braid relation. -/
theorem qJM_comm_sigma_high (i : Fin n) (hi1 : (i : ℕ) + 1 < n) :
    ∀ k : ℕ, (i : ℕ) + 2 ≤ k →
      σ K q qi n i * qJM K q qi n k = qJM K q qi n k * σ K q qi n i := by
  intro k hk
  induction k, hk using Nat.le_induction with
  | base =>
    have hi0 : (i : ℕ) < n := i.isLt
    have e1 : qJM K q qi n ((i : ℕ) + 1)
        = σ K q qi n i * qJM K q qi n (i : ℕ) * σ K q qi n i := by
      have := qJM_succ K q qi n hi0; simpa using this
    have e2 : qJM K q qi n ((i : ℕ) + 2)
        = σ K q qi n ⟨(i : ℕ)+1, hi1⟩ * qJM K q qi n ((i : ℕ)+1)
          * σ K q qi n ⟨(i : ℕ)+1, hi1⟩ := qJM_succ K q qi n hi1
    have hbr : σ K q qi n i * σ K q qi n ⟨(i : ℕ)+1, hi1⟩ * σ K q qi n i
        = σ K q qi n ⟨(i : ℕ)+1, hi1⟩ * σ K q qi n i * σ K q qi n ⟨(i : ℕ)+1, hi1⟩ :=
      σ_braid K q qi n i hi1
    have hcm : σ K q qi n ⟨(i : ℕ)+1, hi1⟩ * qJM K q qi n (i : ℕ)
        = qJM K q qi n (i : ℕ) * σ K q qi n ⟨(i : ℕ)+1, hi1⟩ :=
      qJM_comm_sigma K q qi n ⟨(i : ℕ)+1, hi1⟩ (i : ℕ) (by simp)
    rw [e2, e1]
    set s := σ K q qi n i
    set t := σ K q qi n ⟨(i : ℕ)+1, hi1⟩
    set B := qJM K q qi n (i : ℕ)
    calc s * (t * (s * B * s) * t)
        = (s * t * s) * B * s * t := by simp only [mul_assoc]
      _ = (t * s * t) * B * s * t := by rw [hbr]
      _ = t * s * (t * B) * s * t := by simp only [mul_assoc]
      _ = t * s * (B * t) * s * t := by rw [hcm]
      _ = t * s * B * (t * s * t) := by simp only [mul_assoc]
      _ = t * s * B * (s * t * s) := by rw [← hbr]
      _ = t * (s * B * s) * t * s := by simp only [mul_assoc]
  | succ k hk ih =>
    by_cases hkn : k < n
    · have e : qJM K q qi n (k + 1)
          = σ K q qi n ⟨k, hkn⟩ * qJM K q qi n k * σ K q qi n ⟨k, hkn⟩ :=
        qJM_succ K q qi n hkn
      have hfar : σ K q qi n i * σ K q qi n ⟨k, hkn⟩
          = σ K q qi n ⟨k, hkn⟩ * σ K q qi n i :=
        (σ_commute K q qi n ⟨k, hkn⟩ i (by simpa using hk)).symm
      rw [e]
      calc σ K q qi n i * (σ K q qi n ⟨k, hkn⟩ * qJM K q qi n k * σ K q qi n ⟨k, hkn⟩)
          = (σ K q qi n i * σ K q qi n ⟨k, hkn⟩) * qJM K q qi n k * σ K q qi n ⟨k, hkn⟩ := by
            simp only [mul_assoc]
        _ = (σ K q qi n ⟨k, hkn⟩ * σ K q qi n i) * qJM K q qi n k * σ K q qi n ⟨k, hkn⟩ := by
            rw [hfar]
        _ = σ K q qi n ⟨k, hkn⟩ * (σ K q qi n i * qJM K q qi n k) * σ K q qi n ⟨k, hkn⟩ := by
            simp only [mul_assoc]
        _ = σ K q qi n ⟨k, hkn⟩ * (qJM K q qi n k * σ K q qi n i) * σ K q qi n ⟨k, hkn⟩ := by
            rw [ih]
        _ = σ K q qi n ⟨k, hkn⟩ * qJM K q qi n k * (σ K q qi n i * σ K q qi n ⟨k, hkn⟩) := by
            simp only [mul_assoc]
        _ = σ K q qi n ⟨k, hkn⟩ * qJM K q qi n k * (σ K q qi n ⟨k, hkn⟩ * σ K q qi n i) := by
            rw [hfar]
        _ = σ K q qi n ⟨k, hkn⟩ * qJM K q qi n k * σ K q qi n ⟨k, hkn⟩ * σ K q qi n i := by
            simp only [mul_assoc]
    · have e : qJM K q qi n (k + 1) = qJM K q qi n k := dif_neg hkn
      rw [e]; exact ih


/-! ### The assembly, and the inverse half

`qJM_sum_comm_sigma` below splits `Finset.range (n+1)` into `{i, i+1}` and its
complement: the pair takes `qJM_pair_comm`, and every remaining `k` is either
`≤ i-1` or `≥ i+2`, so it takes one of the other two rows. **That settles the
`L`-half of `barSymJMSum_central`.**

The remaining half is the inverse family. Two facts make it a transfer rather
than a re-derivation: `σInv = σ - (q-qi)•1` is a *polynomial in `σ`*, so
`comm_σInv_iff` says commuting with one is commuting with the other; and
`σInv_quadratic` shows `σ⁻¹` obeys the same quadratic with `d ↦ -d`, which is
exactly the shape `pair_comm` consumes. `qJMInv` has the same recursion as
`qJM` with `σ ↦ σInv`, so the three rows should re-run verbatim against it. -/

/-- **The first Murphy power sum `Σ_{k≤n} L_k` is central.** -/
theorem qJM_sum_comm_sigma (hqi : q * qi = 1) (i : Fin n) (hi1 : (i : ℕ) + 1 < n) :
    σ K q qi n i * (∑ k ∈ Finset.range (n + 1), qJM K q qi n k)
      = (∑ k ∈ Finset.range (n + 1), qJM K q qi n k) * σ K q qi n i := by
  classical
  set s := σ K q qi n i with hs
  set P : Finset ℕ := {(i : ℕ), (i : ℕ) + 1} with hP
  have hsub : P ⊆ Finset.range (n + 1) := by
    intro x hx
    simp only [hP, Finset.mem_insert, Finset.mem_singleton] at hx
    rcases hx with rfl | rfl <;> simp [Finset.mem_range] <;> omega
  have hsplit := Finset.sum_sdiff (f := fun k => qJM K q qi n k) hsub
  -- the pair
  have hpair : s * (∑ k ∈ P, qJM K q qi n k) = (∑ k ∈ P, qJM K q qi n k) * s := by
    have hne : (i : ℕ) ≠ (i : ℕ) + 1 := by omega
    have : (∑ k ∈ P, qJM K q qi n k)
        = qJM K q qi n (i : ℕ) + qJM K q qi n ((i : ℕ) + 1) := by
      simp [hP, Finset.sum_insert, Finset.mem_singleton]
    rw [this]
    exact qJM_pair_comm K q qi n hqi (i : ℕ) i.isLt
  -- everything else, termwise
  have hrest : s * (∑ k ∈ Finset.range (n + 1) \ P, qJM K q qi n k)
      = (∑ k ∈ Finset.range (n + 1) \ P, qJM K q qi n k) * s := by
    rw [Finset.mul_sum, Finset.sum_mul]
    refine Finset.sum_congr rfl fun k hk => ?_
    simp only [Finset.mem_sdiff, Finset.mem_range, hP, Finset.mem_insert,
      Finset.mem_singleton, not_or] at hk
    obtain ⟨_, hki, hki1⟩ := hk
    rcases Nat.lt_or_ge k (i : ℕ) with hlt | hge
    · exact qJM_comm_sigma K q qi n i k (by omega)
    · exact qJM_comm_sigma_high K q qi n i hi1 k (by omega)
  rw [← hsplit, mul_add, add_mul, hpair, hrest]

/-- `σ_i⁻¹` satisfies the same quadratic with `d ↦ -d`: `σ⁻¹² = (qi-q)·σ⁻¹ + 1`
when `q·qi = 1`. -/
theorem σInv_quadratic (hqi : q * qi = 1) (i : Fin n) :
    σInv K q qi n i * σInv K q qi n i
      = (qi - q) • σInv K q qi n i + (1 : Hecke K q qi n) := by
  have hq := σ_quadratic K q qi n i
  rw [hqi] at hq
  simp only [σInv, sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul,
    mul_one, hq, smul_smul, sub_smul, smul_sub]
  abel_nf
  module

/-- **Commuting with `σ_i` and with `σ_i⁻¹` are the same condition** — `σInv` is
`σ - (q-qi)•1`, a polynomial in `σ`, so the two differ by a central term. -/
theorem comm_σInv_iff (i : Fin n) (x : Hecke K q qi n) :
    x * σInv K q qi n i = σInv K q qi n i * x ↔ x * σ K q qi n i = σ K q qi n i * x := by
  simp only [σInv, mul_sub, sub_mul, mul_smul_comm, smul_mul_assoc, mul_one, one_mul]
  exact sub_left_inj

/-- Commuting with a two-sided unit transfers to its inverse. -/
theorem comm_inv_of_comm {R : Type*} [Ring R] (s A A' : R)
    (hAA' : A * A' = 1) (hA'A : A' * A = 1) (h : s * A = A * s) :
    s * A' = A' * s := by
  calc s * A' = (A' * A) * (s * A') := by rw [hA'A, one_mul]
    _ = A' * (A * s) * A' := by simp only [mul_assoc]
    _ = A' * (s * A) * A' := by rw [h]
    _ = A' * s * (A * A') := by simp only [mul_assoc]
    _ = A' * s := by rw [hAA', mul_one]

/-- Row 1 for the inverse family. -/
theorem qJMInv_comm_sigma (hqi : q * qi = 1) (m : Fin n) (k : ℕ)
    (hk : k + 1 ≤ (m : ℕ)) (hkn : k ≤ n) :
    σ K q qi n m * qJMInv K q qi n k = qJMInv K q qi n k * σ K q qi n m :=
  comm_inv_of_comm _ _ _ (qJM_mul_qJMInv K q qi n hqi k hkn)
    (qJMInv_mul_qJM K q qi n hqi k hkn) (qJM_comm_sigma K q qi n m k hk)

/-- Row 3 for the inverse family. -/
theorem qJMInv_comm_sigma_high (hqi : q * qi = 1) (i : Fin n) (hi1 : (i : ℕ) + 1 < n)
    (k : ℕ) (hk : (i : ℕ) + 2 ≤ k) (hkn : k ≤ n) :
    σ K q qi n i * qJMInv K q qi n k = qJMInv K q qi n k * σ K q qi n i :=
  comm_inv_of_comm _ _ _ (qJM_mul_qJMInv K q qi n hqi k hkn)
    (qJMInv_mul_qJM K q qi n hqi k hkn) (qJM_comm_sigma_high K q qi n i hi1 k hk)

/-- Row 2 for the inverse family: `σ_i` commutes with `L_i⁻¹ + L_{i+1}⁻¹`. -/
theorem qJMInv_pair_comm (hqi : q * qi = 1) (i : ℕ) (hi : i < n) :
    σ K q qi n ⟨i, hi⟩ * (qJMInv K q qi n i + qJMInv K q qi n (i + 1))
      = (qJMInv K q qi n i + qJMInv K q qi n (i + 1)) * σ K q qi n ⟨i, hi⟩ := by
  have hq := σInv_quadratic K q qi n hqi ⟨i, hi⟩
  rw [qJMInv_succ K q qi n hi]
  have hpc := pair_comm (σInv K q qi n ⟨i, hi⟩) (qJMInv K q qi n i) (qi - q) hq
  exact ((comm_σInv_iff K q qi n ⟨i, hi⟩ _).mp hpc.symm).symm

/-- Generic Finset assembly: a family `F` whose `{i,i+1}` pair commutes with
`σ_i` and whose other members commute individually has a central sum. -/
theorem sum_comm_of_rows (i : Fin n) (F : ℕ → Hecke K q qi n)
    (hpair : σ K q qi n i * (F (i : ℕ) + F ((i : ℕ) + 1))
           = (F (i : ℕ) + F ((i : ℕ) + 1)) * σ K q qi n i)
    (hlow : ∀ k, k < (i : ℕ) → σ K q qi n i * F k = F k * σ K q qi n i)
    (hhigh : ∀ k, (i : ℕ) + 2 ≤ k → k ≤ n → σ K q qi n i * F k = F k * σ K q qi n i) :
    σ K q qi n i * (∑ k ∈ Finset.range (n + 1), F k)
      = (∑ k ∈ Finset.range (n + 1), F k) * σ K q qi n i := by
  classical
  set P : Finset ℕ := {(i : ℕ), (i : ℕ) + 1} with hP
  have hsub : P ⊆ Finset.range (n + 1) := by
    intro x hx
    simp only [hP, Finset.mem_insert, Finset.mem_singleton] at hx
    have := i.isLt
    rcases hx with rfl | rfl <;> simp [Finset.mem_range] <;> omega
  have hsplit := Finset.sum_sdiff (f := F) hsub
  have hpairsum : (∑ k ∈ P, F k) = F (i : ℕ) + F ((i : ℕ) + 1) := by
    have hne : (i : ℕ) ≠ (i : ℕ) + 1 := by omega
    simp [hP, Finset.sum_insert, Finset.mem_singleton]
  have hrest : σ K q qi n i * (∑ k ∈ Finset.range (n + 1) \ P, F k)
      = (∑ k ∈ Finset.range (n + 1) \ P, F k) * σ K q qi n i := by
    rw [Finset.mul_sum, Finset.sum_mul]
    refine Finset.sum_congr rfl fun k hk => ?_
    simp only [Finset.mem_sdiff, Finset.mem_range, hP, Finset.mem_insert,
      Finset.mem_singleton, not_or] at hk
    obtain ⟨hkr, hki, hki1⟩ := hk
    rcases Nat.lt_or_ge k (i : ℕ) with hlt | hge
    · exact hlow k hlt
    · exact hhigh k (by omega) (by omega)
  rw [← hsplit, hpairsum, mul_add, add_mul, hpair, hrest]

/-- **`Σ_{k≤n} L_k⁻¹` is central.** -/
theorem qJMInv_sum_comm_sigma (hqi : q * qi = 1) (i : Fin n) :
    σ K q qi n i * (∑ k ∈ Finset.range (n + 1), qJMInv K q qi n k)
      = (∑ k ∈ Finset.range (n + 1), qJMInv K q qi n k) * σ K q qi n i := by
  refine sum_comm_of_rows K q qi n i _ ?_ ?_ ?_
  · have := qJMInv_pair_comm K q qi n hqi (i : ℕ) i.isLt
    simpa using this
  · intro k hk
    exact qJMInv_comm_sigma K q qi n hqi i k (by omega) (by have := i.isLt; omega)
  · intro k hk hkn
    exact qJMInv_comm_sigma_high K q qi n hqi i (by omega) k hk hkn

/-- **`Σ_{k≤n} L_k` is central**, with no side hypothesis on `i`. -/
theorem qJM_sum_comm_sigma' (hqi : q * qi = 1) (i : Fin n) :
    σ K q qi n i * (∑ k ∈ Finset.range (n + 1), qJM K q qi n k)
      = (∑ k ∈ Finset.range (n + 1), qJM K q qi n k) * σ K q qi n i := by
  refine sum_comm_of_rows K q qi n i _ ?_ ?_ ?_
  · have := qJM_pair_comm K q qi n hqi (i : ℕ) i.isLt
    simpa using this
  · intro k hk; exact qJM_comm_sigma K q qi n i k (by omega)
  · intro k hk hkn; exact qJM_comm_sigma_high K q qi n i (by omega) k hk

end AdjacentReduction

/-- **[GAP] The Murphy elements commute pairwise** — they generate the commutative
Gelfand–Tsetlin subalgebra `GZ_{n+1} ⊂ H_{n+1}(q)`.

-- Ref: [murphy1992] — the q-deformed Murphy operators generate a maximal commutative
-- subalgebra of `H_{n+1}(q)`.  Also [ram1997] Corollary 2.4.
-- The classical proof (the `L_k` are simultaneously diagonalised by the
-- seminormal basis) lifts verbatim to the q-deformed setting.
-- Blocked on: the general seminormal rep (bean SW-4 residual). -/
theorem qJM_commute (K : Type*) [CommRing K] (q qi : K) (n : ℕ) (i j : ℕ)
    (hi : i ≤ n) (hj : j ≤ n) :
    qJM K q qi n i * qJM K q qi n j = qJM K q qi n j * qJM K q qi n i :=
  -- PROVED 2026-08-16 (bean `qou-gjg6`). The GAP note this replaced said
  -- "requires the seminormal diagonalisation" — it does not. `qJM_commute_proved`
  -- derives it from the braid relation and far commutation alone, by induction on
  -- the recursion `L_{k+1} = σ_k L_k σ_k`; no representation, no invertibility,
  -- and no quadratic relation. The hypotheses `hi`/`hj` are not needed either,
  -- since the recursion freezes above `n`.
  qJM_commute_proved K q qi n i j

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

/-! ## Seminormal eigenvalue grounded on the concrete representations (sorry-free)

The `q^{2c}` convention (§ Convention above) is not left as an assertion: it is *computed*
sorry-free on every seminormal representation that the corpus currently constructs.

* On the **trivial** (one-row shape `(N)`) representation `ρ_triv`, entry `m` sits in cell
  `(0, m−1)` of content `m−1`, and `L_k` acts by `q^{2k}` — the symmetric channel, contents
  `0, 1, …, n`.
* On the **sign** (one-column shape `(1^N)`) representation `ρ_sign`, entry `m` sits in cell
  `(m−1, 0)` of content `−(m−1)`, and `L_k` acts by `qi^{2k} = q^{−2k}` (once `q·qi = 1`) — the
  antisymmetric channel, contents `0, −1, …, −n`.
* On the genuine `2×2` **`(2,1)`** representation `ρ_{(2,1)}`, `L_1 = σ_0²` acts as
  `diag(q², q⁻²) = diag(q^{2·(+1)}, q^{2·(−1)})` — the two SYT of `(2,1)` whose entry `2`
  occupies cells of content `+1` resp. `−1`.

Together these exhibit `q^{2c}` for contents `c ∈ {−n, …, n}` with the correct sign structure,
grounding the convention in real representation matrices rather than a docstring.
Ref: [ram1997] Theorem 4.1; [murphy1992]; [murphy1981]; [hoefsmit1974]. -/

section EigenvalueGrounding

variable (K : Type*) [CommRing K] (q qi : K) (n : ℕ)

/-- `ρ_triv(σ_i⁻¹) = qi` (sorry-free): `σ_i⁻¹ = σ_i − (q − qi)·1 ↦ q − (q − qi) = qi`. -/
@[simp] theorem rhoTriv_σInv (i : Fin n) :
    rhoTriv K q qi n (σInv K q qi n i) = qi := by
  simp only [σInv, map_sub, map_smul, rhoTriv_σ, map_one, smul_eq_mul, mul_one]
  ring

/-- `ρ_sign(σ_i⁻¹) = −q` (sorry-free): `σ_i⁻¹ ↦ (−qi) − (q − qi) = −q`. -/
@[simp] theorem rhoSign_σInv (i : Fin n) :
    rhoSign K q qi n (σInv K q qi n i) = -q := by
  simp only [σInv, map_sub, map_smul, rhoSign_σ, map_one, smul_eq_mul, mul_one]
  ring

/-- **Trivial-rep eigenvalue** (sorry-free): `ρ_triv(L_k) = q^{2k}` for `k ≤ n`.
The Murphy element `L_k` acts on the (unique) SYT of the one-row shape `(N)` by `q^{2c}` with
`c = k` the content of the cell holding entry `k+1`.  Realises the `q^{2c}` convention on the
symmetric channel.  Ref: [ram1997] Thm 4.1; [murphy1992]. -/
theorem qJM_rhoTriv : ∀ k, k ≤ n → rhoTriv K q qi n (qJM K q qi n k) = q ^ (2 * k)
  | 0, _ => by simp
  | k + 1, hk => by
    have h : k < n := Nat.lt_of_succ_le hk
    rw [qJM_succ K q qi n h, map_mul, map_mul, rhoTriv_σ, qJM_rhoTriv k h.le]
    ring

/-- **Trivial-rep eigenvalue of the inverse Murphy element** (sorry-free): `ρ_triv(L_k⁻¹) = qi^{2k}`
for `k ≤ n`.  With `q·qi = 1` this is `q^{−2k}`, the bar-partner of `qJM_rhoTriv`. -/
theorem qJMInv_rhoTriv : ∀ k, k ≤ n → rhoTriv K q qi n (qJMInv K q qi n k) = qi ^ (2 * k)
  | 0, _ => by simp
  | k + 1, hk => by
    have h : k < n := Nat.lt_of_succ_le hk
    rw [qJMInv_succ K q qi n h, map_mul, map_mul, rhoTriv_σInv, qJMInv_rhoTriv k h.le]
    ring

/-- **Sign-rep eigenvalue** (sorry-free): `ρ_sign(L_k) = qi^{2k}` for `k ≤ n`.
On the one-column shape `(1^N)` the cell holding entry `k+1` has content `−k`, so once `q·qi = 1`
this reads `q^{2·(−k)} = q^{−2k}` — the `q^{2c}` convention on the antisymmetric channel.
Ref: [ram1997] Thm 4.1; [murphy1992]. -/
theorem qJM_rhoSign : ∀ k, k ≤ n → rhoSign K q qi n (qJM K q qi n k) = qi ^ (2 * k)
  | 0, _ => by simp
  | k + 1, hk => by
    have h : k < n := Nat.lt_of_succ_le hk
    rw [qJM_succ K q qi n h, map_mul, map_mul, rhoSign_σ, qJM_rhoSign k h.le]
    ring

/-- **Block eigenvalue of `Θ` on the trivial rep** (sorry-free): `ρ_triv(Θ_n) = Σ_{k=0}^{n}(q^{2k}+qi^{2k})`.
This is the "cosh" block eigenvalue `Σ_{c∈λ}(q^{2c}+q^{−2c})` realised concretely for the one-row
shape `(N)` (contents `c = 0, …, n`) — the bar-even scalar that bean `qou-8vt2` consumes. -/
theorem barSymJMSum_rhoTriv :
    rhoTriv K q qi n (barSymJMSum K q qi n)
      = ∑ k ∈ Finset.range (n + 1), (q ^ (2 * k) + qi ^ (2 * k)) := by
  rw [barSymJMSum, map_sum]
  refine Finset.sum_congr rfl (fun k hk => ?_)
  have hk' : k ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
  rw [map_add, qJM_rhoTriv K q qi n k hk', qJMInv_rhoTriv K q qi n k hk']

end EigenvalueGrounding

/-- **`(2,1)` eigenvalue** (sorry-free, over `ℝ`): `ρ_{(2,1)}(L_1) = diag(q², q⁻²)`.
`L_1 = σ_0²` and `ρ_{(2,1)}(σ_0) = S0 = diag(q, −q⁻¹)`, so `ρ_{(2,1)}(L_1) = S0² = diag(q², q⁻²)`.
The diagonal entries are `q^{2·(+1)}` and `q^{2·(−1)}`: the two SYT of `(2,1)` whose cell holding
entry `2` has content `+1` (row-sharing) resp. `−1` (column-sharing).  This is the first
*genuinely 2-dimensional* witness of the `q^{2c}` convention.  Ref: [ram1997] Thm 4.1. -/
theorem qJM_seminormalRep21_one (q : ℝ) (hq : q ≠ 0) :
    seminormalRep21 q hq (qJM ℝ q q⁻¹ 2 1) = !![q ^ 2, 0; 0, (q⁻¹) ^ 2] := by
  have h1 : qJM ℝ q q⁻¹ 2 1 = σ ℝ q q⁻¹ 2 0 * σ ℝ q q⁻¹ 2 0 :=
    qJM_one ℝ q q⁻¹ 2 (by norm_num)
  rw [h1, map_mul, seminormalRep21_σ0 q hq]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [S0, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-! ## Block-level cosh–bracket identity and the cell-content sum (sorry-free)

The `Finset`-level lift of `cosh_eq_sq_bracket_add_two`, and its instantiation over the cells of a
partition `λ` — the "one free identity" of bean `qou-ck0g`, showing the two bar-even brackets
`Σ_{c∈λ}(q^{2c}+q^{−2c})` and `Σ_{c∈λ}(q^{c}−q^{−c})²` differ only by the λ-independent shift `2n`
(and, after factoring `[c]_q`, the bar-even scalar `(q−q⁻¹)²`). -/

section CellSum

/-- **Block-level cosh–bracket identity** (sorry-free).  For `a, b : ι → R` with `a i · b i = 1`
on `s`: `Σ_{i∈s}(a i² + b i²) = Σ_{i∈s}(a i − b i)² + 2·|s|`.  The `Finset` sum of
`cosh_eq_sq_bracket_add_two`. -/
theorem barSym_block_sum_eq {R : Type*} [CommRing R] {ι : Type*} (s : Finset ι)
    (a b : ι → R) (hab : ∀ i ∈ s, a i * b i = 1) :
    (∑ i ∈ s, (a i ^ 2 + b i ^ 2)) = (∑ i ∈ s, (a i - b i) ^ 2) + 2 * (s.card : R) := by
  have h : ∀ i ∈ s, a i ^ 2 + b i ^ 2 = (a i - b i) ^ 2 + 2 :=
    fun i hi => cosh_eq_sq_bracket_add_two (a i) (b i) (hab i hi)
  rw [Finset.sum_congr rfl h, Finset.sum_add_distrib, Finset.sum_const, nsmul_eq_mul]
  ring

variable {R : Type*} [Field R] {N : ℕ}

/-- **The cosh sum over the cells of `λ`** — the block eigenvalue candidate for `barSymJMSum` on the
irreducible `ρ_λ`: `Σ_{c∈λ}(q^{2c} + q^{−2c})`, `c = cellContent` the content of each cell (a
`ℤ`-power, so the base ring is a `Field` — §7c: this is the archimedean/observation side, `q ≠ 0`). -/
noncomputable def cellContentCoshSum (lam : Partition N) (q : R) : R :=
  ∑ c ∈ (shape lam).cells, (q ^ (2 * cellContent c) + q ^ (-(2 * cellContent c)))

/-- **`cellContentCoshSum` in bracket form** (sorry-free): with `q ≠ 0`,
  `Σ_{c∈λ}(q^{2c}+q^{−2c}) = Σ_{c∈λ}(q^{c}−q^{−c})² + 2·|λ|`.
After factoring `[c]_q = (q^{c}−q^{−c})/(q−q⁻¹)` this is `(q−q⁻¹)²·Σ_c[c]_q² + 2n`: the two bar-even
brackets coincide up to the bar-even scalar `(q−q⁻¹)²` and the λ-independent shift `2n = 2|λ|`, so
**neither is a spectral degree of freedom** (bean `qou-ck0g` / `qou-8vt2`). -/
theorem cellContentCoshSum_eq_bracket (lam : Partition N) (q : R) (hq : q ≠ 0) :
    cellContentCoshSum lam q
      = (∑ c ∈ (shape lam).cells, (q ^ (cellContent c) - q ^ (-(cellContent c))) ^ 2)
        + 2 * ((shape lam).cells.card : R) := by
  have hsq : ∀ m : ℤ, q ^ (2 * m) = (q ^ m) ^ 2 := fun m => by
    rw [two_mul, zpow_add₀ hq, pow_two]
  have hab : ∀ c ∈ (shape lam).cells,
      q ^ (cellContent c) * q ^ (-(cellContent c)) = 1 :=
    fun c _ => by rw [← zpow_add₀ hq, add_neg_cancel, zpow_zero]
  have key := barSym_block_sum_eq (shape lam).cells
    (fun c => q ^ (cellContent c)) (fun c => q ^ (-(cellContent c))) hab
  have hL : cellContentCoshSum lam q
      = ∑ c ∈ (shape lam).cells, ((q ^ (cellContent c)) ^ 2 + (q ^ (-(cellContent c))) ^ 2) := by
    rw [cellContentCoshSum]
    refine Finset.sum_congr rfl (fun c _ => ?_)
    rw [hsq (cellContent c),
        show -(2 * cellContent c) = 2 * (-(cellContent c)) by ring, hsq (-(cellContent c))]
  rw [hL, key]

end CellSum

/-! ## General-`λ` block eigenvalue and centrality — honest `sorry` + `-- Ref:`

One statement remains here.  It needs the **general** Hoefsmit seminormal representation, which is
itself a documented GAP (`hoefsmit_seminormal_rep`, bean `qou-im9l` / SW-4 residual).  The scalar
it evaluates to is computed sorry-free above (`cellContentCoshSum`); only the bridge
"the central element acts by that scalar on the irreducible block" awaits the general rep.

Centrality used to be the second statement in this section and is no longer a gap: it is proved
sorry-free as `barSymJMSum_central` below, given `q · qi = 1`. -/

section GeneralGap

/-- **Block eigenvalue of `Θ` on the irreducible `ρ_λ`, at generic `q` — GAP.**  For every `λ ⊢ N`
there is a seminormal representation `ρ_λ : H_N(q) →ₐ M_{d_λ}` on which the central bar-symmetrised
sum `Θ = barSymJMSum` acts as the scalar `cellContentCoshSum λ q = Σ_{c∈λ}(q^{2c}+q^{−2c})·1`.
The scalar is sorry-free (`cellContentCoshSum` + `cellContentCoshSum_eq_bracket`); the bridge
`ρ_λ(Θ) = scalar·1` needs the general seminormal construction and the per-element eigenvalue
`L_k ↦ q^{2·cellContent}`.

**Hypotheses re-scoped 2026-08-17 (bean `qou-gjg6`), `q ≠ 0` → `0 < q ∧ q ≠ 1`.**  The old `q ≠ 0`
was under-hypothesised, and not in the same way `barSymJMSum_central` was: at `Hecke ℝ q q⁻¹` the
normalisation `q · q⁻¹ = 1` is already free from `q ≠ 0`, so centrality is not what was missing.
What was missing is that the *seminormal representation itself* does not exist at every nonzero
real `q`.  Its matrix entries carry denominators `1 − q^{−2d}` indexed by content differences `d`,
so it degenerates exactly where `q^{2d} = 1` for some `d ≠ 0` — i.e. at `q = 1` (every `d`) and at
`q = −1` (every even `d`, and there `0/0`).  `0 < q` excludes the negative branch and `q ≠ 1`
excludes the classical point; together they are the concrete-`ℝ` reading of *generic `q`*, which is
the regime in which [ram1997] and [hoefsmit1974] construct the representation at all.

**Recorded gap, not silently dropped: the roots-of-unity regime.**  The excluded `q` are not a
technicality to be relaxed later by a better proof of the same statement.  At a root of unity
`H_N(q)` is no longer semisimple, the `λ ⊢ N` no longer index the irreducibles, and the statement's
whole shape (one `d_λ`-dimensional block per partition, `Θ` acting by a scalar on it) is the thing
that fails — so the excluded case needs a *different* statement, via cellular/Specht theory rather
than seminormal form.  Nothing here claims that case is true, and nothing here claims it is false.
It is open and is tracked as such; do not read the `0 < q` hypothesis as an artefact of this proof
route.

**The `0 < q` half is stronger than the construction needs — recorded, not silently changed.**
When this hypothesis was put to the owner I described the constraint as `0 < q ∧ q ≠ 1`. That was
my reading, and it was not sharp: `SeminormalRep.seminormalRep` and `hoefsmit_seminormal_rep` both
take `(hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1)`, which over `ℝ` says exactly *`q` is not a root of unity* —
the genericity condition `[ram1997]` presupposes — and which **admits negative `q`**.  `0 < q ∧
q ≠ 1` implies both (`q > 0` with `q ^ 2 = 1` forces `q = 1`), so the statement below is **sound,
just narrower than necessary**: it excludes the whole `q < 0` branch that the construction handles.
The owner's ruling is kept as given rather than quietly widened; when the `sorry` is discharged
from `seminormalRep`, the hypotheses can be relaxed to `q ≠ 0 ∧ q ^ 2 ≠ 1` and the discharge
becomes direct instead of needing a strengthening step. -/
theorem barSymJMSum_block_eigenvalue {N : ℕ} (q : ℝ) (hq : 0 < q) (hq1 : q ≠ 1)
    (lam : Partition N) :
    ∃ ρ : Hecke ℝ q q⁻¹ (N - 1) →ₐ[ℝ] Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) ℝ,
      ρ (barSymJMSum ℝ q q⁻¹ (N - 1))
        = cellContentCoshSum lam q • (1 : Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) ℝ) := by
  -- Ref: [ram1997] Theorem 4.1 (seminormal eigenvalues q^{2c}); [murphy1992] (the Murphy operators
  --   are central and act by scalars on the irreducibles); [hoefsmit1974].
  -- GAP, NARROWED 2026-08-19.  The note here used to name TWO inputs; one has landed and the
  --   surrounding scaffolding is now proved, so what is left is a single statement:
  --
  --     `ρ(L_k + L_k⁻¹) = diagonal (fun T => q^{2c} + q^{-2c})  at  c = cellContent (cellOf T (k+1))`
  --
  --   i.e. [ram1997] Thm 4.1 itself.  Everything around it is discharged:
  --     * `hoefsmit_seminormal_rep` — PROVED (bean qou-im9l, merged 45817bf516); no longer a gap.
  --     * the scalar value — `cellContentCoshSum` + `cellContentCoshSum_eq_bracket`, above.
  --     * that a DIAGONAL family sums to a SCALAR — `TableauCells.sum_diagonal_eq_scalar` in
  --       `JMBlockEigenvalue.lean`, sorry-free.  This is the step that makes Θ central-looking:
  --       `cellOf T` is a bijection `[1,|μ|] → cells`, so every column sums the same multiset of
  --       contents and the T-dependence cancels (`sum_comp_cellOf`).  It assumes nothing about
  --       the eigenvalue being `q^{2c}` — it holds for an arbitrary per-cell function.
  --     * the `L_0 = 1` ↔ entry-1-at-(0,0) index alignment — `content_cellOf_one`, checked rather
  --       than assumed, since an off-by-one would range the two sums over different cell multisets.
  --
  --   NOT claimed: that the per-element eigenvalue is close.  `L_k` is a product of `genMat`s under
  --   `L_{k+1} = σ_k L_k σ_k`, and showing that product is diagonal is the substance of Ram's
  --   theorem, not packaging around it.
  sorry

section BarSymCentral

variable (K : Type*) [CommRing K] (q qi : K) (n : ℕ)

/-- **`barSymJMSum` is central**, given `q · qi = 1` — sorry-free.

The hypothesis is not decoration.  `σ_i` commutes with the pair `L_i + L_{i+1}` only up to the
residue `(1 − q·qi)(σ_i L_i − L_i σ_i)` (see `pair_comm`), and without `q · qi = 1` the element
`qJMInv` is not an inverse of `qJM` at all.  A hypothesis-free version of this statement was
carried here as a `sorry` until 2026-08-17 (bean `qou-gjg6`); it is not provable by this route,
and it was deleted rather than left standing as proof debt it never was. -/
theorem barSymJMSum_central (hqi : q * qi = 1) (i : Fin n) :
    barSymJMSum K q qi n * σ K q qi n i = σ K q qi n i * barSymJMSum K q qi n := by
  have hL := qJM_sum_comm_sigma' K q qi n hqi i
  have hI := qJMInv_sum_comm_sigma K q qi n hqi i
  simp only [barSymJMSum, Finset.sum_add_distrib, add_mul, mul_add, hL, hI]

end BarSymCentral

end GeneralGap

end QOU.SchurWeyl
