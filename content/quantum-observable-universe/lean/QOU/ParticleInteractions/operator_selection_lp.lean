import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Data.Fintype.Fin
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# QOU.ParticleInteractions.operator_selection_lp

**Proposition** ([`prop:operator-selection-lp`](../../../quantum-observable-universe/mass-theory/operator-selection-lp.md)):
*Knot operator selection as a linear program with LP duality.*

The knot operator `Φ = Σᵢ xᵢ bᵢ ∈ Hₙ(q)` for a target interaction
with net value `n_target` is the optimum of

  minimise   Σᵢ tᵢ xᵢ
  subject to Σᵢ xᵢ = n_target           (net constraint)
             Σⱼ G_{ij} xⱼ ≥ 0  ∀ i      (Frobenius positivity)
             xᵢ ≥ -M          ∀ i       (boundedness),

and the dual certificate `(y₀*, y*)` satisfies strong duality
`Σᵢ tᵢ xᵢ* = n_target · y₀*` and complementary slackness.

## Disposition (integrity)

The class below carries only the **LP data** — the cost vector `t`,
the Frobenius Gram matrix `G`, a candidate `x*`, the target
`n_target`, and the dual variable `y₀*`.  It does **not** carry the
optimality / strong-duality conclusions as fields (the previous
version did, then projected them — a self-assuming projection
forbidden by AGENTS.md §3b-cond item 5).

`operator_selection_lp` states the genuine conclusion — `x*` is
primal-feasible AND optimal among all feasible points AND strong
duality holds — and is now **proved, sorry-free**.  The
feasible-set definition `IsFeasible` is genuine (no opaque `Prop`
field projected).

**2026-08-16.** The previous version ended in `sorry`, citing the LP
strong-duality theorem as missing infrastructure.  That was the wrong
diagnosis twice over.

First, the statement was **false**: stripping the conclusions out of the
class (rightly, per §3b-cond item 5) left the class carrying *only data*
and *no* hypotheses, so the theorem asserted `IsFeasible x_star` for an
arbitrary `x_star`.  With `d = 1`, `n_target = 1`, `x_star = 0` the first
conjunct reads `0 = 1`, and `False` was derivable.  See bean `qou/k4ul`.

Second, no strong-duality theorem is needed.  `x*` is a *given* candidate
and `y₀*` a *given* dual variable, so this is certificate verification,
not optimisation: the class now carries the dual slack `s ≥ 0`, the dual
equality `tⱼ = y₀ + Σᵢ sᵢGᵢⱼ`, primal feasibility of `x*`, and the
zero-gap identity — all hypotheses **about the data**, never the block's
own conclusion.  Optimality then follows by the weak-duality computation
inlined below: for any feasible `x`,

    Σⱼ tⱼxⱼ = y₀·n_target + Σᵢ sᵢ(Gx)ᵢ ≥ y₀·n_target = Σⱼ tⱼx*ⱼ ,

since `sᵢ ≥ 0` and `(Gx)ᵢ ≥ 0`.  Farkas' lemma is irrelevant here (it is
still the open input for *general* strong duality — see bean `qou/kl8z`).

If the substrate's concrete `x*`/`y₀*` do not satisfy these hypotheses,
that is a **content** finding about the claimed optimum, not a Lean one.

## Checking a certificate index by index

The zero-gap hypothesis is a single equation over the whole data,
which a symbolic evaluation cannot discharge without summing `d`
products.  `zero_gap_iff_complementary_slackness` replaces it, for
feasible points, with the equivalent **per-index** condition

    ∀ i,  sᵢ · (Gx)ᵢ = 0

— each Frobenius constraint is inactive (`sᵢ = 0`) or tight
(`(Gx)ᵢ = 0`).  Both directions matter and are used differently:

- **`.mp`** (`complementary_slackness_x_star`) extracts the per-index
  facts from a context that has already been built, so an evaluation
  can check them one at a time.
- **`zero_gap_of_complementary_slackness`** runs the other way and is
  stated over *raw data*, not over the class: `zero_gap` is a field,
  so a lemma assuming `OperatorSelectionLpContext` could never supply
  it.  This is what an instantiation for concrete `t`, `G`, `x*` uses.

The algebra common to all of it is `sum_cost_mul_eq`, which needs no
order on `R` at all and no sign hypotheses — the ordering enters only
where non-negativity is genuinely required.

## What the substrate actually is (2026-08-16, bean `qou/k4f8`)

Computed exactly in `ℚ(q)` by
`computations/operator_selection_lp_symbolic_qq.py` — 18/18 checks, no
floating point, because the question is whether `det G` is *zero*, not
whether it is small.  For `H₃(q)` (`d = 6`):

- **`t` is row `0` of `G`.**  Not a coincidence: `tⱼ = tr_M(bⱼ) =
  tr_M(b₀·bⱼ) = G₀ⱼ` whenever the basis contains the identity.  So a
  certificate always exists — `y₀ = 0`, `s = e₀` — and certificate
  existence is not, and never was, the obstruction.  What it certifies
  is `Σⱼtⱼxⱼ ≥ 0` *from the constraint* `(Gx)₀ ≥ 0`, which is the same
  inequality.  See `dualCertificateExists_of_cost_eq_gram_row`.
