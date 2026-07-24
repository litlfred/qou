import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

/-!
# QOU.FluidDynamics.surreal_enstrophy_finite_modes — the surreal enstrophy at
finite truncation (S1–S3 of the surreal-enstrophy campaign)

**Scope discipline (owner directive 2026-07-24).** *Given a QOU*, working in the
surreal-bridge picture (`qou_ns_surreal_bridge`): the `q → 1` limit is
`q = 1 − ε` with `ε` a positive infinitesimal on a non-archimedean line. This
file builds the **finite-mode** surreal enstrophy concretely and proves that at
every finite truncation `N` its deviation from the classical value is
infinitesimal — so the standard part of `Ω_N(1−ε)` *is* the classical enstrophy.
This closes the *finite-mode* half of the bridge field `blowup_iff_infinite` and
**localises the open wall entirely in the `N → ∞` (UV) limit**: whether
`st ∘ lim_N = lim_N ∘ st` on the full tower is exactly the
`classical_regular_iff_finite` analytic hypothesis, deliberately not asserted.
No claim about the classical `ℝ³` PDE is made.

## Contents

* **S1 — infinitesimal calculus** over a generic linearly ordered field `K`
  (`Infinitesimal`, `IsFinite`; closure under `+`, `·`-by-finite). No
  archimedean axiom is assumed — `K` may be a surreal line; for archimedean `K`
  (e.g. `ℝ`) the only infinitesimal is `0` and all statements degenerate
  correctly.
* **S2 — q-integer perturbation**: `[k]_{1−ε} − k` is infinitesimal for every
  fixed `k` (`qInt_one_sub_infinitesimal`), where `[k]_q = Σ_{j<k} q^j` (so
  `[k]_1 = k`, the `q → 1` degeneration of the spectral tower —
  `regularity-breakdown` Obstruction 1).
* **S3 — finite-mode enstrophy**: with mode amplitudes `a k` finite,
  `Ω_N(1−ε) − Ω_N(1)` is infinitesimal (`enstrophy_perturbation_infinitesimal`)
  — the standard part of the surreal enstrophy at truncation `N` equals the
  classical enstrophy `Σ_{k<N} k² a_k`.

## Honest scope (anti-laundering)

Everything here is proved sorry-free; nothing open is asserted. The open
analytic content (UV limit `N → ∞`, where `N_eff ~ log_q Re → ∞` as `q → 1⁺`)
is *named* in the module docstring and carried by `qou_ns_surreal_bridge`'s
`classical_regular_iff_finite` hypothesis — it is **not** discharged here, and
the finite-mode results must not be cited as if they were the full bridge.

## Base ring (§7c)

Generic `[Field K] [LinearOrder K] [IsStrictOrderedRing K]` — deliberately NOT
`ℝ`: the intended instance is a non-archimedean (surreal) line, and no
archimedean construct is used. `ℝ` remains an instance (degenerate case).

## References
- [manuscript] fluid-dynamics/regularity-breakdown (Obstruction 1: `[k]_1 = k`),
  p2-critical-exponent; appendix-surreals/surreal-blowup-calculus,
  standard-part-classical-limits; QOU/FluidDynamics/qou_ns_surreal_bridge
-/

namespace QOU.FluidDynamics

set_option linter.unusedSectionVars false

open Finset

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-! ### S1 — infinitesimal calculus over a generic ordered field -/

/-- `x` is **infinitesimal** (relative to the naturals): every natural multiple
    of `|x|` stays below `1`. On an archimedean field this forces `x = 0`; on a
    surreal line it carries the genuine infinitesimals (e.g. `ε = 1/ω`). -/
def Infinitesimal (x : K) : Prop := ∀ n : ℕ, (n : K) * |x| < 1

/-- `x` is **finite** (bounded by a natural): `|x| < n` for some `n : ℕ`. -/
def IsFinite (x : K) : Prop := ∃ n : ℕ, |x| < (n : K)

theorem infinitesimal_zero : Infinitesimal (0 : K) := by
  intro n; simp

theorem Infinitesimal.neg {x : K} (h : Infinitesimal x) : Infinitesimal (-x) := by
  intro n; simpa using h n

