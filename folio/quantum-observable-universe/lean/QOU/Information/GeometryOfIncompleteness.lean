import QOU.Information.PhysicalIntractability

/-!
# QOU.Information.GeometryOfIncompleteness — the capstone

The corpus unification (`incompleteness-implies-horizon-proof.md`): Turing
completeness, Gödel incompleteness, and physical intractability are three
witnesses of **one** phenomenon — the vanishing of degree-0 sections
`Γ(𝓗, A₀) = 0`.  A degree-0 datum (a decision answer, a particle identity, a
Gödel sentence's truth value) is **behind the jet horizon** when it is
*inaccessible*, and there are two independent routes to inaccessibility:

* **formal** — the datum is unprovable (Gödel, forced by Turing-completeness);
* **physical** — extracting it is super-polynomial (the bandwidth bound,
  `qou_physical_intractability_unconditional`, derived from the `3^{3n}`
  resolution tree).

The capstone below assembles both into: *a Turing-complete substrate has a
nonempty horizon — degree-0 truth is inaccessible.*  Honest scope: the formal
witness is Gödel incompleteness (standard, taken as the hypothesis
`¬ formallyProvable`); the physical witness is **derived** here; the identity
"horizon = this inaccessibility" is the framework's degree-0 reading.  This is
an **existence/necessity** statement about substrate structure — it does *not*
assert `P ≠ NP` (which needs the separate, open counting→decision transfer).
-/

namespace QOU.Information

universe u

/-- A **degree-0 datum**: a decision answer / particle identity / truth value,
    carried as an element of a caller-supplied `Datum` type, together with the
    step-count needed to physically extract it.

    **`formallyProvable : Prop` was a field until 2026-09-14 and is now a
    caller-supplied predicate** (`FormallyProvable : Datum → Prop`, a parameter
    of `Inaccessible` below).  As a field it was typed with the *universe*
    `Prop`, so the CONSTRUCTOR chose the proposition — and that made the
    capstone dischargeable with no mathematical content.  Verified before the
    change, not asserted:

    ```
    example : ∃ d : DegreeZeroDatum, Inaccessible d :=
      horizon_nonempty { formallyProvable := False, extractSteps := fun n => n }
        not_false          -- compiled, exit 0
    ```

    "There exists a datum that is not formally provable" was proved by
    *defining* one whose provability proposition is literally `False`.  The
    structure also had no datum in it — only a `Prop` and a step-count — so
    there was nothing for provability to be *about*.

    With `Datum` and `FormallyProvable` supplied by the caller, applying the
    capstone now requires exhibiting a real carrier and a real failure of
    provability on it — which is Gödel's theorem, i.e. content.  And it is
    refutable: see `not_inaccessible_of_all_provable`. -/
structure DegreeZeroDatum (Datum : Type u) where
  /-- The datum itself — the thing whose provability is at issue. -/
  datum : Datum
  /-- The step-count of a physical extractor (as a function of instance size). -/
  extractSteps : ℕ → ℕ

/-- A datum is **inaccessible** — behind the jet horizon `Γ(𝓗, A₀) = 0` — when
    it is either formally unprovable (Gödel) or physically intractable
    (super-polynomial extraction), with provability judged by the caller's
    `FormallyProvable`. -/
def Inaccessible {Datum : Type u} (FormallyProvable : Datum → Prop)
    (d : DegreeZeroDatum Datum) : Prop :=
  ¬ FormallyProvable d.datum ∨ SuperPolynomial d.extractSteps

/-- **A Gödel-unprovable datum is behind the horizon (sorry-free).** -/
theorem inaccessible_of_unprovable {Datum : Type u}
    {FormallyProvable : Datum → Prop} {d : DegreeZeroDatum Datum}
    (h : ¬ FormallyProvable d.datum) : Inaccessible FormallyProvable d := Or.inl h

/-- **A physically-intractable datum is behind the horizon (sorry-free).** -/
theorem inaccessible_of_intractable {Datum : Type u}
    {FormallyProvable : Datum → Prop} {d : DegreeZeroDatum Datum}
    (h : SuperPolynomial d.extractSteps) : Inaccessible FormallyProvable d := Or.inr h

/-- **The notion is refutable**, which it was not while provability was a
    constructor-chosen field: under a predicate that holds of everything, a
    datum with a polynomially-bounded extractor is NOT behind the horizon.

    Previously `Inaccessible` could be discharged for a fabricated datum at
    any `FormallyProvable`, so no instance of "accessible" existed to exhibit. -/
theorem not_inaccessible_of_all_provable {Datum : Type u}
    (d : DegreeZeroDatum Datum) (h : ¬ SuperPolynomial d.extractSteps) :
    ¬ Inaccessible (fun _ : Datum => True) d := by
  rintro (hnp | hsp)
  · exact hnp trivial
  · exact h hsp

/-- **The geometry of incompleteness (capstone, sorry-free).**  Given
    (i) a Gödel datum that is formally unprovable — the incompleteness witness,
    forced in any Turing-complete substrate — and
    (ii) a boundary datum whose bandwidth-`B` extractor must read the full
    `3^{3n}` surviving resolution tree — the physical witness —
    the jet horizon is **nonempty**: some degree-0 truth is inaccessible.  The
    boundary datum is inaccessible *physically* (derived via
    `qou_physical_intractability_unconditional`), and the Gödel datum is
    inaccessible *formally*.  Incompleteness and physical intractability are the
    two faces of the vanishing of degree-0 sections. -/
theorem geometry_of_incompleteness {Datum : Type u}
    (FormallyProvable : Datum → Prop)
    (godelDatum : DegreeZeroDatum Datum)
    (hgodel : ¬ FormallyProvable godelDatum.datum)
    (boundaryDatum : DegreeZeroDatum Datum) (B : ℕ) (hB : 0 < B)
    (hphysical : ∀ n,
      resolutionTreeSize (3 * n) ≤ boundaryDatum.extractSteps n * B) :
    Inaccessible FormallyProvable godelDatum ∧
      Inaccessible FormallyProvable boundaryDatum :=
  ⟨inaccessible_of_unprovable hgodel,
   inaccessible_of_intractable
     (qou_physical_intractability_unconditional B hB _ hphysical)⟩

/-- **The horizon is nonempty (sorry-free).**  Corollary: under the same
    hypotheses there exists an inaccessible degree-0 datum — the jet horizon
    `Γ(𝓗, A₀) = 0` is realised.  A Turing-complete substrate necessarily hosts
    a region where degree-0 truth is inaccessible: the event horizon is the
    geometry of incompleteness. -/
theorem horizon_nonempty {Datum : Type u}
    (FormallyProvable : Datum → Prop)
    (godelDatum : DegreeZeroDatum Datum)
    (hgodel : ¬ FormallyProvable godelDatum.datum) :
    ∃ d : DegreeZeroDatum Datum, Inaccessible FormallyProvable d :=
  ⟨godelDatum, inaccessible_of_unprovable hgodel⟩

end QOU.Information