- **`det G = 0` identically**, rank 5, radical spanned by
  `v = (−q³, q², q², −q, −q, 1) ∼ (−1/q)^len(wᵢ)`, the
  q-antisymmetriser.  `G` has no inverse, so
  `dualCertificateExists_of_left_inverse` does not apply here.
- **`y₀ = 0` is forced** for every dual-feasible pair, at every
  `q ≠ 1`, since `⟨𝟙,v⟩ = −(q−1)(q²−q+1)`.  See
  `y_0_eq_zero_of_radical`.  The optimum is attained on the radical
  itself with objective `0` and every Frobenius constraint tight — see
  `OperatorSelectionLpContext.ofRadical`.
- `H₂(q)` is **not** degenerate (`det G = (q⁴+q²+1)/(q²+1)²`), so this
  is a fact about `H₃`, not about how the LP was written down.

The consequence is a **content** question, not a Lean one: the dual
objective is `n_target · y₀`, so the optimal value is `0` for every
`n_target`, and `y₀` cannot be the shadow price of the net constraint.
Anything dividing by it is `0/0`.  Nothing in this file asserts
otherwise; the theorems below are exactly as strong as their
hypotheses.

## Rebuilding `G` does not help (bean `qou/ndsa`)

`ndsa` proposes breaking the confinement LP's homogeneity by getting
the braid into the objective `t` or the Gram `G` rather than only into
`n_target`.  Two of its candidates are ruled out here.

`y_0_eq_zero_of_cost_perp_radical` is the reason, and it is stated so
that **nothing in its hypotheses mentions where `G` came from**: a
right radical direction, a cost vector orthogonal to it, and
`Σⱼvⱼ ≠ 0`.  For a Gram of the form `G^w_{ij} = tr_M(bᵢ w bⱼ)` — any
fixed algebra element `w`, so any braid — both survive: `V = Σⱼvⱼbⱼ`
spans a two-sided ideal (the sign block), so `G^w v = 0`; and
`⟨t,v⟩ = tr_M(V) = 0` is a fact about the *cost* vector and the
radical, independent of the Gram.  Verified exactly in `ℚ(q)` for nine
braid words on both sides by
`computations/confinement_lp_braid_gram_probe.py`, rank 5/6 throughout.

The equality-constrained variant fares worse: by
`objective_eq_demand_coord`, `t·x = u_{i₀}` for *every* feasible `x`,
so the program has nothing to optimise and a knot-dependent `u` buys a
knot-dependent answer only by reading a coordinate of its own input
back out.  `demand_perp_radical` adds that `u` is not even free — it
must be orthogonal to the radical for a feasible point to exist.

So the degeneracy is not a property of `G`.  It is the conjunction of
"the cost vector is the Markov trace vector" and "the Gram annihilates
the trace form's radical", and the second is automatic for anything
built from `tr_M`.  A formulation that survives has to change the
**objective**.

## Base ring (§7c)

Nothing in the program is archimedean: feasibility, optimality and
strong duality are statements about `Finset.sum`, `*` and `≤`, and a
linear program makes sense over any ordered commutative ring.  The
scalars are therefore a generic `R`, and the substrate evaluation is
the instantiation `R := ℝ`. -/

namespace QOU.ParticleInteractions

section RawData

variable {R : Type*} [CommRing R] {d : ℕ}

/-- **Dual decomposition** of the objective, over raw LP data.

For any `x` meeting the net constraint, dual feasibility rewrites the
objective as the dual bound plus the *slack pairing* `Σᵢ sᵢ (Gx)ᵢ`:

    Σⱼ tⱼ xⱼ = y₀ · n_target + Σᵢ sᵢ (Gx)ᵢ .

This is pure algebra — no order on `R` is used, and neither `sᵢ ≥ 0`
nor `(Gx)ᵢ ≥ 0` is assumed.  Both the optimality bound and the
complementary-slackness equivalence below are corollaries of this one
identity. -/
theorem sum_cost_mul_eq {t : Fin d → R} {G : Fin d → Fin d → R} {s : Fin d → R}
    {n_target y_0_star : R} (x : Fin d → R)
    (dual_feasible : ∀ j, t j = y_0_star + Finset.univ.sum (fun i => s i * G i j))
    (net : (Finset.univ.sum fun j => x j) = n_target) :
    (Finset.univ.sum fun j => t j * x j)
      = y_0_star * n_target
        + Finset.univ.sum (fun i => s i * Finset.univ.sum fun j => G i j * x j) := by
  have h1 : ∀ j, t j * x j
      = y_0_star * x j + Finset.univ.sum (fun i => s i * (G i j * x j)) := by
    intro j
    rw [dual_feasible j, add_mul, Finset.sum_mul]
    simp [mul_assoc]
  rw [Finset.sum_congr rfl (fun j _ => h1 j), Finset.sum_add_distrib,
    ← Finset.mul_sum, net, Finset.sum_comm]
  congr 1
  exact Finset.sum_congr rfl (fun i _ => by rw [Finset.mul_sum])

