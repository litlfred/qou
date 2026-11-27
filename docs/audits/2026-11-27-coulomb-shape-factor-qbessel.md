# Coulomb shape factor from the q-Hankel (Hahn–Exton) state — bean qou-usft, shape half

Date: 2026-11-27. Probe: `computations/probes/coulomb_shape_factor_qbessel_probe.py`
(pre-registered in its own commit before the first run at q₀). Witness:
`computations/probes/coulomb-shape-factor-qbessel-probe.witness.json`. Scope (a): not wired to
`coulomb_energy.py` or the scorecard.

## What is computed

A scale-free shape factor `f` defined by `E_C = f · Q² / r_rms`. No radius is produced:
E_q(2) has a `q^ℤ` dilation symmetry, so only the product `E_C · r_rms` is meaningful.

## The state, and why it is forced

* Arena: the SU_q(2) → E_q(2) contraction with Hahn–Exton q-Bessel functions at real q₀ > 1,
  as already settled for the keystone (`KeystoneQBesselRadialTarget.lean`). Written with
  `p = 1/q₀`, functions `J_ν(·; p²)` (Koelink's E_q(2) convention, the same q² base as the
  Haar moments `[k+1]_{q²}`).
* Koelink–Swarttouw q-Hankel orthogonality on the **full** Jackson lattice `p^ℤ`:
  `Σ_k p^{2k} J_ν(p^{k+n}; p²) J_ν(p^{k+m}; p²) = p^{-2n} δ_{nm}`.
  Each `J_ν(p^n x; p²)` is therefore a normalisable radial state for the measure `x d_p x`,
  with no box, no boundary condition and no extra length. All `n` give the same density up to
  dilation, so `f` does not depend on `n`. The probe checks this orthogonality at q₀
  (norm 1 to 30 digits, overlaps < 1e-40). Classically (q = 1) no such normalisable state
  exists; this is a q-deformed object.
* `ν = l + ½ = ½`: Coulomb energy is a 3-D quantity, the ground channel is `l = 0`, and the 3-D
  radial density of an s-wave is `r |J_{1/2}(r)|² dr`.
* Density: shell charges `P_k ∝ p^{2k} J_{1/2}(p^k; p²)²` on spheres of radius `p^k`, `k ∈ ℤ`.
  Energy by exact concentric-shell electrostatics, `E = ½ Σ P_i P_j / max(r_i, r_j)`.
  No derivative convention is needed.

## Result

| construction | f |
|---|---|
| **primary: ν = ½, step 1/q₀** | **0.520011** |
| alt (a) ν = 0 (2-D E_q(2) channel used as 3-D) | 0.528300 |
| alt (b) ν = ½, step 1/q₀² | 0.516543 |
| alt (c) q-uniform ball (q-Neumann ground state) | 0.465383 |
| classical uniform ball (3/5 shape, shipped) | 0.464758 |
| classical Gaussian | 0.488603 |
| classical exponential density e^{-r/a} (5√3/16) | 0.541266 |
| classical box s-wave sin²(πr)/r² | 0.474801 |
| f that would close the ³He CDE with zero strong CSB (bean STEP 3) | 0.521413 |

Primary / uniform ball = 1.1189 (+11.9 %). Primary / required = 0.9973 (−0.27 %).

## How to read it (honest limits)

1. **The match to 0.5214 is not a sharp test of q₀.** The primary f is nearly flat in q:
   0.5234 (q = 1.03), 0.5224 (1.05), 0.5200 (q₀), 0.5168 (1.2), 0.5132 (1.5), 0.5193 (2).
   What the construction fixes is the *shape class* (more peaked than a Gaussian, less than an
   exponential); q₀ moves f by well under 1 % across 1.03–1.2. Whether f has a limit as
   q → 1 is not claimed; any such analytic statement belongs in `QOU/Transcendental/`.
2. **The convention spread is ±1.1 %** (alternates 0.5165–0.5283), about four times the
   distance to the required value. The primary was fixed in advance; the alternates were not
   selected.
3. **The "required f" inherits the bean's definition**: it uses the measured ³He charge radius
   (which includes nucleon size) and treats the whole mirror split as Coulomb. It is a
   comparison target, not an input; nothing in f depends on it.
4. **Correction to bean qou-usft RESULT 3 / STEP 3.** The row "exponential 0.454663" does not
   reproduce: an exponential density gives 5√3/16 = 0.541266. So the statement "the required
   f is above all classical shapes" is false; a classical exponential overshoots it. The
   q-Hankel state lands between Gaussian and exponential without any shape being chosen.
5. The q-uniform ball (alt c) moves the shipped 3/5 ball by only +0.13 % at q₀, so the
   q-deformation of the *measure* alone is small; the change comes from the *state*.

## What this does not do

* It gives no radius. `r_rms` still needs the open energy-scale map.
* It is not wired into `coulomb_energy.py`. Wiring it would replace the 3/5 ball with
  f = 0.520011 and needs an owner decision.
* No Lean file: no toolchain in this session. The natural formal statement (dilation
  invariance of `E · r_rms` for shell configurations, over a linear ordered field) is a
  follow-up.
