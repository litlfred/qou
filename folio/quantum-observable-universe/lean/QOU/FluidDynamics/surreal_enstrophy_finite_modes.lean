import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import QOU.MathlibExt.QIntegerCanonical

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
- [leitner2026] fluid-dynamics/regularity-breakdown (Obstruction 1: `[k]_1 = k`),
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

/-- **Bridge to the canonical geometric q-integer.**  This site is the
geometric form `∑_{j<k} q^j`, not the balanced one — so it ties to `qIntGeo`,
and tying it to `qIntBal` would be exactly the mis-consolidation
`QIntegerCanonical` warns about.  Unconditional: `qIntGeo` asks only for a
`CommRing`, which `K` has as a `Field`, and neither side divides. -/
theorem qInt_eq_canonical_geo (q : K) (k : ℕ) :
    qInt q k = QOU.QInteger.qIntGeo q k := rfl

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
-- Ref: [leitner2026] fluid-dynamics/regularity-breakdown (Obstruction 1)
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
-- Ref: [leitner2026] fluid-dynamics/p2-critical-exponent, regularity-breakdown;
-- Ref: [leitner2026] appendix-surreals/surreal-blowup-calculus
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
-- Ref: [leitner2026] fluid-dynamics/regularity-breakdown (enstrophy blow-up);
-- Ref: [leitner2026] appendix-surreals/surreal-blowup-calculus
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
-- Ref: [leitner2026] fluid-dynamics/regularity-breakdown, q-ns-wellposedness;
-- Ref: [leitner2026] appendix-surreals/surreal-blowup-calculus
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
-- Ref: [leitner2026] predicted-spectra/golden-ratio-degeneration, deconfinement-golden-threshold
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
-- Ref: [leitner2026] fluid-dynamics/regularity-breakdown (Obstruction 1)
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
-- Ref: [leitner2026] fluid-dynamics/leray-profile (finite truncation), regularity-breakdown
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
-- Ref: [leitner2026] appendix-surreals/surreal-blowup-calculus
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
-- Ref: [leitner2026] fluid-dynamics/regularity-breakdown, q-ns-wellposedness;
-- Ref: [leitner2026] predicted-spectra/golden-ratio-degeneration
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
-- Ref: [leitner2026] fluid-dynamics/regularity-breakdown (enstrophy blow-up)
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
-- Ref: [leitner2026] fluid-dynamics/p2-critical-exponent, regularity-breakdown;
-- Ref: [leitner2026] appendix-surreals/surreal-blowup-calculus (§7ab ord_ω)
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

/-! ### X — the grade trichotomy: the α question as a single surreal criterion

Within the ω-grade-1 cap (`enstrophy_grade_one_of_dissipation_closure`), the
remaining open content of the super-classical side is classified exhaustively
by **one surreal-valued criterion: is `ε · Ω` infinitesimal?** The trichotomy
below is the enstrophy-grade analogue of the growth-exponent trichotomy in
`levi_growth_trichotomy` (that file no longer carries Levi data: re-scoped
2026-10-13, `conj:levi-degeneracy`). -/

/-- **Saturation forces blow-up.** If `ε · Ω` is *not* infinitesimal (the flow
    saturates the grade-1 cap, `α = 1`), then `Ω` is not a finite surreal —
    the QOU-internal q-NS observable blows up. Contrapositive of
    `Infinitesimal.mul_finite`. -/
-- Ref: [leitner2026] fluid-dynamics/p2-critical-exponent
theorem saturated_implies_infinite {ε Ω : K} (hε : Infinitesimal ε)
    (hsat : ¬ Infinitesimal (ε * Ω)) : ¬ IsFinite Ω :=
  fun hfin => hsat (hε.mul_finite hfin)

/-- **The grade trichotomy.** For infinitesimal `ε`, the enstrophy observable
    falls into exactly one of three mutually-exclusive regimes (disjoint by
    construction: the first is finite, the last two are not; the last two
    differ on the criterion):

    * **grade 0 (regular):** `Ω` finite — and then `ε·Ω` is automatically
      infinitesimal;
    * **saturated (`α = 1`):** `Ω` infinite with `ε·Ω` non-infinitesimal — the
      flow saturates the dissipation-closure cap;
    * **intermediate (`0 < α < 1`):** `Ω` infinite yet `ε·Ω` still
      infinitesimal.

    Hence the entire remaining α question of the super-classical side reduces
    to the single surreal criterion **"is `ε · Ω(1+ε)` infinitesimal?"** —
    infinitesimal + finite `Ω` ⟺ regular; non-infinitesimal ⟺ saturated
    blow-up (`saturated_implies_infinite`). Which regime the QOU's flow
    realises is the open critical-exponent content (`p2-critical-exponent`);
    not decided here. -/