/-- **Certificate builder.** Over raw LP data, the zero-gap identity
    follows from dual feasibility, the net constraint, and *per-index*
    complementary slackness `sᵢ (Gx*)ᵢ = 0`.

This is the form an instantiation needs.  `zero_gap` is a *field* of
`OperatorSelectionLpContext`, so a lemma assuming the class cannot be
used to supply it; this one assumes only the data.  Checking `d`
scalar products vanish is decidable on concrete symbolic `t`, `G`,
`x*`, whereas the global sum identity is not. -/
theorem zero_gap_of_complementary_slackness {t : Fin d → R} {G : Fin d → Fin d → R}
    {s : Fin d → R} {n_target y_0_star : R} {x_star : Fin d → R}
    (dual_feasible : ∀ j, t j = y_0_star + Finset.univ.sum (fun i => s i * G i j))
    (net : (Finset.univ.sum fun j => x_star j) = n_target)
    (cs : ∀ i, s i * (Finset.univ.sum fun j => G i j * x_star j) = 0) :
    (Finset.univ.sum fun j => t j * x_star j) = n_target * y_0_star := by
  rw [sum_cost_mul_eq x_star dual_feasible net, Finset.sum_eq_zero (fun i _ => cs i),
    add_zero, mul_comm]

end RawData

section DualCertificate

variable {R : Type*} [CommRing R] [PartialOrder R] {d : ℕ}

/-- A **dual certificate** for cost vector `t` and Gram matrix `G`: a
    scalar `y₀` together with non-negative slacks `s` satisfying
    `t = y₀·𝟙 + sᵀG`.

Existence is *not* automatic.  It asks whether `t` lies in the cone
`{y₀·𝟙 + sᵀG : y₀ ∈ R, s ≥ 0}` — `d` equations in `d+1` unknowns with
a sign constraint, a genuine Farkas-type question about the substrate
data.  Bean `qou/k4f8`. -/
def DualCertificateExists (t : Fin d → R) (G : Fin d → Fin d → R) : Prop :=
  ∃ (y_0 : R) (s : Fin d → R), (∀ i, 0 ≤ s i) ∧
    ∀ j, t j = y_0 + Finset.univ.sum (fun i => s i * G i j)

/-- **Reduction to a one-parameter sign condition.**

If `K` is a left inverse of `G` — `Σᵢ K k i · G i j = δₖⱼ` — then the
dual equation `t = y₀·𝟙 + sᵀG` determines `s` outright:

    s i = Σₖ (t k − y₀) · K k i .

So a certificate exists as soon as *some single scalar* `y₀` makes all
`d` of those entries non-negative.  A `d`-dimensional feasibility
problem collapses to a search over one parameter.

This is the statement the symbolic stage answers: invert `G` over
`ℚ(q)`, form `s(y₀)`, and ask for which `y₀` every entry is `≥ 0`.
Note the hypothesis is a *given* left inverse, not `G⁻¹` — so no
invertibility API, no determinant, and the symbolic stage supplies
`K` explicitly and checks `hK` by multiplication. -/
theorem dualCertificateExists_of_left_inverse (t : Fin d → R) (G K : Fin d → Fin d → R)
    (hK : ∀ k j, (Finset.univ.sum fun i => K k i * G i j) = if k = j then 1 else 0)
    (y_0 : R)
    (hsign : ∀ i, 0 ≤ Finset.univ.sum fun k => (t k - y_0) * K k i) :
    DualCertificateExists t G := by
  have assoc : ∀ k i j, (t k - y_0) * K k i * G i j = (t k - y_0) * (K k i * G i j) :=
    fun k i j => mul_assoc _ _ _
  have step : ∀ k j, (Finset.univ.sum fun i => (t k - y_0) * K k i * G i j)
      = if k = j then t k - y_0 else 0 := by
    intro k j
    rw [Finset.sum_congr rfl (fun i _ => assoc k i j), ← Finset.mul_sum, hK k j]
    by_cases h : k = j <;> simp [h]
  have distrib : ∀ i j, (Finset.univ.sum fun k => (t k - y_0) * K k i) * G i j
      = Finset.univ.sum fun k => (t k - y_0) * K k i * G i j :=
    fun i j => Finset.sum_mul _ _ _
  have main : ∀ j, (Finset.univ.sum fun i =>
      (Finset.univ.sum fun k => (t k - y_0) * K k i) * G i j) = t j - y_0 := by
    intro j
    rw [Finset.sum_congr rfl (fun i _ => distrib i j), Finset.sum_comm,
      Finset.sum_congr rfl (fun k _ => step k j)]
    simp
  refine ⟨y_0, fun i => Finset.univ.sum fun k => (t k - y_0) * K k i, hsign, fun j => ?_⟩
  simp only [main j]
  ring

