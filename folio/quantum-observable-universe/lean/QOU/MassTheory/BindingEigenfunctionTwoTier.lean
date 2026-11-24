/-
# Binding eigenfunction — two-tier structure: seed q-integer + Habiro cyclotomic tail

The na-Stokes / Reeb binding period is the mean quantum dimension
`a_D^(n) = S(n)/n` with `S(n) = Σ_{λ⊢n} dim_q(λ)` (the q-involution number;
`q → 1` gives the involution/telephone numbers `1, 1, 2, 4, 10, 26, …`,
OEIS A000085). `S` obeys the monic three-term recurrence

    S(n) = S(n−1) + c_n · S(n−2),   c_n := (S(n) − S(n−1)) / S(n−2),

its own **eigenfunction relation** (S is the eigen-sequence of the order-2
q-difference operator with coefficient `c_n`). This file certifies, as machine-
checked algebraic identities in the formal fibre parameter `q`, the **two-tier**
structure of that coefficient. The closed-form `S`-values are the symbolic
compute output (q-hook-length formula; `Σ_{λ⊢n} dim_q(λ)`), verified here at the
low orders used:

* `S(0)=S(1)=1`, `S(2)=2` (q-independent: both partitions of 2 have `dim_q = 1`),
* `S(3) = 2 + [2]_q`   (partitions `[3],[1³] ↦ 1`; `[2,1] ↦ [2]_q`),
* `S(4) = 2 + 2[3]_q + (q² + q⁻²)`   (`[4],[1⁴] ↦ 1`; `[3,1],[2,1²] ↦ [3]_q`;
  `[2,2] ↦ [4]_q/[2]_q = q² + q⁻²`).

## Tier 1 — the seed is the symmetric q-integer (ONE nontrivial point)

`c_2 = [1]_q = 1` (near-trivial: `S(2)=2`, `S(1)=S(0)=1`) and
**`c_3 = [2]_q` exactly** — the single nontrivial seed coincidence. Equivalently
the recurrence with coefficient `[n−1]_q` holds exactly at `n = 2, 3`
(`D(2) = D(3) = 0`, below).

**This is NOT a pattern.** The naive `c_n = [n−1]_q` law is exact ONLY at
`n = 2, 3`; the deviation `D(n)` is nonzero from `n = 4` (adversarially
confirmed by exact symbolic factorization, `n = 4..8`). So the "seed = symmetric
q-integer" statement is genuinely just the two anchor points — where the
calibration lives — not an all-`n` recurrence.

## Tier 2 — the deviation carries the Habiro `(q−1)²·Φ_d` signature

`D(n) := S(n) − (S(n−1) + [n−1]_q·S(n−2))`. The first nonzero deviation is
`D(4) = (q²+q⁻²) − (q+q⁻¹)`, and clearing `q²`:

    q²·D(4) = (q−1)²·(q²+q+1) = (q−1)²·Φ₃,

the universal `(q−1)²` (double root at `q=1`; the deviation is a pure fibre /
q-deformation effect) times a **cyclotomic** leading factor. This is the Habiro-
ring (cyclotomic-completion) signature.

**Honest scope of "Habiro" (adversarial).** The `(q−1)²` is universal and the
LEADING factors of `D(n)` are cyclotomic (`Φ₃` at `n=4`; `Φ₅`, `Φ₆`, `Φ₇` deeper),
but `D(6), D(7), D(8)` carry **non-cyclotomic** cofactors. "Habiro-class" is a
ring-membership claim about the leading structure, NOT a purely-cyclotomic claim.

## What this file does NOT certify (STRICT scope)

* It does **not** make `S(n)` a Rogers–Szegő / q-Hermite moment at `q ≠ 1`. The
  clean RS recurrence `μ(n) = μ(n−1) + [n−1]_q·μ(n−2)` belongs to the **crossing**
  moment `μ_q`, which FORKS from the quantum-dimension binding period `S(n)`
  (+0.3 % at `n=4` → +7.9 % at `n=8`). The `q → 1` limits agree (both `= I(n)`);
  the `q₀`-values do not. So no q-Fourier eigenfunction property for `S(n)` is
  asserted here — only the seed + first-order-deviation algebra.
* It does **not** close the per-atom residue weight `w_n(K)` (the open
  q-difference kernel `R(q,x)` of `conj:binding-manybody-eq-jet-filtration`), and
  it does **not** improve any mass or binding prediction. The two-tier structure
  is a *derived, parameter-free target* the weight kernel must reproduce, per the
  AGENTS.md permanence principle (a proved algebraic piece is a correct
  contribution even while the total binding is not derived) — nothing more.

Base ring: `[Field R]` for the symmetric q-integers `[k]_q = (qᵏ−q⁻ᵏ)/(q−q⁻¹)`
(inverse `q⁻¹`; fibre q-deformation, no archimedean structure — AGENTS.md §7c
allows `Field` for `x⁻¹`), plus a pure `[CommRing R]` companion for the
division-free Habiro-tail polynomial identity. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-06-27-lever1-qinvolution-cyclotomic-kernel.md §"Stage 2"
-- Ref: [leitner2026] docs/audits/2026-06-26-binding-period-qinvolution-qhermite-identification.md
-/
import Mathlib.Tactic

