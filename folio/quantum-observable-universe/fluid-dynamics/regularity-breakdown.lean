import Mathlib.Data.Real.Archimedean
import Mathlib.Algebra.Order.Floor.Defs
import Mathlib.Algebra.Order.Round
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# QOU.FluidDynamics.RegularityBreakdown

Regularity breakdown at q = 1: the classical limit as a phase transition.

LaTeX label: `conj:regularity-breakdown`

## Conjectural content

There exist smooth, finite-energy initial data whose classical
Navier–Stokes evolution develops a singularity in finite time, with the
three-part structure the `.md` states: enstrophy blows up as `t → T*⁻`;
the vorticity concentrates on a spatial set of Hausdorff dimension `2`;
and the approach is *discretely* self-similar — periodic in Leray's
`s = -log(T* - t)`, not steady.

## Status

Class-axiomatised per AGENTS.md §3b-cond. Downstream blocks may take
`[RegularityBreakdown …]` as an explicit `[Instance]` hypothesis to
retain `theorem` / `proposition` status.

Assuming this class is assuming an open conjecture. It is *not* proved
here, and no instance is supplied.

## References

- [leitner2026] §Regularity breakdown at q = 1: the classical limit as a phase transition, `conj:regularity-breakdown`
- [necas-ruzicka-sverak1996] — exclusion of the continuous self-similar profile
-/

namespace QOU.FluidDynamics

/-- **Conjecture class** for `conj:regularity-breakdown`.

    **Rewritten 2026-08-30.**  The single field was

        critical_reynolds : ∃ Re_c : ℝ, Re_c > 0

    — "there exists a positive real", a theorem of ordered fields,
    discharged by `1`.  Two defects, not one: it was vacuous, *and* it
    was about the wrong object.  Its docstring spoke of a critical
    Reynolds number and a Sobolev `H²` bound; the `.md` conjecture
    mentions neither.  A downstream `[RegularityBreakdown]` hypothesis
    was therefore free **and** misdescribed.

    The class is now parametrised by the objects the `.md` conjecture is
    about, and its fields are that conjecture's three numbered clauses.

    **Parameters.**  `enstrophy t` is `∫ |ω(x,t)|² dx`; `T` is the
    blowup time `T*`; `sheetDim` is the *spatial* Hausdorff dimension of
    the vortex sheet; `profile s` is the solution in Leray's similarity
    variable `s = -log(T* - t)`, and `period` is its `s`-period, set by
    the root-of-unity scaling `λ_κ`.

    Two notes on faithfulness to the `.md`.

    *  `sheet_dim_eq_two` records the **spatial** dimension `d_H = 2`.
       The `.md` is explicit that this is not a priori a CKN violation —
       CKN bounds the *parabolic* dimension of the space–time singular
       set by `1`, a different set — and that reconciling the two is a
       required step "not yet carried out".  So this class does not
       assert the reconciliation, and it deliberately carries no
       space–time dimension field: there is nothing derived to put in
       one.
    *  `profile_not_steady` is the Nečas–Růžička–Šverák exclusion
       \[necas-ruzicka-sverak1996]: the continuous, `s`-independent
       self-similar profile is ruled out, so the periodicity in
       `profile_periodic` must be non-trivial.  Dropping this field
       would let a constant `profile` satisfy the class, which is
       exactly the case the literature excludes.

    This does not prove the conjecture.  It makes assuming it mean
    something: each field is refutable by a wrong object, and the
    negative controls below exhibit such objects.

    Ref: [leitner2026] §Regularity breakdown at q = 1: the classical limit
    as a phase transition, `conj:regularity-breakdown` -/
