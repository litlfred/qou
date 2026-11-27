import QOU.FluidDynamics.DSSObstructions

/-!
# QOU.FluidDynamics.RegularityBreakdown

LaTeX label: `conj:regularity-breakdown`

## Rewritten 2026-11-21 (issue #8864)

The class previously carried five fields: enstrophy blow-up, a vortex sheet of
spatial Hausdorff dimension `2`, and a non-steady periodic profile with period
"set by the root-of-unity scaling `λ_κ`". Three changes, each backed by a
lemma in `QOU.FluidDynamics.DSSObstructions`:

* **Enstrophy blow-up is no longer a field.** It is *derived*
  (`RegularityBreakdown.enstrophy_blowup`) from the periodic, nonzero profile
  enstrophy by `lerayEnstrophy_blowup` (L3). It was a consequence, not a
  separate conjecture.
* **The `sheetDim = 2` field is removed.** A discretely self-similar blow-up
  has a single singular point (Chae–Wolf, arXiv:1610.09464), and
  `conj:ns-counterexample` states `d_H = 1`. The `.md` no longer asserts a
  vortex sheet.
* **The period is not tied to `λ_κ`.** `q_κ = exp(iπ/κ)` is a root of unity
  (`qKappa_is_root_of_unity`, L2), which `def:substrate-parameter` excludes.
  The period `P` is a free positive parameter.

## What the class does and does not encode

The class records only the profile-level shape of Part B of the `.md`: the
enstrophy `E(s) = ‖∇_y V(·, s)‖²` of the rescaled profile is `P`-periodic and
positive somewhere. It does **not** encode that `V` solves the Leray (Navier–
Stokes) equations; that is not formalised. Consequently the class is satisfied
by functions that have nothing to do with fluids (any positive constant `E`),
and assuming it is weaker than assuming the conjecture. It is kept as a carrier
because the derivation below is the content: once a DSS profile exists,
enstrophy blow-up follows with no further input.

No instance for an actual Navier–Stokes solution is supplied; the conjecture
is open.

## References
- [leitner2026] §Regularity breakdown, `conj:regularity-breakdown`
- Leray, Acta Math. 63 (1934) (`leray1934`)
- Chae–Wolf, arXiv:1610.09464 (`chae-wolf2016dss`)
-/

namespace QOU.FluidDynamics

open QOU.FluidDynamics.DSSObstructions

/-- **Conjecture carrier** for `conj:regularity-breakdown`, Part B, at the
    level of the profile enstrophy.

    `E s` is the enstrophy `‖∇_y V(·, s)‖²` of the Leray profile at similarity
    time `s = -log(T - t)`; `T` is the blow-up time and `P` the `s`-period. -/
class RegularityBreakdown (E : ℝ → ℝ) (T P : ℝ) : Prop where
  /-- The period is a genuine positive period. No value is asserted. -/
  period_pos : 0 < P
  /-- **Discrete self-similarity**: the profile enstrophy is `P`-periodic. -/
  profile_periodic : Function.Periodic E P
  /-- **Nontriviality**: the profile is not identically zero, so its
      enstrophy is positive at some similarity time. -/
  profile_nonzero : ∃ s, 0 < E s

/-- **Enstrophy blow-up, derived.** Under the carrier, the physical enstrophy
    `(T - t)^{-1/2} E(-log(T - t))` exceeds every bound arbitrarily close to
    `T` from below. This was clause 1 of the old statement; it is a
    consequence of clause 3 (L3). -/
theorem RegularityBreakdown.enstrophy_blowup {E : ℝ → ℝ} {T P : ℝ}
    [h : RegularityBreakdown E T P] :
    ∀ M ε : ℝ, 0 < ε → ∃ t, T - ε < t ∧ t < T ∧ M < lerayEnstrophy E T t := by
  obtain ⟨s₀, hs₀⟩ := h.profile_nonzero
  exact lerayEnstrophy_blowup h.period_pos h.profile_periodic hs₀ T

/-! ### Each field can fail -/

/-- An identically zero profile refutes `profile_nonzero`. -/
example : ¬ RegularityBreakdown (fun _ => 0) 1 1 := by
  rintro ⟨-, -, s, hs⟩
  exact lt_irrefl _ hs

/-- A non-periodic enstrophy (`E s = s`) refutes `profile_periodic`. -/
example : ¬ RegularityBreakdown (fun s => s) 1 1 := by
  rintro ⟨-, hper, -⟩
  have := hper 0
  norm_num at this

/-- A non-positive period refutes `period_pos`. -/
example : ¬ RegularityBreakdown (fun _ => 1) 1 0 := by
  rintro ⟨hP, -, -⟩
  exact lt_irrefl _ hP

end QOU.FluidDynamics
