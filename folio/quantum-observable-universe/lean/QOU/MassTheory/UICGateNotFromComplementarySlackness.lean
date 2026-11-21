import QOU.ParticleInteractions.operator_selection_lp
import Mathlib.Algebra.Order.Ring.Int
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.NormNum

/-!
# QOU.MassTheory.UICGateNotFromComplementarySlackness

**The Pass-2 sign gate in `hecke_core_legacy.unified_iterative_correction` is
not a consequence of complementary slackness on the operator-selection LP.**

## What the producer does, and what it says it is doing

`computations/hecke_core_legacy.py:2176-2199` keeps a Wedderburn block only when
`final_tr_sign <= 0` and returns that gated sum.  Its comment derives the gate
from LP duality, verbatim:

> LP duality theorem: on the OPTIMAL primal-dual pair `(Φ*, y*)`,
> `y_λ* × ⟨Φ*, π_λ⟩_F = 0` for every partition `λ`.
> So `y_λ* > 0` only when the Frobenius constraint is TIGHT at the
> atom's FINAL state, i.e. `tr(M_λ(W_atom)) ≤ 0`.  Partitions with
> positive final trace are SLACK → `y_λ* = 0` → zero contribution.

The LP being invoked exists: it is [`prop:operator-selection-lp`], formalised in
`QOU.ParticleInteractions.operator_selection_lp`, whose
`OperatorSelectionLpContext` carries the cost vector `t`, the Frobenius Gram `G`,
a primal point `x*` and the Frobenius multipliers `s` (the narrative's `y*`),
and whose `complementary_slackness_x_star` is exactly `∀ i, sᵢ (Gx*)ᵢ = 0`.

## Where the inference fails

The comment identifies two different vectors.  Complementary slackness
constrains the **constraint value** `(Gx*)ᵢ` — a function of the operator the LP
is *selecting*.  The gate reads the **cost** entry `t_λ = tr(M_λ(W_atom))` — a
datum of the atom, fixed before any optimisation, appearing in the LP only as
the objective.  Three results below, and one witness:

* `frobeniusValue_nonpos_iff_eq_zero` — on any primal-feasible point the
  constraint value is non-negative, so `≤ 0` and `= 0` are the *same* predicate
  on it.  A sign gate read on a Frobenius constraint value is therefore the
  tightness gate, and keeps only blocks sitting exactly at zero.  The producer's
  gate keeps 4 of 10 blocks at `A = 2` and returns `-0.0896`, so it is not
  reading a constraint value of any feasible point of this LP.
* `frobeniusValue_of_diagonal` / `complementarySlackness_diagonal_iff` — in the
  Wedderburn basis the block projectors are orthogonal idempotents, so
  `G_{λμ} = tr_M(P_λ P_μ) = δ_{λμ} tr_M(P_λ)` is diagonal, complementary
  slackness decouples to `s_λ · G_{λλ} · x_λ = 0`, and the cost vector does not
  occur in it at all.  (Measured independently in
  `computations/probes/h6_block_selection_lp_probe.py`, which found the LP
  selects 10-11 of 11 blocks at every reachable target for this reason.)
* `exists_lpData_activeSet_gateSet_disjoint` — the refutation.  There is a
  genuine `OperatorSelectionLpContext` (built through the corpus's own
  `ofCertificate`, so every LP hypothesis holds and the duality gap is *derived*)
  in which complementary slackness holds, the active set `{i | 0 < sᵢ}` is
  non-empty, the gate set `{i | tᵢ ≤ 0}` is non-empty, and the two are
  **disjoint**.  So `y_λ* > 0` does not imply `t_λ ≤ 0`: the implication the
  comment asserts has a counterexample inside the very program it cites.

## Scope

This is a **scope-(b) structural exclusion** in the sense of AGENTS.md
§"Before declaring refuted": the invariant is *primal feasibility of the
Frobenius constraints* (`0 ≤ (Gx)ᵢ`, a defining conjunct of `IsFeasible`),
together with the *orthogonality of Wedderburn projectors* which makes the Gram
diagonal.  It excludes complementary slackness on this LP as a derivation of a
sign gate on the cost vector — for every `n`, every `q`, and every trace
convention, since neither invariant depends on them.

It does **not** say the producer's gate is numerically wrong, and it does not
exclude some *other* selection principle.  It says this justification has no
referent, which is what the owner's 2026-09-12 hunt asked.

Bean `qou-8urh`; appends to `qou-t6be`, `qou-zlra`, `qou-brng`.
-/

-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP duality, complementary slackness)
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/operator-selection-lp.md

namespace QOU.MassTheory.UICGateLP

