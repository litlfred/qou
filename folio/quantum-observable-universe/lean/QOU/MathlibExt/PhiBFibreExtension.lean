import QOU.MathlibExt.FaddeevQuantumDilogarithm
import QOU.MathlibExt.FaddeevPhiBRealIntegral

/-!
# The def↔contour identification as an honest conjecture class (G1 remainder)

The last analytic gap of the fibre-branch `Φ_b` construction: the constructed
real-integral `phiB` (`QOU.MathlibExt.FaddeevPhiBRealIntegral`) is numerically
pinned to the Faddeev contour integral to `8e-29`, but the identification has
had no Lean shape — the contour integral itself is outside Mathlib's reach.

This file gives the identification its honest §3b form **without** the
contour: the open claim is that `phiB b` is the restriction to the real axis
of a full `Φ : ℂ → ℂ` satisfying the two modular-double shift equations
(`FaddeevPhi`).  Those functional equations characterize the contour integral
up to the pentagon/Faddeev–Volkov rigidity (see
`QOU.QBeta.CyclicDilogPentagon.faddeevPhi_unique_of_pentagon` for the
uniqueness lever on the finite fibre analog), so the class carries exactly the
def↔contour content that IS statable.  **No instance** — inhabiting it
requires the analytic continuation of the real integral, which is the open
input; the `8e-29` pin stays numerical evidence in
`computations/qbeta/qbeta_phi_b_real_form_pin.py`, never a Lean claim.

The derived theorems show the class is rigid rather than decorative: any
extension is pinned by the constructed `phiB` on the real axis AND on the
`ib`-shifted lattice lines (via quasi-periodicity), and it can never vanish on
the real axis (unimodularity of the constructed phase) — so the zero lattice
of a genuine extension is strictly off-axis, matching the known analytic
structure of the Faddeev integral.

-- Ref: [faddeev1995] Faddeev, Lett. Math. Phys. 34 (1995) 249. https://doi.org/10.1007/BF01872779
-- Ref: [leitner2026] conj:algebraic-geometric-dilog-equivalence; docs/audits/2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md §G1
-/

namespace QOU.MathlibExt

open QOU.MathlibExt.FaddeevQuantumDilogarithm
open QOU.MathlibExt.FaddeevPhiBRealIntegral

/-- **The def↔contour identification (§3b conjecture class).**  The
    constructed real-integral `phiB b` extends to a full Faddeev `Φ_b` on the
    fibre branch: a function `Φ : ℂ → ℂ` that (i) restricts to `phiB b` on
    the real axis and (ii) satisfies the two modular-double shift equations.
    The open content is the analytic continuation; no instance is fabricated.
    (`0 < b` puts the real `b` in `FaddeevPhi`'s `Re b > 0` scope.) -/
-- Ref: [leitner2026] docs/audits/2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md §G1
class PhiBFibreExtension (b : ℝ) where
  /-- The extension. -/
  Φ : ℂ → ℂ
  /-- (i) It restricts to the constructed real integral on the real axis. -/
  extends_phiB : ∀ x : ℝ, Φ (x : ℂ) = phiB b x
  /-- (ii) It satisfies the Faddeev modular-double shift equations. -/
  faddeev : FaddeevPhi (b : ℂ) Φ

variable {b : ℝ}

/-- **Off-axis bridge (derived).**  Quasi-periodicity pins the extension on
    the `+ib`-shifted line in terms of the CONSTRUCTED `phiB` values on the
    real axis: the identification is rigid along the `b`-lattice, not free. -/
theorem offAxis_bridge [hext : PhiBFibreExtension b] (x : ℝ) :
    phiB b x
      = (1 + Complex.exp (Complex.I * (Real.pi : ℂ) * ((b : ℂ)) ^ 2)
          * Complex.exp (2 * (Real.pi : ℂ) * (b : ℂ) * (x : ℂ)))
        * hext.Φ ((x : ℂ) + Complex.I * (b : ℂ)) := by
  haveI := hext.faddeev
  rw [← hext.extends_phiB x]
  exact phi_b_quasiperiod (x : ℂ)

/-- **No zeros on the real axis (derived).**  The constructed `phiB` is a
    unimodular phase, so any extension is nonvanishing on `ℝ` — the zero
    lattice of a genuine Faddeev extension is strictly off-axis. -/
theorem extension_ne_zero_on_axis [hext : PhiBFibreExtension b] (x : ℝ) :
    hext.Φ (x : ℂ) ≠ 0 := by
  rw [hext.extends_phiB x]
  intro h0
  have h1 := norm_phiB b x
  rw [h0] at h1
  simp at h1

/-- **σ-unitarity transfers to the axis values of any extension (derived).** -/
theorem extension_mul_conj_on_axis [hext : PhiBFibreExtension b] (x : ℝ) :
    hext.Φ (x : ℂ) * (starRingEnd ℂ) (hext.Φ (x : ℂ)) = 1 := by
  rw [hext.extends_phiB x]
  exact phiB_mul_conj b x

end QOU.MathlibExt
