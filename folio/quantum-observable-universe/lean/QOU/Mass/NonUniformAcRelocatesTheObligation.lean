/-
QOU.Mass.NonUniformAcRelocatesTheObligation — dropping vertex-transitivity does
not free the mirror split; it moves the whole `A`-dependence onto the carrier.

Arc context (em-linking; bean `qou-o6ml`). Two escapes were left formally open by
the merged charge-blindness result (#6423) and the precision result (#6485):

  (1) a carrier link that is **not vertex-transitive**, so `ac(L_k, L)` differs
      between components;
  (2) an `ac` that **depends on the charge assignment**.

They are one escape, not two, and this file settles what it buys.

**On (2), briefly, because it is a category error rather than a model choice.**
`ac(L_k, L)` is Freedman–He's asymptotic crossing number of one component against
the whole link — a topological invariant of `L` alone. It takes no charge input,
and neither Komendarczyk (arXiv:0808.1533v1 eq. (43)) nor Khesin defines any such
refinement. Making it charge-dependent is not a weaker reading of eq. (43); it is
a different functional, for which no bound is in evidence. Nothing here refutes
such a functional — there is simply no theorem to appeal to, so it cannot be
cited as an escape from one.

**On (1), which is a real generalisation.** Give each component `k` its own
weight `a k`, and let the proton set be an arbitrary `Finset`. Then the mirror
split factorises (`mirrorSplit_nonuniform_eq`) as

  `ΔE = C·m·(φp − φn)·( Σ_{k ∈ P} a k − Σ_{k ∈ Q} a k )`

with `P` and `Q` the proton sets of the two partners. Every ingredient except the
last bracket is `A`-independent, so **all `A`-dependence the split can possibly
have is carried by that bracket** — a purely topological quantity of the carrier
link together with the charge assignment.

That is the point. Non-uniformity does not manufacture `A`-dependence out of
nothing; it relocates the obligation onto `Σ_{k ∈ P} a k − Σ_{k ∈ Q} a k`, which
cannot be evaluated without saying which link the nucleus **is**. And `qou-5vhf`
establishes that the `A ≤ 4` carrier assignments are an admitted AME-driven census
search. So escape (1) is not independent of the blocker that ended route (2) — it
*is* that blocker, reached from a different direction.

The uniform case is recovered as a corollary (`mirrorSplit_uniform_eq`): with
`a k = a` throughout, the bracket collapses to `a·(|P| − |Q|)`, reproducing the
merged `FreedmanHeMirrorSplitChargeBlind.mirrorSplit_eq` — constant on the `d = 1`
ladder, where `|P| − |Q| = 1`.

SCOPE — **scope-(a)**, and deliberately weak. Nothing here says a non-uniform
carrier *cannot* produce the observed 13.63× growth; the bracket is unconstrained
in general, and with enough spread in `a k` it could. What is shown is that doing
so requires a specified carrier, which is the ingredient the arc does not have
un-fitted. Eq. (43) is untouched throughout.

Base ring: a generic `CommRing` suffices — the content is the cancellation of the
complement sum, which is ring algebra. No ordering is used, so per AGENTS.md §7c
none is assumed.
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring

namespace QOU.Mass.NonUniformAcRelocatesTheObligation

variable {R : Type*} [CommRing R]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- The Freedman–He link-bound functional with a **per-component** weight `a k`
(dropping vertex-transitivity) and an arbitrary proton set `P`.

`C` absorbs the pure constant `(π/16)^{1/4}`, `m` is `min_k |Flux(X_k)|`, the
components in `P` carry flux `φp` and those in `Pᶜ` carry `φn`. -/
def fhBoundNonuniform (C m : R) (a : ι → R) (φp φn : R) (P : Finset ι) : R :=
  C * m * ((∑ k ∈ P, a k) * φp + (∑ k ∈ Pᶜ, a k) * φn)

/-- **The whole `A`-dependence sits in one bracket.** For any two proton sets the
split factorises, with the total weight `∑ k, a k` cancelling entirely:

  `ΔE = C·m·(φp − φn)·( Σ_{k ∈ P} a k − Σ_{k ∈ Q} a k )`

So a non-vertex-transitive carrier does not create `A`-dependence; it relocates
it into a topological quantity of the carrier and the charge assignment. -/
theorem mirrorSplit_nonuniform_eq (C m φp φn : R) (a : ι → R) (P Q : Finset ι) :
    fhBoundNonuniform C m a φp φn P - fhBoundNonuniform C m a φp φn Q
      = C * m * ((φp - φn) * ((∑ k ∈ P, a k) - (∑ k ∈ Q, a k))) := by
  have hP : (∑ k ∈ Pᶜ, a k) = (∑ k, a k) - (∑ k ∈ P, a k) := by
    rw [eq_sub_iff_add_eq, Finset.sum_compl_add_sum]
  have hQ : (∑ k ∈ Qᶜ, a k) = (∑ k, a k) - (∑ k ∈ Q, a k) := by
    rw [eq_sub_iff_add_eq, Finset.sum_compl_add_sum]
  unfold fhBoundNonuniform
  rw [hP, hQ]
  ring

/-- **The uniform case is recovered**, reproducing the merged
`FreedmanHeMirrorSplitChargeBlind.mirrorSplit_eq`: the bracket collapses to
`a·(|P| − |Q|)`, which on the `d = 1` mirror ladder is just `a`, independent of
the nucleus. -/
theorem mirrorSplit_uniform_eq (C m φp φn a : R) (P Q : Finset ι) :
    fhBoundNonuniform C m (fun _ => a) φp φn P
        - fhBoundNonuniform C m (fun _ => a) φp φn Q
      = C * m * ((φp - φn) * (a * ((P.card : R) - (Q.card : R)))) := by
  rw [mirrorSplit_nonuniform_eq]
  simp only [Finset.sum_const, nsmul_eq_mul]
  ring

/-- **Equal proton-set weight kills the split outright.** If the two partners'
proton sets carry the same total weight — which vertex-transitivity forces only
when they also have equal cardinality, but which can happen accidentally
otherwise — the predicted split is exactly zero, whatever the fluxes.

Recorded because it is the sharpest form of the relocation: the bracket is not
merely where the `A`-dependence lives, it is the *only* thing standing between
this model and a vanishing prediction. -/
theorem mirrorSplit_eq_zero_of_equal_weight (C m φp φn : R) (a : ι → R)
    (P Q : Finset ι) (hw : (∑ k ∈ P, a k) = (∑ k ∈ Q, a k)) :
    fhBoundNonuniform C m a φp φn P - fhBoundNonuniform C m a φp φn Q = 0 := by
  rw [mirrorSplit_nonuniform_eq, hw, sub_self, mul_zero, mul_zero]

/-- **Self-difference specialization of `mirrorSplit_eq_zero_of_equal_weight` (`qou-8jfh`).**
For any finite set `P : Finset ι`,
`fhBoundNonuniform C m a φp φn P - fhBoundNonuniform C m a φp φn P = 0`. -/
theorem mirrorSplit_self_eq_zero (C m φp φn : R) (a : ι → R) (P : Finset ι) :
    fhBoundNonuniform C m a φp φn P - fhBoundNonuniform C m a φp φn P = 0 :=
  mirrorSplit_eq_zero_of_equal_weight C m φp φn a P P rfl

end QOU.Mass.NonUniformAcRelocatesTheObligation
