/-
  Where a Diophantine birthday separation can and cannot live.

  Bean `qou-bday`.  Reads on from `qou-hypr` and `BirthdayFaithful.lean`.

  ═══ THE CONJECTURE, AND A PROBLEM WITH ITS SHAPE ═══

  `QOU/AppendixSurreals/DiophantineBirthday.lean` carries `conj:diophantine-birthday`,
  glossed as *"Algebraic vs transcendental numbers are separated by birthday trajectory"*,
  with Liouville and Roth as the motivating content.

  Two separate defects, and they need separating.

  **1. The formalisation was degenerate — FIXED UPSTREAM, bean `qou-ffwk` (#5238).**
  The class used to carry a scalar field plus a field asserting that it vanishes, so a
  one-line anonymous constructor inhabited it.  Its comment said *"No instance is
  provided — that is the honest open state"*, but withholding an instance encodes
  nothing when the only available instance stipulates the answer.  Recorded in bean
  `bday`.  `qou-ffwk` replaced the schema with
  `DiophantineBirthday (trajectory : ℝ → ℕ → ℕ) : Prop`, whose single field is the
  block's algebraic-rigidity bound, and proved that inhabitation now depends on the
  data (`not_of_quadratic` refutes it at `n²`).  Defect 1 is therefore **closed**; it
  is kept here because defect 2 was diagnosed alongside it and reads as its sequel.

  **Defect 2 is untouched by that fix** — it is about the *target*, not the encoding,
  and the new class dodges it only by taking `trajectory` as a parameter rather than
  computing it from the birthday.

  **2. The separation cannot be by the birthday of the number.**  That is this module.

  ═══ WHY BIRTHDAY-OF-THE-NUMBER CANNOT SEPARATE ═══

  `SurrealField` axiom `birthday_ofReal_le_omega` puts **every** real — algebraic,
  transcendental, alike — at birthday `≤ ω`.  So any separation must already live inside
  `[0, ω]`.

  In Conway's actual surreals it collapses completely: the reals are exactly the surreals
  born on or before day `ω`, with the **dyadic rationals born strictly earlier and every
  other real born exactly on day `ω`**.  So

      birthday(√2)  =  ω  =  birthday(π)

  — an algebraic irrational and a transcendental with the *same* birthday.  No function of
  the birthday can tell them apart, and §2 below says exactly that.

  **This is a fact about Conway's model, not a consequence of the corpus's axioms**, and
  it is cited rather than proved: nothing in `SurrealField` pins the birthday of an
  irrational, which is precisely the gap `BirthdayFaithful` addresses for the naturals and
  nobody has addressed for the irrationals.

  ═══ WHERE THE CONJECTURE MUST LIVE INSTEAD ═══

  The Liouville/Roth content is about *how fast rationals approximate `α`*, which in
  surreal terms is the shape of the **sign expansion** — the trajectory `gonshor`
  traces — not the ordinal it terminates at.  The word "trajectory" in the conjecture's
  own gloss is doing real work and should be taken literally.

  The corpus has that infrastructure already: `SignSequence.gonshor : List Sign → ℚ` and
  `gonshorIn`.  A faithful statement would compare *prefixes* — the rate at which
  `gonshor` on length-`n` prefixes approaches `α` — against the Liouville exponent.  Not
  attempted here; this module fixes the target, not the theorem.

  -- Ref: [conway1976] Ch. 0 (reals are the surreals of birthday ≤ ω)
  -- Ref: [gonshor1986] Ch. 4 (sign expansions of the reals)
-/
import QOU.AppendixSurreals.BirthdayFaithful

namespace QOU.AppendixSurreals

open SurrealField

universe u

variable {K : Type u} [SurrealField K]

/-! ## §1 — every real sits at birthday `≤ ω`, from the axioms

A restatement, but the one worth having in front of you: whatever separation is proposed,
it has to fit inside `[0, ω]` for *both* classes of number. -/

/-- **Every real embeds with birthday at most `ω`** — algebraic and transcendental alike.
Directly the `birthday_ofReal_le_omega` axiom, named here because it is the constraint the
conjecture has to live inside. -/
theorem birthday_ofReal_le_omega' (r : ℝ) :
    birthday (ofReal r : K) ≤ Ordinal.omega0 :=
  birthday_ofReal_le_omega r

/-- Both classes of real are confined to the same interval; the axioms distinguish
nothing. -/
theorem birthday_ofReal_mem_Iic (r : ℝ) :
    birthday (ofReal r : K) ∈ Set.Iic Ordinal.omega0 :=
  birthday_ofReal_le_omega' r

/-! ## §2 — equal birthdays are indistinguishable by any birthday-only criterion

Trivial to prove and the entire point: if a proposed separation is a predicate applied to
`birthday (ofReal ·)`, then two reals with equal birthday fall on the same side of it, no
matter how the predicate is chosen. -/

/-- **No birthday-only criterion separates two reals of equal birthday.**

`P` ranges over *every* predicate on ordinals, so this covers any separation criterion
phrased in terms of the birthday alone — thresholds, limit/successor tests, anything.

Combined with Conway's `birthday(√2) = ω = birthday(π)` (cited in the header, not
derivable from these axioms), this is why `conj:diophantine-birthday` cannot be a
statement about `birthday ∘ ofReal`. -/
theorem no_birthday_only_separation {a b : ℝ}
    (h : birthday (ofReal a : K) = birthday (ofReal b : K)) :
    ∀ P : Ordinal → Prop, P (birthday (ofReal a : K)) ↔ P (birthday (ofReal b : K)) := by
  intro P
  rw [h]

/-- The same statement in the form the conjecture would need to contradict: there is **no**
predicate on ordinals witnessing a separation between two reals of equal birthday. -/
theorem not_exists_birthday_separator {a b : ℝ}
    (h : birthday (ofReal a : K) = birthday (ofReal b : K)) :
    ¬ ∃ P : Ordinal → Prop,
        P (birthday (ofReal a : K)) ∧ ¬ P (birthday (ofReal b : K)) := by
  rintro ⟨P, hPa, hPb⟩
  exact hPb ((no_birthday_only_separation (K := K) h P).mp hPa)

/-! ## §3 — what this does and does not settle

**Settled.** A Diophantine separation cannot be a predicate on `birthday (ofReal α)`,
because in the intended model the birthdays coincide.

**Not settled.** Whether a separation exists at the level of the *sign-expansion
trajectory* — the prefixes of `gonshor`, compared against the Liouville exponent. That is
the statement the conjecture's own gloss describes, and it remains open and unformalised.

**Also not settled.** That the corpus's axioms are consistent with Conway's birthday on
irrationals at all: nothing in `SurrealField` pins it, which is the same gap
`BirthdayFaithful` closes for the naturals. -/

end QOU.AppendixSurreals