-- Ref: [leitner2026] fluid-dynamics/p2-critical-exponent, regularity-breakdown;
-- Ref: [leitner2026] appendix-surreals/surreal-blowup-calculus (§7ab ord_ω)
theorem grade_trichotomy {ε Ω : K} (hε : Infinitesimal ε) :
    (IsFinite Ω ∧ Infinitesimal (ε * Ω))
    ∨ (¬ IsFinite Ω ∧ ¬ Infinitesimal (ε * Ω))
    ∨ (¬ IsFinite Ω ∧ Infinitesimal (ε * Ω)) := by
  by_cases hf : IsFinite Ω
  · exact Or.inl ⟨hf, hε.mul_finite hf⟩
  · by_cases hs : Infinitesimal (ε * Ω)
    · exact Or.inr (Or.inr ⟨hf, hs⟩)
    · exact Or.inr (Or.inl ⟨hf, hs⟩)

/-! ### Z — Gevrey data is grade-0 regular (promoting the probe's Model B)

The probe (`qns_enstrophy_grade_probe.py`) measured `α ≈ 0` for Gevrey
amplitudes. Here that becomes a **theorem**: geometrically-decaying amplitudes
with the combined damping `q² r ≤ 1/2` give a uniform bound `Ω_M(q) ≤ 6C` on
every truncation, hence (with the lub property) a **finite** total — the
grade-0 regular branch of `grade_trichotomy`. For `q = 1 + ε` with `ε`
infinitesimal the damping condition holds for any fixed `r < 1/2`. The open
content shrinks to non-Gevrey (sustained/forced) spectra, plus Gevrey
*persistence* under the actual dynamics. -/

/-- `[k]_q ≤ k·q^k` for `1 ≤ q` (each of the `k` powers is at most `q^k`). -/
theorem qInt_le_mul_pow {q : K} (hq : 1 ≤ q) (k : ℕ) :
    qInt q k ≤ (k : K) * q ^ k := by
  have hb : ∀ j ∈ Finset.range k, q ^ j ≤ q ^ k := fun j hj =>
    pow_le_pow_right₀ hq (le_of_lt (Finset.mem_range.mp hj))
  calc qInt q k ≤ ∑ _j ∈ Finset.range k, q ^ k := Finset.sum_le_sum hb
    _ = (k : K) * q ^ k := by simp [mul_comm]

/-- **Closed form for the half-geometric quadratic sum:**
    `Σ_{k<M} k²(1/2)^k = 6 − (2M² + 4M + 6)(1/2)^M`. -/
theorem sum_sq_half_pow (M : ℕ) :
    ∑ k ∈ Finset.range M, (k : K) ^ 2 * (1 / 2) ^ k
      = 6 - (2 * (M : K) ^ 2 + 4 * (M : K) + 6) * (1 / 2) ^ M := by
  induction M with
  | zero => norm_num
  | succ M ih =>
      rw [Finset.sum_range_succ, ih, pow_succ]
      push_cast
      ring

/-- **The half-geometric quadratic sum is bounded by `6`.** -/
theorem sum_sq_half_pow_le (M : ℕ) :
    ∑ k ∈ Finset.range M, (k : K) ^ 2 * (1 / 2) ^ k ≤ 6 := by
  rw [sum_sq_half_pow]
  have hpow : (0 : K) < (1 / 2 : K) ^ M := by positivity
  have hcoef : (0 : K) ≤ 2 * (M : K) ^ 2 + 4 * (M : K) + 6 := by positivity
  nlinarith

/-- **Gevrey amplitudes are grade-0 regular (theorem form of probe Model B).**
    If the amplitudes decay geometrically, `0 ≤ a_k ≤ C·r^k` with `C : ℕ`, and
    the combined damping `q² r ≤ 1/2` holds (`1 ≤ q`, `0 ≤ r` — satisfied at
    `q = 1 + ε`, `ε` infinitesimal, for any fixed `r < 1/2`), then every
    truncation obeys the uniform bound `Ω_M(q) ≤ 6C`, and with the lub property
    the total surreal enstrophy is **finite**: the QOU-internal flow with fixed
    Gevrey data sits in the grade-0 **regular** branch of `grade_trichotomy`.
    In-QOU, blow-up is thereby confined to non-Gevrey (sustained/forced)
    spectra. Whether the internal dynamics *preserves* the Gevrey class as
    `q → 1⁺` (Gevrey persistence, the analytic core of
    `thm:q-ns-wellposedness`) is the remaining open content; not decided
    here. -/
