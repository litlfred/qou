import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Data.Rat.Defs

/-!
# QOU.Molecular — the shell state space as a self-square (residual conjecture)

Carries `conj:shell-space-is-self-square`: the one modelling step that the
`2n²` shell-capacity derivation still rests on.

## What is exact and what is conjectural

The `2n²` capacity itself is **derived** — see `prop:shell-capacity-self-square`
and `QOU.Molecular.shell_capacity_self_square`, sorry-free at `q = 1`.  Per the
owner ruling of 2026-06-20
(`docs/audits/2026-06-20-shell-2n2-from-self-square-no-second-su2.md`) the
`(j,j)` doubling that standard physics obtains from
`SO(4) = SU(2) × SU(2)` is here the **self-fusion `V ⊗ V` of one angular
object**, the second factor a copy of the first tied by the coproduct.  There is
**no second compact `SU(2)`**, and the earlier `SO(4)`/Runge–Lenz framing is
retracted.

Exactly one step is not derived: *that the physical shell state space **is** that
self-square*, rather than merely having a dimension that agrees with it.  That
step is the class `ShellSpaceIsSelfSquare` below.  Everything downstream of it is
proved here.

## Base ring (AGENTS.md §7c)

Everything is stated over a generic `{R : Type*} [CommRing R]`.  The inverse is
carried as a companion variable `qi` subject to the unit relation `q * qi = 1`.
The file is therefore division-free — the `ℤ[q, q⁻¹]` form, matching
`QOU.BraidKnot.meson_qCG_3x4`.  A field instance is recovered by taking
`qi = q⁻¹` and `hq = mul_inv_cancel₀`.  No `ℝ`, no ordering, no archimedean
construct appears.

## Normalisation

`q`-dimensions are carried in **unnormalised** form: `[m]_q` is represented by
`q^m - qi^m`, i.e. `(q - qi) · [m]_q`.  Clearing the common denominator
`(q - qi)` turns the `q`-Clebsch–Gordan statement
`[n]_q² = ∑_{ℓ<n} [2ℓ+1]_q` into the polynomial identity `qCG_self_square`
below.  The two forms are equivalent wherever `q ≠ qi`; at `q = qi` the
unnormalised identity degenerates to `0 = 0` and says nothing, so the classical
`q → 1` count is **not** obtained by substitution here — it is the separate,
separately-proved `QOU.Molecular.orbital_n_squared`.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.Molecular

variable {R : Type*} [CommRing R]

/-- `q^m · qi^m = 1` for every `m`, from the unit relation `q · qi = 1`.
    Lets the `q`-Clebsch–Gordan induction stay inside `CommRing`. -/
theorem pow_mul_pow_unit (q qi : R) (hq : q * qi = 1) (m : ℕ) :
    q ^ m * qi ^ m = 1 := by
  rw [← mul_pow, hq, one_pow]

/-- **`q`-Clebsch–Gordan self-square, division-free, all `n`.**

    The unnormalised form of `[n]_q² = ∑_{ℓ=0}^{n-1} [2ℓ+1]_q`: the self-fusion
    `V ⊗ V` of the `n`-dimensional `SU(2)_q` irrep decomposes into the sub-shell
    irreps of `q`-dimensions `[1]_q, [3]_q, …, [2n-1]_q`.

    This is the **exact** leg of `conj:shell-space-is-self-square`.  It is new
    relative to `QOU.Molecular.orbital_n_squared`, which proves only the `q = 1`
    integer specialisation `∑_{ℓ<n} (2ℓ+1) = n²`; the `q`-deformed identity was
    previously only checked symbolically for `n = 1…8` in
    `computations/shell_capacity_chebyshev_bridge.py`. -/
