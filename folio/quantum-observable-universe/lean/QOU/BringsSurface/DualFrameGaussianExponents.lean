/-
# Dual-frame Gaussian exponent identities — the exact algebraic core of
# the (REP) kernel family's one-Gaussian structure

The KSel-3 modular-double audit
(`docs/audits/2026-08-01-ksel3-modular-double-covariance.md` §2) proved
two sympy-exact identities that carry the entire "one Gaussian in dual
frames" structure of the balanced-kernel continuum:

* **M1 (lattice-Gaussian completion of the square).** With kernel-base
  log `L = ln q̃`, translate log `uln = ln u`, lattice point
  `t_j = uln + j·L`, center `μ̂ = −L/2` and variance `σ² = L`, the
  atomic B-factor mass exponent is the sampled Gaussian:
  `−(t_j − μ̂)²/(2L) = −L·j(j+1)/2 − j·uln − (uln + L/2)²/(2L)` — the
  `j`-dependence is exactly the atomic mass exponent, the `j`-free
  remainder is the translate-dependent constant `C(u)`. Hence every
  member of the `u`-continuum is a lattice sampling of the SAME
  Gaussian, which is the a.c. log-normal B-factor.
* **M2 (dual-mode moment shift).** For the `m`-th Poisson dual mode the
  complex shift is `z = k + d` with `d·L = 2πi m`; the Gaussian
  exponential-moment exponent splits EXACTLY as
  `z·μ̂ + z²L/2 = L·k(k−1)/2 + (d·μ̂ + d²L/2) + k·(d·L)`:
  a mode-independent moment ladder `L·k(k−1)/2`, a `k`-independent
  mode mass, and the integer cross term `k·d·L = 2πi mk` (killed by
  `e^{2πimk} = 1` at the exponential level). Mechanism: `σ² = L`, the
  variance equals the lattice step. Consequence: every dual mode
  carries the same normalized moment ladder — the balanced moment
  functional is blind to the whole dual-mode sector, which is the
  (REP) indeterminacy continuum.

This module proves both identities sorry-free over a generic field
with `2 ≠ 0` (the identities divide by 2, so characteristic 2 is
honestly excluded; §7c: the identities are polynomial/rational in the
exponent data; no archimedean input — `exp`, reality and positivity of dual coefficients
stay wall-side and are NOT formalized here, per the audit's honest gap
list).

-- Ref: [leitner2026] docs/audits/2026-08-01-ksel3-modular-double-covariance.md §2;
--      docs/audits/2026-08-01-rep-jackson-identification.md §3;
--      predicted-spectra, conj:schwinger-measure-computational-time.
-/

import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.AlgebraicSubstrate.DualFrameGaussianExponents

variable {K : Type*} [Field K]

/-- **M1 — lattice-Gaussian completion of the square.** The Gaussian
exponent at the lattice point `t_j = uln + j·L`, with center
`μ̂ = −L/2` and variance `σ² = L`, equals the atomic B-factor mass
exponent `−L·j(j+1)/2 − j·uln` plus the `j`-independent translate
constant `−(uln + L/2)²/(2L)`. This is the exact statement that the
whole `u`-translate atomic continuum samples ONE Gaussian — the a.c.
log-normal member. -/
theorem lattice_gaussian_complete_square (L uln j : K) (hL : L ≠ 0)
    (h2 : (2 : K) ≠ 0) :
    -((uln + j * L) - (-(L / 2))) ^ 2 / (2 * L)
      = (-(L * (j * (j + 1))) / 2 - j * uln)
        + (-(uln + L / 2) ^ 2 / (2 * L)) := by
  field_simp
  ring

/-- **M2 — dual-mode moment shift.** For the complex shift `z = k + d`
(`d` the dual-mode shift, `d·L = 2πi m` in the wall-side reading), the
Gaussian exponential-moment exponent with `μ̂ = −L/2`, `σ² = L` splits
exactly into (i) the mode-independent moment ladder `L·k(k−1)/2`,
(ii) the `k`-independent mode mass `d·μ̂ + d²L/2`, and (iii) the cross
term `k·(d·L)` — an integer multiple of `2πi` in the wall-side
reading, invisible to the exponential. The algebraic mechanism is
`variance = lattice step`. -/
theorem dual_mode_moment_shift (L k d : K) (h2 : (2 : K) ≠ 0) :
    (k + d) * (-(L / 2)) + (k + d) ^ 2 * L / 2
      = L * (k * (k - 1)) / 2 + (d * (-(L / 2)) + d ^ 2 * L / 2)
        + k * (d * L) := by
  field_simp
  ring

/-- **M1 restated on the mass side** (rearrangement of
`lattice_gaussian_complete_square`): the atomic mass exponent is the
sampled Gaussian minus the translate constant — the form used when
reading the continuum as samplings. -/
theorem atomic_mass_exponent_eq_sampled_gaussian (L uln j : K)
    (hL : L ≠ 0) (h2 : (2 : K) ≠ 0) :
    -(L * (j * (j + 1))) / 2 - j * uln
      = -((uln + j * L) - (-(L / 2))) ^ 2 / (2 * L)
        - (-(uln + L / 2) ^ 2 / (2 * L)) := by
  field_simp
  ring

end QOU.AlgebraicSubstrate.DualFrameGaussianExponents
