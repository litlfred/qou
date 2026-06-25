import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import QOU.Mass.HeckeStokesEigenvalues

/-!
# QOU.Mass.NaStokesKeystone — the prolongation-period keystone (§3b conjecture) and the conditional τ

This file formalises the **neighbourhood** of the Lever-1 keystone identity

  `a_D^(n) = ∮_{S_c} λ_SW^(n) = lw(n−1)`        (conj #1765)

— stating the keystone as a §3b conjecture *class* and proving, **conditional on it**,
that the depth-2 SL₂ binding trace `τ` assembles (sorry-free) to its bar-even closed form.

## The non-abelian-Stokes utilisation (the bridge made explicit)

The keystone is the last link of the categorical derivation chain. The non-abelian
Stokes step supplies *what* the period integrates to:

1. **Yekutieli non-abelian Stokes (`prop:hecke-spectral-sequence`).** The abelianised
   Cartan connection on the exceptional divisor `S_c` has curvature 2-form
   `F(σ) = σ² − (q − q⁻¹)σ − 1`. Flatness `F = 0` *derives* the Hecke quadratic, whose
   two roots are the Stokes/Hecke eigenvalues `λ₊ = q` (symmetric `L₊`),
   `λ₋ = −q⁻¹` (antisymmetric `L₋`) — `QOU.Mass.HeckeStokes.stokes_curvature_factors`.
2. **Holonomy = multiplicative surface integral.** The loop holonomy
   `Hol(∂S_c) = ∮_{S_c} F` (Yekutieli's MI∫) is therefore a **Hecke element**.
3. **Markov trace (`QOU.Hecke.MarkovTrace`).** Closing the loop applies the canonical
   trace `tr_M`, which Wedderburn-decomposes as `tr_M(x) = Σ_λ y_λ χ^λ(x)`
   (`QOU.Hecke.Wedderburn.trace_decomp`).
4. **Mean quantum dimension.** Averaging the selection-rule character sum over the
   partitions `λ ⊢ c+1` is precisely `lw(c) = (1/(c+1)) Σ_{λ⊢c+1} dim_q V_λ`. The
   keystone asserts the `n`-jet prolongation period equals this categorical average.

So the open core is **only** the geometric step 1→4 equality (`period = lw`); everything
downstream of it — the τ assembly here — is unconditional Lean algebra. The bar-evenness
of τ is inherited from the **eigenvalue gap** `[2]_q = λ₊ − λ₋ = q − (−q⁻¹)`
(`QOU.Mass.HeckeStokes.quantum_dim_is_eigenvalue_gap`), which this file uses directly.

## Scope honesty — the depth-2 SL₂ τ is the `n ≤ 4` effective reading

Sibling PR #2795 (`sw_period_growth_probe.py`, fork verdict
[`docs/audits/2026-06-25-sw-jet-prolongation-explicit-and-fork.md`]) settles, structurally,
that `γ` encircles a `disc_X = 0` branch point ⇒ a **√-branch** ⇒
`X^(n) ~ (z−z_k)^{1/2−n}` ⇒ the period coefficient is the falling factorial `(1/2)_n`,
so the **true global** `a_D^(n)` grows **super-exponentially** (= the mean quantum dimension
`lw`; the q-Bessel class is its fast kernel). The depth-2 SL₂ recurrence
`a_D^(n+2) = τ a_D^(n+1) − a_D^(n)` is **geometric** (ratio → λ₊ ≈ 2.18), so τ is an
**effective fit to the three binding anchors `n = 2, 3, 4`** (deuteron `n=2`, ⁴He
magic-shell `n=4`). They agree through `n = 5` and split at `n = 6`. Accordingly the
theorem below consumes the keystone **only at `c = 1, 2, 3`** — it is the honest finite
`n ≤ 4` assembly, not a claim that the global prolongation is SL₂.

The three selection-rule values fed as hypotheses are proved unconditionally on `main`:
`selection_rule_c1_eq_one`, `selection_rule_c2_eq_closed_form`,
`selection_rule_c3_eq_family_a_q_form` (`climax-volume-mass/selection-rule-*.lean`).

Ground ring `ℝ` (substrate-anchor regime: `0 < q` is used to clear denominators).
AGENTS.md §3b-cond: the keystone is the *single* class-axiomatised conjectural input; the
τ conclusion is **derived** from it (not carried as a class field), so the result is a
rigorous conditional theorem, not a self-assuming projection.
-/

namespace QOU.Mass.NaStokesKeystone

open QOU.Mass.HeckeStokes

/-- **The prolongation-period keystone — `conj:sw-prolongation-period-eq-mean-qdim` (#1765),
axiomatised as a §3b conjecture class.**

`aD n` is the `n`-th jet-prolongation period `a_D^(n) = ∮_{S_c} λ_SW^(n)` of the
Seiberg–Witten differential; `lw c` is the selection-rule mean quantum dimension
`(1/(c+1)) Σ_{λ⊢c+1} dim_q V_λ`. The conjecture asserts the period equals the
non-abelian-Stokes / Markov-trace average `lw` at every level:

  `a_D^(n) = lw(n−1)`   i.e.   `aD (c+1) = lw c`.

This `sorry`-free class is the *only* unproved input of the conditional results below; an
instance is the geometric content (step 1→4 of the docstring bridge), not a missing proof. -/
class ProlongationPeriodMeanQuantumDim (aD lw : ℕ → ℝ) : Prop where
  /-- #1765: the `n`-jet Seiberg–Witten period equals the mean quantum dimension `lw(n−1)`,
  i.e. `aD (c+1) = lw c`. This is the non-abelian-Stokes holonomy → Markov-trace →
  `Σ_λ y_λ χ^λ` → mean-quantum-dimension bridge, asserted to hold as an equality. -/
  keystone : ∀ c, aD (c + 1) = lw c

/-- The **depth-2 SL₂ binding trace** `τ = (a_D^(2) + a_D^(4)) / a_D^(3)`, the trace of the
transfer matrix `R(q,x) = x² − τ x + 1` fit to the three binding anchors `n = 2, 3, 4`
(`sl2-prolongation-recurrence`). -/
noncomputable def tauOf (aD : ℕ → ℝ) : ℝ := (aD 2 + aD 4) / aD 3

/-- **The `c = 2` selection-rule anchor in the non-abelian-Stokes eigenvalue gap.**
`lw(2) = (q+1)²/(3q) = (2 + [2]_q)/3`, where `[2]_q = λ₊ − λ₋ = q − (−q⁻¹)` is the gap
between the two Stokes/Hecke eigenvalues (`quantum_dim_is_eigenvalue_gap`). This exhibits
the proton-channel anchor that feeds τ as `(2 + eigenvalue-gap)/3`, a direct na-Stokes datum. -/
theorem lw2_eq_two_plus_stokes_gap (q : ℝ) (hq : 0 < q) :
    (q + 1) ^ 2 / (3 * q) = (2 + (q - (-q⁻¹))) / 3 := by
  rw [quantum_dim_is_eigenvalue_gap q]
  have hq0 : q ≠ 0 := ne_of_gt hq
  field_simp
  ring

/-- **Theorem (conditional on `conj:sw-prolongation-period-eq-mean-qdim`, #1765).**
Given the keystone (period = mean quantum dimension) at the three binding anchors and the
unconditionally-proved selection-rule values
`lw(1) = 1`, `lw(2) = (q+1)²/(3q)`, `lw(3) = (3q²+4+3q⁻²)/4`, the depth-2 SL₂ binding trace
assembles to the **bar-even** closed form

  `τ = 3(3q⁴ + 8q² + 3) / (4q(q+1)²)`.

Only `ProlongationPeriodMeanQuantumDim` is conjectural; the assembly is sorry-free real
algebra. (The `n ≤ 4` effective reading — see the file docstring / PR #2795.) -/
theorem tau_conditional_on_keystone
    {aD lw : ℕ → ℝ} [K : ProlongationPeriodMeanQuantumDim aD lw]
    (q : ℝ) (hq : 0 < q)
    (h1 : lw 1 = 1)
    (h2 : lw 2 = (q + 1) ^ 2 / (3 * q))
    (h3 : lw 3 = (3 * q ^ 2 + 4 + 3 * q⁻¹ ^ 2) / 4) :
    tauOf aD = 3 * (3 * q ^ 4 + 8 * q ^ 2 + 3) / (4 * q * (q + 1) ^ 2) := by
  unfold tauOf
  rw [K.keystone 1, K.keystone 2, K.keystone 3, h1, h2, h3]
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq1 : q + 1 ≠ 0 := by positivity
  field_simp
  ring

/-- **τ in the non-abelian-Stokes eigenvalue-gap form.** The same conditional τ, written in
the eigenvalue gap `b = λ₊ − λ₋ = q − (−q⁻¹) = [2]_q` (`quantum_dim_is_eigenvalue_gap`):

  `τ = 3(3b² + 2) / (4(b + 2))`,

matching `QOU.Mass.TauQuantumIntegerForm` (`τ = 3(3[2]² + 2)/(4([2]+2))`). This is the
na-Stokes utilisation made fully explicit: the binding trace is a rational function of the
Hecke/Stokes eigenvalue gap, hence bar-even. -/
theorem tau_in_stokes_eigenvalue_gap
    {aD lw : ℕ → ℝ} [K : ProlongationPeriodMeanQuantumDim aD lw]
    (q : ℝ) (hq : 0 < q)
    (h1 : lw 1 = 1)
    (h2 : lw 2 = (q + 1) ^ 2 / (3 * q))
    (h3 : lw 3 = (3 * q ^ 2 + 4 + 3 * q⁻¹ ^ 2) / 4) :
    tauOf aD
      = 3 * (3 * (q - (-q⁻¹)) ^ 2 + 2) / (4 * ((q - (-q⁻¹)) + 2)) := by
  rw [quantum_dim_is_eigenvalue_gap q, tauOf,
    K.keystone 1, K.keystone 2, K.keystone 3, h1, h2, h3]
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq1 : q + 1 ≠ 0 := by positivity
  field_simp
  ring

/-! ## The even/odd (cosh/sinh) hyperbolic structure

Writing `q = e^ξ` (`ξ = log q`), the two Stokes/Hecke eigenvalue combinations are the two
hyperbolic functions of `ξ`:

  `[2]_q = q + q⁻¹ = 2 cosh ξ`     (the **gap** `λ₊ − λ₋`; **bar-even**, `q ↦ q⁻¹` invariant)
  `q − q⁻¹ = 2 sinh ξ`             (the **curvature coefficient** `λ₊ + λ₋`; **bar-odd**)

The Hecke bar-involution `q ↦ q⁻¹` is `ξ ↦ −ξ`, under which `cosh` is even and `sinh` is odd.
This is exactly the "even/odd" split: `τ` is a rational function of the **even** gap alone
(`tau_in_stokes_eigenvalue_gap`), hence bar-even — it is the algebraic face of
`τ = 2 cosh θ_binding`. The lemmas below pin the even/odd dichotomy without leaving the
substrate-algebra regime (no `Real.cosh`/`exp` needed; the bar-involution carries the parity).
The bar-odd `q − q⁻¹` is the `sinh`-partner whose physical face is the bar-odd `Q_β` scale
(canonical cheat sheet: `Q_β` = the `sinh` partner of the bar-even `cosh` meson scale `m_π`). -/

/-- **Bar-odd (sinh) partner of the eigenvalue gap.** The curvature coefficient `q − q⁻¹`
flips sign under the Hecke bar-involution `q ↦ q⁻¹`: `q⁻¹ − (q⁻¹)⁻¹ = −(q − q⁻¹)`. Contrast
`QOU.Mass.HeckeStokes.quantum_dim_bar_even` (the gap `[2]_q`, bar-**even**, cosh). The two
combinations are the `sinh`/`cosh` of `ξ = log q` under `ξ ↦ −ξ`. (A pure bar-involution
identity — its generic-field partner `quantum_dim_bar_even` lives in `HeckeStokesEigenvalues`;
here it is stated over the file's archimedean ring `ℝ`, no ordering needed.) -/
theorem curvature_coeff_bar_odd (q : ℝ) :
    q⁻¹ - (q⁻¹)⁻¹ = -(q - q⁻¹) := by
  rw [inv_inv]; ring

/-- **τ is bar-even (the cosh-like invariance).** The conditional closed form
`τ(q) = 3(3q⁴+8q²+3)/(4q(q+1)²)` is invariant under `q ↦ q⁻¹`: `τ(q⁻¹) = τ(q)`. Because `τ`
factors through the **even** eigenvalue gap (`tau_in_stokes_eigenvalue_gap`), it inherits the
bar-evenness of `cosh ξ` — the binding trace cannot see the bar-odd `sinh` direction. -/
theorem tau_closed_form_bar_even (q : ℝ) (hq : 0 < q) :
    3 * (3 * (q⁻¹) ^ 4 + 8 * (q⁻¹) ^ 2 + 3) / (4 * q⁻¹ * (q⁻¹ + 1) ^ 2)
      = 3 * (3 * q ^ 4 + 8 * q ^ 2 + 3) / (4 * q * (q + 1) ^ 2) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq1 : q + 1 ≠ 0 := by positivity
  field_simp
  ring

end QOU.Mass.NaStokesKeystone
