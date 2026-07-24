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

/-! ### U1 — golden-window membership: `1/φ² < 1 − ε < 1`

The corpus confinement window (`rem:golden-ratio-degeneration`,
`deconfinement-golden-threshold`): the elliptic fiber is smooth and the
confinement machinery intact on the **classical band** `q_gold < q < 1`, where
`q_gold = 1/φ² = s²` with `s = 1/φ` the positive root of `s² + s = 1`. The
substrate point `q = 1 − ε` of the surreal bridge lies in this band
*automatically* for every positive infinitesimal `ε`, because
`1 − q_gold = 1/φ > 1/2` is a non-infinitesimal margin. -/

/-- **Golden-window membership.** For every positive infinitesimal `ε` the
    surreal substrate point `q = 1 − ε` lies strictly inside the classical band
    `q_gold < q < 1` (`q_gold = s²`, `s` the positive root of `s² + s = 1`,
    i.e. `s = 1/φ`): the elliptic fiber is smooth and the confinement window's
    hypotheses apply at the infinitesimally-perturbed substrate. -/
-- Ref: [manuscript] observations/golden-ratio-degeneration, deconfinement-golden-threshold
theorem golden_window_mem {ε s : K} (hε : Infinitesimal ε) (hε0 : 0 < ε)
    (hs0 : 0 < s) (hgold : s ^ 2 + s = 1) :
    s ^ 2 < 1 - ε ∧ 1 - ε < 1 := by
  have hshalf : (1 : K) / 2 < s := by
    by_contra hle
    push_neg at hle
    nlinarith
  have hε2 : ε < 1 / 2 := by
    have h2 := hε 2
    rw [abs_of_pos hε0] at h2
    have hcast : ((2 : ℕ) : K) = 2 := by norm_num
    rw [hcast] at h2
    linarith
  constructor
  · nlinarith
  · linarith

/-! ### U2 — uniform UV damping at `q = 1 − ε` -/

/-- **Exact geometric identity:** `ε · [k]_{1−ε} = 1 − (1−ε)^k`. -/
theorem eps_mul_qInt (ε : K) (k : ℕ) :
    ε * qInt (1 - ε) k = 1 - (1 - ε) ^ k := by
  induction k with
  | zero => simp [qInt]
  | succ k ih =>
      have hstep : qInt (1 - ε) (k + 1) = qInt (1 - ε) k + (1 - ε) ^ k := by
        rw [qInt, qInt, Finset.sum_range_succ]
      have hpow : (1 - ε) ^ (k + 1) = (1 - ε) ^ k * (1 - ε) := pow_succ _ _
      rw [hstep, mul_add, ih, hpow]
      ring

/-- **Uniform UV damping.** On the `q = 1 − ε < 1` side the q-integers are
    bounded *uniformly in the mode index*: `[k]_{1−ε} ≤ ε⁻¹` for every `k`
    (an infinite surreal bound, but `k`-independent) — in sharp contrast to
    `[k]_1 = k`, which is unbounded. This is the algebraic seed of UV
    exhaustion: at the infinitesimally-perturbed substrate the spectral tower
    retains one-sided UV control that the classical point `q = 1` has lost
    (`conj:regularity-breakdown` Obstruction 1). -/
-- Ref: [manuscript] fluid-dynamics/regularity-breakdown (Obstruction 1)
theorem qInt_le_inv {ε : K} (h0 : 0 < ε) (h1 : ε ≤ 1) (k : ℕ) :
    qInt (1 - ε) k ≤ ε⁻¹ := by
  have hpow : (0 : K) ≤ (1 - ε) ^ k := pow_nonneg (by linarith) k
  have hle : ε * qInt (1 - ε) k ≤ 1 := by
    rw [eps_mul_qInt]; linarith
  have h2 : ε * qInt (1 - ε) k ≤ ε * ε⁻¹ := by
    rw [mul_inv_cancel₀ (ne_of_gt h0)]
    exact hle
  exact le_of_mul_le_mul_left h2 h0

/-! ### U3 — UV exhaustion from a uniform tail bound -/

/-- Monotonicity of the truncated enstrophy in the cutoff (non-negative
    amplitudes): more modes, more enstrophy. -/
theorem enstrophyN_mono (q : K) (a : ℕ → K) (ha0 : ∀ k, 0 ≤ a k)
    {M N : ℕ} (h : M ≤ N) :
    enstrophyN q a M ≤ enstrophyN q a N :=
  Finset.sum_le_sum_of_subset_of_nonneg
    (fun _ hx => Finset.mem_range.mpr
      (lt_of_lt_of_le (Finset.mem_range.mp hx) h))
    (fun k _ _ => mul_nonneg (sq_nonneg _) (ha0 k))

