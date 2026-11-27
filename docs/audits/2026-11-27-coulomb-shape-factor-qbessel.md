# Coulomb shape factor from the q-Hankel (Hahn–Exton) state — bean qou-usft, shape half

Date: 2026-11-27. Probe: `computations/probes/coulomb_shape_factor_qbessel_probe.py`
(pre-registered in its own commit before the first run at q₀). Witness:
`computations/probes/coulomb-shape-factor-qbessel-probe.witness.json`. Lean:
`QOU/Nuclear/CoulombShellShapeFactor.lean` (sorry-free). Wired into `coulomb_energy.py` for
A ≤ 4 only (owner instruction 2026-11-27: "wire in what is derived. keep probes and options
documented"; "formalize first!"). See §Wiring.

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
* It gives no radius for the wired path either: `coulomb_energy.py` keeps the selected
  R = λ̄_π·A^{1/3} and uses r_rms = √(3/5)·R. That radius choice is the remaining
  selection (bean qou-usft, radius half).

## Lean

`folio/quantum-observable-universe/lean/QOU/Nuclear/CoulombShellShapeFactor.lean`, over a
linearly ordered field, lean-direct exit 0, axioms propext / Classical.choice / Quot.sound:

* `shellEnergy_dilate`, `shellMoment_dilate`: E(λr) = E/λ, M₂(λr) = λ²M₂.
* `shapeFactorSq_dilate`: f² = E²M₂/Q⁵ is invariant under every dilation λ > 0.
* `shapeFactorSq_charge_scale`: invariant under rescaling the charges (normalisation drops out).
* `shapeFactorSq_lattice_shift`: on r_k = p^k, the shift p^{k+n} gives the same f² — every
  dilate of the q-Hankel state has the same f.
* `shapeFactorSq_single_shell`: one shell has f² = 1/4 (non-vacuity).

The probe now also evaluates the literal Lean double sum and asserts it equals the cumulative
form used for speed (|Δf| = 7.8e-62). The value 0.520011 itself is computed, not proved; the
q-Hankel orthogonality is cited (Koelink–Swarttouw), not formalised.

## Wiring (A ≤ 4 only) and options kept

`coulomb_energy.shape_factor(A, shape=...)`:

| option | meaning | used by default for |
|---|---|---|
| `"derived"` (default) | q-Hankel f for A ≤ 4, uniform ball for A ≥ 5 | everything |
| `"uniform_ball"` | classical √(3/5)·(3/5) ≈ 0.4648 in f units | the old behaviour, byte-identical |
| `"qhankel"` | q-Hankel f at every A | comparison only |

Why A ≤ 4: the derivation assumes one s-wave state (ν = 1/2); at A ≤ 4 every nucleon is in 0s.
At A ≥ 5 the p shell is occupied and the single-state form is outside its own hypothesis, so
the classical ball stays there, labelled as a classical import. Extending it to the shell model
is a separate derivation.

## What the wiring does to the consumers (measured, honest)

The derived f is larger than the ball's, and the selected radius is unchanged, so every A ≤ 4
Coulomb energy rises by 11.9 %:

| quantity | ball (old) | derived (new) |
|---|---|---|
| E_C(Z=2, A=3) MeV | 0.8474 | 0.9482 |
| E_C(Z=2, A=4) MeV | 0.7699 | 0.8615 |
| ³H/³He: ΔB_AME / ΔE_C | 0.901 | 0.806 |
| `coulomb-mirror-killswitch` worst-case mirror error | 17 % | 24 % |
| `binding-wn-kernel` `csb_A3_mirror_residual` | 0.0098 | 0.0215 |

So at A = 3 the derived shape makes the mirror split **worse**. The old 0.901 came from a
selected radius together with an imported 3/5, and those two partly cancelled. Removing one
import removes the cancellation. This is information about the radius, not a reason to keep
the ball. The killswitch assertion
`derived_coulomb_reproduces_every_mirror_split_within_nolen_schiffer_scale` (threshold 20 %)
will fail when that probe is next run. It is left as is and must not be relaxed.

`mirror_split_continuum_em_probe.py` builds its own prediction from the 3/5 uniform-sphere form,
and its rescale cross-check compared that against the canonical path. It now asks for
`shape="uniform_ball"` explicitly, so it still compares like with like. Its payload is unchanged.

Consumer witnesses were **not** regenerated in this PR. The container's environment was degraded
(mpmath pinned to 1.3.0 by sympy, no `pyhecke_native`), and one regeneration truncated
`canonical-isotope-witness-index` (z_max 118 → 20). Under the fast-merge ruling, they are
refreshed after the merge: the 17 `coulomb_energy` consumers. The figures above were measured
with a re-run in this container and are not committed numbers.
