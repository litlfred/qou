import Mathlib.Tactic
import QOU.MathlibExt.PosSemidefTraceZero

/-!
# QOU.MassTheory.BlockSDPNondegeneracy

Formalize-first groundwork for **O3′**, the amended replacement for the
operator-selection objective (owner ruling, 2026-09-05).

## What is being separated

`prop:operator-selection-lp` is degenerate: the NF basis contains the identity,
so its first Frobenius row *is* the objective vector, the program minimises
`t · x` subject to `t · x ≥ 0`, its optimal value is identically `0`, and by
strong duality the net-constraint dual is `y₀* = 0`.  The value therefore
**cannot respond to `n_target`** — which is the whole content of a shadow price.
(Commit `6b7d2ec4a8`; `y_0_eq_zero_of_radical`.)

O3 re-poses the program blockwise over the Wedderburn decomposition
`H_n(q) ≅ ⊕_λ M_{d_λ}`, replacing `n!` scalar constraints by `p(n)` PSD
constraints `Φ_λ ⪰ 0`.  A falsifier run against that form **fires**: under the
`SU(2)` specialisation the Markov weight of every `ℓ(λ) ≥ 3` partition vanishes
identically, so a `Φ` supported on such a block is feasible with objective `0`
and nonzero net — the optimum is again `0` on a ray.  Measured: that ray is the
q-antisymmetriser radical, matched to `6.4e-51`.

O3′ poses the same program on the **radical quotient**, i.e. over the blocks of
strictly positive weight.  This file proves that this is exactly the condition
that removes the degeneracy, and that dropping it brings the degeneracy back.

## What is proved here (all sorry-free)

* `obj_pos_of_pos_weights` — if every block weight is **strictly positive** and
  the blocks are PSD (so their traces are non-negative), then every feasible
  point has **strictly positive** objective.  There is no zero-objective ray,
  hence no degenerate optimum.
* `exists_zero_obj_of_zero_weight` — the converse failure, which is the O3
  falsifier as a theorem: a **single** vanishing weight suffices to exhibit a
  feasible point of objective `0` at any target.  So positivity is not a
  convenience assumption; it is the hypothesis that does the work.
* `feasible_smul` — the value is homogeneous of degree one in `n_target`.  This
  is the property the LP provably lacks (`n_target · y₀* = 0` for every target),
  and it is what makes the program price its net constraint at all.
* `trace_nonneg_of_posSemidef` — the bridge supplying the `0 ≤ t λ` hypothesis
  from `Φ_λ ⪰ 0`, so the results above are about block traces and not about an
  abstract non-negative vector invented for the proof.

## The positivity hypothesis is MEASURED on the real program, not derived

`obj_pos_of_pos_weights` takes `∀ λ, 0 < y λ` as a hypothesis, and the real
program's objective coefficient is **not** the Markov weight alone — it is
`t_λ = w_λ · χ^λ(W_atom)` (see `computations/aK_via_lp_dual_full.py`). A
character can be negative, so positivity of `t_λ` does not follow from
positivity of `w_λ`.

Measured over every row of the committed `a-K-via-lp-dual-full.witness.json`
(n = 3, 3, 6, 9, 9, 12): **no surviving block carries a negative objective
coefficient**, in any row. The one negative character at `n = 3`,
`χ^{(1,1,1)} = −0.7392`, sits on the block whose weight vanishes, so the product
is exactly `0` rather than negative. Survivor counts are **2, 2, 4, 5, 5, 7** —
matching the `≤ 2`-row prediction of `sdp_o3prime_weight_positivity_probe`
exactly, from an independent producer.

**So the hypothesis holds wherever it has been checked, and it is a statement
about the ATOM, not a structural fact.** A braid word whose character went
negative on a surviving block would falsify it and the non-degeneracy result
would not apply. Whoever implements the O3′ compute should assert
`t_λ > 0` on survivors per atom rather than assume it — the theorem below is
conditional on exactly that.

Reproduce:

```sh
python3 -c "import json;from mpmath import mp;mp.dps=25;\
d=json.load(open('computations/a-K-via-lp-dual-full.witness.json'));\
print([sum(1 for p in r['per_partition'] \
  if mp.mpf(p['y_lambda'])!=0 and mp.mpf(p['contribution'])<0) \
  for r in d['data']['rows']])"
```

## What is NOT proved here

**That O3′ selects a distinguished operator.**  It does not follow, and the
proposal says so: S4 (relative-interior exclusion) is untouched by re-posing.
Non-degeneracy means the optimal *value* is well-defined and responds to the
target; uniqueness of the *minimiser* is a separate question and stays open.

**That O3′ is a new idea.**  `computations/aK_via_lp_dual_full.py:231-258` already
states the two-row re-posing and deliberately declines to apply it.  This file
supplies the structural reason the quotient is the canonical cut rather than a
convenient one.

## References

- [boyd-vandenberghe-2004] §5.5 (complementary slackness, strong duality)
-/

namespace QOU.MassTheory.BlockSDPNondegeneracy

open Matrix Finset

variable {Λ : Type*} [Fintype Λ]

/-- The block-diagonal operator-selection objective: a weighted sum of block
traces.  `y λ` is the Markov/Plancherel weight of block `λ`, `t λ = tr Φ_λ`. -/
def obj (y t : Λ → ℝ) : ℝ := ∑ lam, y lam * t lam