/-- Closure of infinitesimals under addition (via the `2n` trick). -/
theorem Infinitesimal.add {x y : K} (hx : Infinitesimal x) (hy : Infinitesimal y) :
    Infinitesimal (x + y) := by
  intro n
  have hx2 := hx (2 * n)
  have hy2 := hy (2 * n)
  have hcast : ((2 * n : ℕ) : K) = 2 * (n : K) := by push_cast; ring
  rw [hcast] at hx2 hy2
  have habs : |x + y| ≤ |x| + |y| := abs_add_le x y
  have hn : (0 : K) ≤ (n : K) := Nat.cast_nonneg n
  have h1 : (n : K) * |x + y| ≤ (n : K) * (|x| + |y|) :=
    mul_le_mul_of_nonneg_left habs hn
  have h2 : (n : K) * (|x| + |y|) = (2 * (n : K) * |x| + 2 * (n : K) * |y|) / 2 := by
    ring
  have h3 : (2 * (n : K) * |x| + 2 * (n : K) * |y|) / 2 < (1 + 1) / 2 := by
    apply div_lt_div_of_pos_right _ (by norm_num)
    exact add_lt_add hx2 hy2
  calc (n : K) * |x + y| ≤ (n : K) * (|x| + |y|) := h1
    _ = (2 * (n : K) * |x| + 2 * (n : K) * |y|) / 2 := h2
    _ < (1 + 1) / 2 := h3
    _ = 1 := by norm_num

/-- An infinitesimal times a finite element is infinitesimal. -/
theorem Infinitesimal.mul_finite {x y : K} (hx : Infinitesimal x)
    (hy : IsFinite y) : Infinitesimal (x * y) := by
  intro n
  obtain ⟨m, hm⟩ := hy
  have hxm := hx (n * m)
  have hcast : ((n * m : ℕ) : K) = (n : K) * (m : K) := by push_cast; ring
  rw [hcast] at hxm
  have hxnn : (0 : K) ≤ |x| := abs_nonneg x
  have hn : (0 : K) ≤ (n : K) := Nat.cast_nonneg n
  have habs : |x * y| = |x| * |y| := abs_mul x y
  have hyle : |y| ≤ (m : K) := le_of_lt hm
  calc (n : K) * |x * y| = (n : K) * (|x| * |y|) := by rw [habs]
    _ ≤ (n : K) * (|x| * (m : K)) := by
        apply mul_le_mul_of_nonneg_left _ hn
        exact mul_le_mul_of_nonneg_left hyle hxnn
    _ = (n : K) * (m : K) * |x| := by ring
    _ < 1 := hxm

/-- Natural-number constants are finite. -/
theorem isFinite_natCast (k : ℕ) : IsFinite ((k : K)) := by
  refine ⟨k + 1, ?_⟩
  rw [abs_of_nonneg (Nat.cast_nonneg k)]
  exact_mod_cast Nat.lt_succ_self k

/-- `1` is finite. -/
theorem isFinite_one : IsFinite (1 : K) := by
  simpa using isFinite_natCast (K := K) 1

/-- Every infinitesimal is finite. -/
theorem Infinitesimal.isFinite {x : K} (h : Infinitesimal x) : IsFinite x := by
  refine ⟨1, ?_⟩
  have := h 1
  simpa using this

/-- Finites are closed under addition. -/
theorem IsFinite.add {x y : K} (hx : IsFinite x) (hy : IsFinite y) :
    IsFinite (x + y) := by
  obtain ⟨n, hn⟩ := hx
  obtain ⟨m, hm⟩ := hy
  refine ⟨n + m, ?_⟩
  have : |x + y| ≤ |x| + |y| := abs_add_le x y
  have hsum : |x| + |y| < (n : K) + (m : K) := add_lt_add hn hm
  have hcast : ((n + m : ℕ) : K) = (n : K) + (m : K) := by push_cast; ring
  rw [hcast]
  exact lt_of_le_of_lt this hsum

/-- Finites are closed under negation. -/
theorem IsFinite.neg {x : K} (h : IsFinite x) : IsFinite (-x) := by
  obtain ⟨n, hn⟩ := h; exact ⟨n, by simpa using hn⟩