-- Ref: [leitner2026] fluid-dynamics/q-ns-wellposedness, p2-critical-exponent;
-- Ref: [leitner2026] appendix-surreals/surreal-blowup-calculus
theorem gevrey_grade_zero {q r : K} (hq : 1 ≤ q) (hr : 0 ≤ r)
    (hdamp : q ^ 2 * r ≤ 1 / 2)
    (a : ℕ → K) (C : ℕ) (ha : ∀ k, 0 ≤ a k ∧ a k ≤ (C : K) * r ^ k)
    (Ω_tot : K) (hnn : 0 ≤ Ω_tot)
    (hlub : ∀ b : K, (∀ M, enstrophyN q a M ≤ b) → Ω_tot ≤ b) :
    IsFinite Ω_tot := by
  have hq0 : (0 : K) ≤ q := le_trans zero_le_one hq
  -- per-truncation uniform bound Ω_M ≤ 6C
  have hbound : ∀ M, enstrophyN q a M ≤ 6 * (C : K) := by
    intro M
    have hterm : ∀ k ∈ Finset.range M,
        (qInt q k) ^ 2 * a k ≤ (C : K) * ((k : K) ^ 2 * (1 / 2) ^ k) := by
      intro k _
      have hqk0 : (0 : K) ≤ qInt q k :=
        Finset.sum_nonneg fun j _ => pow_nonneg hq0 j
      have hqk : qInt q k ≤ (k : K) * q ^ k := qInt_le_mul_pow hq k
      have hk0 : (0 : K) ≤ (k : K) := Nat.cast_nonneg k
      have hqpow0 : (0 : K) ≤ q ^ k := pow_nonneg hq0 k
      -- (qInt)² ≤ k² q^{2k}
      have hsq : (qInt q k) ^ 2 ≤ (k : K) ^ 2 * (q ^ k) ^ 2 := by nlinarith
      have ha0 := (ha k).1
      have haC := (ha k).2
      -- (q²r)^k ≤ (1/2)^k
      have hq2r0 : (0 : K) ≤ q ^ 2 * r := mul_nonneg (by positivity) hr
      have hgeo : (q ^ 2 * r) ^ k ≤ (1 / 2 : K) ^ k :=
        pow_le_pow_left₀ hq2r0 hdamp k
      have hrk0 : (0 : K) ≤ r ^ k := pow_nonneg hr k
      calc (qInt q k) ^ 2 * a k
          ≤ ((k : K) ^ 2 * (q ^ k) ^ 2) * a k := by
            exact mul_le_mul_of_nonneg_right hsq ha0
        _ ≤ ((k : K) ^ 2 * (q ^ k) ^ 2) * ((C : K) * r ^ k) := by
            apply mul_le_mul_of_nonneg_left haC
            positivity
        _ = (C : K) * ((k : K) ^ 2 * ((q ^ 2 * r) ^ k)) := by
            rw [mul_pow, ← pow_right_comm q k 2]
            ring
        _ ≤ (C : K) * ((k : K) ^ 2 * (1 / 2) ^ k) := by
            apply mul_le_mul_of_nonneg_left _ (Nat.cast_nonneg C)
            exact mul_le_mul_of_nonneg_left hgeo (by positivity)
    calc enstrophyN q a M
        ≤ ∑ k ∈ Finset.range M, (C : K) * ((k : K) ^ 2 * (1 / 2) ^ k) :=
          Finset.sum_le_sum hterm
      _ = (C : K) * ∑ k ∈ Finset.range M, (k : K) ^ 2 * (1 / 2) ^ k := by
          rw [Finset.mul_sum]
      _ ≤ (C : K) * 6 :=
          mul_le_mul_of_nonneg_left (sum_sq_half_pow_le M) (Nat.cast_nonneg C)
      _ = 6 * (C : K) := by ring
  refine ⟨6 * C + 1, ?_⟩
  have hup : Ω_tot ≤ 6 * (C : K) := hlub _ hbound
  rw [abs_of_nonneg hnn]
  push_cast
  linarith

/-! ### AA — closure vs cascade: a structural incompatibility (promoting probe Model A)

The probe measured `α ≈ 4/3 > 1` for sustained Kolmogorov spectra — exceeding
the dissipation-closure grade-1 cap. Here that incompatibility becomes a
**theorem**: say the tower **reaches grade-1 cascade depth** when
`∀ m, ∃ N, m ≤ ε·Ω_N(1)` (the classical enstrophy along the cutoff ladder
overtakes every multiple of `ε⁻¹` — what a Kolmogorov spectrum at the cascade
cutoff `N_eff ~ ε⁻¹` does, since `ε·N_eff^{4/3} ~ ε^{-1/3}`). Then the total
cannot be grade 1 — so the dissipation closure (which forces grade 1)
**structurally excludes** grade-1-deep cascades. Scope (a): the two
*ingredients* cannot hold together; which one the true flow realises stays
open. -/

/-- **Grade-1-deep cascades beat the grade-1 cap.** If `0 ≤ ε`, amplitudes are
    non-negative, the total dominates the truncations, and the tower reaches
    grade-1 cascade depth (`hcascade`), then `Ω_tot` is **not** finite of
    ω-grade 1. -/