/-- The net functional of the program: the total trace across blocks.  This is
the blockwise image of the LP's net constraint `Σ_i x_i = n_target`. -/
def net (t : Λ → ℝ) : ℝ := ∑ lam, t lam

/-! ### The bridge from PSD blocks to non-negative traces -/

/-- The trace of a positive-semidefinite real matrix is non-negative.  Supplies
the `0 ≤ t λ` hypothesis below from `Φ_λ ⪰ 0`, so nothing here is assumed of the
blocks beyond feasibility. -/
theorem trace_nonneg_of_posSemidef {n : ℕ} {A : Matrix (Fin n) (Fin n) ℝ}
    (hA : A.PosSemidef) : 0 ≤ A.trace := by
  refine Finset.sum_nonneg fun i _ => ?_
  exact QOU.MathlibExt.PosSemidefTraceZero.Matrix.PosSemidef.diag_nonneg hA i

/-! ### O3′: strictly positive weights remove the degeneracy -/

/-- A non-negative vector with strictly positive sum has a strictly positive
entry. -/
theorem exists_pos_of_net_pos {t : Λ → ℝ} (ht : ∀ lam, 0 ≤ t lam)
    (hnet : 0 < net t) : ∃ lam, 0 < t lam := by
  by_contra hcon
  push_neg at hcon
  have hzero : ∀ lam ∈ (univ : Finset Λ), t lam = 0 := fun lam _ =>
    le_antisymm (hcon lam) (ht lam)
  rw [net, Finset.sum_congr rfl hzero, Finset.sum_const_zero] at hnet
  exact lt_irrefl 0 hnet

/-- **O3′ is non-degenerate.**  If every surviving block carries a strictly
positive weight, then every feasible point of the program has strictly positive
objective.  In particular the optimal value is not `0`, so — unlike the LP,
whose value is identically `0` for every target — the program prices its net
constraint. -/
theorem obj_pos_of_pos_weights {y t : Λ → ℝ}
    (hy : ∀ lam, 0 < y lam) (ht : ∀ lam, 0 ≤ t lam) (hnet : 0 < net t) :
    0 < obj y t := by
  obtain ⟨lam0, hlam0⟩ := exists_pos_of_net_pos ht hnet
  refine Finset.sum_pos' (fun lam _ => ?_) ⟨lam0, Finset.mem_univ lam0, ?_⟩
  · exact mul_nonneg (le_of_lt (hy lam)) (ht lam)
  · exact mul_pos (hy lam0) hlam0

/-! ### The falsifier as a theorem: one zero weight restores the degeneracy -/

/-- **The O3 falsifier, formalised.**  A single block of vanishing weight is
enough to produce a feasible point with objective `0` at *any* positive target,
so the optimum collapses to `0` exactly as it does for the LP.  This is why O3
had to be amended to O3′: the hypothesis `∀ λ, 0 < y λ` above is doing real
work, and the `SU(2)` specialisation violates it for every `ℓ(λ) ≥ 3`. -/
theorem exists_zero_obj_of_zero_weight [DecidableEq Λ] {y : Λ → ℝ}
    {lam0 : Λ} (hy0 : y lam0 = 0) {n_target : ℝ} (hn : 0 ≤ n_target) :
    ∃ t : Λ → ℝ, (∀ lam, 0 ≤ t lam) ∧ net t = n_target ∧ obj y t = 0 := by
  refine ⟨Pi.single lam0 n_target, ?_, ?_, ?_⟩
  · intro lam
    rcases eq_or_ne lam lam0 with rfl | hne
    · simpa using hn
    · simp [hne]
  · simp [net]
  · rw [obj]
    rw [Finset.sum_eq_single lam0]
    · simp [hy0]
    · intro b _ hb
      simp [hb]
    · intro h
      exact absurd (Finset.mem_univ lam0) h

/-! ### The value tracks the target -/

/-- **Homogeneity of degree one.**  Scaling a feasible point scales the target
and the objective by the same factor.  This is precisely the property the LP
lacks: there `n_target · y₀* = 0` for every target, so the optimal value is
constant in the target and prices nothing. -/
theorem feasible_smul (y t : Λ → ℝ) {c : ℝ} (hc : 0 ≤ c)
    (ht : ∀ lam, 0 ≤ t lam) :
    (∀ lam, 0 ≤ (c • t) lam) ∧ net (c • t) = c * net t ∧
      obj y (c • t) = c * obj y t := by
  refine ⟨fun lam => mul_nonneg hc (ht lam), ?_, ?_⟩
  · simp [net, Finset.mul_sum]
  · simp [obj, Finset.mul_sum]
    exact Finset.sum_congr rfl fun lam _ => by ring

/-- **Additivity of the O3′ block objective and net trace functional (`qou-sv7h`).**
For any block weight vector `y` and trace vectors `t₁, t₂`, both `net` and `obj y`
distribute additively over `t₁ + t₂`. -/
theorem net_and_obj_add (y t₁ t₂ : Λ → ℝ) :
    net (t₁ + t₂) = net t₁ + net t₂ ∧
    obj y (t₁ + t₂) = obj y t₁ + obj y t₂ := by
  refine ⟨?_, ?_⟩
  · rw [net, net, net, ← Finset.sum_add_distrib]
    rfl
  · rw [obj, obj, obj, ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun lam _ => by ring

end QOU.MassTheory.BlockSDPNondegeneracy
