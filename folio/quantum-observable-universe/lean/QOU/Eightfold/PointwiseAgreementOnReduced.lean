/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.RingTheory.Nilpotent.Lemmas
import Mathlib.RingTheory.Ideal.Quotient.Defs
import Mathlib.Data.ZMod.Basic

/-!
# When pointwise agreement IS equality: reducedness is the whole hypothesis

A standing objection to reading a finite check as an identity of maps runs: *two distinct
maps can agree on a finite set.*  That is true in general, and it is the right objection to
raise.  This file isolates exactly what has to be measured for it to fail, so that a claim
of the form "these two maps agree" can be audited against hypotheses rather than against an
agent's confidence.

Two conditions do it, and **both are facts about the target, not about the two maps**:

1. the points tested **exhaust** the space -- there is no unexamined point left for the maps
   to differ at;
2. the coordinate ring is **REDUCED**.

Condition 2 is the one that is easy to lose.  Pointwise agreement says each difference
`f b - g b` lies in every prime, i.e. in the nilradical; that is `0` precisely when the ring
is reduced.  In a non-reduced ring a nonzero nilpotent lies in every prime and is therefore
invisible to every point, so two genuinely different maps agree at all of them.

`eq_of_apply_sub_mem_all_primes` is the positive direction.
`exists_ne_of_not_isReduced` is its sharpness: drop reducedness and the conclusion fails,
with `twoNilpotentZModFour` exhibiting a concrete ring where it does -- `(2 : ZMod 4)` is a
nonzero element lying in every prime.  The pair mirrors the shape of
`GaloisOrbitTransport.lean`, where a transport theorem is stated next to the theorem saying
its hypothesis cannot be dropped.

**What Lean supplies and what it does not.**  The hypothesis here is *"the difference lies
in every prime"*.  Bridging a finite list of tested points to that hypothesis is a
MEASUREMENT, not a theorem: it needs the points to exhaust the spectrum.  Nothing in this
file establishes that for any particular variety, and a caller who has checked finitely many
points has not discharged it until the exhaustion is measured separately.
-/

namespace QOU.Eightfold.PointwiseAgreementOnReduced

variable {A : Type*} [CommRing A]

/-- In a reduced ring, an element lying in **every** prime ideal is zero -- so two elements
agreeing modulo every prime are equal.  This is the algebraic content of "pointwise
agreement is equality". -/
theorem eq_of_sub_mem_all_primes [IsReduced A] {x y : A}
    (h : ∀ p : Ideal A, p.IsPrime → x - y ∈ p) : x = y := by
  have hmem : x - y ∈ nilradical A := by
    rw [nilradical_eq_sInf]
    exact Ideal.mem_sInf.mpr fun {p} hp => h p hp
  rw [nilradical_eq_zero] at hmem
  have hzero : x - y = 0 := by simpa using hmem
  exact sub_eq_zero.mp hzero

/-- **Pointwise agreement is equality, for a reduced target.**  Two maps into a reduced ring
whose values agree modulo every prime are equal as maps.  This is the shape the objection
takes: the conclusion is an identity of maps, not a list of coincidences. -/
theorem eq_of_apply_sub_mem_all_primes [IsReduced A] {B : Type*} {f g : B → A}
    (h : ∀ b : B, ∀ p : Ideal A, p.IsPrime → f b - g b ∈ p) : f = g :=
  funext fun b => eq_of_sub_mem_all_primes (h b)

/-- **Sharpness: reducedness cannot be dropped.**  In any non-reduced ring there are two
DISTINCT elements agreeing modulo every prime -- invisible to every point of the spectrum.
So a pointwise check, however exhaustive, does not by itself give equality. -/
theorem exists_ne_of_not_isReduced (h : ¬ IsReduced A) :
    ∃ x y : A, x ≠ y ∧ ∀ p : Ideal A, p.IsPrime → x - y ∈ p := by
  rw [isReduced_iff] at h
  push_neg at h
  obtain ⟨x, hx, hx0⟩ := h
  refine ⟨x, 0, hx0, fun p hp => ?_⟩
  haveI := hp
  simpa using nilradical_le_prime p (mem_nilradical.mpr hx)

/-- A concrete non-reduced witness, so the sharpness theorem is not vacuous: `(2 : ZMod 4)`
is nonzero and nilpotent, hence lies in every prime ideal while differing from `0`. -/
theorem twoNilpotentZModFour : IsNilpotent (2 : ZMod 4) ∧ (2 : ZMod 4) ≠ 0 :=
  ⟨⟨2, by decide⟩, by decide⟩

/-- **Prime-agreement equivalence for maps into a reduced ring (`qou-qjhc`).**
In a reduced commutative ring `A`, two maps `f, g : B → A` are equal if and only if
`f b - g b` lies in every prime ideal at every `b : B`. -/
theorem apply_eq_iff_sub_mem_all_primes [IsReduced A] {B : Type*} {f g : B → A} :
    f = g ↔ ∀ b : B, ∀ p : Ideal A, p.IsPrime → f b - g b ∈ p := by
  constructor
  · rintro rfl b p _
    rw [sub_self]
    exact p.zero_mem
  · exact eq_of_apply_sub_mem_all_primes

end QOU.Eightfold.PointwiseAgreementOnReduced