-- Ref: [leitner2026] fluid-dynamics/p2-critical-exponent (cascade depth)
theorem deep_cascade_not_grade_one {ε : K} (hε0 : 0 ≤ ε)
    (a : ℕ → K) (ha0 : ∀ k, 0 ≤ a k) (Ω_tot : K)
    (hdom : ∀ N, enstrophyN (1 + ε) a N ≤ Ω_tot)
    (hcascade : ∀ m : ℕ, ∃ N, (m : K) ≤ ε * enstrophyN 1 a N) :
    ¬ FiniteOfGrade ε 1 Ω_tot := by
  rintro ⟨m, hm⟩
  rw [pow_one] at hm
  obtain ⟨N, hN⟩ := hcascade m
  have h1 : enstrophyN 1 a N ≤ enstrophyN (1 + ε) a N :=
    enstrophyN_ge_classical hε0 a ha0 N
  have h2 : ε * enstrophyN 1 a N ≤ ε * Ω_tot :=
    mul_le_mul_of_nonneg_left (le_trans h1 (hdom N)) hε0
  have habs : ε * Ω_tot ≤ |ε * Ω_tot| := le_abs_self _
  linarith

/-- **The dissipation closure excludes grade-1-deep cascades** (scope (a),
    structural incompatibility — the theorem form of probe Model A). Under the
    closure `ε·Ω_tot = 2(1+ε)·D` with finite `D` and finite `ε`, the tower
    cannot reach grade-1 cascade depth: the closure and a sustained
    Kolmogorov-type cascade are mutually exclusive ingredients. Which one the
    QOU's actual flow realises is the open content (`p2-critical-exponent`);
    neither is asserted. -/
-- Ref: [leitner2026] fluid-dynamics/p2-critical-exponent, regularity-breakdown
theorem closure_excludes_deep_cascade {ε : K} (hε0 : 0 ≤ ε)
    (hεf : IsFinite ε) {D : K} (hD : IsFinite D)
    (a : ℕ → K) (ha0 : ∀ k, 0 ≤ a k) (Ω_tot : K)
    (hdom : ∀ N, enstrophyN (1 + ε) a N ≤ Ω_tot)
    (hclosure : ε * Ω_tot = 2 * (1 + ε) * D) :
    ¬ ∀ m : ℕ, ∃ N, (m : K) ≤ ε * enstrophyN 1 a N :=
  fun hcascade =>
    deep_cascade_not_grade_one hε0 a ha0 Ω_tot hdom hcascade
      (enstrophy_grade_one_of_dissipation_closure hD hεf hclosure)

/-! ### GP — Gevrey persistence, brick 1: discrete Gronwall + the rate wall

The remaining analytic core: does the QOU-internal q-NS dynamics *keep* smooth
data in the Gevrey class as `q → 1⁺` (`thm:q-ns-wellposedness`)? Entry brick:
the enstrophy inequality `dΩ/dt ≤ Λ_q Ω` discretises to `Ω_{n+1} ≤ G·Ω_n`,
`G = 1 + Λ_q δ`. We prove the discrete Gronwall bound and finite-horizon
persistence for **finite** growth rate — and record the honest wall: the naive
rate `Λ_q ~ (q−1)^{-1} = ε^{-1}` (`p2-critical-exponent`, "too crude") makes
`G^n` an *exponentially infinite* surreal over any fixed physical horizon, so
persistence is exactly the question of whether the q-damping improves the
naive rate to a **finite** effective `G`. That improvement is the open
analytic content; not proved here. -/

/-- **Discrete Gronwall.** `Ω_{n+1} ≤ G·Ω_n` with `G ≥ 0`, non-negative
    states ⇒ `Ω_n ≤ G^n·Ω_0`. -/
theorem discrete_gronwall {G : K} (Ω : ℕ → K) (hG : 0 ≤ G)
    (hstep : ∀ n, Ω (n + 1) ≤ G * Ω n) : ∀ n, Ω n ≤ G ^ n * Ω 0 := by
  intro n
  induction n with
  | zero => simp
  | succ n ih =>
      calc Ω (n + 1) ≤ G * Ω n := hstep n
        _ ≤ G * (G ^ n * Ω 0) := mul_le_mul_of_nonneg_left ih hG
        _ = G ^ (n + 1) * Ω 0 := by rw [pow_succ]; ring

/-- Finites are closed under powers. -/
theorem IsFinite.pow {x : K} (h : IsFinite x) (n : ℕ) : IsFinite (x ^ n) := by
  induction n with
  | zero => simpa using isFinite_one
  | succ n ih => rw [pow_succ]; exact ih.mul h

/-- **Finite-horizon Gevrey-enstrophy persistence for finite rate.** If the
    per-step growth factor `G` is a *finite* surreal and the initial enstrophy
    is finite, the enstrophy stays finite at every fixed step `n`. The open
    wall (`p2-critical-exponent`): the naive `G = 1 + Λ_q δ` with
    `Λ_q ~ ε^{-1}` is NOT finite, so this theorem applies exactly when the
    q-damping improves the naive rate — that improvement is the Gevrey-
    persistence question, not decided here. -/
