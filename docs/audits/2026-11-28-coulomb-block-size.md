# The Coulomb pair weight's size law from the strand count (gap G3)

Date: 2026-11-28. Bean `qou-tcl3`. Follows PR #9854 (μ = 1 − αh², a contact factor with no size).
Lean: `QOU/Nuclear/CoulombBlockSize.lean` (any field, sorry-free).
Probe: `computations/probes/coulomb_ring_mu/coulomb_ring_mu_probe.py` (size-law block added).

## 1. Result

Two named hypotheses fix the exponent and leave one scale.

* **(H1) Homogeneity.** The Coulomb pair energy has degree −1 under dilation: `ε·L = κ`.
  This is the dilation law PR #9699 proves for the shape factor.
* **(H2) Volume additive in strands.** A block of `3A` strands has `L³ = A·v`, one cell per
  nucleon. This is the Freedman–He `Vol^{−1/3}` reading of the 2026-08-01 EM-linking audit.

Then `ε³·A·v = κ³` (`size_law`). Across blocks, `ε₁³A₁ = ε₂³A₂` (`size_ratio`), and in mirror
form `(2Δ₁/(A₁−1))³A₁ = (2Δ₂/(A₂−1))³A₂` (`size_ratio_mirror`). No cube root is taken, so the
statement is algebraic. Nothing is fitted: the exponent is −1/3 and no other exponent was tried.

## 2. Test of the exponent (comparison only, AME mirror splits from the #9691 table)

| quantity over the 8 mirror pairs, A = 3 to 41 | max/min |
|---|---|
| `ε` needed `= 2ΔB/(A−1)` (contact, exponent 0) | 2.099 |
| `ε·A^{1/3}` (size law, exponent −1/3) | 1.244 |

The size law removes most of the A dependence. The remaining 24 % spread is the same size as
the shape change at A = 5 that PR #9699 recorded (the ball against the q-Hankel factor, a jump of
1.119), so it is not evidence against (H2) yet.

## 3. The scale that is left

`κ³/v` is one length. The mean `ε·A^{1/3}` is 1.187 MeV, about 940 times the vertex-pair
`ε_U(μ₁) = 1.262 keV`. So the contact factor μ does not supply the scale either. Fixing `κ³/v`
is exactly the energy-to-length map of bean `qou-mbfv` (candidate `r = D·ħc/M`, PR #9717), which
still needs a derived three-nucleon gap `E₁(A = 3)`.

## 4. Status

* Derived: ranks 0, 1, 2 and their ratios (#9691); the ring form for every reading (#9839);
  the ring factor's shape (#9854); the exponent −1/3 under (H1), (H2) (this note).
* Open: one length, `κ³/v`, shared with `qou-mbfv`. Nothing is wired.

Scope (a). No measured value is in any proof.