/-- **UV exhaustion from a uniform tail bound.** If the truncations are
    monotone (non-negative amplitudes), `Ω_tot` is a least-upper-bound-type
    limit of the truncations (`hlub`), and the tower satisfies a **uniform tail
    bound** past some level `N` (`htail`: every deeper truncation exceeds
    `Ω_N(1−ε)` by at most a finite `c` — the surreal `N_eff` cutoff physics,
    cf. the `k_max ≈ 4` active-mode truncation of `prop:leray-profile`), then
    the **UV-exhaustion hypothesis of `surreal_finite_of_classical_bounded`
    holds**. Combined with that theorem and
    `classical_unbounded_implies_surreal_infinite`, the bridge biconditional is
    proved modulo the uniform tail bound alone — which is exactly where the
    uniform damping `[k]_{1−ε} ≤ ε⁻¹` (`qInt_le_inv`) gives the tail sum
    `Σ_{k≥N} [k]² a_k ≤ ε⁻² Σ_{k≥N} a_k` a chance to be finite that the
    classical point `q = 1` does not have. Whether the QOU's amplitude tail
    mass is `O(ε²)` past `N_eff` remains the open spectral question; it is not
    asserted. -/
-- Ref: [manuscript] fluid-dynamics/leray-profile (finite truncation), regularity-breakdown
theorem uv_exhaustion_of_uniform_tail {ε : K} (a : ℕ → K) (ha0 : ∀ k, 0 ≤ a k)
    (Ω_tot : K)
    (hlub : ∀ b : K, (∀ M, enstrophyN (1 - ε) a M ≤ b) → Ω_tot ≤ b)
    (htail : ∃ (N c : ℕ), ∀ M, N ≤ M →
      enstrophyN (1 - ε) a M ≤ enstrophyN (1 - ε) a N + (c : K)) :
    ∃ (N c : ℕ), Ω_tot ≤ enstrophyN (1 - ε) a N + (c : K) := by
  obtain ⟨N, c, hNc⟩ := htail
  refine ⟨N, c, hlub _ fun M => ?_⟩
  rcases le_or_gt N M with h | h
  · exact hNc M h
  · have hmono := enstrophyN_mono (1 - ε) a ha0 (le_of_lt h)
    have hc : (0 : K) ≤ (c : K) := Nat.cast_nonneg c
    linarith

/-- **Combined reduction.** Given a QOU's surreal enstrophy data with
    non-negative finite amplitudes, the lub property, a uniform tail bound, and
    bounded classical enstrophy, the surreal observable is finite — the full
    converse half assembled from `uv_exhaustion_of_uniform_tail` +
    `surreal_finite_of_classical_bounded`. The open remainder of the whole
    bridge is now the single **uniform tail bound** hypothesis. -/
-- Ref: [manuscript] appendix-surreals/surreal-blowup-calculus
theorem surreal_finite_of_uniform_tail {ε : K} (hε : Infinitesimal ε)
    (a : ℕ → K) (ha : ∀ k, IsFinite (a k)) (ha0 : ∀ k, 0 ≤ a k)
    (Ω_tot : K) (hnn : 0 ≤ Ω_tot)
    (hlub : ∀ b : K, (∀ M, enstrophyN (1 - ε) a M ≤ b) → Ω_tot ≤ b)
    (htail : ∃ (N c : ℕ), ∀ M, N ≤ M →
      enstrophyN (1 - ε) a M ≤ enstrophyN (1 - ε) a N + (c : K))
    (hbnd : ∃ B : ℕ, ∀ N, enstrophyN 1 a N < (B : K)) :
    IsFinite Ω_tot :=
  surreal_finite_of_classical_bounded hε a ha Ω_tot hnn
    (uv_exhaustion_of_uniform_tail a ha0 Ω_tot hlub htail) hbnd

/-! ### V — sub-classical closure: `[k]_{1−ε} ≤ k` kills the tail question

On the sub-classical approach `q = 1 − ε` (inside the golden window,
`golden_window_mem`) the q-integers are dominated **termwise** by their
classical values, so the surreal enstrophy is dominated by the classical one at
*every* truncation — and the uniform tail bound of
`surreal_finite_of_uniform_tail` becomes a **theorem** rather than a
hypothesis. The bridge biconditional **closes on this side** with no spectral
hypothesis at all (only the definitional limit properties). The super-classical
approach `q = 1 + ε`, where `[k]_{1+ε} ≥ k` and the tail question is genuine,
remains open. -/

/-- **Termwise classical domination:** for `0 ≤ ε ≤ 1`, `[k]_{1−ε} ≤ k` — each
    sub-classical q-integer is at most its classical value (every power
    `(1−ε)^j ≤ 1`). The exact opposite of the super-classical side. -/