-- Ref: [leitner2026] fluid-dynamics/q-ns-wellposedness, p2-critical-exponent
theorem gronwall_finite_horizon {G : K} (hG0 : 0 ≤ G) (hGf : IsFinite G)
    (Ω : ℕ → K) (hstep : ∀ n, Ω (n + 1) ≤ G * Ω n) (hnn : ∀ n, 0 ≤ Ω n)
    (h0 : IsFinite (Ω 0)) (n : ℕ) : IsFinite (Ω n) := by
  obtain ⟨m, hm⟩ := (hGf.pow n).mul h0
  refine ⟨m, ?_⟩
  rw [abs_of_nonneg (hnn n)]
  have h1 := discrete_gronwall Ω hG0 hstep n
  have h2 : G ^ n * Ω 0 ≤ |G ^ n * Ω 0| := le_abs_self _
  linarith

/-! ### GP2 — mode splitting: the q-damping threshold

The q-mechanism that can beat the naive rate wall: dissipation acts per mode as
`ν·[k]_q²`, and on the super-classical side `[k]_q ~ q^k` grows exponentially,
so *every* stretching rate `Λ` is overtaken at a finite mode index. Above that
threshold the per-step factor `1 + δΛ − δν[k]_q²` is `≤ 1`
(`damping_threshold`): **high modes are non-growing**. Splitting the enstrophy
into a low-mode block (factor `G`) and a damped high-mode block, the split
Gronwall bound (`split_gronwall`, `split_persistence`) reduces Gevrey
persistence to a single question: **is the low-mode block's effective
stretching rate finite?** The naive interpolation bound gives `Λ ~ ν_q⁻¹ ~ ε⁻¹`
(infinite); whether the finite-dimensional low-mode dynamics improves it to a
finite `G` is the open GP3 content — not decided here. -/

/-- **q-damping threshold.** Once a mode clears the threshold
    `Λ ≤ ν·[k]_q²`, its per-step factor is at most `1`: the mode is
    non-growing. On the super-classical side `[k]_q` grows exponentially, so
    every `Λ` is cleared at a finite mode index. -/
-- Ref: [leitner2026] fluid-dynamics/q-ns-wellposedness (UV damping), p2-critical-exponent
theorem damping_threshold {q ν Λ δ : K} (hδ : 0 ≤ δ) (k : ℕ)
    (hthresh : Λ ≤ ν * (qInt q k) ^ 2) :
    1 + δ * Λ - δ * (ν * (qInt q k) ^ 2) ≤ 1 := by
  have := mul_le_mul_of_nonneg_left hthresh hδ
  linarith

/-- A step-non-increasing sequence is bounded by its initial value. -/
theorem le_initial_of_step {H : ℕ → K} (hH : ∀ n, H (n + 1) ≤ H n) :
    ∀ n, H n ≤ H 0 := by
  intro n
  induction n with
  | zero => exact le_refl _
  | succ n ih => exact le_trans (hH n) ih

/-- **Split Gronwall.** Low-mode block growing at factor `G`, high-mode block
    non-increasing (above the damping threshold): the total obeys
    `L n + H n ≤ G^n·L 0 + H 0`. -/
-- Ref: [leitner2026] fluid-dynamics/p2-critical-exponent
theorem split_gronwall {G : K} (hG : 0 ≤ G) (L H : ℕ → K)
    (hL : ∀ n, L (n + 1) ≤ G * L n) (hH : ∀ n, H (n + 1) ≤ H n) (n : ℕ) :
    L n + H n ≤ G ^ n * L 0 + H 0 := by
  have h1 := discrete_gronwall L hG hL n
  have h2 := le_initial_of_step hH n
  linarith

/-- **Split persistence.** With a *finite* low-mode factor `G`, finite initial
    blocks, and the high modes damped, the total enstrophy is finite at every
    step. Gevrey persistence thereby reduces to the finiteness of the low-mode
    effective rate — the open GP3 content. -/
-- Ref: [leitner2026] fluid-dynamics/q-ns-wellposedness, p2-critical-exponent
theorem split_persistence {G : K} (hG0 : 0 ≤ G) (hGf : IsFinite G)
    (L H : ℕ → K) (hL : ∀ n, L (n + 1) ≤ G * L n) (hH : ∀ n, H (n + 1) ≤ H n)
    (hLnn : ∀ n, 0 ≤ L n) (hHnn : ∀ n, 0 ≤ H n)
    (hL0 : IsFinite (L 0)) (hH0 : IsFinite (H 0)) (n : ℕ) :
    IsFinite (L n + H n) := by
  obtain ⟨m, hm⟩ := ((hGf.pow n).mul hL0).add hH0
  refine ⟨m, ?_⟩
  rw [abs_of_nonneg (add_nonneg (hLnn n) (hHnn n))]
  have h1 := split_gronwall hG0 L H hL hH n
  have h2 : G ^ n * L 0 + H 0 ≤ |G ^ n * L 0 + H 0| := le_abs_self _
  linarith

