# Pre-registration: does "only the molecule must pass" depend on word order? (owner: "measure first")

Bean `qou-a1hh`, PR #7741. Owner card 2026-11-15, "Must each particle pass reading 3 on its own
strands?", answered "3. Measure first", with "i think A" (option 1, every particle alone). Written and
pushed **before** any computation below.

## Question

Under option 2 (only the whole molecule must pass reading 3 at every level), does the verdict depend on
which particle sits on the lowest strands? If it does, option 2 is not a property of the molecule but of
a writing order.

## Prediction, derived before the run

In the owner-option-1 cell there is no p–e or junction letter, so the H₂ word is a tensor product of
four 3-strand words X₁ ⊗ X₂ ⊗ X₃ ⊗ X₄ on strands 1–3, 4–6, 7–9 and 10–12. Closing from the top down to
level m ≤ 3 closes X₂, X₃ and X₄ completely. By the Markov property each contributes its scalar trace as
a factor, so χ_μ at level m ≤ 3 equals (that product of traces) × χ_μ(E_{3→m} X₁). Whenever the product
is positive, **levels 1–3 of the molecule are exactly the test of X₁ on its own strands.** So under
option 2 the bottom particle always gets the per-particle test and the others need not. That predicts:

- with the nucleon at the bottom (order p e | …), a nucleon that fails alone (V, V², V⁴, V⁵, V⁷) fails
  the molecule at a level ≤ 3, and the torus electron can pass (as measured: m = 7, 9, t = +1);
- with the electron at the bottom (order e p | …), the torus electron fails at a level ≤ 3, and a nucleon
  that fails alone is no longer tested at levels 1–3.

## Family and tests

Nucleon P ∈ {Vᵏ : k = 1 … 7} (V = σ₀σ₁⁻¹). Electron E ∈ {V³ (γγ), σ₀⁷σ₁ (torus, m = 7, t = +1)}.
Bare H₂ only, no bond letter. Atom 1 order ∈ {pe, ep}, atom 2 order ∈ {pe, ep}: 7 × 2 × 4 = 56 molecules.
Reading 3 at every level 1–12, convention D, proton pin, mpmath at the reused code's dps (40).

- **O1:** for each molecule, the list of failing levels.
- **O2 (prediction check):** for each molecule, levels 1–3 pass iff the bottom particle passes reading 3
  on its own three strands. A mismatch is a FAIL of the check.
- **O3 (the answer):** is the set of passing (P, E) pairs the same for atom-1 order pe and ep?

## Outcomes, fixed now

- **(i) Order-dependent:** O3 differs between pe and ep. Then option 2 is a statement about word order,
  and requiring every particle to pass alone (option 1) is the order-independent version.
- **(ii) Order-independent:** O3 is the same. Then option 2 stands as a property of the molecule.

Nothing fitted, selected against data, or wired. Trace ratios are not computed (bare words only).
