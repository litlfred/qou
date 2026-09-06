import QOU.BraidKnot.MarkovAxiomsPrimitive

open QOU.BraidKnot

/-- Does the `MarkovTraceAxioms` instance do any work in
`MarkovTraceAxioms_implies_disjoint_stabilisation`?  Same statement, proved by
handing back the right-hand side and never touching `h`. -/
theorem probe_no_instance_needed {R : Type*} [Field R] (u : R)
    [h : MarkovTraceAxioms u] :
    ∀ τ_x : R, ∃ τ_x_stab : R, τ_x_stab = τ_x * markovZax u :=
  fun τ_x => ⟨τ_x * markovZax u, rfl⟩

/-- Stronger: the statement holds for an ARBITRARY function in place of
`markovZax`, so it constrains the Markov parameter not at all. -/
theorem probe_holds_for_any_function {R : Type*} [Field R] (f : R → R) (u : R) :
    ∀ τ_x : R, ∃ τ_x_stab : R, τ_x_stab = τ_x * f u :=
  fun τ_x => ⟨τ_x * f u, rfl⟩