/-! ### GP3 — the low-mode bootstrap: local persistence, ε-free

GP2 reduced persistence to the low-mode block. Its genuine nonlinearity is
quadratic in the enstrophy (`dΩ/dt ≤ cΩ²`, the supercritical vortex-stretching
form); the discrete bootstrap below proves **local persistence**: over any
horizon with `N·δ·c·Ω₀ ≤ 1/4`, the block stays within `2Ω₀` — with **no
hypothesis on `ε` at all**. This is the discrete, in-QOU form of classical
local-in-time well-posedness (horizon `~ 1/(cΩ₀)`), now theorem-grade.
Combined with the GP2 split, the QOU-internal flow with finite smooth data
persists over the bootstrap horizon.

**The honest final landing of the epic:** what remains open is **global**
persistence — continuation beyond the bootstrap horizon — isolated at the
finite-dimensional low-mode block. The framework thus reproduces the classical
local theory sorry-free, and the global question *is* the open problem, as it
must be; it is named and not asserted. -/

/-- **Discrete quadratic bootstrap (local persistence).** If the low-mode block
    obeys the quadratic step `Ω_{n+1} ≤ Ω_n + δcΩ_n²` and the horizon satisfies
    `N·δ·c·Ω₀ ≤ 1/4`, then `Ω_n ≤ 2Ω₀` for every `n ≤ N`. No hypothesis on `ε`:
    the local theory is uniform in the substrate deformation. -/
