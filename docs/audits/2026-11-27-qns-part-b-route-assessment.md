# q-NS Part B: non-Galerkin route assessment

Date: 2026-11-27. Bean `qou-innq` (wall: Part B by a non-Galerkin method).
Branch `claude/qns-part-b-route-2026-11-27`.
Lean: [`QOU/FluidDynamics/DSSTailMatching.lean`](../../folio/quantum-observable-universe/lean/QOU/FluidDynamics/DSSTailMatching.lean)
(sorry-free, no axioms, no empirical values).

**Source rule (owner, 2026-11-27):** *"i dont wnat to make use of any of the openAI announced work on NS.
keep it only what is fomalized in QOU."* Nothing below uses that work. The inputs are QOU blocks and
Lean, plus classical results the corpus already cites (Nečas–Růžička–Šverák, Tsai, Seregin, Chae,
Chae–Wolf) and standard special-function facts (DLMF ch. 13).

## 0. Summary

Part B (`conj:regularity-breakdown`, Part B; `def:leray-profile`) asks for a nonzero smooth backward
discretely self-similar (DSS) Leray profile `V(y, s)`, `P`-periodic in `s`, with `|V| ~ |y|⁻¹` and
`V(·, s) ∉ L³`. The Galerkin route is closed (scope a, owner 2026-11-22,
`docs/audits/2026-11-21-leray-dss-galerkin-search.md`).

| Route | Verdict | Tier |
|---|---|---|
| R1 Generalized Beltrami / Lamb-gradient ansatz (the R³ analogue of `prop:reeb-beltrami-regular-flow`) | **Closed for every profile in the decay class, steady or not.** The nonlinearity becomes a pressure gradient, and the linear Stokes–Leray system has no nonzero DSS profile in the decay class. | algebraic core Lean (§2, §3 of the file); sector analysis cited (DLMF 13.2, 13.7) |
| R2 Homogeneity reduction (`V` homogeneous of degree −1 in `y`) | **Closed.** Forces `∂_s V = 0`; what remains are the Landau solutions, singular at `y = 0`. | algebra (§3 below) |
| R3 QOU energy definitions (`def:q-energy`, `def:categorical-hamiltonian`, `def:mobius-energy`) | **No direct route.** They are knot / Reeb-clock functionals, and Navier–Stokes has no Lagrangian whose Legendre transform they could supply. The fluid replacement is the weighted Bernoulli flux identity (§4). | assessment |
| R4 **Tail matching + degree** (recommended) | **Open, and reduced to one named estimate.** Part B ⇔ a nonzero zero of `g(c) = A c + Q(c)` on log-phase tail data. Parity of the even part forces nonzero zeros in every finite truncation whose quadratic part has no real projective zero; existence for Part B is then equivalent to a priori bounds uniform in the truncation. | finite-dim core Lean (§1 of the file); reduction is a proof sketch |
| R5 Integer-spin symmetry reduction to a finite ODE | **Not recommended.** Without a truncation it is not finite; with one it is the closed Galerkin scheme. | assessment |

Owner card (2026-11-27): which route next. Recommendation (judgement): R4.

## 1. Corpus grep (what was checked)

- `docs/audits/`: `2026-11-21-leray-dss-galerkin-search.md` (dead end, five phases),
  `2026-07-18-q-ns-classical-gap-decomposition.md` (original wall list).
- `folio/.../fluid-dynamics/`: `regularity-breakdown`, `leray-profile`, `leray-profile-exclusions`,
  `leray-profile-construction`, `reeb-beltrami-regular-flow`, `helicity-physical`,
  `blowup-*` (three blocks). Energy blocks: `climax-volume-mass/q-energy*`, `mobius-energy`,
  `quantum-observable-universes/categorical-hamiltonian`.
- Lean: `DSSObstructions.lean` (L1–L5), `dss_escapes_nrs.lean`, `leray_profile.lean`,
  `BeltramiSteadyEuler.lean` (Lamb identity `lamb₁/₂/₃`), `physical_layer_leray.lean`.
- Beans (branch `cat/cat-harness/beans`): `qou-innq`; `qou-4670`, `qou-93hu` (critical-exponent
  carrier); no bean exists for items 3, 5 or 6 of `qou-innq` as separate work.
- Parent survey: `/mnt/project-files/qns-gaps-2026-11-27/briefs/attack-vectors-2026-11-27.md`.

No prior route assessment beyond Galerkin was found. Nothing in the corpus states the Lamb-gradient
exclusion, the Bernoulli flux identity or the parity mechanism below.