open QOU.ParticleInteractions

/-- **A Frobenius constraint value cannot be negative on a feasible point.**

`IsFeasible` demands `0 ≤ (Gx)ᵢ` for every `i`, so the predicate `(Gx)ᵢ ≤ 0`
collapses to `(Gx)ᵢ = 0`.  "Sign gate" and "tightness gate" are the same
predicate when read on a constraint value; they differ only when read on
something that is *not* a constraint value of a feasible point. -/
theorem frobeniusValue_nonpos_iff_eq_zero {R : Type*} [CommRing R] [PartialOrder R]
    {d : ℕ} {G : Fin d → Fin d → R} {x : Fin d → R} {i : Fin d}
    (hx : 0 ≤ Finset.univ.sum fun j => G i j * x j) :
    (Finset.univ.sum fun j => G i j * x j) ≤ 0
      ↔ (Finset.univ.sum fun j => G i j * x j) = 0 :=
  ⟨fun h => le_antisymm h hx, fun h => h.le⟩

/-- The same statement for the corpus context, at its own candidate `x*`:
every block's Frobenius value is `≥ 0`, so gating on `≤ 0` keeps exactly the
tight blocks. -/
theorem gateSet_eq_tightSet {R : Type*} [CommRing R] [LinearOrder R]
    [IsStrictOrderedRing R] (ctx : OperatorSelectionLpContext R) (i : Fin ctx.d) :
    (Finset.univ.sum fun j => ctx.G i j * ctx.x_star j) ≤ 0
      ↔ (Finset.univ.sum fun j => ctx.G i j * ctx.x_star j) = 0 :=
  frobeniusValue_nonpos_iff_eq_zero (ctx.x_star_feasible.2 i)

/-- **Orthogonal Wedderburn projectors make the Gram diagonal**, and a diagonal
Gram collapses the Frobenius constraint value to a single product.

`G_{λμ} = tr_M(P_λ P_μ) = δ_{λμ} tr_M(P_λ)` because block projectors are
orthogonal idempotents. -/
theorem frobeniusValue_of_diagonal {R : Type*} [CommRing R]
    {d : ℕ} {G : Fin d → Fin d → R} {x : Fin d → R} {i : Fin d}
    (hdiag : ∀ a b : Fin d, a ≠ b → G a b = 0) :
    (Finset.univ.sum fun j => G i j * x j) = G i i * x i := by
  refine Finset.sum_eq_single i ?_ ?_
  · intro b _ hb
    rw [hdiag i b (Ne.symm hb), zero_mul]
  · intro h
    exact absurd (Finset.mem_univ i) h

/-- **Complementary slackness does not mention the cost vector.**

Under a diagonal Gram the condition `∀ i, sᵢ (Gx)ᵢ = 0` is equivalent to
`∀ i, sᵢ · G_{ii} · xᵢ = 0`, an equation in the multipliers, the block norms and
the *selected operator's* coefficients.  The Markov traces of the atom — the
producer's `t_λ` — do not occur.  No predicate on `t` follows from it. -/
theorem complementarySlackness_diagonal_iff {R : Type*} [CommRing R]
    {d : ℕ} {G : Fin d → Fin d → R} {x s : Fin d → R}
    (hdiag : ∀ a b : Fin d, a ≠ b → G a b = 0) :
    (∀ i, s i * Finset.univ.sum (fun j => G i j * x j) = 0)
      ↔ ∀ i, s i * (G i i * x i) = 0 := by
  constructor
  · intro h i
    rw [← frobeniusValue_of_diagonal (x := x) hdiag]
    exact h i
  · intro h i
    rw [frobeniusValue_of_diagonal (x := x) hdiag]
    exact h i

/-! ### The witness

A two-index instance with `G = I`, `x* = (1, 0)`, `n_target = 1`, multipliers
`s = (0, 2)` and `y₀* = -1`, hence — by dual feasibility `tⱼ = y₀ + Σᵢ sᵢGᵢⱼ` —
cost `t = (-1, 1)`.  Every LP hypothesis holds and complementary slackness holds,
yet the active index is `1` while the only index the sign gate keeps is `0`. -/

private def G2 : Fin 2 → Fin 2 → ℤ := fun i j => if i = j then 1 else 0
private def x2 : Fin 2 → ℤ := ![1, 0]
private def s2 : Fin 2 → ℤ := ![0, 2]
private def t2 : Fin 2 → ℤ := ![-1, 1]

