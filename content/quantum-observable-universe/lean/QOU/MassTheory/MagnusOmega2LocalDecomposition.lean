/-
# QOU.MassTheory.MagnusOmega2LocalDecomposition — the per-window LOCAL structure of the Magnus Ω₂ pairing

Backs the structural assertions of the per-window-local tr-decay result (bean `qou-o6ov`,
PR #6311; probe `computations/deltalambda/magnus_tr_decay_perpair_cluster_probe.py`).

The probe measures that `tr(ρ_λ Ω₂_λ)/dim_λ` decays with `b(λ)=n−λ₁` **per window** — every
local commutator window peaks at `b=1`, so the decay is not an inter-window cancellation. That
*decay* is an empirical fact and is **NOT** formalized here (it is measured, and remains open;
see the audit). What IS formalizable — and is proved here, sorry-free — are the two structural
identities the probe *relies on*:

1. `commutator_eq_zero_of_commute` — a commutator of commuting operators is zero. This is the
   exact justification for the probe's `if |a−b| ≠ 1: continue` (far-commutativity): germs at
   Coxeter distance ≥ 2 commute, so their commutator drops from `Ω₂`.

2. `omega2_reduces_to_adjacent` — consequently the full ordered-pair sum
   `Σ_{i<j} ⁅A_i,A_j⁆` equals the sum over the *adjacent* (non-commuting) pairs alone. This is
   the operator identity `Ω₂ = ½ Σ_{(a,a+1)} mult·⁅A_a,A_{a+1}⁆` — Ω₂ is a lattice sum of
   3-strand-local windows.

3. `trace_rho_localSum` / `trace_rho_weightedLocalSum` — the trace of `ρ` against a (weighted)
   sum of local windows is the (weighted) sum of the per-window traces. This is the exact
   algebraic identity the probe's numeric self-check verifies (`2·tr(ρΩ₂) = Σ mult·tr(ρ⁅A_a,A_{a+1}⁆)`,
   confirmed to 4.3e-57). It makes the b-decay *attributable window-by-window*, which is what
   lets "per-window vs inter-window" be a well-posed question.

The `ρ = I` control `tr(Ω₂)=0` is already proved sorry-free as
`QOU.MassTheory.trace_commutator_eq_zero` (MagnusPairingSignStructure.lean) — cited, not
re-proved.

Base ring (§7c): all of this is generic `CommRing R` matrix algebra — no ordering, no
`Real.*`, no archimedean construct. `n` is any `Fintype`; the crossing/window index is any
`Fintype`/`Finset`. Nothing physical is asserted; no MeV, no fit, no `q₀`.

HONESTY (STRICT). These formalize the algebraic SKELETON (the far-comm reduction and the linear
per-window decomposition), NOT the analytic content. The theorem `|tr(ρ_λ[A_a,A_{a+1}])|/dim_λ`
decays with `b` is the open work and carries no Lean here — stating it as `True`/`rfl` or
axiomatizing it would be laundering and is deliberately not done.
-/
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic

namespace QOU.MassTheory

open Matrix Finset

variable {R : Type*} [CommRing R] {n : Type*} [Fintype n]

/-- **Far-commutativity reduction core.** A commutator of commuting operators vanishes:
`Commute A B → A*B − B*A = 0`. For the Magnus germs `A_a = q·(∂_q σ_a)·σ_a⁻¹`, germs at
Coxeter distance `|a−b| ≥ 2` commute (their generators do), so `⁅A_a,A_b⁆ = 0` — the term
drops from `Ω₂`. This is the operator content of the probe's `if |a−b| ≠ 1: continue`. -/
theorem commutator_eq_zero_of_commute (A B : Matrix n n R) (h : Commute A B) :
    A * B - B * A = 0 :=
  sub_eq_zero_of_eq h.eq

/-- **Ω₂ reduces to adjacent windows.** Sum a family of commutators `⁅fst p, snd p⁆` over a
finset `s` of ordered crossing-pairs; if every *non-adjacent* pair commutes, the sum equals the
sum over the *adjacent* pairs alone. This is the operator identity
`Σ_{i<j} ⁅A_i,A_j⁆ = Σ_{adjacent} ⁅A_a,A_{a+1}⁆` — far pairs contribute nothing, so `Ω₂` is a
lattice sum of 3-strand-local windows. -/
theorem omega2_reduces_to_adjacent {ι : Type*} (s : Finset ι)
    (fst snd : ι → Matrix n n R) (adj : ι → Prop) [DecidablePred adj]
    (hfar : ∀ p ∈ s, ¬ adj p → Commute (fst p) (snd p)) :
    (∑ p ∈ s, (fst p * snd p - snd p * fst p))
      = ∑ p ∈ s.filter adj, (fst p * snd p - snd p * fst p) := by
  rw [← Finset.sum_filter_add_sum_filter_not s adj (fun p => fst p * snd p - snd p * fst p)]
  have hzero : (∑ p ∈ s.filter (fun p => ¬ adj p),
      (fst p * snd p - snd p * fst p)) = 0 := by
    refine Finset.sum_eq_zero ?_
    intro p hp
    rw [Finset.mem_filter] at hp
    exact commutator_eq_zero_of_commute _ _ (hfar p hp.1 hp.2)
  rw [hzero, add_zero]

/-- **Per-window trace decomposition (linearity).** The trace of `ρ` against a sum of local
window operators is the sum of the per-window traces:
`tr(ρ · Σ_k O_k) = Σ_k tr(ρ · O_k)`. This is the algebraic identity the probe's numeric
self-check confirms; it makes `tr(ρ Ω₂)`'s b-decay attributable window-by-window. -/
theorem trace_rho_localSum {ι : Type*} (s : Finset ι)
    (ρ : Matrix n n R) (O : ι → Matrix n n R) :
    (ρ * ∑ k ∈ s, O k).trace = ∑ k ∈ s, (ρ * O k).trace := by
  rw [Finset.mul_sum, Matrix.trace_sum]

/-- **Weighted per-window trace decomposition.** With integer/scalar window multiplicities `c k`
(the probe's `mult(a,a+1)`), `tr(ρ · Σ_k c_k • O_k) = Σ_k c_k · tr(ρ · O_k)`. Instantiated at
`O_k = ⁅A_a,A_{a+1}⁆` and `c_k = mult` this is exactly the probe's self-check identity
`2·tr(ρ Ω₂) = Σ mult·tr(ρ ⁅A_a,A_{a+1}⁆)`. -/
theorem trace_rho_weightedLocalSum {ι : Type*} (s : Finset ι)
    (ρ : Matrix n n R) (c : ι → R) (O : ι → Matrix n n R) :
    (ρ * ∑ k ∈ s, c k • O k).trace = ∑ k ∈ s, c k * (ρ * O k).trace := by
  rw [Finset.mul_sum, Matrix.trace_sum]
  refine Finset.sum_congr rfl ?_
  intro k _
  rw [mul_smul_comm, Matrix.trace_smul, smul_eq_mul]

end QOU.MassTheory