## 2. R1: Lamb-gradient profiles are trivial

**Proposition (proof sketch; algebraic steps in Lean).** Let `V` be a smooth DSS profile in the decay
class, with `|∇V| = O(|y|⁻²)`. If its Lamb vector `V × curl V` is a gradient `∇φ` for every `s`
(this includes every Beltrami field, `curl V = f V` with `φ = 0`), then `V ≡ 0`.

1. *Nonlinearity is a gradient.* `(V·∇)V = ∇(|V|²/2) − V × curl V = ∇(|V|²/2 − φ)`
   (`adv_grad_of_lambGrad`, from `lamb₁/₂/₃`). Absorbing it into the pressure, `V` solves the linear
   Stokes–Leray system `∂_s V − ΔV + ½V + ½(y·∇)V + ∇Π' = 0` (ν = 1 after rescaling `y`).
2. *Vorticity.* `Ω = curl V` solves `∂_s Ω − ΔΩ + Ω + ½(y·∇)Ω = 0` and `|Ω| = O(|y|⁻²)`.
3. *Sectors.* Expand `Ω` in vector spherical harmonics of integer degree `l` (L1, `IntegerSpin`) and in
   `e^{iμs}`, `μ ∈ (2π/P)ℤ`. Writing a sector as `r^l g(z)`, `z = r²/4`, gives Kummer's equation
   `z g'' + (b − z) g' − a g = 0` with `a = (l+2)/2 + iμ`, `b = l + 3/2`.
4. *Connection coefficients.* The solution regular at `0` is `M(a, b, z) ~ Γ(b)/Γ(a) · e^z z^{a−b}`
   (DLMF 13.7.1): it grows like `e^{r²/4}`. The solution with the decay `z^{−a}` is `U(a, b, z)`, whose
   singular part at `0` is `Γ(b−1)/Γ(a) · z^{1−b}` (DLMF 13.2.42), i.e. `r^{−l−1}`. Both coefficients
   are nonzero for every `l` and `μ` (`growth_coeff_ne_zero`, `singular_coeff_ne_zero`, from
   `Re a > 0`). So no sector is both regular at `0` and `O(|y|⁻²)`: `Ω ≡ 0`.
5. *Conclusion.* `V` is curl-free and divergence-free, so `V = ∇h` with `h` harmonic and
   `|∇h| → 0`; by Liouville `V ≡ 0`.

Consequence: Beltrami-type families (survey vector V4, and the R³ analogue of the exact Reeb–Beltrami
solutions on `UT(Σ₄)`) cannot give Part B, steady or not. This sharpens the survey's "excluded if
steady" to all profiles. It is a (b)-scope exclusion of the *ansatz*, resting on the invariant
`Γ(a) ≠ 0` for `Re a > 0`; it does not exclude Beltrami components inside a profile whose Lamb vector
is not a gradient.

## 3. R2: homogeneity reduction

If `V(y, s) = |y|⁻¹ W(ŷ, s)`, then `(y·∇)V = −V`, so `½V + ½(y·∇)V = 0`. The remaining terms scale as
`|y|⁻³` except `∂_s V ~ |y|⁻¹`; matching powers forces `∂_s W = 0`, and `V` is a steady, (−1)-homogeneous
solution: a Landau solution, which is singular at `y = 0` (a point force). Excluded by smoothness. This
is why the admissible tail in the Galerkin search carries a log phase `|y|^{−1−2imω}` rather than a pure
power: the tail of a nonsteady profile is the final datum `v(·, T*)`, which is discretely (not
continuously) homogeneous.

## 4. R3: what the new energy definitions give

- `def:q-energy` and `def:mobius-energy` are functionals of knots/braids. A DSS profile's vortex lines
  are discretely scale-invariant, and the Möbius energy is scale-invariant, so each scale copy carries
  the same Möbius energy. That is a consistency remark, not a constraint: nothing in the corpus links a
  vortex-line knot energy to the Leray system.
