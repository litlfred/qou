import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

/-!
# QOU.Archimedean.eos_borromean_cfl

Canonical Lean declaration for content block at
[`quantum-observable-universe/observations/eos-borromean-cfl.ts`](quantum-observable-universe/observations/eos-borromean-cfl.ts).

The three manuscript sub-claims (the two-phase equations of state and
their stiffness ratio) relate **opaque physical quantities** (the
energy densities, pressures, chemical potential — derived from
many-body Fermi-gas physics, with no faithful Mathlib structure), so per
the vacuity-fix playbook pattern C the proposition is **named** as a
`def … : Prop` over the context — honestly recording the conditional
conjecture rather than projecting context fields.  The context class
carries the genuine *inputs*; a Lean instance would be the conjecture.
-/

namespace QOU.Archimedean


/-- Abstract context (inputs) for the `eos_borromean_cfl` claim — the
    substrate parameter, the two phase masses, the densities, pressures,
    gap and chemical potential.  No field asserts a conclusion. -/
class EosBorromeanCflContext where
  /-- Substrate parameter `q : ℝ`. -/
  q : ℝ
  /-- Borromean baryon mass. -/
  M_B : ℝ
  /-- CFL effective quark mass. -/
  M_D : ℝ
  /-- Baryon number density `n_B`. -/
  n_B : ℝ
  /-- The Borromean-phase energy density `ε_B(n_B)`. -/
  ε_B : ℝ
  /-- The Borromean-phase pressure `P_B(n_B)`. -/
  P_B : ℝ
  /-- The CFL-phase energy density `ε_D(n_B)`. -/
  ε_D : ℝ
  /-- The CFL-phase pressure `P_D(n_B)`. -/
  P_D : ℝ
  /-- CFL gap `Δ_CFL = q + q⁻¹`. -/
  Δ_CFL : ℝ
  /-- Substrate `ℏ_q = (q − 1)/q`. -/
  hbar_q : ℝ
  /-- Quark chemical potential `μ_q`. -/
  μ_q : ℝ

/-- **Manuscript statement** (full body):

**Proposition.**
Let $q > 1$ be the substrate parameter, $\hbar_q = (q-1)/q$,
and $V_B = 7.32772$ the Borromean volume.  The two topological
phases of dense quark matter have distinct equations of state:

**1. Borromean phase** (confined hadronic matter, $\rho < \rho_c$).

The baryon mass is $M_B = V_B / \hbar_q^2$.  For a cold,
degenerate Fermi gas of baryons at number density $n_B$, the
energy density and pressure are

$$
  \varepsilon_B(n_B)
  = 
  M_B  n_B
  + 
  \frac{3}{5}
  \frac{\hbar_q^2(3\pi^2)^{2/3}}{2M_B}
   n_B^{5/3},
$$

$$
  P_B(n_B)
  = 
  \frac{\hbar_q^2(3\pi^2)^{2/3}}{5M_B}
   n_B^{5/3}.
$$

The speed of sound in the Borromean phase is

$$
  c_{s,B}^2
  = 
  \frac{dP_B}{d\varepsilon_B}
  = 
  \frac{2}{3}
  \frac{E_F}{M_B + E_F}
$$

where $E_F = \hbar_q^2(3\pi^2 n_B)^{2/3} / (2M_B)$ is the
Fermi energy.  Since $M_B \gg E_F$ at nuclear densities:
$c_{s,B}^2 \ll 1$ (non-relativistic regime).

**2. CFL phase** (color superconducting, $\rho > \rho_c$).

The effective quark mass is $M_D = \frac{1}{3}(q + q^{-1})$
(crossing energy per quark, no volume contribution since
$\mathrm{Vol}(\mathcal{L}_H) = 0$).  For a degenerate quark
Fermi gas at quark number density $n_q = 3 n_B$, the energy
density includes the CFL gap contribution:

$$
  \varepsilon_D(n_B)
  = 
  3M_D n_B
  + 
  \frac{3}{5}
  \frac{\hbar_q^2(3\pi^2)^{2/3}}{2M_D}
   (3 n_B)^{5/3}
  - 
  \frac{3\Delta_{\mathrm{CFL}}^2 \mu_q^2}{\pi^2},
$$

$$
  P_D(n_B)
  = 
  \frac{\hbar_q^2(3\pi^2)^{2/3}}{5M_D}
   (3 n_B)^{5/3}
  + 
  \frac{3\Delta_{\mathrm{CFL}}^2 \mu_q^2}{\pi^2},
$$

where $\mu_q = \hbar_q(3\pi^2 n_q)^{1/3}/(2M_D)^{1/2}$ is
the quark chemical potential and
$\Delta_{\mathrm{CFL}} = q + q^{-1}$ is the gap
([Hopf diquark](#def:hopf-diquark)).

**3. Stiffness ratio.**  The ratio of pressures at equal baryon
density is

$$
  \frac{P_D}{P_B}
  = 
  \frac{M_B}{M_D} \cdot 3^{5/3}
  + 
  \frac{3\Delta_{\mathrm{CFL}}^2 \mu_q^2}{\pi^2 P_B}.
$$

The first term gives the dominant contribution.  At
$q =

[…truncated; see manuscript for remainder…]

    The proposition is **named** below as a `def … : Prop` (pattern C):
    the energy densities, pressures and chemical potential are opaque
    many-body inputs, so the three-part EOS claim is recorded as the
    conditional conjecture over the context rather than discharged by a
    fake projection. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/eos-borromean-cfl.ts
def eos_borromean_cfl (ctx : EosBorromeanCflContext) : Prop :=
  (ctx.ε_B = ctx.M_B * ctx.n_B +
    (3 / 5) * (ctx.hbar_q ^ 2 * (3 * Real.pi ^ 2) ^ ((2 : ℝ) / 3) /
      (2 * ctx.M_B)) * ctx.n_B ^ ((5 : ℝ) / 3) ∧
   ctx.P_B = (ctx.hbar_q ^ 2 * (3 * Real.pi ^ 2) ^ ((2 : ℝ) / 3) /
      (5 * ctx.M_B)) * ctx.n_B ^ ((5 : ℝ) / 3)) ∧
  ctx.P_D = (ctx.hbar_q ^ 2 * (3 * Real.pi ^ 2) ^ ((2 : ℝ) / 3) /
    (5 * ctx.M_D)) * (3 * ctx.n_B) ^ ((5 : ℝ) / 3) +
    3 * ctx.Δ_CFL ^ 2 * ctx.μ_q ^ 2 / Real.pi ^ 2 ∧
  ctx.P_D / ctx.P_B = (ctx.M_B / ctx.M_D) * (3 : ℝ) ^ ((5 : ℝ) / 3) +
    3 * ctx.Δ_CFL ^ 2 * ctx.μ_q ^ 2 / (Real.pi ^ 2 * ctx.P_B)

end QOU.Archimedean
