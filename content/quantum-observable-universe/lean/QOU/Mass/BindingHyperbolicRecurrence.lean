import QOU.QBeta.ReebTowerJacobiAnger

/-!
# QOU.Mass.BindingHyperbolicRecurrence — Layer 1: the hyperbolic (cosh/sinh) recurrence

**The n ≤ 4 effective layer of the binding prolongation `a_D^(n)`.** Sibling PR #2795 settled
that the *global* `a_D^(n)` is super-exponential (`lw`/#1765, a q-Bessel-class object — see the
companion `BindingQBesselKernel`), while the **depth-2 SL₂ recurrence**

  `a_D^(n+2) = τ · a_D^(n+1) − a_D^(n)`,    `det = 1`   (`sl2-prolongation-recurrence`)

is the **geometric** effective reading fit to the three binding anchors `n = 2, 3, 4`
(deuteron `n=2`, ⁴He magic-shell `n=4`). `NaStokesKeystone.tau_in_stokes_eigenvalue_gap` proved
`τ = 3(3[2]²+2)/(4([2]+2))`, a **bar-even** number ≥ 2.

## The binding Layer-1 tower **is** the Reeb growth tower

The cosh/sinh recurrence is already formalised generally in `QOU.QBeta.ReebTowerJacobiAnger`
(`reeb_tower_cosh_step` / `reeb_tower_sinh_step`, the bar-even / bar-odd Reeb towers). This file
**specialises** that machinery to the binding index tower `n ↦ a_D^(n)` and adds the two
binding-specific facts not in the Reeb file: the `det = +1` transfer factorisation and the
`τ = 2 cosh θ` trace.

## Even/odd = cosh/sinh — the answer to "what comes out naturally"

With `τ = 2 cosh θ`, the two independent solutions of the depth-2 recurrence are the two
hyperbolic functions of `nθ`:

  `a_D^(n) = cosh(nθ)`   (**even** in `θ` — the bar-even / `[2]_q` / `m_π` channel; `τ` lives here)
  `a_D^(n) = sinh(nθ)`   (**odd**  in `θ` — the bar-odd / curvature-coefficient / `Q_β` channel)

The bar-involution `q ↦ q⁻¹` is `θ ↦ −θ`, so this is the same even/odd split as
`NaStokesKeystone.tau_closed_form_bar_even` (cosh) vs `NaStokesKeystone.curvature_coeff_bar_odd`
(sinh). `τ`, built from the **even** gap `[2]_q` alone, lands on the cosh branch ⟹ `τ = 2 cosh θ`.

Ground ring `ℝ` (archimedean: `Real.cosh`/`Real.sinh`/`Real.exp`), matching §7c — the hyperbolic
angle `θ` is a post-τ archimedean datum.
-/

namespace QOU.Mass.BindingHyperbolicRecurrence

open Real QOU.QBeta

/-- **The binding transfer kernel factors into a `det = +1` hyperbolic eigenvalue pair.**
`R(q,x) = x² − (λ + λ⁻¹)x + 1 = (x − λ)(x − λ⁻¹)` for `λ ≠ 0`. The two roots `λ, λ⁻¹` multiply
to `+1` — the SL₂(ℝ) hyperbolic pair `e^{±θ}` of the depth-2 binding recurrence. This is the
`det = +1` companion of the Hecke curvature kernel `x²−(q−q⁻¹)x−1 = (x−q)(x+q⁻¹)` (`det = −1`,
`QOU.Mass.HeckeStokes.stokes_curvature_factors`): binding is the *symmetric* hyperbolic face.
(Not in the Reeb file — the binding-transfer determinant is the genuinely new datum here.) -/
theorem binding_kernel_factors (lam x : ℝ) (hlam : lam ≠ 0) :
    x ^ 2 - (lam + lam⁻¹) * x + 1 = (x - lam) * (x - lam⁻¹) := by
  field_simp
  ring

/-- **`cosh(nθ)` is the EVEN solution of the depth-2 binding recurrence** with `τ = 2 cosh θ`:
`cosh((n+2)θ) = 2 cosh θ · cosh((n+1)θ) − cosh(nθ)`. The binding-index specialisation of the
bar-even Reeb tower `reeb_tower_cosh_step` (at `a = (n+1)θ`, `η = θ`). -/
theorem cosh_satisfies_binding_recurrence (θ : ℝ) (n : ℕ) :
    cosh (((n : ℝ) + 2) * θ)
      = 2 * cosh θ * cosh (((n : ℝ) + 1) * θ) - cosh ((n : ℝ) * θ) := by
  have h := reeb_tower_cosh_step (((n : ℝ) + 1) * θ) θ
  rwa [show ((n : ℝ) + 1) * θ + θ = ((n : ℝ) + 2) * θ from by ring,
       show ((n : ℝ) + 1) * θ - θ = (n : ℝ) * θ from by ring] at h

/-- **`sinh(nθ)` is the ODD solution of the depth-2 binding recurrence** with `τ = 2 cosh θ`:
`sinh((n+2)θ) = 2 cosh θ · sinh((n+1)θ) − sinh(nθ)`. The binding-index specialisation of the
bar-odd Reeb tower `reeb_tower_sinh_step`. Same recurrence as `cosh` — the recurrence is blind to
the even/odd boundary data; that is exactly the cosh/sinh degeneracy of a `det = +1` hyperbolic
transfer. -/
theorem sinh_satisfies_binding_recurrence (θ : ℝ) (n : ℕ) :
    sinh (((n : ℝ) + 2) * θ)
      = 2 * cosh θ * sinh (((n : ℝ) + 1) * θ) - sinh ((n : ℝ) * θ) := by
  have h := reeb_tower_sinh_step (((n : ℝ) + 1) * θ) θ
  rwa [show ((n : ℝ) + 1) * θ + θ = ((n : ℝ) + 2) * θ from by ring,
       show ((n : ℝ) + 1) * θ - θ = (n : ℝ) * θ from by ring] at h

/-- **The binding trace is `2 cosh θ` when the eigenvalue is `e^θ`.** `e^θ + (e^θ)⁻¹ = 2 cosh θ`,
so the `det = +1` pair `λ = e^θ`, `λ⁻¹ = e^{−θ}` has trace `τ = 2 cosh θ` — the hyperbolic-angle
form of the depth-2 binding trace `τ = 2 cosh θ_binding ≈ 2.6424` (`θ_binding ≈ 0.78145`). -/
theorem binding_trace_two_cosh (θ : ℝ) :
    exp θ + (exp θ)⁻¹ = 2 * cosh θ := by
  rw [← Real.exp_neg, Real.cosh_eq]
  ring

end QOU.Mass.BindingHyperbolicRecurrence