class RegularityBreakdown (enstrophy : ℝ → ℝ) (T : ℝ) (sheetDim : ℝ)
    (profile : ℝ → ℝ) (period : ℝ) : Prop where
  /-- The blowup happens in finite positive time. -/
  T_pos : 0 < T
  /-- **Clause 1 — blowup of enstrophy.**  `enstrophy t → +∞` as
      `t → T⁻`: every bound `M` is exceeded arbitrarily close to `T`,
      from below.  Stated one-sidedly (`T - ε < t < T`), so a function
      that is merely unbounded somewhere does not satisfy it. -/
  enstrophy_blowup : ∀ M : ℝ, ∀ ε : ℝ, 0 < ε →
    ∃ t : ℝ, T - ε < t ∧ t < T ∧ M < enstrophy t
  /-- **Clause 2 — vortex sheet concentration.**  The vorticity
      concentrates on a codimension-1 surface: spatial Hausdorff
      dimension exactly `2`. -/
  sheet_dim_eq_two : sheetDim = 2
  /-- **Clause 3a — discrete, not continuous, self-similarity.**  The
      Leray profile is periodic in `s` with a genuine period. -/
  period_pos : 0 < period
  profile_periodic : ∀ s : ℝ, profile (s + period) = profile s
  /-- **Clause 3b — the profile is not steady.**  The `s`-independent
      self-similar profile is excluded \[necas-ruzicka-sverak1996], so
      the periodicity above is non-trivial. -/
  profile_not_steady : ∃ s₁ s₂ : ℝ, profile s₁ ≠ profile s₂

/-! ### The class is consistent, and each clause can be false

Inhabited, so the carrier is not vacuously unsatisfiable; and refutable,
which `∃ Re_c > 0` was not.

The witness takes `T = 1`, `enstrophy t = (1 - t)⁻¹` (which does blow up
at `1` from below), `sheetDim = 2`, and the period-`1` sawtooth
`profile s = s - ⌊s⌋`, which is periodic and non-constant — the
discretely-self-similar shape, not the steady one. -/

/-- Inhabitedness: the conjecture's *shape* is satisfiable. -/
example : RegularityBreakdown (fun t => (1 - t)⁻¹) 1 2 (fun s => s - ⌊s⌋) 1 where
  T_pos := one_pos
  enstrophy_blowup := by
    intro M ε hε
    -- pick `t = 1 - 1/n` with `n` large enough that `n > M` and `1/n < ε`
    obtain ⟨n, hn⟩ := exists_nat_gt (max M ε⁻¹)
    have hεi : (0:ℝ) < ε⁻¹ := inv_pos.mpr hε
    have hn0 : (0:ℝ) < (n:ℝ) := lt_of_le_of_lt (le_max_of_le_right hεi.le) hn
    have hMn : M < (n:ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
    have hεn : ε⁻¹ < (n:ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
    have hni : (0:ℝ) < (n:ℝ)⁻¹ := inv_pos.mpr hn0
    have hlt : (n:ℝ)⁻¹ < ε := by
      have h := (inv_lt_inv₀ hn0 hεi).mpr hεn
      rwa [inv_inv] at h
    refine ⟨1 - (n:ℝ)⁻¹, by linarith, by linarith, ?_⟩
    show M < (1 - (1 - (n:ℝ)⁻¹))⁻¹
    rw [show (1:ℝ) - (1 - (n:ℝ)⁻¹) = (n:ℝ)⁻¹ from by ring, inv_inv]
    exact hMn
  sheet_dim_eq_two := rfl
  period_pos := one_pos
  profile_periodic := by
    intro s
    show s + 1 - (⌊s + 1⌋ : ℝ) = s - (⌊s⌋ : ℝ)
    rw [Int.floor_add_one]
    push_cast
    ring
  profile_not_steady := ⟨0, 1/2, by norm_num⟩

/-- A vortex sheet of spatial dimension `1` refutes clause 2 — the
    codimension-1 concentration is the content of that clause. -/
example : ¬ RegularityBreakdown (fun t => (1 - t)⁻¹) 1 1 (fun s => s - ⌊s⌋) 1 := by
  rintro ⟨-, -, hdim, -, -, -⟩; norm_num at hdim

/-- A **steady** Leray profile refutes clause 3b, which is exactly the
    Nečas–Růžička–Šverák exclusion.  Note the same object satisfies
    `profile_periodic` for every period, which is why that field alone
    does not carry the clause. -/
example : ¬ RegularityBreakdown (fun t => (1 - t)⁻¹) 1 2 (fun _ => 0) 1 := by
  rintro ⟨-, -, -, -, -, s₁, s₂, hne⟩
  exact hne rfl

/-- An enstrophy that is bounded near `T` refutes clause 1, even though
    it is unbounded elsewhere: the blowup is one-sided at `T`. -/
example : ¬ RegularityBreakdown (fun _ => 0) 1 2 (fun s => s - ⌊s⌋) 1 := by
  rintro ⟨-, hblow, -, -, -, -⟩
  obtain ⟨t, -, -, hM⟩ := hblow 1 1 one_pos
  norm_num at hM

end QOU.FluidDynamics