-- Ref: [leitner2026] fluid-dynamics/q-ns-wellposedness (local theory), p2-critical-exponent
theorem local_bootstrap {δ c : K} (hδ : 0 ≤ δ) (hc : 0 ≤ c)
    (Ω : ℕ → K) (hnn : ∀ n, 0 ≤ Ω n)
    (hstep : ∀ n, Ω (n + 1) ≤ Ω n + δ * c * (Ω n) ^ 2)
    (N : ℕ) (hhor : (N : K) * (δ * c * Ω 0) ≤ 1 / 4) :
    ∀ n ≤ N, Ω n ≤ 2 * Ω 0 := by
  have hΩ00 : 0 ≤ Ω 0 := hnn 0
  have hδc : 0 ≤ δ * c := mul_nonneg hδ hc
  have hdc0 : (0 : K) ≤ δ * c * Ω 0 := mul_nonneg hδc hΩ00
  -- envelope-to-2Ω₀ conversion, used at every horizon step
  have envelope_le : ∀ n : ℕ, n ≤ N →
      Ω 0 + (n : K) * (4 * (δ * c) * (Ω 0) ^ 2) ≤ 2 * Ω 0 := by
    intro n hn
    have hcast : (n : K) ≤ (N : K) := by exact_mod_cast hn
    have hmul1 : (n : K) * (δ * c * Ω 0) ≤ (N : K) * (δ * c * Ω 0) :=
      mul_le_mul_of_nonneg_right hcast hdc0
    have hmul1' : Ω 0 * ((n : K) * (δ * c * Ω 0))
        ≤ Ω 0 * ((N : K) * (δ * c * Ω 0)) :=
      mul_le_mul_of_nonneg_left hmul1 hΩ00
    have hmul2 : Ω 0 * ((N : K) * (δ * c * Ω 0)) ≤ Ω 0 * (1 / 4) :=
      mul_le_mul_of_nonneg_left hhor hΩ00
    nlinarith [hmul1', hmul2]
  -- strengthened linear-in-n envelope
  have key : ∀ n, n ≤ N → Ω n ≤ Ω 0 + (n : K) * (4 * (δ * c) * (Ω 0) ^ 2) := by
    intro n
    induction n with
    | zero => intro _; simp
    | succ n ih =>
        intro hn1
        have hnN : n ≤ N := Nat.le_of_succ_le hn1
        have hSn := ih hnN
        have h2B : Ω n ≤ 2 * Ω 0 := le_trans hSn (envelope_le n hnN)
        have hstepn := hstep n
        have hsq : (Ω n) ^ 2 ≤ (2 * Ω 0) ^ 2 := by nlinarith [hnn n]
        have hsq' : δ * c * (Ω n) ^ 2 ≤ δ * c * (2 * Ω 0) ^ 2 :=
          mul_le_mul_of_nonneg_left hsq hδc
        have hpush : ((n + 1 : ℕ) : K) = (n : K) + 1 := by push_cast; ring
        rw [hpush]
        nlinarith [hstepn, hSn, hsq']
  intro n hn
  exact le_trans (key n hn) (envelope_le n hn)

/-- **Local persistence, finiteness form.** Under the bootstrap hypotheses with
    finite initial enstrophy, the low-mode block is finite at every step of the
    horizon — the in-QOU discrete local well-posedness statement, uniform in
    `ε`. Global continuation beyond the horizon is the (named, open) remainder
    of the epic. -/
-- Ref: [leitner2026] fluid-dynamics/q-ns-wellposedness
theorem local_persistence {δ c : K} (hδ : 0 ≤ δ) (hc : 0 ≤ c)
    (Ω : ℕ → K) (hnn : ∀ n, 0 ≤ Ω n)
    (hstep : ∀ n, Ω (n + 1) ≤ Ω n + δ * c * (Ω n) ^ 2)
    (N : ℕ) (hhor : (N : K) * (δ * c * Ω 0) ≤ 1 / 4)
    (h0 : IsFinite (Ω 0)) : ∀ n ≤ N, IsFinite (Ω n) := by
  intro n hn
  obtain ⟨m, hm⟩ := h0
  refine ⟨2 * m, ?_⟩
  have hb := local_bootstrap hδ hc Ω hnn hstep N hhor n hn
  have h1 : Ω 0 ≤ |Ω 0| := le_abs_self _
  rw [abs_of_nonneg (hnn n)]
  push_cast
  linarith

/-! ### GP4 — small-data GLOBAL persistence: the sub-threshold basin

The last provable piece of the epic. Including the low-mode damping term
(dissipation acts on *every* mode with rate at least `ν·μ`, `μ = [1]_q² = 1` at
worst), the low-mode step is `Ω_{n+1} ≤ Ω_n + δ·(cΩ_n² − νμΩ_n)`. For
**sub-threshold data** `c·Ω₀ ≤ ν·μ` the quadratic production never exceeds the
linear dissipation, so the enstrophy is non-increasing **for all time** — no
horizon condition, no hypothesis on `ε`. This is the discrete in-QOU form of
classical small-data global regularity.

**The epic's final honest state:** local persistence for all finite data
(GP3), global persistence for sub-threshold data (GP4). The sole remaining
open item is **large-data global persistence** — exactly the classical
local-vs-global dichotomy, reproduced in-QOU at the finite-dimensional
low-mode block; named, not asserted. -/

/-- **Small-data global persistence.** With the damped low-mode step
    `Ω_{n+1} ≤ Ω_n + δ(cΩ_n² − νμΩ_n)` and sub-threshold data
    `c·Ω₀ ≤ ν·μ`, the enstrophy never increases: `Ω_n ≤ Ω₀` for **every** `n`.
    No horizon, no `ε` hypothesis — the discrete in-QOU small-data global
    regularity statement. -/
-- Ref: [leitner2026] fluid-dynamics/q-ns-wellposedness, regularity-breakdown
theorem global_persistence_subthreshold {δ c ν μ : K}
    (hδ : 0 ≤ δ) (hc : 0 ≤ c)
    (Ω : ℕ → K) (hnn : ∀ n, 0 ≤ Ω n)
    (hstep : ∀ n, Ω (n + 1) ≤ Ω n + δ * (c * (Ω n) ^ 2 - ν * μ * Ω n))
    (hsub : c * Ω 0 ≤ ν * μ) :
    ∀ n, Ω n ≤ Ω 0 := by
  intro n
  induction n with
  | zero => exact le_refl _
  | succ n ih =>
      have hstepn := hstep n
      have hΩn := hnn n
      -- c·Ω_n ≤ c·Ω₀ ≤ ν·μ, so the production−dissipation term is ≤ 0
      have hcΩ : c * Ω n ≤ ν * μ :=
        le_trans (mul_le_mul_of_nonneg_left ih hc) hsub
      have hneg : c * (Ω n) ^ 2 - ν * μ * Ω n ≤ 0 := by nlinarith
      have hδneg : δ * (c * (Ω n) ^ 2 - ν * μ * Ω n) ≤ 0 :=
        mul_nonpos_of_nonneg_of_nonpos hδ hneg
      linarith

/-- **Small-data global finiteness.** Sub-threshold finite data stays finite at
    every step, globally. -/
-- Ref: [leitner2026] fluid-dynamics/q-ns-wellposedness
theorem global_finiteness_subthreshold {δ c ν μ : K}
    (hδ : 0 ≤ δ) (hc : 0 ≤ c)
    (Ω : ℕ → K) (hnn : ∀ n, 0 ≤ Ω n)
    (hstep : ∀ n, Ω (n + 1) ≤ Ω n + δ * (c * (Ω n) ^ 2 - ν * μ * Ω n))
    (hsub : c * Ω 0 ≤ ν * μ) (h0 : IsFinite (Ω 0)) :
    ∀ n, IsFinite (Ω n) := by
  intro n
  obtain ⟨m, hm⟩ := h0
  refine ⟨m, ?_⟩
  have h1 : Ω 0 ≤ |Ω 0| := le_abs_self _
  have h2 := global_persistence_subthreshold hδ hc Ω hnn hstep hsub n
  rw [abs_of_nonneg (hnn n)]
  linarith

/-! ### GP5 — the Riccati lower bound: mechanism-level branch A

The blow-up side of the GP calculus. If super-threshold colliding-pair data
satisfies the quadratic *lower* bound `Ω_{n+1} ≥ Ω_n + δc'Ω_n²` (the
production-dominated regime the categorical mechanism selects at the collision
locus, cf. `rem:hyperbolic-overlap-saturation` /
`rem:townsend-biot-savart-strain`), the enstrophy grows at least linearly at
rate `δc'Ω₀²` — on any archimedean instance this forces divergence past every
bound; on a surreal line it certifies growth of that grade. Whether the actual
colliding-pair data satisfies the lower bound is the open verification (the
in-QOU residue of the millennium problem); not asserted. -/

/-- **Discrete Riccati lower growth.** `Ω_{n+1} ≥ Ω_n + δc'Ω_n²` with `δc' ≥ 0`
    ⇒ the sequence is non-decreasing and `Ω_n ≥ Ω₀ + n·δc'Ω₀²`: linear growth
    at the initial production rate, forever. -/
-- Ref: [leitner2026] fluid-dynamics/hyperbolic-overlap-saturation, townsend-biot-savart-strain
theorem riccati_lower_growth {δ c' : K} (hδ : 0 ≤ δ) (hc : 0 ≤ c')
    (Ω : ℕ → K) (hnn : ∀ n, 0 ≤ Ω n)
    (hstep : ∀ n, Ω n + δ * c' * (Ω n) ^ 2 ≤ Ω (n + 1)) :
    ∀ n : ℕ, Ω 0 + (n : K) * (δ * c' * (Ω 0) ^ 2) ≤ Ω n := by
  have hδc : 0 ≤ δ * c' := mul_nonneg hδ hc
  -- monotonicity
  have hmono : ∀ n, Ω 0 ≤ Ω n := by
    intro n
    induction n with
    | zero => exact le_refl _
    | succ n ih =>
        have h1 := hstep n
        have h2 : 0 ≤ δ * c' * (Ω n) ^ 2 := by positivity
        linarith
  intro n
  induction n with
  | zero => simp
  | succ n ih =>
      have h1 := hstep n
      have h0n := hmono n
      have hsq : (Ω 0) ^ 2 ≤ (Ω n) ^ 2 := by nlinarith [hnn 0]
      have hsq' : δ * c' * (Ω 0) ^ 2 ≤ δ * c' * (Ω n) ^ 2 :=
        mul_le_mul_of_nonneg_left hsq hδc
      have hpush : ((n + 1 : ℕ) : K) = (n : K) + 1 := by push_cast; ring
      rw [hpush]
      linarith

/-! ### PC5 — the overlap race, Lean brick

Phase 1 of the pair-collision model integrates exactly (`d² = d₀²(1−u)`,
`V₁ = V₁₀(1−u)^{−1/2}`), so overlap engages where `(1−u)^{3/2} = V₁₀/d₀²`;
cubing both sides removes the fractional power: `(1−u)³ = x²` with
`x = V₁₀/d₀² > 0`. The brick proves the **race inequality**: any such crossing
has `u < 1` — the hyperbolic-overlap saturation engages *strictly before* the
inviscid singular time, for every positive core size (witness
`qns-overlap-race-probe`, 7-decade ODE verification). In-model, the pair
channel is regular (branch B); the measure-zero `x = 0` point-vortex limit is
excluded by the hypothesis. Scope (a): model-level. -/

/-- **The race inequality.** If the overlap-crossing equation `(1−u)³ = x²`
    holds with `x ≠ 0` (positive core size), then `u < 1`: overlap engages
    strictly before the singular time. -/
-- Ref: [leitner2026] fluid-dynamics/hyperbolic-overlap-saturation, townsend-biot-savart-strain
theorem overlap_race_strict {u x : K} (hx : x ≠ 0)
    (hcross : (1 - u) ^ 3 = x ^ 2) : u < 1 := by
  have hx2 : 0 < x ^ 2 := by positivity
  have hcube : 0 < (1 - u) ^ 3 := hcross ▸ hx2
  by_contra h
  push_neg at h
  have h1u : 1 - u ≤ 0 := by linarith
  have hsq : 0 ≤ (1 - u) ^ 2 := sq_nonneg _
  have hid : (1 - u) ^ 3 = (1 - u) * (1 - u) ^ 2 := by ring
  rw [hid] at hcube
  nlinarith [hsq, h1u]

end QOU.FluidDynamics