theorem qInt_le_self {ε : K} (h0 : 0 ≤ ε) (h1 : ε ≤ 1) (k : ℕ) :
    qInt (1 - ε) k ≤ (k : K) := by
  have hb : ∀ j ∈ Finset.range k, (1 - ε) ^ j ≤ 1 :=
    fun j _ => pow_le_one₀ (by linarith) (by linarith)
  calc qInt (1 - ε) k ≤ ∑ _j ∈ Finset.range k, (1 : K) :=
        Finset.sum_le_sum hb
    _ = (k : K) := by simp

/-- **Enstrophy domination:** with non-negative amplitudes, the sub-classical
    enstrophy is dominated by the classical enstrophy at every truncation. -/
theorem enstrophyN_le_classical {ε : K} (h0 : 0 ≤ ε) (h1 : ε ≤ 1)
    (a : ℕ → K) (ha0 : ∀ k, 0 ≤ a k) (M : ℕ) :
    enstrophyN (1 - ε) a M ≤ enstrophyN 1 a M := by
  refine Finset.sum_le_sum fun k _ => ?_
  have hq0 : (0 : K) ≤ qInt (1 - ε) k :=
    Finset.sum_nonneg fun j _ => pow_nonneg (by linarith) j
  have hle : qInt (1 - ε) k ≤ qInt 1 k := by
    rw [qInt_one]; exact qInt_le_self h0 h1 k
  have hsq : qInt (1 - ε) k ^ 2 ≤ qInt 1 k ^ 2 := by nlinarith
  exact mul_le_mul_of_nonneg_right hsq (ha0 k)

/-- **Sub-classical closure of the converse — NO spectral hypothesis.** On the
    `q = 1 − ε` side (`0 ≤ ε ≤ 1` — in particular any positive infinitesimal,
    which sits in the golden window by `golden_window_mem`), bounded classical
    enstrophy plus the definitional lub property already force the surreal
    observable to be finite: by termwise domination every truncation satisfies
    `Ω_M(1−ε) ≤ Ω_M(1) < B`, so `Ω_tot ≤ B`. **No tail hypothesis, no
    amplitude-finiteness, not even infinitesimality of `ε` is needed.**

    Together with `classical_unbounded_implies_surreal_infinite` (whose
    domination hypothesis is the definitional lower-limit property), the bridge
    biconditional `classical_regular_iff_finite` **closes on the sub-classical
    approach**, given only the definitional limit pair (truncations below
    `Ω_tot`, `Ω_tot` a lub) and non-negative amplitudes. The honest remaining
    open content of the whole bridge is now confined to the **super-classical
    approach** `q = 1 + ε` (`[k]_{1+ε} ≥ k`), where the tail question is
    genuine. -/
-- Ref: [manuscript] fluid-dynamics/regularity-breakdown, q-ns-wellposedness;
-- Ref: [manuscript] observations/golden-ratio-degeneration
theorem surreal_finite_of_classical_bounded_subclassical {ε : K}
    (h0 : 0 ≤ ε) (h1 : ε ≤ 1)
    (a : ℕ → K) (ha0 : ∀ k, 0 ≤ a k)
    (Ω_tot : K) (hnn : 0 ≤ Ω_tot)
    (hlub : ∀ b : K, (∀ M, enstrophyN (1 - ε) a M ≤ b) → Ω_tot ≤ b)
    (hbnd : ∃ B : ℕ, ∀ N, enstrophyN 1 a N < (B : K)) :
    IsFinite Ω_tot := by
  obtain ⟨B, hB⟩ := hbnd
  refine ⟨B + 1, ?_⟩
  have hup : Ω_tot ≤ (B : K) := hlub _ fun M =>
    le_of_lt (lt_of_le_of_lt (enstrophyN_le_classical h0 h1 a ha0 M) (hB M))
  rw [abs_of_nonneg hnn]
  push_cast
  linarith

/-! ### W — the super-classical side `q = 1 + ε`

The remaining open side of the bridge. Here the domination **reverses**:
`[k]_{1+ε} ≥ k` termwise, so the surreal enstrophy dominates the classical one
and the *forward* direction (classical blow-up ⇒ surreal infinite) is immediate
— no infinitesimality needed. The *converse* is the genuine open side; the
dissipation closure (`enstrophy_alpha_one_of_dissipation_closure`,
`q_ns_classical_bridge`) caps the possible blow-up at **ω-grade 1**
(`FiniteOfGrade`), the surreal reading of the critical exponent `α = 1`. The
open content is thereby sharpened from "is `Ω(1+ε)` finite?" to "grade 1 vs
grade 0" — exactly the `α` question of `p2-critical-exponent`. -/

/-- **Termwise classical domination, reversed:** for `0 ≤ ε`,
    `k ≤ [k]_{1+ε}` — each super-classical q-integer is at least its classical
    value (every power `(1+ε)^j ≥ 1`). -/
