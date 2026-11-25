Every proof in this paper possesses a corresponding Lean 4 formalisation, except where explicitly citing external references for large prior results. **716 of 726 (98.6%) provable claims** (theorems, lemmas, propositions, corollaries) carry **full Lean proofs**; the remainder bear the `sorry` marker against an explicit bibliographic reference. The paper poses **104 primary open conjectures** of its own—famous external open problems it connects to, and conjectures conditional on those primaries, are tallied separately—of which **77 (74%) are class-axiomatised in Lean** using the conditional-class convention. This allows downstream results to persist as fully verified conditional theorems. The Lean sources reside at [https://github.com/litlfred/qou](https://github.com/litlfred/qou).

## Four-tier formalisation architecture

Across approximately $4{,}850$ Lean 4 modules under `QOU/`, formalised declarations are stratified into a strict four-tier directed acyclic graph so that reusable pure mathematics never depends on physical interpretations or numerical constants:

1. **Tier 0 — `Mathlib4` foundation.** Commutative algebra, monoidal and rigid categories, representation theory, algebraic topology, measure theory, and analytic special functions imported directly from `Mathlib`.
2. **Tier A — `Mathlib4` core upstreaming additions (`QOU/MathlibExt/`).** General-purpose theorems filling immediate upstream library gaps—including the unit group $\mathbb{Z}[q,q^{-1}]^\times = \{\pm q^m\}$, the Clausen and Bloch--Wigner dilogarithm pentagon identities, and piecewise-linear link isotopy—designed to drop directly into existing `Mathlib` namespaces.
3. **Tier B — Six standalone Reservoir community libraries (`QOU/MathlibInfra/`, `QOU/HeckeAlgebra/`, `QOU/Nuclear/`).** Self-contained pure-mathematics packages covering Iwahori--Hecke and Temperley--Lieb towers, Nakayama-twisted Frobenius--Hopf algebras, generic-ordered-ring conic duality and toric Gröbner bases, finite Rieffel compact quantum metric spaces, Thomae--Jackson $q$-calculus, and Artin braid / Bring surface / octonionic colour geometry.
4. **Tier C — QOU categorical core and Archimedean boundary (`QOU/QuantumUniverse/`, `QOU/Torsion/`, `QOU/Archimedean/`).** Pre-wall categorical constructions over arbitrary commutative rings $R$ (`|q| > 1` or $q \in R^\times$), separated explicitly from the post-wall real comparison layer at $q_0 \in \mathbb{R}_{>1}$.

## Kernel trust and non-vacuity discipline

Every closed theorem in Tiers A--C satisfies three mechanical verification invariants:

- **Standard kernel axioms only.** Inspecting the kernel axiom footprint of any complete theorem yields at most Lean's three standard foundational axioms `propext`, `Classical.choice`, and `Quot.sound`. Zero custom `axiom` declarations are permitted anywhere in the formalisation.
- **Explicit typeclass packaging of open hypotheses.** Unproved mathematical or physical conjectures are encoded as explicit Lean `class` or `structure` parameters rather than global axioms, ensuring that every downstream theorem displays its exact conditional dependencies in its type signature.
- **Automated non-vacuity auditing.** A four-rule syntactic and semantic vacuity gate scans every module for self-assuming hypotheses, tautological typeclass field projections, conjunction projections, and direct hypothesis rewrites, preventing vacuous wrappers from masquerading as substantive derivations.
