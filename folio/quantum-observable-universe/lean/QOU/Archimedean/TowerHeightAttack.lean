import QOU.Archimedean.HyperbolicVolumeTranscendence
import Mathlib.Analysis.SpecificLimits.Basic

/-!
# QOU.Archimedean.TowerHeightAttack — the tower-height contrapositive, examined

[`rem:yekutieli-transcendence-shadow`](../../../quantum-observable-universe/predicted-spectra/yekutieli-transcendence-shadow.md)
argues for algebraic independence of `Vol(4₁)`, `Vol(5₂)`, `Vol(𝓑₃)` by a
contrapositive:

1. a polynomial relation `P(V₁, V₂, V₃) = 0` …
2. … *"would force holonomy contributions at different tower levels to close up
   after finitely many levels"*;
3. closure at finite height gives `Φ_n = 0` for `n > h`, hence `κ_n = 0` there
   (`CSEvaluationFaithful`, contrapositive);
4. which contradicts perpetual obstruction (`κ_n ≠ 0` for all `n`).

Note (2026-11-15, owner decision, PR #7747, bean `qou-lx8f`): the premise of
step 4 is withdrawn for the Kummer tower of Bring's surface, where `κ_n = 0`
for `n ∣ χ = -6`. Only the weaker "κ_n ≠ 0 for `n ∤ 6`" is available, and it
does not by itself contradict closure at finite height.

The prune in `QOU.Archimedean.SurrealGradingPrune` showed the *squeeze* cannot
supply step 1→4. This file examines the contrapositive itself, which is the
corpus's other route. Result: **step 1 ⟹ 2 is invalid as stated, and becomes
valid — with an immediately effective height — exactly when the tower
decomposition is graded.**

## §1 The gap (proved)

`VolumeTowerDecomposition` (in `HyperbolicVolumeTranscendence`) is an
**ungraded** decomposition: its content is `HasSum levelContribution
totalVolume`, a convergent sum of reals. A polynomial relation among the
*totals* is therefore **one real equation**, and one equation cannot force
term-wise vanishing.

`relation_does_not_force_closure` exhibits two decompositions over any tower
with **every** level non-zero whose totals satisfy the non-trivial ℚ-linear
relation `3·A − 2·B = 0`. Linear is a special case of polynomial, so the
counterexample kills the general inference: a relation among the totals is
compatible with a tower that never closes.

## §2 A second, independent problem (proved)

The only concrete decompositions the corpus builds —
`volumeTowerDecomp_4_1`, `volumeTowerDecomp_5_2`, `volumeTowerDecomp_B3` — are
all `baselineDecomposition`, i.e. `Φ₀ = Vol`, `Φ_n = 0` for `n ≥ 1`. That is a
tower closed at height `0`: the *opposite* of perpetual obstruction.
`perpetual_excludes_baseline` proves no `CSEvaluationFaithful` over a perpetual
tower can use one. So the argument's step 3 currently has no instance to run
on. (The file's own docstring flags the baseline as trivial and promises a
"REFINEMENT"; the refinement does not exist yet.)

## §3 The repair, and where the effective height comes from (proved)

Suppose instead the decomposition is **graded**: level `n` contributes at
`q`-grade `n`, and a relation over `ℚ[q,q⁻¹]` must hold **grade by grade**.
Then a relation is no longer one equation but one equation *per level*, and
everything the contrapositive wants follows:

* `gradewise_determines_level` — a gradewise relation pins each level of one
  tower to the corresponding level of the other.
* `gradewise_closure_propagates` — so closure transfers level-by-level.
* `recurrence_step` — the general shape. A relation of `q`-degree `D`
  convolves grade `k` of the relation with grade `n−k` of the tower, so the
  grade-`n` equation is `Σ_{k≤D} c_k Φ_{n−k} = 0`: an **order-`D` linear
  recurrence**. With `c₀ ≠ 0`, once `D` consecutive levels vanish every later
  level vanishes — the tower closes.
* `closed_above_window` — the induction: a vanishing window of width `D`
  closes the tower from there on.

**This answers the effectivity question.** The height is `h(P) = deg_q P`,
read straight off the relation — no arithmetic input needed. The entire
difficulty migrates from "bound the height" to "**grade the tower**".

That is the same conclusion the surreal prune reaches from the other side:
`SurrealGradingPrune.grade_separation_needs_nonstandard` says grade separation
needs a non-standard object, and a graded tower is exactly such an object
(level `n` at `ω`-grade `n`). The two routes converge on one target.

## What is NOT claimed

None of this proves or refutes `HyperbolicVolumeIndependence`. §1 and §2 are
**scope-(a)** findings about the *stated argument*, not about the conjecture:
the conjecture may well be true and provable by a graded version of exactly
this route. §3 is a conditional: it supplies the height bound *given* a
grading, and constructing the grading is open (bean `qou-5b23`).

## References

* [yekutieli2015] Yekutieli, *Nonabelian multiplicative integration on surfaces*.
* [zagier1986] Zagier, *Hyperbolic manifolds and special values of Dedekind
  zeta-functions*.
-/

namespace QOU.Archimedean.TowerHeight

open QOU.Archimedean

/-! ## §0  A note on universes (AGENTS.md §7d)

`RecursiveBraneTower` carries twelve `Type*`-valued universe parameters and
`VolumeTowerDecomposition` inherits them through its `tower` field, so both are
*universe-carrying* in the §7d sense: each unpinned occurrence in a signature
elaborates with fresh rigid universes. A theorem binding a tower **and**
independently quantifying `∃ A B : VolumeTowerDecomposition` therefore fails to
unify (`RecursiveBraneTower.{u_1,…} ≠ RecursiveBraneTower.{u_24,…}`).

Rather than positionally apply `.{…}` to two auto-bound declarations whose
universe order is an elaboration artifact (§7d U5 forbids exactly that), this
file uses the §7d U4 route — **restate so unification happens inside one
binder**. The mathematical content of §1 involves no tower at all, so it is
stated on the underlying summable sequences (`relation_does_not_force_closure`);
the packaged form (`geomDecomp_relation`) then mentions a single tower binder
and derives both decompositions from it. -/

/-! ## §1  A relation among the totals does not force closure -/

/-- Geometric tower with ratio `r`, every level non-zero, total `s·(1-r)⁻¹`.
Used to package the counterexample as a genuine `VolumeTowerDecomposition`. -/
noncomputable def geomDecomp (tower : QOU.Torsion.RecursiveBraneTower)
    (s r : ℝ) (hs : 0 < s) (hr0 : 0 ≤ r) (hr1 : r < 1) :
    VolumeTowerDecomposition where
  tower := tower
  totalVolume := s * (1 - r)⁻¹
  totalVolume_pos := by
    have : 0 < 1 - r := by linarith
    positivity
  levelContribution := fun n => s * r ^ n
  summable := by
    have hgeo : Summable (fun n : ℕ => s * r ^ n) :=
      ((hasSum_geometric_of_lt_one hr0 hr1).mul_left s).summable
    refine hgeo.congr (fun n => ?_)
    exact (abs_of_nonneg (by positivity)).symm
  sum_eq := (hasSum_geometric_of_lt_one hr0 hr1).mul_left s
  baseline_dominant := by simpa using hs

@[simp] theorem geomDecomp_level (tower : QOU.Torsion.RecursiveBraneTower)
    (s r : ℝ) (hs : 0 < s) (hr0 : 0 ≤ r) (hr1 : r < 1) (n : ℕ) :
    (geomDecomp tower s r hs hr0 hr1).levelContribution n = s * r ^ n := rfl

@[simp] theorem geomDecomp_total (tower : QOU.Torsion.RecursiveBraneTower)
    (s r : ℝ) (hs : 0 < s) (hr0 : 0 ≤ r) (hr1 : r < 1) :
    (geomDecomp tower s r hs hr0 hr1).totalVolume = s * (1 - r)⁻¹ := rfl

/-- **The stated inference fails.**

There exist two tower decompositions — over *any* brane tower — with **every**
level contribution non-zero, whose totals satisfy the non-trivial ℚ-linear
relation `3·A − 2·B = 0`.

A relation among the totals is one real equation; it cannot reach the
individual levels. Since linear relations are polynomial relations, this
refutes the general step *"a polynomial relation would force the holonomy
contributions to close up after finitely many levels"* for the **ungraded**
`VolumeTowerDecomposition` the corpus actually defines.

Scope-(a): a statement about this inference, not about the conjecture. -/
theorem relation_does_not_force_closure :
    ∃ (ΦA ΦB : ℕ → ℝ) (VA VB : ℝ),
      HasSum ΦA VA ∧ HasSum ΦB VB ∧
      Summable (fun n => |ΦA n|) ∧ Summable (fun n => |ΦB n|) ∧
      (∀ n, ΦA n ≠ 0) ∧ (∀ n, ΦB n ≠ 0) ∧
      3 * VA - 2 * VB = 0 := by
  have hA : HasSum (fun n : ℕ => (1 : ℝ) * (1 / 2 : ℝ) ^ n) (1 * (1 - 1 / 2 : ℝ)⁻¹) :=
    (hasSum_geometric_of_lt_one (by norm_num) (by norm_num)).mul_left 1
  have hB : HasSum (fun n : ℕ => (2 : ℝ) * (1 / 3 : ℝ) ^ n) (2 * (1 - 1 / 3 : ℝ)⁻¹) :=
    (hasSum_geometric_of_lt_one (by norm_num) (by norm_num)).mul_left 2
  refine ⟨_, _, _, _, hA, hB, ?_, ?_, fun n => ?_, fun n => ?_, by norm_num⟩
  · exact hA.summable.congr fun n => (abs_of_nonneg (by positivity)).symm
  · exact hB.summable.congr fun n => (abs_of_nonneg (by positivity)).symm
  · positivity
  · positivity

/-- The same counterexample packaged as two genuine `VolumeTowerDecomposition`s
over one brane tower — every level non-zero, totals satisfying `3·A − 2·B = 0`.

Stated with a *single* universe-carrying binder (`tower`) and both
decompositions derived from it, per §7d U4. -/
theorem geomDecomp_relation (tower : QOU.Torsion.RecursiveBraneTower) :
    (∀ n, (geomDecomp tower 1 (1/2) one_pos (by norm_num) (by norm_num)
             ).levelContribution n ≠ 0) ∧
    (∀ n, (geomDecomp tower 2 (1/3) two_pos (by norm_num) (by norm_num)
             ).levelContribution n ≠ 0) ∧
    3 * (geomDecomp tower 1 (1/2) one_pos (by norm_num) (by norm_num)).totalVolume
      - 2 * (geomDecomp tower 2 (1/3) two_pos (by norm_num) (by norm_num)).totalVolume
      = 0 := by
  refine ⟨fun n => ?_, fun n => ?_, ?_⟩
  · simp only [geomDecomp_level, one_mul]; positivity
  · simp only [geomDecomp_level]; positivity
  · simp only [geomDecomp_total]; norm_num

/-! ## §2  The corpus's concrete decompositions are already closed -/

/-- **No `CSEvaluationFaithful` over a perpetual tower can use a
`baselineDecomposition`.**

`baselineDecomposition` sets `Φ_n = 0` for `n ≥ 1` — a tower closed at height
`0`. Faithfulness over a perpetual tower forces every `Φ_n ≠ 0`. The two are
contradictory, so the corpus's only concrete decompositions
(`volumeTowerDecomp_4_1/5_2/B3`, all baseline) cannot instantiate step 3 of the
contrapositive. -/
theorem perpetual_excludes_baseline
    (csf : CSEvaluationFaithful)
    (h_tower : ∀ n, Nonempty (csf.ylc.obstructionClass n))
    (tower : QOU.Torsion.RecursiveBraneTower) (vol : ℝ) (hvol : 0 < vol)
    (hbase : csf.vtd = baselineDecomposition tower vol hvol) : False := by
  have h := QOU.Archimedean.infinitely_many_nonzero csf h_tower 1
  rw [hbase] at h
  exact h (by simp [baselineDecomposition])

/-! ## §3  Graded relations: per-level constraints and an effective height -/

/-- **A gradewise relation determines each level.**

Contrast with §1: when the relation holds at every grade rather than only on
the totals, level `n` of one tower is pinned to level `n` of the other. This is
the whole difference between the failed and the repaired inference. -/
theorem gradewise_determines_level {c₁ c₂ : ℝ} {ΦA ΦB : ℕ → ℝ}
    (hrel : ∀ n, c₁ * ΦA n + c₂ * ΦB n = 0) (n : ℕ) :
    c₁ * ΦA n = -(c₂ * ΦB n) := by
  linarith [hrel n]

/-- Closure transfers level-by-level under a gradewise relation. -/
theorem gradewise_closure_propagates {c₁ c₂ : ℝ} (hc₁ : c₁ ≠ 0) {ΦA ΦB : ℕ → ℝ}
    (hrel : ∀ n, c₁ * ΦA n + c₂ * ΦB n = 0) {n : ℕ} (h : ΦB n = 0) :
    ΦA n = 0 := by
  have hd := gradewise_determines_level hrel n
  rw [h, mul_zero, neg_zero] at hd
  exact (mul_eq_zero.mp hd).resolve_left hc₁

/-- **The recurrence step — where the effective height comes from.**

A relation of `q`-degree `D` convolves grade `k` of the relation with grade
`n − k` of the tower, so the grade-`n` equation is
`Σ_{k ≤ D} c_k · Φ_{n−k} = 0` — an order-`D` linear recurrence. With
`c₀ ≠ 0`, a vanishing window of the `D` preceding levels forces `Φ_n = 0`.

Hence `h(P) = deg_q P`: the height bound is read off the relation, with no
arithmetic input. Effectivity is free once the tower is graded. -/
theorem recurrence_step {D : ℕ} {c : ℕ → ℝ} (hc0 : c 0 ≠ 0) {Φ : ℕ → ℝ}
    {n : ℕ} (hrec : ∑ k ∈ Finset.range (D + 1), c k * Φ (n - k) = 0)
    (hprev : ∀ k, 1 ≤ k → k ≤ D → Φ (n - k) = 0) : Φ n = 0 := by
  rw [Finset.sum_range_succ'] at hrec
  have hzero : ∑ i ∈ Finset.range D, c (i + 1) * Φ (n - (i + 1)) = 0 :=
    Finset.sum_eq_zero fun i hi => by
      rw [hprev (i + 1) (Nat.le_add_left 1 i)
        (Nat.succ_le_of_lt (Finset.mem_range.mp hi)), mul_zero]
  rw [hzero, zero_add, Nat.sub_zero] at hrec
  exact (mul_eq_zero.mp hrec).resolve_left hc0

/-- **Closure above a vanishing window.** Once `D` consecutive levels vanish,
the order-`D` recurrence closes the tower from there on: `Φ_n = 0` for every
`n ≥ N`. This is the finite-height conclusion the contrapositive needs. -/
theorem closed_above_window {D N : ℕ} (hDN : D ≤ N) {c : ℕ → ℝ} (hc0 : c 0 ≠ 0)
    {Φ : ℕ → ℝ}
    (hrec : ∀ n, N ≤ n → ∑ k ∈ Finset.range (D + 1), c k * Φ (n - k) = 0)
    (hwin : ∀ j, N - D ≤ j → j < N → Φ j = 0) :
    ∀ n, N ≤ n → Φ n = 0 := by
  intro n hn
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    refine recurrence_step hc0 (hrec n hn) (fun k hk1 hkD => ?_)
    rcases lt_or_ge (n - k) N with hlt | hge
    · exact hwin (n - k) (by omega) hlt
    · exact ih (n - k) (by omega) hge

/-! ## §4  Jet-order independence does not transfer to algebraic independence

`JetOrderIndependence` asserts that the order-`N` jet-coefficient Jacobian of
`tr_M(4₁), tr_M(5₂), tr_M(𝓑₃)` has full rank `3` — **linear** independence of
the coefficient vectors. The gap-closing reduction then wants to transfer this,
via `JetTransportImpliesIndependence`, to **algebraic** independence of the
volumes.

That transfer cannot be a transfer *of independence*, because the jet series
are algebraically **dependent** — necessarily so:

* each `tr_M(K)` is a rational function of `u = √q` (verified: numerator /
  denominator `u`-degrees `14/9`, `16/9`, `18/9` for `4₁ / 5₂ / 𝓑₃`), so all
  three lie in `ℚ(u)`;
* `ℚ(u)` has transcendence degree `1` over `ℚ`, so **any two** of them already
  satisfy a polynomial relation, let alone all three.

The minimal degree is not predicted by that argument; it is measured. The probe
[`computations/jet_algebraic_independence_probe.py`](../../../../computations/jet_algebraic_independence_probe.py)
finds, by exact null space over `ℚ`:

| degree `d` | equations | null space | stable under more equations? |
|---|---|---|---|
| ≤ 6 | 93 → 385 | `0` | yes — no relation |
| 7 | 129 → 421 | `3` | yes — **genuine**, 3-dimensional |

So the minimal degree of an algebraic relation among the three canonical
Markov-trace jets is exactly `7`.

`linearIndependent_not_algebraicallyIndependent` below is the general reason a
rank certificate cannot deliver algebraic independence, in the cheapest
possible form: `t`, `t²`, `t³` are linearly independent yet satisfy the
degree-2 relation `z = x·y`. Rank counts linear relations; it says nothing
about polynomial ones. -/

/-- **Linear independence does not imply algebraic independence.**

`t`, `t²`, `t³` are linearly independent as functions, yet annihilated by
`z − x·y`. So a full-rank jet Jacobian — which is exactly a linear-independence
certificate — cannot by itself support an algebraic-independence conclusion. -/
theorem linearIndependent_not_algebraicallyIndependent :
    ∃ f g h : ℝ → ℝ,
      (∀ a b c : ℝ, (∀ t : ℝ, a * f t + b * g t + c * h t = 0) →
        a = 0 ∧ b = 0 ∧ c = 0) ∧
      (∀ t : ℝ, h t - f t * g t = 0) := by
  refine ⟨fun t => t, fun t => t ^ 2, fun t => t ^ 3, fun a b c hlin => ?_,
          fun t => by ring⟩
  have h1 := hlin 1
  have h2 := hlin (-1)
  have h3 := hlin 2
  norm_num at h1 h2 h3
  refine ⟨by linarith, by linarith, by linarith⟩

/-- **Three-tower gradewise relation pins each level (`qou-zynz`):**
In a graded three-manifold relation `c₁ Φ_A(n) + c₂ Φ_B(n) + c₃ Φ_C(n) = 0`,
level `n` of tower `A` is determined by level `n` of towers `B` and `C`. -/
theorem gradewise_three_term_determines_level {c₁ c₂ c₃ : ℝ} {ΦA ΦB ΦC : ℕ → ℝ}
    (hrel : ∀ n, c₁ * ΦA n + c₂ * ΦB n + c₃ * ΦC n = 0) (n : ℕ) :
    c₁ * ΦA n = -(c₂ * ΦB n + c₃ * ΦC n) := by
  linarith [hrel n]

/-- **Three-tower gradewise closure propagation (`qou-zynz`):**
When `c₁ ≠ 0`, vanishing of `Φ_B(n)` and `Φ_C(n)` at grade `n` forces `Φ_A(n) = 0`,
contrasting with the ungraded `VolumeTowerDecomposition` sum relation. -/
theorem gradewise_three_term_closure_propagates {c₁ c₂ c₃ : ℝ} (hc₁ : c₁ ≠ 0)
    {ΦA ΦB ΦC : ℕ → ℝ}
    (hrel : ∀ n, c₁ * ΦA n + c₂ * ΦB n + c₃ * ΦC n = 0) {n : ℕ}
    (hB : ΦB n = 0) (hC : ΦC n = 0) :
    ΦA n = 0 := by
  have hd := gradewise_three_term_determines_level hrel n
  rw [hB, hC, mul_zero, mul_zero, add_zero, neg_zero] at hd
  exact (mul_eq_zero.mp hd).resolve_left hc₁

end QOU.Archimedean.TowerHeight