end DualCertificate

section TraceForm

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R] {d : ℕ}

/-- **A cost vector that is a row of the Gram matrix certifies itself.**

For a *trace form* this hypothesis is not an assumption but an
identity: `tᵢ = tr(bᵢ) = tr(b_{i₀}·bᵢ) = G_{i₀ i}` whenever the basis
contains the identity element `b_{i₀} = 1`.  The certificate is then
`y₀ = 0`, `s = e_{i₀}`.

So certificate *existence* is never the obstruction for a trace-form
LP.  But look at what the certificate bounds: it gives
`Σⱼ tⱼxⱼ ≥ 0` using the constraint `(Gx)_{i₀} ≥ 0`, and `(Gx)_{i₀}`
*is* `Σⱼ tⱼxⱼ`.  The objective is bounded below by one of its own
constraints, and the bound is a tautology. -/
theorem dualCertificateExists_of_cost_eq_gram_row (t : Fin d → R) (G : Fin d → Fin d → R)
    (i_0 : Fin d) (ht : ∀ j, t j = G i_0 j) :
    DualCertificateExists t G := by
  refine ⟨0, fun i => if i = i_0 then 1 else 0, fun i => ?_, fun j => ?_⟩
  · by_cases h : i = i_0 <;> simp [h]
  · simp [ht j, ite_mul]

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **The degeneracy criterion, in the only form that is really needed.**

Strip everything away and dual feasibility for the `x`-block of *any*
conic program has the shape

    tⱼ = y₀ + cⱼ

where `c` is whatever the constraints contribute.  For a linear
program `cⱼ = Σᵢ sᵢGᵢⱼ`; for an SDP with lift `M₀ + Σₖ xₖMₖ ⪰ 0` and
dual `Z ⪰ 0` it is `cⱼ = ⟨Z, Mⱼ⟩`; for a moment relaxation it picks up
the moment block as well.

Whatever it is, `y₀ = 0` follows as soon as the contribution is
orthogonal to `v`.  So the question to ask of any proposed
reformulation is exactly one thing:

> **does the constraint map annihilate the radical?**

If it does, the reformulation is degenerate before it is solved.  For
the LP that is `Gv = 0`; for a dense PSD lift it is `Σⱼ vⱼMⱼ = 0`.
Bean `qou/ndsa`. -/
theorem y_0_eq_zero_of_contribution_perp_radical [NoZeroDivisors R]
    {t v c : Fin d → R} {y_0 : R}
    (htv : (Finset.univ.sum fun j => t j * v j) = 0)
    (hcv : (Finset.univ.sum fun j => c j * v j) = 0)
    (hone : (Finset.univ.sum fun j => v j) ≠ 0)
    (dual : ∀ j, t j = y_0 + c j) :
    y_0 = 0 := by
  have key : (Finset.univ.sum fun j => t j * v j)
      = y_0 * (Finset.univ.sum fun j => v j)
        + Finset.univ.sum fun j => c j * v j := by
    have h1 : ∀ j, t j * v j = y_0 * v j + c j * v j := by
      intro j
      rw [dual j, add_mul]
    rw [Finset.sum_congr rfl (fun j _ => h1 j), Finset.sum_add_distrib,
      ← Finset.mul_sum]
  rw [htv, hcv, add_zero] at key
  rcases mul_eq_zero.mp key.symm with h | h
  · exact h
  · exact absurd h hone

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **The radical of the form forces the dual variable to vanish.**

Three hypotheses, and *none of them says where the Gram came from*:

- `hv` — `v` is a right radical direction, `∀ i, Σⱼ Gᵢⱼvⱼ = 0`;
- `htv` — the cost vector is orthogonal to it, `Σⱼ tⱼvⱼ = 0`;
- `hone` — `Σⱼ vⱼ ≠ 0`.

Then *every* dual-feasible `y₀` is `0`.

The dual objective is `n_target · y₀`, so this says the LP's value is
identically zero however `n_target` is chosen, and `y₀` is **not** a
shadow price of the net constraint: it cannot respond to the constraint
it is supposed to price.

Note how little is assumed.  No symmetry of `G`, no non-negativity of
the slacks, no primal feasibility, no optimality.  Degeneracy is a
property of the cost vector and the form alone — which is why it
cannot be repaired by choosing a better `x*`, and (bean `qou/ndsa`)
why it cannot be repaired by rebuilding `G` either: see
`y_0_eq_zero_of_radical` below for the version whose `htv` comes for
free.