theorem qInt_ge_self {ε : K} (h0 : 0 ≤ ε) (k : ℕ) :
    (k : K) ≤ qInt (1 + ε) k := by
  have hb : ∀ j ∈ Finset.range k, (1 : K) ≤ (1 + ε) ^ j :=
    fun j _ => one_le_pow₀ (by linarith)
  calc (k : K) = ∑ _j ∈ Finset.range k, (1 : K) := by simp
    _ ≤ qInt (1 + ε) k := Finset.sum_le_sum hb

/-- **Enstrophy domination, reversed:** with non-negative amplitudes the
    super-classical enstrophy dominates the classical one at every truncation. -/
theorem enstrophyN_ge_classical {ε : K} (h0 : 0 ≤ ε)
    (a : ℕ → K) (ha0 : ∀ k, 0 ≤ a k) (M : ℕ) :
    enstrophyN 1 a M ≤ enstrophyN (1 + ε) a M := by
  refine Finset.sum_le_sum fun k _ => ?_
  have hk0 : (0 : K) ≤ (k : K) := Nat.cast_nonneg k
  have hge : (k : K) ≤ qInt (1 + ε) k := qInt_ge_self h0 k
  have hsq : qInt 1 k ^ 2 ≤ qInt (1 + ε) k ^ 2 := by
    rw [qInt_one]; nlinarith
  exact mul_le_mul_of_nonneg_right hsq (ha0 k)

/-- **Forward direction on the super-classical side.** If the total surreal
    enstrophy dominates every truncation and the classical enstrophy is
    unbounded, the surreal observable at `q = 1 + ε` is infinite — immediate
    from the reversed domination; no infinitesimality of `ε` needed. -/
-- Ref: [manuscript] fluid-dynamics/regularity-breakdown (enstrophy blow-up)
theorem superclassical_infinite_of_classical_unbounded {ε : K} (h0 : 0 ≤ ε)
    (a : ℕ → K) (ha0 : ∀ k, 0 ≤ a k) (Ω_tot : K)
    (hdom : ∀ N, enstrophyN (1 + ε) a N ≤ Ω_tot)
    (hunb : ∀ n : ℕ, ∃ N, (n : K) < enstrophyN 1 a N) :
    ¬ IsFinite Ω_tot := by
  rintro ⟨m, hm⟩
  obtain ⟨N, hN⟩ := hunb m
  have h1 := enstrophyN_ge_classical h0 a ha0 N
  have h2 := hdom N
  have habs : Ω_tot ≤ |Ω_tot| := le_abs_self Ω_tot
  linarith

/-- `x` is **finite of ω-grade `n`** (relative to the infinitesimal `ε`):
    `ε^n · x` is finite. Grade `0` is ordinary finiteness; grade `1` allows one
    factor of the infinite surreal `ε⁻¹` — the surreal bookkeeping of the
    blow-up order `ord_ω` (`def:surreal-blowup-calculus`, §7ab). -/
def FiniteOfGrade (ε : K) (n : ℕ) (x : K) : Prop := IsFinite (ε ^ n * x)

/-- **Grade cap from the dissipation closure.** Under the dissipation closure
    `ε · Ω = 2(1+ε) · D` (the `q = 1+ε` reading of
    `enstrophy_alpha_one_of_dissipation_closure` with `ν_q · Ω = D` cleared of
    denominators) with finite mean dissipation `D` and finite `ε`, the
    super-classical enstrophy is **finite of ω-grade 1**: `ε · Ω` is finite, so
    `Ω` blows up at most like `ε⁻¹` — the surreal statement of the critical
    exponent `α = 1`. The remaining open content of the super-classical side is
    thereby the gap **grade 1 vs grade 0**: whether the flow saturates the
    closure's `ε⁻¹` cap (blow-up, `α = 1`) or stays at grade 0 (regular) — the
    `α` question of `p2-critical-exponent`, not decided here. -/
-- Ref: [manuscript] fluid-dynamics/p2-critical-exponent, regularity-breakdown;
-- Ref: [manuscript] appendix-surreals/surreal-blowup-calculus (§7ab ord_ω)
theorem enstrophy_grade_one_of_dissipation_closure {ε D Ω : K}
    (hD : IsFinite D) (hεf : IsFinite ε)
    (hclosure : ε * Ω = 2 * (1 + ε) * D) :
    FiniteOfGrade ε 1 Ω := by
  unfold FiniteOfGrade
  rw [pow_one, hclosure]
  have h2 : IsFinite (2 : K) := by
    simpa using isFinite_natCast (K := K) 2
  have h1ε : IsFinite (1 + ε : K) := isFinite_one.add hεf
  exact (h2.mul h1ε).mul hD

end QOU.FluidDynamics