- `def:categorical-hamiltonian` is a Legendre transform along the Reeb clock of a Lagrangian `L_q`. The
  DSS time `s` is a periodic clock, but the Leray system is dissipative and has no Lagrangian whose
  clock polynomial would play the role of `L_clock`. The honest fluid analogue is the energy balance
  in the Gaussian weight `ρ = e^{−|y|²/4}`:

  ```
  d/ds ½‖V‖²_ρ = −‖∇V‖²_ρ − ½‖V‖²_ρ − ½ ∫ B (y·V) ρ dy,     B = |V|²/2 + Π.
  ```

  The drift term `½(y·∇)V` cancels exactly against the weight (`∇ρ = −(y/2)ρ`), and the cubic term
  survives only as the radial flux of the Bernoulli function `B`. Integrating over one period:

  **Bernoulli flux identity.** A nonzero DSS profile has
  `½ ∮∫ B (y·V) ρ dy ds = −∮ (‖∇V‖²_ρ + ½‖V‖²_ρ) ds < 0`.

  This is the abstract statement `flux_pos_of_ne_zero` with `A` the weighted Ornstein–Uhlenbeck part
  (strictly negative, spectrum `≤ −½`) and `Q` the projected nonlinearity. `eq_zero_of_conservative`
  says the converse in the abstract: any scheme in which the nonlinearity conserves the pairing in a
  norm where the linear part is dissipative has only the zero solution. **The Bernoulli flux is the
  necessary leak.** Survey vector V5 (fluid energy = `H_vel`) is a Part A question and depends on
  bean `qou-0nqs`; it is not used here.

## 5. R4: tail matching and the parity mechanism (recommended)

**Reformulation (proof sketch).** Split `V = T_c + W`, where `T_c` is the log-phase tail with
coefficients `c = (c_{l,m})` (the free data, one per sector) and `W` decays faster. In each sector the
linear analysis of §2 gives one *growth coefficient* that must vanish for `V` to stay in the decay class.
So Part B becomes: find `c ≠ 0` with `g(c) = 0`, where `g(c) = A c + Q(c)` has a linear part `A` that is
invertible (diagonal, entries built from `Γ(b)/Γ(a) ≠ 0`) and a quadratic part `Q` from the
nonlinearity. Linear invertibility alone gives only `c = 0`, which is §2 again.

**Parity (finite truncations).** Truncate to `n ≥ 2` coefficients. `Q` is even, `Q(−c) = Q(c)`. If `Q`
has no nonzero real zero, then on a large sphere `g` is homotopic to `Q` through nonvanishing maps, so
`deg(g, B_R, 0) = deg(Q/|Q|)`, the degree of an even map `S^{n−1} → S^{n−1}`, which is even. The zero
at `c = 0` has index `sign det A = ±1`, which is odd. So `g` has nonzero zeros of total index odd.
(Brouwer degree; not in Mathlib, so this step is cited, not formalized.)

**What this explains.** The Galerkin search found nonzero steady and periodic solutions at every
truncation that vanished or jumped under refinement (§§5–6 of the Galerkin audit). The parity argument
predicts exactly that: truncation-level zeros exist for a topological reason, whatever the true
problem does. **Not verified on the Galerkin truncations:** it needs a check that their quadratic parts
have no real projective zero. That is a finite computation on the existing seeds.

**The open step, named.** Passing to the limit needs bounds on the nonzero zeros uniform in the
truncation (a Leray–Schauder setting). The §2 and §4 results constrain where such bounds can come
from: they cannot come from an energy that the nonlinearity conserves, and they must be compatible with
a negative weighted Bernoulli flux. That estimate is the whole difficulty of Part B and is not claimed.

**Lean scaffold.** `DSSTailMatching.lean` §1 states the finite-dimensional energy dichotomy, with a
non-vacuity witness. A statement of Part B in matching form (`∃ c ≠ 0, g c = 0` for the
infinite-dimensional `g`) needs the sector expansion and Kummer functions, neither in Mathlib; it is
left as prose rather than encoded as a hypothesis class.

## 6. Items 3, 5, 6 of `qou-innq`

- **Item 3 (Levi branch value β).** The survey (§0d) found branch (A) of `conj:levi-degeneracy`
  withdrawn on 2026-11-15 (`qou-fm7s`), so the item may have no subject. A bean records the check.
- **Item 5 (true α from the q-NS spectrum).** `p2-critical-exponent` gives two closure-dependent
  heuristic values (1 and 4/3) and `q_turbulence_spectrum.lean` keeps 8 sorries. Depends on the Part A
  layer ruling (survey §0b). A bean records it.
- **Item 6 (DSS singular set within CKN parabolic dimension ≤ 1).** Under the scale-critical bound of
  Chae–Wolf 2016 a DSS blow-up has a single singular point, parabolic dimension 0. Without that bound it
  is open. A bean records the remaining case.

## 7. What this note does not show

It does not show that Part B is false or true. The §2 exclusion is of the Lamb-gradient ansatz only.
The §5 reformulation is a proof sketch whose analytic steps (sector expansion, compactness of the
nonlinear map in the chosen space) are not written out here.