The `omit` above is load-bearing documentation, not tidying: this
statement holds over any commutative ring without zero divisors, with
no order in sight. -/
theorem y_0_eq_zero_of_cost_perp_radical [NoZeroDivisors R] {t : Fin d → R}
    {G : Fin d → Fin d → R} {v : Fin d → R} {y_0 : R} {s : Fin d → R}
    (hv : ∀ i, (Finset.univ.sum fun j => G i j * v j) = 0)
    (htv : (Finset.univ.sum fun j => t j * v j) = 0)
    (hone : (Finset.univ.sum fun j => v j) ≠ 0)
    (dual : ∀ j, t j = y_0 + Finset.univ.sum (fun i => s i * G i j)) :
    y_0 = 0 := by
  refine y_0_eq_zero_of_contribution_perp_radical
    (c := fun j => Finset.univ.sum fun i => s i * G i j) htv ?_ hone dual
  have h1 : ∀ j, (Finset.univ.sum fun i => s i * G i j) * v j
      = Finset.univ.sum fun i => s i * (G i j * v j) := by
    intro j
    rw [Finset.sum_mul]
    exact Finset.sum_congr rfl (fun i _ => by ring)
  have h2 : ∀ i, (Finset.univ.sum fun j => s i * (G i j * v j)) = 0 := by
    intro i
    rw [← Finset.mul_sum, hv i, mul_zero]
  rw [Finset.sum_congr rfl (fun j _ => h1 j), Finset.sum_comm,
    Finset.sum_congr rfl (fun i _ => h2 i), Finset.sum_const_zero]

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- The trace-form instance of the above: when the cost vector is row
    `i₀` of `G`, orthogonality to the radical is automatic, since
    `Σⱼ tⱼvⱼ = Σⱼ G_{i₀j}vⱼ = 0` is just `hv` at `i₀`. -/
theorem y_0_eq_zero_of_radical [NoZeroDivisors R] {t : Fin d → R}
    {G : Fin d → Fin d → R} {v : Fin d → R} {i_0 : Fin d} {y_0 : R} {s : Fin d → R}
    (ht : ∀ j, t j = G i_0 j)
    (hv : ∀ i, (Finset.univ.sum fun j => G i j * v j) = 0)
    (hone : (Finset.univ.sum fun j => v j) ≠ 0)
    (dual : ∀ j, t j = y_0 + Finset.univ.sum (fun i => s i * G i j)) :
    y_0 = 0 :=
  y_0_eq_zero_of_cost_perp_radical hv
    (by
      have hj : ∀ j, t j * v j = G i_0 j * v j := fun j => by rw [ht j]
      rw [Finset.sum_congr rfl (fun j _ => hj j)]
      exact hv i_0)
    hone dual

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **Fixing `Gx` fixes the objective.**

The *equality*-constrained variant of the program — `min t·x` subject
to `1·x = n_target` and `Gx = u` — has nothing to optimise when the
cost vector is row `i₀` of `G`:

    t·x = Σⱼ G_{i₀j}xⱼ = (Gx)_{i₀} = u_{i₀} .

Every feasible point scores the same, and the score is a coordinate of
the demand vector the caller passed in.  Making `u` depend on a knot
therefore makes the "optimum" depend on the knot only by reading one
component of its own input back out.

Bean `qou/ndsa` names this formulation as the cheapest candidate for
breaking the confinement LP's homogeneity.  This is why it does not. -/
theorem objective_eq_demand_coord {t : Fin d → R} {G : Fin d → Fin d → R}
    {u x : Fin d → R} {i_0 : Fin d}
    (ht : ∀ j, t j = G i_0 j)
    (hGx : ∀ i, (Finset.univ.sum fun j => G i j * x j) = u i) :
    (Finset.univ.sum fun j => t j * x j) = u i_0 := by
  have hj : ∀ j, t j * x j = G i_0 j * x j := fun j => by rw [ht j]
  rw [Finset.sum_congr rfl (fun j _ => hj j)]
  exact hGx i_0

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- Two points with the same demand score the same — the objective is
    constant on each fibre of `x ↦ Gx`, so "optimal" is vacuous. -/