theorem qCG_self_square (q qi : R) (hq : q * qi = 1) (n : ℕ) :
    (q ^ n - qi ^ n) ^ 2
      = (q - qi) * ∑ l ∈ Finset.range n, (q ^ (2 * l + 1) - qi ^ (2 * l + 1)) := by
  induction n with
  | zero => simp
  | succ k ih =>
      rw [Finset.sum_range_succ, mul_add, ← ih]
      have eq : q ^ (2 * k + 1) = q ^ k * q ^ k * q := by
        rw [pow_succ, two_mul, pow_add]
      have eqi : qi ^ (2 * k + 1) = qi ^ k * qi ^ k * qi := by
        rw [pow_succ, two_mul, pow_add]
      rw [eq, eqi, pow_succ, pow_succ]
      linear_combination ((q ^ k - qi ^ k) ^ 2) * hq

/-- **The conjecture** (`conj:shell-space-is-self-square`), axiomatised as a
    content-bearing class per AGENTS.md §3b.

    `shellDim n` is the unnormalised `q`-dimension of the *physical* orbital
    state space at principal level `n` — whatever the substrate hands us.  The
    conjectural content is `isSelfSquare`: that this space is the self-fusion
    `V_n ⊗ V_n` of the single angular object of unnormalised `q`-dimension
    `q^n - qi^n`, so its `q`-dimension is that quantity **squared**.

    This is a **primary** conjecture in the §3b-tax sense: its signature binds no
    other conjecture class.  It is falsifiable — `not_selfSquare_linear` below
    exhibits a concrete `shellDim` that refutes it — and it is *not* satisfied by
    an arbitrary `shellDim`, so the class is not a vacuous marker. -/
class ShellSpaceIsSelfSquare {R : Type*} [CommRing R]
    (q qi : R) (shellDim : ℕ → R) : Prop where
  /-- `q` and `qi` are mutually inverse (the `ℤ[q, q⁻¹]` unit relation). -/
  unit : q * qi = 1
  /-- The shell state space at level `n` is the self-square of the angular
      object: `dim_q 𝒪_n = [n]_q²`, unnormalised. -/
  isSelfSquare : ∀ n : ℕ, shellDim n = (q ^ n - qi ^ n) ^ 2

/-- **Derived from the conjecture: the sub-shell decomposition.**

    Conditional on `ShellSpaceIsSelfSquare`, the shell space at level `n`
    decomposes into sub-shells of `q`-dimension `[2ℓ+1]_q` for
    `ℓ = 0, …, n-1` — the `ℓ`-tower with its cutoff, and with the *`q`-deformed*
    multiplicities, not merely the `q = 1` integers `2ℓ+1`.

    This is the §3b-cond non-degenerate shape: the class carries the *hypothesis*
    (the shell space is a self-square), and the conclusion — an observable
    sub-shell structure — is **derived** from it through `qCG_self_square`, not
    projected back out of a field.  It is also the sharp empirical content of the
    conjecture: an experiment that resolved sub-shell multiplicities departing
    from `[2ℓ+1]_q` would refute the identification. -/
theorem subshell_decomposition_of_self_square
    (q qi : R) (shellDim : ℕ → R)
    [h : ShellSpaceIsSelfSquare q qi shellDim] (n : ℕ) :
    shellDim n
      = (q - qi) * ∑ l ∈ Finset.range n, (q ^ (2 * l + 1) - qi ^ (2 * l + 1)) := by
  rw [h.isSelfSquare n, qCG_self_square q qi h.unit n]

/-- **The conjecture has content: a concrete refuting witness.**

    The *linear* alternative — a shell space whose `q`-dimension is the angular
    `[n]_q` itself rather than its self-square — fails the class at `q = 2`,
    `n = 2`: `2² - (1/2)² = 15/4` but `(15/4)² = 225/16`.

    So `ShellSpaceIsSelfSquare` is not satisfied by every `shellDim`, and is not
    an empty marker in the sense of the `proof-no-empty-prop-carrier` /
    `proof-claims-unencoded` criteria. -/
theorem not_selfSquare_linear :
    ¬ ShellSpaceIsSelfSquare (2 : ℚ) (1 / 2) (fun n => (2 : ℚ) ^ n - (1 / 2) ^ n) := by
  intro h
  have h2 := h.isSelfSquare 2
  norm_num at h2

end QOU.Molecular
