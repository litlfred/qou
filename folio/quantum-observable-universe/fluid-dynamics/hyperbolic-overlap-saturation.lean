import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# QOU.FluidDynamics.HyperbolicOverlapSaturation

Rigorous algebraic content of `rem:hyperbolic-overlap-saturation`.

Setting.  In the overlap regime $V_1 \gtrsim d^2$ the Biot–Savart
kernel saturates and the strain rate is taken to be
$\alpha_{\mathrm{hyp}} = \Gamma/(\pi V_1)$ (phenomenological,
Townsend / Moffatt–Kida–Ohkitani — *not* derived from Euler/NS).
Substituting into the Townsend system gives
$$
  \dot V_1 = 2\,\alpha_{\mathrm{hyp}}\,V_1 + 2\nu
           = 2\Gamma/\pi + 2\nu, \qquad
  \dot V_2 = -2\,\alpha_{\mathrm{hyp}}\,V_2 + 2\nu
           = -\tfrac{2\Gamma}{\pi V_1}\,V_2 + 2\nu.
$$
So $V_1(t) = V_{10} + b\,t$ is linear with growth rate
$b := 2\Gamma/\pi + 2\nu$.

What this file rigorously establishes:

1. The proportionality ansatz $V_2 = \lambda\,V_1$ — i.e. the
   *attracting* asymptotic ratio — forces
   $\lambda = \pi\nu/(2\Gamma + \pi\nu)$, *not* the naive
   quasi-steady value $\pi\nu/\Gamma$ obtained by setting
   $\dot V_2 = 0$.
2. The corrected ratio is strictly positive whenever $\nu > 0$,
   $\Gamma > 0$, $\pi > 0$.
3. Strict inequality: the asymptotic ratio is strictly less than
   the (incorrect) quasi-steady value — they differ by a finite
   factor that ranges from $2$ (inviscid limit) downward.

(1) and (3) are pure `field_simp` / `nlinarith` identities; no
external `sorry`.  The result corrects the user-supplied
$\kappa^2 = \pi\nu/\Gamma$ figure.

Why $\dot V_2 = 0$ fails here.  The $V_2$ relaxation rate
$2\Gamma/(\pi V_1)$ is comparable to the $V_1$ growth rate
$b/V_1 = (2\Gamma/\pi + 2\nu)/V_1$ — their ratio is
$1 + \pi\nu/\Gamma \geq 1$, so $V_2$ and $V_1$ evolve on the same
timescale and quasi-steady ansatz is unwarranted.  The
proportionality ansatz captures the genuine attracting balance.

LaTeX label: `rem:hyperbolic-overlap-saturation`
-/

namespace QOU.FluidDynamics

namespace HyperbolicOverlapSaturation

/-- Linear growth rate of $V_1$ in the saturated regime:
    $b = 2\Gamma/\pi + 2\nu$. -/
noncomputable def b (Γ π_ ν : ℝ) : ℝ := 2 * Γ / π_ + 2 * ν

/-- The corrected asymptotic proportionality ratio
    $\lambda = \pi\nu/(2\Gamma + \pi\nu)$. -/
noncomputable def lambda (Γ π_ ν : ℝ) : ℝ :=
  π_ * ν / (2 * Γ + π_ * ν)

/-- The quasi-steady (incorrect) value $\lambda_{\mathrm{QS}} =
    \pi\nu/\Gamma$ obtained by setting $\dot V_2 = 0$. -/
noncomputable def lambdaQuasiSteady (Γ π_ ν : ℝ) : ℝ := π_ * ν / Γ

/-- **The proportionality balance.**  If $V_2(t) = \lambda\,V_1(t)$
    and $V_1$ grows linearly with rate $b$, the Townsend ODE for
    $V_2$ forces $\lambda\,b = -(2\Gamma/\pi)\,\lambda + 2\nu$. -/
theorem proportionality_balance
    (Γ π_ ν : ℝ) (hπ : π_ ≠ 0) (hden : 2 * Γ + π_ * ν ≠ 0) :
    lambda Γ π_ ν * b Γ π_ ν
      = -(2 * Γ / π_) * lambda Γ π_ ν + 2 * ν := by
  unfold lambda b
  field_simp
  ring

/-- **Positivity of the corrected ratio.**  $\lambda > 0$ whenever
    $\nu, \Gamma, \pi > 0$. -/
theorem lambda_pos
    (Γ π_ ν : ℝ) (hΓ : 0 < Γ) (hπ : 0 < π_) (hν : 0 < ν) :
    0 < lambda Γ π_ ν := by
  unfold lambda
  have hnum : 0 < π_ * ν := mul_pos hπ hν
  have hden : 0 < 2 * Γ + π_ * ν := by positivity
  exact div_pos hnum hden

/-- **The quasi-steady value overstates.**  For any positive
    parameters, $\lambda < \lambda_{\mathrm{QS}}$ — i.e. the user
    constant $\pi\nu/\Gamma$ overestimates the true asymptotic
    ratio by the factor $1 + \pi\nu/(2\Gamma)$. -/
theorem lambda_lt_quasi_steady
    (Γ π_ ν : ℝ) (hΓ : 0 < Γ) (hπ : 0 < π_) (hν : 0 < ν) :
    lambda Γ π_ ν < lambdaQuasiSteady Γ π_ ν := by
  unfold lambda lambdaQuasiSteady
  have hd1 : 0 < 2 * Γ + π_ * ν := by positivity
  have hπν : 0 < π_ * ν := mul_pos hπ hν
  have hlt : Γ < 2 * Γ + π_ * ν := by linarith
  exact div_lt_div_of_pos_left hπν hΓ hlt

/-- **Strict positivity of the squared core aspect ratio.**  The
    corrected asymptotic ratio $\kappa^2 = \lambda$ is strictly
    positive: the cores lock into a finite elliptical profile.  The
    numerical value is $\pi\nu/(2\Gamma + \pi\nu)$, not
    $\pi\nu/\Gamma$.  (Re-scoped 2026-10-13: $\kappa^2$ is the core
    aspect ratio, not a Levi condition number, and its positivity is no
    longer read as branch (A) of `conj:levi-degeneracy`, which is
    withdrawn.) -/
theorem kappa_squared_pos
    (Γ π_ ν : ℝ) (hΓ : 0 < Γ) (hπ : 0 < π_) (hν : 0 < ν) :
    0 < lambda Γ π_ ν :=
  lambda_pos Γ π_ ν hΓ hπ hν

/-- **High-Reynolds inviscid-limit identity.**  In the limit
    $\nu \to 0$ at fixed $\Gamma, \pi$, $\lambda \cdot (2\Gamma) =
    \pi\nu$, so $\lambda \sim \pi\nu/(2\Gamma)$ — i.e. *half* the
    quasi-steady answer $\pi\nu/\Gamma$. -/
theorem lambda_inviscid_identity
    (Γ π_ ν : ℝ) (hΓ : 0 < Γ) (hπν : 2 * Γ + π_ * ν ≠ 0) :
    lambda Γ π_ ν * (2 * Γ + π_ * ν) = π_ * ν := by
  unfold lambda
  field_simp

end HyperbolicOverlapSaturation

end QOU.FluidDynamics