theorem objective_constant_on_demand_fibre {t : Fin d → R} {G : Fin d → Fin d → R}
    {u x x' : Fin d → R} {i_0 : Fin d}
    (ht : ∀ j, t j = G i_0 j)
    (hx : ∀ i, (Finset.univ.sum fun j => G i j * x j) = u i)
    (hx' : ∀ i, (Finset.univ.sum fun j => G i j * x' j) = u i) :
    (Finset.univ.sum fun j => t j * x j)
      = Finset.univ.sum fun j => t j * x' j := by
  rw [objective_eq_demand_coord ht hx, objective_eq_demand_coord ht hx']

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **A demand profile has to be orthogonal to the radical to be
    feasible at all.**

If `v` is a *left* radical direction then `Gx = u` forces `⟨u,v⟩ = 0`.
So a knot-derived `u` is not free: it must satisfy this linear
condition before the program has any feasible point.  (For a symmetric
Gram the left and right radicals coincide, so this is the same `v` as
everywhere else here.) -/
theorem demand_perp_radical {G : Fin d → Fin d → R} {u x v : Fin d → R}
    (hvl : ∀ j, (Finset.univ.sum fun i => v i * G i j) = 0)
    (hGx : ∀ i, (Finset.univ.sum fun j => G i j * x j) = u i) :
    (Finset.univ.sum fun i => v i * u i) = 0 := by
  have h1 : ∀ i, v i * u i = Finset.univ.sum fun j => v i * (G i j * x j) := by
    intro i
    rw [← Finset.mul_sum, hGx i]
  have h2 : ∀ j, (Finset.univ.sum fun i => v i * (G i j * x j)) = 0 := by
    intro j
    have hi : ∀ i, v i * (G i j * x j) = (v i * G i j) * x j :=
      fun i => by ring
    rw [Finset.sum_congr rfl (fun i _ => hi i), ← Finset.sum_mul, hvl j, zero_mul]
  rw [Finset.sum_congr rfl (fun i _ => h1 i), Finset.sum_comm,
    Finset.sum_congr rfl (fun j _ => h2 j), Finset.sum_const_zero]

end TraceForm

/-- Data of the operator-selection LP: the cost vector `t`, the
    Frobenius Gram matrix `G`, the target net value `n_target`, a
    candidate primal point `x*`, and the net-constraint dual variable
    `y₀*`.  These are *inputs*; nothing here asserts the conclusion. -/
class OperatorSelectionLpContext (R : Type*) [CommRing R] [LinearOrder R]
    [IsStrictOrderedRing R] where
  /-- The strand number `n ≥ 2`. -/
  n : ℕ
  /-- The basis cardinality `d = n!`. -/
  d : ℕ
  /-- The target net value `n_target`. -/
  n_target : R
  /-- The Markov-trace cost coefficients `t : Fin d → R`. -/
  t : Fin d → R
  /-- The Frobenius Gram matrix `G : Fin d → Fin d → R`. -/
  G : Fin d → Fin d → R
  /-- The candidate primal point `x* : Fin d → R`. -/
  x_star : Fin d → R
  /-- The Markov-trace dual variable `y₀* : R`. -/
  y_0_star : R
  /-- Dual slack for the Frobenius-positivity constraints. -/
  s : Fin d → R
  /-- Dual feasibility: the slacks are non-negative. -/
  s_nonneg : ∀ i, 0 ≤ s i
  /-- Dual feasibility: `tⱼ = y₀ + Σᵢ sᵢ Gᵢⱼ`. -/
  dual_feasible : ∀ j, t j = y_0_star + Finset.univ.sum (fun i => s i * G i j)
  /-- `x*` is primal feasible. -/
  x_star_feasible :
    (Finset.univ.sum fun i => x_star i) = n_target ∧
    (∀ i, 0 ≤ Finset.univ.sum fun j => G i j * x_star j)
  /-- Zero duality gap at `x*`. -/
  zero_gap : (Finset.univ.sum fun i => t i * x_star i) = n_target * y_0_star

/-- **Build a context from a dual certificate and a primal point.**

This is the constructor an instantiation should use.  It takes only
facts that are *checkable on concrete data* — slack signs, the dual
equation, the net constraint, Frobenius positivity, and per-index
complementary slackness — and derives `zero_gap` rather than
demanding it.

That the gap is derived, not supplied, is the point: `zero_gap` is the
one field that looks like the block's own conclusion, and building it
by hand is where a self-assuming instance would creep back in. -/
def OperatorSelectionLpContext.ofCertificate {R : Type*} [CommRing R] [LinearOrder R]
    [IsStrictOrderedRing R] (n d : ℕ) (n_target : R) (t : Fin d → R)
    (G : Fin d → Fin d → R) (x_star : Fin d → R) (y_0 : R) (s : Fin d → R)
    (s_nonneg : ∀ i, 0 ≤ s i)
    (dual : ∀ j, t j = y_0 + Finset.univ.sum (fun i => s i * G i j))
    (net : (Finset.univ.sum fun j => x_star j) = n_target)
    (pos : ∀ i, 0 ≤ Finset.univ.sum fun j => G i j * x_star j)
    (cs : ∀ i, s i * (Finset.univ.sum fun j => G i j * x_star j) = 0) :
    OperatorSelectionLpContext R where
  n := n
  d := d
  n_target := n_target
  t := t
  G := G
  x_star := x_star
  y_0_star := y_0
  s := s
  s_nonneg := s_nonneg
  dual_feasible := dual
  x_star_feasible := ⟨net, pos⟩
  zero_gap := zero_gap_of_complementary_slackness dual net cs

/-- **The radical direction, scaled to meet the net constraint, is an
    optimum — and the optimal value is zero.**

Take `x* = c·v` with `c·Σⱼvⱼ = n_target`.  Then `Gx* = 0`, so every
Frobenius constraint is *tight*, complementary slackness is trivial,
and the objective vanishes.

The inputs are three facts about the data and nothing else:

- `ht` — the cost vector is row `i₀` of `G` (automatic for a trace
  form with `b_{i₀} = 1`),
- `hv` — `v` is a right radical direction of `G`,
- `hc` — `c` scales `v` onto the net constraint (solvable exactly when
  `Σⱼvⱼ ≠ 0`, the same non-degeneracy `y_0_eq_zero_of_radical` needs).

Read together with that theorem this is the whole story for a
degenerate trace form: `y₀ = 0` is forced, the optimum is `0`, and it
is attained on the radical — the direction the trace form cannot see. -/
def OperatorSelectionLpContext.ofRadical {R : Type*} [CommRing R] [LinearOrder R]
    [IsStrictOrderedRing R] (n d : ℕ) (n_target : R) (t : Fin d → R)
    (G : Fin d → Fin d → R) (i_0 : Fin d) (v : Fin d → R) (c : R)
    (ht : ∀ j, t j = G i_0 j)
    (hv : ∀ i, (Finset.univ.sum fun j => G i j * v j) = 0)
    (hc : c * (Finset.univ.sum fun j => v j) = n_target) :
    OperatorSelectionLpContext R := by
  have hGx : ∀ i, (Finset.univ.sum fun j => G i j * (c * v j)) = 0 := by
    intro i
    have hj : ∀ j, G i j * (c * v j) = c * (G i j * v j) :=
      fun j => by ring
    rw [Finset.sum_congr rfl (fun j _ => hj j), ← Finset.mul_sum, hv i, mul_zero]
  refine OperatorSelectionLpContext.ofCertificate n d n_target t G (fun j => c * v j) 0
    (fun i => if i = i_0 then 1 else 0) (fun i => ?_) (fun j => ?_) ?_ (fun i => ?_)
    (fun i => ?_)
  · by_cases h : i = i_0 <;> simp [h]
  · simp [ht j, ite_mul]
  · rw [← Finset.mul_sum, hc]
  · exact le_of_eq (hGx i).symm
  · rw [hGx i, mul_zero]

namespace OperatorSelectionLpContext

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
variable [ctx : OperatorSelectionLpContext R]

/-- A vector `x : Fin d → R` is LP-feasible: it satisfies the net
    constraint and Frobenius positivity. (Boundedness `xᵢ ≥ -M` is
    absorbed into the existence of a large `M`; we keep the two
    binding constraints, which are the ones that select the optimum.)

    This is a genuine predicate on the data, not a projected field. -/
def IsFeasible (x : Fin (ctx.d) → R) : Prop :=
  (Finset.univ.sum fun i : Fin ctx.d => x i) = ctx.n_target ∧
  (∀ i : Fin ctx.d, 0 ≤ (Finset.univ.sum fun j : Fin ctx.d => ctx.G i j * x j))

/-- The objective value `Σᵢ tᵢ xᵢ` of a candidate `x`. -/
def objective (x : Fin (ctx.d) → R) : R :=
  Finset.univ.sum fun i : Fin ctx.d => ctx.t i * x i

/-- The **slack pairing** `Σᵢ sᵢ (Gx)ᵢ` — the amount by which a
    feasible point's objective exceeds the dual bound. -/
def slackPairing (x : Fin (ctx.d) → R) : R :=
  Finset.univ.sum fun i : Fin ctx.d =>
    ctx.s i * Finset.univ.sum fun j : Fin ctx.d => ctx.G i j * x j

/-- Dual decomposition, specialised to the class: `objective x` is the
    dual bound plus the slack pairing.  Only the net constraint is
    used, not Frobenius positivity. -/
theorem objective_eq_dual_add_slackPairing (x : Fin ctx.d → R) (hx : IsFeasible x) :
    objective x = ctx.y_0_star * ctx.n_target + slackPairing x :=
  sum_cost_mul_eq x ctx.dual_feasible hx.1

/-- The slack pairing is non-negative on feasible points: `sᵢ ≥ 0` by
    dual feasibility and `(Gx)ᵢ ≥ 0` by primal feasibility. -/
theorem slackPairing_nonneg (x : Fin ctx.d → R) (hx : IsFeasible x) :
    0 ≤ slackPairing x :=
  Finset.sum_nonneg fun i _ => mul_nonneg (ctx.s_nonneg i) (hx.2 i)

/-- **Weak duality.** Every feasible point's objective is bounded below
    by the dual value `n_target · y₀*`. -/
theorem dual_bound_le_objective (x : Fin ctx.d → R) (hx : IsFeasible x) :
    ctx.n_target * ctx.y_0_star ≤ objective x := by
  rw [objective_eq_dual_add_slackPairing x hx, mul_comm ctx.n_target ctx.y_0_star]
  exact le_add_of_nonneg_right (slackPairing_nonneg x hx)

/-- The slack pairing vanishes exactly when every index contributes
    zero — a sum of non-negative terms is zero iff each term is. -/
theorem slackPairing_eq_zero_iff (x : Fin ctx.d → R) (hx : IsFeasible x) :
    slackPairing x = 0
      ↔ ∀ i, ctx.s i * (Finset.univ.sum fun j => ctx.G i j * x j) = 0 := by
  rw [slackPairing,
    Finset.sum_eq_zero_iff_of_nonneg fun i _ => mul_nonneg (ctx.s_nonneg i) (hx.2 i)]
  exact ⟨fun h i => h i (Finset.mem_univ i), fun h i _ => h i⟩

/-- **Complementary slackness is the whole content of the zero gap.**

For a feasible `x`, attaining the dual bound is *equivalent* to the
per-index condition `sᵢ (Gx)ᵢ = 0` for every `i`: each Frobenius
constraint is either inactive (`sᵢ = 0`) or tight (`(Gx)ᵢ = 0`).

This is the reduction that makes the certificate checkable.  The
global identity `Σⱼ tⱼxⱼ = n_target · y₀*` is one equation in the
whole data; the right-hand side is `d` independent scalar equations,
each of which a symbolic evaluation can discharge index by index. -/
theorem zero_gap_iff_complementary_slackness (x : Fin ctx.d → R) (hx : IsFeasible x) :
    objective x = ctx.n_target * ctx.y_0_star
      ↔ ∀ i, ctx.s i * (Finset.univ.sum fun j => ctx.G i j * x j) = 0 := by
  rw [← slackPairing_eq_zero_iff x hx, objective_eq_dual_add_slackPairing x hx,
    mul_comm ctx.n_target ctx.y_0_star]
  constructor
  · intro h
    refine add_left_cancel (a := ctx.y_0_star * ctx.n_target) ?_
    rw [add_zero]
    exact h
  · intro h
    rw [h, add_zero]

/-- **A tightening buys nothing if the optimum survives it.**

`Tighter` is an arbitrary refinement of `IsFeasible` — a PSD lift, a
Lasserre moment relaxation, extra cuts, anything at all.  The only
hypotheses are that it *is* a refinement (`hsub`) and that `x*` still
satisfies it (`hstar`).  Then `x*` is optimal for the tightened
program too, at the same value.

This is what settles the third candidate in bean `qou/ndsa`.  The
moment lift in `computations/sdp_moment_lift.py` keeps `Gx ≥ 0` and
adds `M ⪰ 0`, `X ⪰ 0`, `tr(GX) ≥ 0`, so `hsub` holds by inspection.
And `x*` lifts: take the rank-one moment matrix `X = x*x*ᵀ`, which is
PSD by construction and satisfies `tr(GX) = x*ᵀ(Gx*) = 0` because
`Gx* = 0` — every Frobenius constraint is tight at the radical
optimum.  So `hstar` holds too, and the SDP's optimal value is the
LP's.

The lesson is not about semidefinite programming.  A tightening can
only help when it *cuts off* the incumbent optimum, and this one
cannot: `x*` is the point where all the constraints already hold with
equality. -/
theorem tightening_preserves_optimum {Tighter : (Fin ctx.d → R) → Prop}
    (hsub : ∀ x, Tighter x → IsFeasible x) (hstar : Tighter ctx.x_star) :
    Tighter ctx.x_star ∧
      ∀ x, Tighter x → objective ctx.x_star ≤ objective x := by
  refine ⟨hstar, fun x hx => ?_⟩
  have hgap : objective ctx.x_star = ctx.n_target * ctx.y_0_star := ctx.zero_gap
  rw [hgap]
  exact dual_bound_le_objective x (hsub x hx)

/-- Complementary slackness holds at `x*`, as a consequence of the
    class's `zero_gap` field.  This is the per-index statement a
    substrate evaluation can check directly. -/
theorem complementary_slackness_x_star :
    ∀ i, ctx.s i * (Finset.univ.sum fun j => ctx.G i j * ctx.x_star j) = 0 :=
  (zero_gap_iff_complementary_slackness ctx.x_star ctx.x_star_feasible).mp ctx.zero_gap

end OperatorSelectionLpContext

/-- **Operator selection LP** ([`prop:operator-selection-lp`]).

`x*` is feasible, is the minimum-objective feasible point, and the
dual variable `y₀*` certifies optimality via strong duality
`objective x* = n_target · y₀*`. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP strong duality, feasible bounded programs)
-- Ref: [manuscript] quantum-observable-universe/mass-theory/operator-selection-lp.md
theorem operator_selection_lp {R : Type*} [CommRing R] [LinearOrder R]
    [IsStrictOrderedRing R] [ctx : OperatorSelectionLpContext R] :
    OperatorSelectionLpContext.IsFeasible ctx.x_star ∧
    (∀ x : Fin ctx.d → R, OperatorSelectionLpContext.IsFeasible x →
      OperatorSelectionLpContext.objective ctx.x_star ≤
        OperatorSelectionLpContext.objective x) ∧
    OperatorSelectionLpContext.objective ctx.x_star
      = ctx.n_target * ctx.y_0_star := by
  refine ⟨ctx.x_star_feasible, ?_, ctx.zero_gap⟩
  intro x hx
  have hgap : OperatorSelectionLpContext.objective ctx.x_star
      = ctx.n_target * ctx.y_0_star := ctx.zero_gap
  rw [hgap]
  exact OperatorSelectionLpContext.dual_bound_le_objective x hx

end QOU.ParticleInteractions
