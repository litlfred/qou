import Mathlib.Tactic

/-!
# Garoufalidis–Zagier weight-difference selection rule for the `4₁` Stokes rays

Formalize-first resolution of the **`β = 3/2` failure** in the A_ω odd-channel
attack. The corpus probe `qbeta_modular_resurgence_stokes_probe.py` tested a Borel
loggamma exponent `β = 3/2` against the geometric–conjugate `κ`-ladder and it
**failed** (`β_inf ≈ 0.2–0.26`, `docs/audits/2026-07-18-g3-stokes-keystone-evidence-base.md`).
The literature says why: `3/2` is a **type error** here.

**The `3/2` is the Garoufalidis–Zagier modular weight `κ(σ₀)` of the *trivial*
connection** — the automorphy-factor exponent of the Kashaev `N^{3/2}` prefactor
(`⟨K⟩_N ∼ N^{3/2} e^{v N} Φ(2πi/N)`, GZ eq. 1.1; the weight `κ(σ) = 3/2` iff
`σ = σ₀`, else `0`, GZ eq. 3.7). It is **not** the characteristic exponent of a
single Borel singularity. The Borel exponent of a Stokes ray joining connections
`σ, σ′` is the **weight difference** `b = κ(σ) − κ(σ′)`.

The A_ω singularity sits at `ω = Vol(4₁)/π`, the **geometric ↔ conjugate** ray
(`σ₁ ↔ σ̄₁`, GGM 2007.10190) — **both non-trivial, both weight 0** — so its Borel
exponent is the **integer `b = 0`**, and its Stokes constant is the **integer**
DT/BPS `3d`-index count `[q⁰] Ind^{rot}_{4₁} = 3` (GGM Conj. 2), not a
half-integer-weight modular datum. A value `b = ±3/2` can occur **only** on a
`σ₀ ↔ (non-trivial)` ray — a *different* singularity than A_ω. So testing `β = 3/2`
against the geometric–conjugate ladder was a category error.

This file encodes GZ eq. 3.7's weight function on the three relevant `4₁`
connections and derives the selection consequences over the finite connection type.
No fit; the weight *values* are the cited GZ definition, the selection *rules* are
their algebraic consequences. Verified `lean`-direct (exit 0).

-- Ref: [garoufalidis-zagier-2024] https://arxiv.org/abs/2111.06645 (SIGMA 20 (2024) 055, eq. 3.7)
-- Ref: [garoufalidis-gu-marino2021] https://doi.org/10.1007/s00220-021-04076-0 (Conj. 2, Stokes = rotated 3d-index)
-/

namespace QOU.QBeta.GZWeightSelection

/-- The three flat connections of the figure-eight (`4₁`) parabolic character variety
that carry the resurgent structure: the **trivial** connection `sigma0` (`σ₀`, whose
column is the Kashaev invariant in the Habiro ring), the **geometric** connection
`sigma1` (`σ₁`), and its complex **conjugate** `sigma1bar` (`σ̄₁`). -/
inductive FlatConn where
  | sigma0
  | sigma1
  | sigma1bar
  deriving DecidableEq, Fintype

open FlatConn

/-- **Garoufalidis–Zagier representation weight** `κ` (2111.06645 eq. 3.7):
`κ(σ₀) = 3/2` for the trivial connection, `0` for every non-trivial connection. The
`3/2` is the automorphy-factor exponent of the Kashaev `N^{3/2}` prefactor — a
discrete, representation-indexed weight, **not** a Borel loggamma index. -/
def kappa : FlatConn → ℚ
  | sigma0    => 3 / 2
  | sigma1    => 0
  | sigma1bar => 0

/-- The **Borel characteristic exponent** of a Stokes ray joining `σ, σ′` is the
weight difference `b = κ(σ) − κ(σ′)` (GZ eq. 3.7–3.8: the completed series carries the
automorphy factor `|cℏ|^{κ(σ)}`, so a ray's exponent is the difference of endpoint
weights). -/
def weightDiff (σ σ' : FlatConn) : ℚ := kappa σ - kappa σ'

/-- **`σ₀` is the unique weight-`3/2` connection** (GZ eq. 3.7). The `3/2` belongs to
the trivial connection alone. -/
theorem kappa_eq_three_halves_iff (σ : FlatConn) : kappa σ = 3 / 2 ↔ σ = sigma0 := by
  cases σ <;> simp [kappa] <;> norm_num

/-- **The Borel exponent of any `4₁` Stokes ray is `0` or `±3/2`.** These are the only
values of `κ(σ) − κ(σ′)` — the discrete selection: no continuous `β` to fit. -/
theorem weightDiff_mem (σ σ' : FlatConn) :
    weightDiff σ σ' = 0 ∨ weightDiff σ σ' = 3 / 2 ∨ weightDiff σ σ' = -(3 / 2) := by
  cases σ <;> cases σ' <;> simp [weightDiff, kappa]

/-- **The A_ω ray has integer characteristic exponent `b = 0`.** Both endpoints of the
A_ω ray — geometric `σ₁` and conjugate `σ̄₁` — have weight `0`, so its Borel exponent
is `0 ∈ ℤ`. Hence the A_ω Stokes constant is an **integer** (the DT/BPS `3d`-index
count, GGM Conj. 2), not a half-integer-weight modular quantity. This is the correct
replacement for the refuted `β = 3/2`. -/
theorem weightDiff_aomega_zero : weightDiff sigma1 sigma1bar = 0 := by
  simp [weightDiff, kappa]

/-- **The weight `3/2` requires a trivial endpoint.** `b = ±3/2` can occur only on a
`σ₀ ↔ (non-trivial)` ray — a *different* singularity than A_ω (which is
geometric↔conjugate). Formalizes why testing `β = 3/2` against the
geometric–conjugate ladder is a category error. -/
theorem weightDiff_three_halves_needs_trivial {σ σ' : FlatConn}
    (h : weightDiff σ σ' = 3 / 2 ∨ weightDiff σ σ' = -(3 / 2)) :
    σ = sigma0 ∨ σ' = sigma0 := by
  cases σ <;> cases σ' <;>
    simp_all [weightDiff, kappa] <;> norm_num at h

/-- **Integer-exponent selection rule.** The Borel exponent `b = κ(σ) − κ(σ′)` is `0`
(the only integer value it takes) **iff** the two connections lie on the same side of
triviality — both trivial or both non-trivial. The A_ω ray (both non-trivial) is on
the integer branch; every `σ₀`-ray is on the half-integer branch. -/
theorem weightDiff_eq_zero_iff (σ σ' : FlatConn) :
    weightDiff σ σ' = 0 ↔ (σ = sigma0 ↔ σ' = sigma0) := by
  cases σ <;> cases σ' <;> simp [weightDiff, kappa]

end QOU.QBeta.GZWeightSelection