/-- The witness context, built through the corpus's own `ofCertificate`, so the
zero duality gap is *derived* from the certificate rather than assumed. -/
private def ctxW : OperatorSelectionLpContext ℤ :=
  OperatorSelectionLpContext.ofCertificate 2 2 (1 : ℤ) t2 G2 x2 (-1) s2
    (by decide) (by decide) (by decide) (by decide) (by decide)

/-- **The refutation.**

The witness data satisfy every hypothesis of the operator-selection LP —
non-negative multipliers, dual feasibility `tⱼ = y₀ + Σᵢ sᵢGᵢⱼ`, the net
constraint, Frobenius positivity, and complementary slackness — and yet

* the active set `{i | 0 < sᵢ}` is non-empty (it is `{1}`);
* the gate set `{i | tᵢ ≤ 0}` is non-empty (it is `{0}`);
* the two are **disjoint**.

So on the program the producer's comment cites, `y_λ* > 0` does not imply
`t_λ ≤ 0`.  The Pass-2 sign gate is not a consequence of complementary
slackness — the implication has a counterexample inside the LP itself.

The same data are packaged as `ctxW`, whose mere type-correctness certifies
that they form a genuine `OperatorSelectionLpContext` with a *derived* zero
duality gap; `ctxW_t`, `ctxW_s` and `ctxW_G` identify its fields with the data
used here. -/
theorem exists_lpData_activeSet_gateSet_disjoint :
    ∃ (d : ℕ) (n_target y_0 : ℤ) (t : Fin d → ℤ) (G : Fin d → Fin d → ℤ)
      (x s : Fin d → ℤ),
      (∀ i, 0 ≤ s i) ∧
      (∀ j, t j = y_0 + Finset.univ.sum fun i => s i * G i j) ∧
      (Finset.univ.sum fun j => x j) = n_target ∧
      (∀ i, 0 ≤ Finset.univ.sum fun j => G i j * x j) ∧
      (∀ i, s i * Finset.univ.sum (fun j => G i j * x j) = 0) ∧
      (∃ i, 0 < s i) ∧
      (∃ i, t i ≤ 0) ∧
      (∀ i, ¬ (0 < s i ∧ t i ≤ 0)) := by
  refine ⟨2, 1, -1, t2, G2, x2, s2, ?_, ?_, ?_, ?_, ?_, ⟨1, ?_⟩, ⟨0, ?_⟩, ?_⟩ <;> decide

/-- `ctxW` carries exactly the witness cost vector. -/
theorem ctxW_t : @OperatorSelectionLpContext.t ℤ _ _ _ ctxW = t2 := by
  dsimp [ctxW, OperatorSelectionLpContext.ofCertificate]

/-- `ctxW` carries exactly the witness multipliers. -/
theorem ctxW_s : @OperatorSelectionLpContext.s ℤ _ _ _ ctxW = s2 := by
  dsimp [ctxW, OperatorSelectionLpContext.ofCertificate]

/-- `ctxW` carries exactly the witness Gram matrix. -/
theorem ctxW_G : @OperatorSelectionLpContext.G ℤ _ _ _ ctxW = G2 := by
  dsimp [ctxW, OperatorSelectionLpContext.ofCertificate]

/-- Under a diagonal Gram over a domain without zero divisors, any active dual
index (`s i ≠ 0`) with non-vanishing diagonal entry (`G i i ≠ 0`) forces the
selected primal coordinate `x i = 0`, independent of any cost vector. -/
theorem complementarySlackness_diagonal_active_forces_zero
    {R : Type*} [CommRing R] [NoZeroDivisors R]
    {d : ℕ} {G : Fin d → Fin d → R} {x s : Fin d → R}
    (hdiag : ∀ a b : Fin d, a ≠ b → G a b = 0)
    (hcs : ∀ i, s i * Finset.univ.sum (fun j => G i j * x j) = 0)
    {i : Fin d} (hsi : s i ≠ 0) (hgii : G i i ≠ 0) :
    x i = 0 := by
  have hdiag_cs : s i * (G i i * x i) = 0 :=
    (complementarySlackness_diagonal_iff hdiag).mp hcs i
  have hgx : G i i * x i = 0 := (mul_eq_zero.mp hdiag_cs).resolve_left hsi
  exact (mul_eq_zero.mp hgx).resolve_left hgii

#print axioms frobeniusValue_nonpos_iff_eq_zero
#print axioms gateSet_eq_tightSet
#print axioms frobeniusValue_of_diagonal
#print axioms complementarySlackness_diagonal_iff
#print axioms exists_lpData_activeSet_gateSet_disjoint
#print axioms ctxW_t
#print axioms ctxW_s
#print axioms ctxW_G
#print axioms complementarySlackness_diagonal_active_forces_zero

end QOU.MassTheory.UICGateLP