/-- Finites are closed under multiplication. -/
theorem IsFinite.mul {x y : K} (hx : IsFinite x) (hy : IsFinite y) :
    IsFinite (x * y) := by
  obtain ⟨n, hn⟩ := hx
  obtain ⟨m, hm⟩ := hy
  refine ⟨n * m, ?_⟩
  have hxnn : (0 : K) ≤ |x| := abs_nonneg x
  have hynn : (0 : K) ≤ |y| := abs_nonneg y
  have hnn : (0 : K) ≤ (n : K) := Nat.cast_nonneg n
  have hcast : ((n * m : ℕ) : K) = (n : K) * (m : K) := by push_cast; ring
  rw [abs_mul, hcast]
  calc |x| * |y| ≤ |x| * (m : K) := mul_le_mul_of_nonneg_left (le_of_lt hm) hxnn
    _ < (n : K) * (m : K) := by
        have hmpos : (0 : K) < (m : K) := lt_of_le_of_lt hynn hm
        exact mul_lt_mul_of_pos_right hn hmpos

/-- A finite sum of infinitesimals is infinitesimal. -/
theorem infinitesimal_sum {ι : Type*} (s : Finset ι) (f : ι → K)
    (h : ∀ i ∈ s, Infinitesimal (f i)) :
    Infinitesimal (∑ i ∈ s, f i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simpa using infinitesimal_zero
  | insert a s ha ih =>
      rw [Finset.sum_insert ha]
      exact (h a (Finset.mem_insert_self a s)).add
        (ih fun i hi => h i (Finset.mem_insert_of_mem hi))

/-! ### S2 — q-integer perturbation at `q = 1 − ε` -/

/-- The **q-integer** `[k]_q = Σ_{j<k} q^j` (so `[k]_1 = k`): the spectral
    eigenvalue datum of the q-NS tower whose `q → 1` degeneration to `k` is
    Obstruction 1 of `conj:regularity-breakdown`. -/
def qInt (q : K) (k : ℕ) : K := ∑ j ∈ range k, q ^ j

/-- `[k]_1 = k`. -/
theorem qInt_one (k : ℕ) : qInt (1 : K) k = (k : K) := by
  simp [qInt]

/-- Powers of `1 − ε` deviate from `1` by an infinitesimal (fixed exponent):
    `(1−ε)^j − 1` is infinitesimal. Induction via
    `a^(j+1) − 1 = (a^j − 1)·a − ε` with `a = 1 − ε`. -/
theorem pow_one_sub_infinitesimal {ε : K} (hε : Infinitesimal ε) (j : ℕ) :
    Infinitesimal ((1 - ε) ^ j - 1) := by
  induction j with
  | zero => simpa using infinitesimal_zero
  | succ j ih =>
      have key : (1 - ε) ^ (j + 1) - 1
          = ((1 - ε) ^ j - 1) * (1 - ε) + (-ε) := by ring
      rw [key]
      have hfin : IsFinite (1 - ε : K) := by
        have h1 : IsFinite (1 : K) := isFinite_one
        have h2 : IsFinite (-ε) := hε.isFinite.neg
        simpa [sub_eq_add_neg] using h1.add h2
      exact (ih.mul_finite hfin).add hε.neg

/-- **S2.** `[k]_{1−ε} − k` is infinitesimal for every fixed `k`: at an
    infinitesimally-perturbed substrate the q-integer eigenvalues sit
    infinitesimally close to their classical values. -/
-- Ref: [manuscript] fluid-dynamics/regularity-breakdown (Obstruction 1)
theorem qInt_one_sub_infinitesimal {ε : K} (hε : Infinitesimal ε) (k : ℕ) :
    Infinitesimal (qInt (1 - ε) k - (k : K)) := by
  have key : qInt (1 - ε) k - (k : K) = ∑ j ∈ range k, ((1 - ε) ^ j - 1) := by
    rw [qInt, Finset.sum_sub_distrib]
    simp [Finset.card_range]
  rw [key]
  exact infinitesimal_sum _ _ fun j _ => pow_one_sub_infinitesimal hε j

/-! ### S3 — the finite-mode surreal enstrophy -/

/-- The **finite-mode enstrophy** at substrate value `q`, truncation `N`, mode
    amplitudes `a`: `Ω_N(q) = Σ_{k<N} [k]_q² · a k` (the enstrophy order
    parameter of `conj:regularity-breakdown` / `p2-critical-exponent`,
    truncated at `N` modes). -/
def enstrophyN (q : K) (a : ℕ → K) (N : ℕ) : K :=
  ∑ k ∈ range N, (qInt q k) ^ 2 * a k

/-- **S3 (capstone).** At every finite truncation `N`, the surreal enstrophy at
    `q = 1 − ε` deviates from the classical enstrophy `Ω_N(1) = Σ k² a_k` by an
    infinitesimal — i.e. the **standard part of the finite-mode surreal
    enstrophy is the classical enstrophy**. Requires only that each mode
    amplitude is finite.

    This proves the finite-mode half of the surreal bridge
    (`qou_ns_surreal_bridge.blowup_iff_infinite` restricted to any fixed
    truncation) and localises the open wall in the `N → ∞` (UV) limit: as
    `q → 1⁺` the active-mode count `N_eff ~ log_q Re` diverges, and whether the
    standard part commutes with that limit is precisely the open
    `classical_regular_iff_finite` hypothesis — NOT proved here. -/
-- Ref: [manuscript] fluid-dynamics/p2-critical-exponent, regularity-breakdown;
-- Ref: [manuscript] appendix-surreals/surreal-blowup-calculus
theorem enstrophy_perturbation_infinitesimal {ε : K} (hε : Infinitesimal ε)
    (a : ℕ → K) (ha : ∀ k, IsFinite (a k)) (N : ℕ) :
    Infinitesimal (enstrophyN (1 - ε) a N - enstrophyN 1 a N) := by
  have key : enstrophyN (1 - ε) a N - enstrophyN 1 a N
      = ∑ k ∈ range N,
          ((qInt (1 - ε) k - qInt 1 k) * (qInt (1 - ε) k + qInt 1 k)) * a k := by
    rw [enstrophyN, enstrophyN, ← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl fun k _ => by ring
  rw [key]
  refine infinitesimal_sum _ _ fun k _ => ?_
  -- per-mode: (infinitesimal · finite) · finite
  have hdiff : Infinitesimal (qInt (1 - ε) k - qInt 1 k) := by
    rw [qInt_one]
    exact qInt_one_sub_infinitesimal hε k
  have hsum_fin : IsFinite (qInt (1 - ε) k + qInt 1 k) := by
    have h1 : IsFinite (qInt (1 - ε) k) := by
      have : qInt (1 - ε) k = (qInt (1 - ε) k - (k : K)) + (k : K) := by ring
      rw [this]
      exact (qInt_one_sub_infinitesimal hε k).isFinite.add (isFinite_natCast k)
    have h2 : IsFinite (qInt (1 : K) k) := by
      rw [qInt_one]; exact isFinite_natCast k
    exact h1.add h2
  exact (hdiff.mul_finite hsum_fin).mul_finite (ha k)

/-! ### G1 — half the UV wall: classical-unbounded ⇒ surreal-infinite -/

/-- **Half of the UV wall, proved.** Suppose the total surreal enstrophy
    `Ω_tot` dominates every finite truncation (`hdom` — the monotone-limit /
    tower-domination property, automatic for non-negative mode amplitudes), and
    the **classical** enstrophy is unbounded along the tower (`hunb` — classical
    enstrophy blow-up, `conj:regularity-breakdown` item 1 read at `q = 1`).
    Then `Ω_tot` is **not** a finite surreal: the surreal observable is
    infinite.

    This proves one direction of the open bridge biconditional
    `classical_regular_iff_finite` (`qou_ns_surreal_bridge`), in contrapositive
    form: **surreal-finite ⇒ classically bounded**. The *converse* — that a
    surreal-infinite observable forces classical divergence, i.e. that the
    infinite part cannot come solely from infinitesimal-scale (sub-classical)
    contributions — remains the open analytic content, and is deliberately not
    asserted. The wall is thereby **halved**, not closed.

    Proof: from `|Ω_tot| < m`, pick `N` with `Ω_N(1) > m + 1`; by the
    finite-mode theorem `Ω_N(1−ε)` is within an infinitesimal (hence within
    `1`) of `Ω_N(1)`, so `Ω_tot ≥ Ω_N(1−ε) > m ≥ Ω_tot` — contradiction. -/
-- Ref: [manuscript] fluid-dynamics/regularity-breakdown (enstrophy blow-up);
-- Ref: [manuscript] appendix-surreals/surreal-blowup-calculus
theorem classical_unbounded_implies_surreal_infinite
    {ε : K} (hε : Infinitesimal ε) (a : ℕ → K) (ha : ∀ k, IsFinite (a k))
    (Ω_tot : K)
    (hdom : ∀ N, enstrophyN (1 - ε) a N ≤ Ω_tot)
    (hunb : ∀ n : ℕ, ∃ N, (n : K) < enstrophyN 1 a N) :
    ¬ IsFinite Ω_tot := by
  rintro ⟨m, hm⟩
  obtain ⟨N, hN⟩ := hunb (m + 1)
  have hδ := enstrophy_perturbation_infinitesimal hε a ha N
  have hδ1 : |enstrophyN (1 - ε) a N - enstrophyN 1 a N| < 1 := by
    have := hδ 1; simpa using this
  have hlow : -(1 : K) < enstrophyN (1 - ε) a N - enstrophyN 1 a N :=
    neg_lt_of_abs_lt hδ1
  have hcast : ((m + 1 : ℕ) : K) = (m : K) + 1 := by push_cast; ring
  rw [hcast] at hN
  have hdomN := hdom N
  have habs : Ω_tot ≤ |Ω_tot| := le_abs_self Ω_tot
  linarith

/-! ### H1 — the converse half, under UV exhaustion -/

/-- **The converse half of the UV wall, under UV exhaustion.** Suppose the total
    surreal enstrophy `Ω_tot` is non-negative, is **UV-exhausted** by the tower
    (`hexh`: some finite truncation captures it up to a finite constant `c` —
    "no enstrophy at infinite mode index beyond finite excess"), and the
    **classical** enstrophy is bounded along the tower (`hbnd` — classical
    regularity read at `q = 1`). Then `Ω_tot` **is** a finite surreal.

    Together with `classical_unbounded_implies_surreal_infinite` this proves the
    bridge biconditional `classical_regular_iff_finite`
    (`qou_ns_surreal_bridge`) **modulo one named structural hypothesis: UV
    exhaustion.** The failure mode exhaustion excludes is exactly the
    "conspiracy" scenario — enstrophy concentrating at infinite surreal mode
    index `k ~ ω` (sub-classical scales) while every finite truncation stays
    bounded. Whether the QOU-internal flow satisfies UV exhaustion is the open
    analytic content; it is **not** proved here.

    Proof: `Ω_tot ≤ Ω_N(1−ε) + c`, and by the finite-mode theorem
    `Ω_N(1−ε) < Ω_N(1) + 1 < B + 1`, so `0 ≤ Ω_tot < B + 1 + c`. -/
-- Ref: [manuscript] fluid-dynamics/regularity-breakdown, q-ns-wellposedness;
-- Ref: [manuscript] appendix-surreals/surreal-blowup-calculus
theorem surreal_finite_of_classical_bounded
    {ε : K} (hε : Infinitesimal ε) (a : ℕ → K) (ha : ∀ k, IsFinite (a k))
    (Ω_tot : K) (hnn : 0 ≤ Ω_tot)
    (hexh : ∃ (N c : ℕ), Ω_tot ≤ enstrophyN (1 - ε) a N + (c : K))
    (hbnd : ∃ B : ℕ, ∀ N, enstrophyN 1 a N < (B : K)) :
    IsFinite Ω_tot := by
  obtain ⟨N, c, hNc⟩ := hexh
  obtain ⟨B, hB⟩ := hbnd
  refine ⟨B + 1 + c, ?_⟩
  have hδ := enstrophy_perturbation_infinitesimal hε a ha N
  have hδ1 : |enstrophyN (1 - ε) a N - enstrophyN 1 a N| < 1 := by
    have := hδ 1; simpa using this
  have hup : enstrophyN (1 - ε) a N - enstrophyN 1 a N < 1 :=
    lt_of_le_of_lt (le_abs_self _) hδ1
  have hBN := hB N
  rw [abs_of_nonneg hnn]
  push_cast
  linarith

end QOU.FluidDynamics
