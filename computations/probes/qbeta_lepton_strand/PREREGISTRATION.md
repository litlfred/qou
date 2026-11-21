# Pre-registration: the electron strand next to the γγ base (issue #8833)

Written and committed before the probe below is run. Owner, 2026-11-21: *"Explore the lepton
strands"*; *"formalize first and try to derive ... If they are derivable they should be
included"*.

## Inputs (all rulings, none chosen here)

* Photon: γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹. Vertex V_i = σ_i σ_{i+1}⁻¹.
* Nucleon base: β_Bor = (σ₀σ₁⁻¹)³ on strands 0–2.
* Electron: Δ = σ₀σ₁σ₀ ∈ B₃ (closure: Hopf link), placed on strands 3–5 as σ₃σ₄σ₃.
* Trace: the two-term Lagrangian trace; Markov parameter convention D, z = q³/(q²+1).
* q₀: the proton pin. Representation: Jimbo R-matrix on (C²)^{⊗6}, eigenvalues q, −1/q.

## Lean first

`QOU/QBeta/ElectronHalfTwistBlock.lean`: on V_(2,1), tr Δ = 0, det Δ = −1, Δ² = 1 (unit
circle); on V_(3), Δ = q³ (real positive, phase 3 ln q); Markov value t(Δ) = z(hz + 1), at
convention D q³(q⁴+1)/(q²+1)².

## The closed family

W = X · β_Bor · Δ on six strands, X every product of 0 to 3 letters from {V₀, …, V₄}
(1 + 5 + 25 + 125 = 156 words, mirrors excluded, as in the four-strand scan). Spectrum on the
weight space #d = 3 (dimension 20), which carries every two-row H₆ block, i.e. every block
convention D keeps.

## What is reported for every word

* whether the spectrum has a real positive eigenvalue ≠ 1 (an imaginary phase a = |ln λ|);
* the largest such a, and cosh a;
* whether X touches the junction (contains V₁, V₂ or V₃, the letters that use σ₂).

## What this does NOT do

* No word is selected, and none is scored. A word reaching a = 1.5239 (the factor the scored
  cell lacks) would be reported, not adopted: only a word derived as the minimal admitted one
  could be used, and that is the owner's call.
* Braid spectra are not bounded in word length (pseudo-Anosov growth), so a long enough word
  will reach any a. The length cut-off 3 is fixed here, before running, for that reason.
* The rule for how a disjoint lepton factor enters ε_flavour is not decided here. The Lean
  values above are reported as candidates only.
