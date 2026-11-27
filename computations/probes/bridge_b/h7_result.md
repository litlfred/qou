# H7 result: forms for a Stokes boundary, and the M_QED wall term (2026-11-21)

Pre-registration: `h7_preregistration.md`.

## Part A: connection forms

Paths searched: content `.md` (connection forms, Ω¹, 2-form, crossed module), Lean `QOU/Mathlib`, open
PRs, and `git log` on main since 2026-11-19.

**What exists now.** As of today (`3da1ce17041`, `fdb67a01f15`, beans `qou-ghc6`/`qou-ewc4`/`qou-jvua`)
the corpus has *generic* Lie-valued forms:
- `QOU/Mathlib/LieValuedForms.lean`: `OneForm`, `TwoForm`, curvature `dα + ½[α∧α]`, and `covExtDeriv`
  on a real normed space;
- `ManifoldForms.lean`: a global `d` on manifold forms, with `d∘d = 0`.

`NonAbelianStokes.lean` is rewired onto these forms. So bean `qou-20bk`'s "no forms at all" is now
stale for the infrastructure.

**What does not exist.**
- No *specific* α, β is defined anywhere: no form whose integral is the braid trace or carries a wall.
- Stokes itself is still a §3b-cond class (`MI₁(α; ∂σ) = MI₂(α, F_α; σ)` is assumed).
- Its only model is the degenerate `punitInstance`, where all integrals are 1.
- `cellBoundary σ` is the boundary of a 2-cell. Nothing places a type-B wall on it.
- `braidSurfaceMultTrace z n = z^n` sees only the braid's length.
- The connection 1-form on `O(SU(2))` (`connection-su2.md`) is a noncommutative-calculus object. It
  does not enter the Stokes class.

**Correction (2026-11-21, after the user's note "There is a categorical connection").** The search
above covered the Lean and differential-form side only. The corpus does define a connection at the
categorical layer:
- `def:categorical-connection`: a morphism `∇ : A → A ⊗ Ω¹(A)` satisfying Leibniz, with curvature `∇²`;
- `def:categorical-q-connection`: `∇_q = q⁻¹∇ + (1 − q⁻¹)(ι_ξ∇)ϴ_A`;
- the categorical action is `tr(ℒ_q) = ev ∘ (id ⊗ ℒ_q) ∘ coev`, unique up to one scalar λ.

That trace is a **closed** rigid-duality trace, so it has no boundary term by construction. A wall
would replace `ev`/`coev` at one end by a boundary (module-category) datum, and the corpus does not
define one. The coefficient `(1 − q⁻¹)` is derived, but it weighs the Reeb direction in the bulk, not
a boundary.

**Verdict A: no hit.** Criterion 1 (forms) is met only generically. Criteria 2 and 3 (a wall as a
boundary, and a fixed coefficient) are not met. This is "not found in these paths", not "impossible".
What would change it is a specific connection on a specific surface that the corpus names.

## Part B: the M_QED wall term

**Rule received during the work** (coordinator relay of the user's card): virtual photons do not
exist in QOU. Exchange, including any M_QED wall term, must be modelled as prior entangled photons or
unseen intermediary emitters. That changes how the two computations below are read.

### B1. Carried all-pairs insertion (the reading in PR #8743)

`h7_ruled_qed_wall_check.py`, exact. The insertion `C = Σ_{a<b} Q_a Q_b`, with each strand's charge
carried along the strand, has these properties:
- it is diagonal;
- it is constant on each weight space: `(Y+1)(3Y−1)/4` on the proton space and `(Y−1)(3Y+1)/4` on the
  neutron space;
- so it factors out of every restricted trace, with or without the wall.

So the wall adds nothing to M_QED. It only multiplies the M_QCD wall trace, and `C(n) − C(p) = −Y`
for every `q`, with or without the wall.
- [conditional on Y = 1/3] p: 0, n: −1/3. This agrees with #8743.
- The connected part is 0.

### B2. Slot-averaged exchange functional (EM1), comparison only

`h7_qed_wall_probe.py`, exact in `q, s = x+y, p = xy, Y`. Results:
- the wall eigenvalues cancel;
- the result is the same for all 7 insertion points;
- the difference is `E_wall(n) − E_wall(p) = −2Y` at `q = 1`, and `Y²` cancels from it;
- [conditional on Y = 1/3] at `q₀`: −0.659575 with the wall, against −0.666393 for bulk EM1.

**This functional models exchange between two time slots, which is a virtual-photon reading. Under
the rule above it is not admissible.** It is kept only as a comparison arm.

### B3. The admissible form: real photons in the word

The admissible M_QED with a wall is a word whose photons are real `γ(φ)` letters: prior entangled
γγ pairs, or emitted photons. H5 §6 already computed `γ(φ)γ(φ′)` with a wall. The ratio there depends
on the photon parameters and on the insertion point. So no fixed number appears.

## H7 verdict

No hit. No forms-based boundary fixes ε. On the M_QED side:
- the carried all-pairs insertion is blind to the wall (it gives −Y regardless);
- the exchange functional is ruled out as virtual.

The size of a derived n − p splitting is still open. Scope (a).