namespace QOU.Mass.BindingEigenfunctionTwoTier

variable {R : Type*}

/-! ## Symmetric q-integers (fibre; `q⁻¹`, no archimedean structure) -/

section Field
variable [Field R]

/-- Symmetric `[2]_q = q + q⁻¹`. -/
def qbr2 (q : R) : R := q + q⁻¹

/-- Symmetric `[3]_q = q² + 1 + q⁻²`. -/
def qbr3 (q : R) : R := q ^ 2 + 1 + (q⁻¹) ^ 2

/-! ## Binding-period closed forms `S(n) = Σ_{λ⊢n} dim_q(λ)` (symbolic compute) -/

/-- `S(0) = 1` (empty partition). -/
def S0 : R := 1
/-- `S(1) = 1`. -/
def S1 : R := 1
/-- `S(2) = 2` (q-independent). -/
def S2 : R := 2
/-- `S(3) = 2 + [2]_q`. -/
def S3 (q : R) : R := 2 + qbr2 q
/-- `S(4) = 2 + 2[3]_q + (q² + q⁻²)`. -/
def S4 (q : R) : R := 2 + 2 * qbr3 q + (q ^ 2 + (q⁻¹) ^ 2)

/-! ## Tier 1 — the seed is the symmetric q-integer -/

/-- `c₂ = (S(2) − S(1))/S(0) = 1 = [1]_q` (near-trivial; `S(0)=1`). -/
theorem c2_seed : (S2 : R) - S1 = 1 := by simp only [S2, S1]; norm_num

/-- Recurrence exact at `n = 2`: `D(2) = S(2) − (S(1) + [1]_q·S(0)) = 0`,
with `[1]_q = 1`. -/
theorem D2_zero : (S2 : R) - (S1 + 1 * S0) = 0 := by simp only [S2, S1, S0]; norm_num

/-- **`c₃ = [2]_q` exactly** — the single nontrivial seed coincidence.
`c₃ = (S(3) − S(2)) / S(1) = S(3) − S(2)` since `S(1) = 1`. -/
theorem c3_eq_qbr2 (q : R) : S3 q - S2 = qbr2 q := by
  simp only [S3, S2]; ring

/-- Recurrence exact at `n = 3`: `D(3) = S(3) − (S(2) + [2]_q·S(1)) = 0`. -/
theorem D3_zero (q : R) : S3 q - (S2 + qbr2 q * S1) = 0 := by
  simp only [S3, S2, S1]; ring

/-- At `q = 1`, `[2]_q = 2` — the classical involution recurrence coefficient
`I(3) = I(2) + 2·I(1)` (the `n−1 = 2` weight). Ties Tier 1 to A000085. -/
theorem qbr2_classical_limit : qbr2 (1 : R) = 2 := by norm_num [qbr2]

/-! ## Tier 2 — the Habiro `(q−1)²·Φ₃` deviation at `n = 4` -/

/-- `D(4) = S(4) − (S(3) + [3]_q·S(2)) = (q² + q⁻²) − (q + q⁻¹)`, the first
nonzero deviation from the naive `[n−1]_q` recurrence. -/
theorem D4_eq (q : R) :
    S4 q - (S3 q + qbr3 q * S2) = (q ^ 2 + (q⁻¹) ^ 2) - (q + q⁻¹) := by
  simp only [S4, S3, S2, qbr3, qbr2]; ring

/-- **Habiro cyclotomic signature.** Clearing `q²`, the `n = 4` deviation is
`(q−1)²·Φ₃` with `Φ₃ = q²+q+1` cyclotomic and the universal `(q−1)²` double
root at `q = 1`. -/
theorem D4_habiro_factor (q : R) (hq : q ≠ 0) :
    q ^ 2 * (S4 q - (S3 q + qbr3 q * S2)) = (q - 1) ^ 2 * (q ^ 2 + q + 1) := by
  rw [D4_eq]; field_simp; ring

end Field

/-! ## Pure-ring companion — the division-free Habiro-tail identity -/

section CommRing
variable [CommRing R]

/-- The Habiro-tail polynomial identity (division-free, generic `CommRing`):
`q⁴ + 1 − q³ − q = (q−1)²·Φ₃`, `Φ₃ = q² + q + 1`. This is `q²·D(4)` after the
symmetric brackets are cleared — the `n = 4` deviation's exact cyclotomic form. -/
theorem habiro_tail_poly (q : R) :
    q ^ 4 + 1 - q ^ 3 - q = (q - 1) ^ 2 * (q ^ 2 + q + 1) := by ring

end CommRing

end QOU.Mass.BindingEigenfunctionTwoTier
