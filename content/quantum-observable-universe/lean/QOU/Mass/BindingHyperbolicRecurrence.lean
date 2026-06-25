import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

/-!
# QOU.Mass.BindingHyperbolicRecurrence — Layer 1: the hyperbolic (cosh/sinh) recurrence

**The n ≤ 4 effective layer of the binding prolongation `a_D^(n)`.** Sibling PR #2795 settled
that the *global* `a_D^(n)` is super-exponential (`lw`/#1765, a q-Bessel-class object — see the
companion `BindingQBesselKernel`), while the **depth-2 SL₂ recurrence**

  `a_D^(n+2) = τ · a_D^(n+1) − a_D^(n)`,    `det = 1`   (`sl2-prolongation-recurrence`)

is the **geometric** effective reading fit to the three binding anchors `n = 2, 3, 4`
(deuteron `n=2`, ⁴He magic-shell `n=4`). `NaStokesKeystone.tau_in_stokes_eigenvalue_gap` proved
`τ = 3(3[2]²+2)/(4([2]+2))`, a **bar-even** number ≥ 2; this file pins what that depth-2
recurrence *is*: a **hyperbolic** transfer with the characteristic `det = +1` SL₂(ℝ) eigenvalue
pair `e^{±θ}` (contrast the **Hecke** kernel `x²−(q−q⁻¹)x−1`, `det = −1`, in
`HeckeStokesEigenvalues.stokes_curvature_factors`).

## Even/odd = cosh/sinh — the answer to "what comes out naturally"

The two independent solutions of the depth-2 recurrence with `τ = 2 cosh θ` are exactly the two
hyperbolic functions of `nθ`:

  `a_D^(n) = cosh(nθ)`   (**even** in `θ`: `θ ↦ −θ` invariant — the bar-even / `[2]_q` channel)
  `a_D^(n) = sinh(nθ)`   (**odd**  in `θ`: `θ ↦ −θ` anti-invariant — the bar-odd / `Q_β` channel)

The bar-involution `q ↦ q⁻¹` is `θ ↦ −θ` (with `q = e^θ` up to the substrate scaling), so the
even/odd split here is *the same* even/odd split as `NaStokesKeystone.tau_closed_form_bar_even`
(cosh, bar-even) vs `NaStokesKeystone.curvature_coeff_bar_odd` (sinh, bar-odd). The binding trace
`τ`, built from the **even** gap `[2]_q` alone, lands on the cosh branch — hence `τ = 2 cosh θ`.

Ground ring `ℝ` (archimedean: `Real.cosh`/`Real.sinh`/`Real.exp` are intrinsically real),
matching §7c — the hyperbolic angle `θ` is a post-τ archimedean datum.
-/

namespace QOU.Mass.BindingHyperbolicRecurrence

/-- **The binding transfer kernel factors into a `det = +1` hyperbolic eigenvalue pair.**
`R(q,x) = x² − (λ + λ⁻¹)x + 1 = (x − λ)(x − λ⁻¹)` for `λ ≠ 0`. The two roots `λ, λ⁻¹` multiply
to `+1` — the SL₂(ℝ) hyperbolic pair `e^{±θ}` of the depth-2 binding recurrence. This is the
`det = +1` companion of the Hecke curvature kernel `x²−(q−q⁻¹)x−1 = (x−q)(x+q⁻¹)` (`det = −1`,
`QOU.Mass.HeckeStokes.stokes_curvature_factors`): binding is the *symmetric* hyperbolic face. -/
theorem binding_kernel_factors (lam x : ℝ) (hlam : lam ≠ 0) :
    x ^ 2 - (lam + lam⁻¹) * x + 1 = (x - lam) * (x - lam⁻¹) := by
  field_simp
  ring

/-- **`cosh(nθ)` is the EVEN solution of the depth-2 binding recurrence** with `τ = 2 cosh θ`:
`cosh((n+2)θ) = 2 cosh θ · cosh((n+1)θ) − cosh(nθ)`. (`cosh` is even in `θ`, the bar-even /
`[2]_q` / `m_π` channel — the branch `τ` itself lives on.) -/
theorem cosh_satisfies_binding_recurrence (θ : ℝ) (n : ℕ) :
    Real.cosh (((n : ℝ) + 2) * θ)
      = 2 * Real.cosh θ * Real.cosh (((n : ℝ) + 1) * θ) - Real.cosh ((n : ℝ) * θ) := by
  have e1 : ((n : ℝ) + 2) * θ = ((n : ℝ) + 1) * θ + θ := by ring
  have e2 : (n : ℝ) * θ = ((n : ℝ) + 1) * θ - θ := by ring
  rw [e1, e2, Real.cosh_add, Real.cosh_sub]
  ring

/-- **`sinh(nθ)` is the ODD solution of the depth-2 binding recurrence** with `τ = 2 cosh θ`:
`sinh((n+2)θ) = 2 cosh θ · sinh((n+1)θ) − sinh(nθ)`. (`sinh` is odd in `θ`, the bar-odd /
curvature-coefficient / `Q_β` channel.) Same recurrence as `cosh` — the recurrence is blind to
the even/odd boundary data; that is exactly the cosh/sinh degeneracy of a `det = +1` hyperbolic
transfer. -/
theorem sinh_satisfies_binding_recurrence (θ : ℝ) (n : ℕ) :
    Real.sinh (((n : ℝ) + 2) * θ)
      = 2 * Real.cosh θ * Real.sinh (((n : ℝ) + 1) * θ) - Real.sinh ((n : ℝ) * θ) := by
  have e1 : ((n : ℝ) + 2) * θ = ((n : ℝ) + 1) * θ + θ := by ring
  have e2 : (n : ℝ) * θ = ((n : ℝ) + 1) * θ - θ := by ring
  rw [e1, e2, Real.sinh_add, Real.sinh_sub]
  ring

/-- **The binding trace is `2 cosh θ` when the eigenvalue is `e^θ`.** `e^θ + (e^θ)⁻¹ = 2 cosh θ`,
so the `det = +1` pair `λ = e^θ`, `λ⁻¹ = e^{−θ}` has trace `τ = 2 cosh θ` — the hyperbolic-angle
form of the depth-2 binding trace `τ = 2 cosh θ_binding ≈ 2.6424` (`θ_binding ≈ 0.78145`). -/
theorem binding_trace_two_cosh (θ : ℝ) :
    Real.exp θ + (Real.exp θ)⁻¹ = 2 * Real.cosh θ := by
  rw [← Real.exp_neg, Real.cosh_eq]
  ring

end QOU.Mass.BindingHyperbolicRecurrence
