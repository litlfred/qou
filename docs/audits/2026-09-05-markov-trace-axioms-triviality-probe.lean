import QOU.BraidKnot.MarkovAxiomsPrimitive

open QOU.BraidKnot

/-- Is `MarkovTraceAxioms` trivially inhabited?  Its four fields are two
scalars and two equations pinning them to `1` and `markovZax u`, so the
anonymous constructor should discharge it for ANY `u` with no mathematics. -/
instance probe_trivially_inhabited {R : Type*} [Field R] (u : R) :
    MarkovTraceAxioms u :=
  ⟨1, rfl, markovZax u, rfl⟩

/-- If so, every `[MarkovTraceAxioms u]`-conditional result is unconditional:
here the conditional theorem is obtained with no instance in scope but the
trivial one above. -/
example {R : Type*} [Field R] (u : R) (τ_K1 τ_K2 : R) (k : ℕ) :
    ∃ τ_joint : R, τ_joint = τ_K1 * τ_K2 * (markovZax u)^k :=
  disjoint_product_factorisation u τ_K1 τ_K2 k
