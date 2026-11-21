---
# qou-gp9r
title: 'GPMT radical separation (from qou-2och): no statement or artifact exists'
status: todo
type: task
priority: low
created_at: 2026-11-20T16:10:00Z
updated_at: 2026-11-21T12:20:00Z
parent: qou-uhx0
---

Split out of qou-2och (W12, 2026-11-20). qou-2och's title promised a "GPMT radical separation" result; no file, theorem or probe for it exists on main or any branch. First step: find where GPMT is defined in the corpus and write the claim down; until then this is unscoped.

## 2026-11-21: scoping note (hecke-gs-conj sibling (session_01Qmmkt5sJX34MCerjRMERJN))
Corpus grep: "GPMT" is Geer–Patureau-Mirand–Turaev modified quantum dimension. It is used in `computations/canonical_mass.py:379-460` (`gpmt_dmod_111`, `gpmt_dmod_211`, `gpmt_dmod_1111`) and in Lean `QOU.MassTheory.GPMTThreeRowCumulantBridge`, `QOU.MassTheory.H4GPMTModifiedDimensionCumulants`, `QOU/BraidsAndKnots/NucleonIdempotentModifiedTrace.lean`; related beans qou-8mxc, qou-8ffl. No file states a "radical separation" claim.
A scoping fact that a statement must respect: H_n(q) is semisimple whenever q² is not a root of unity of order ≤ n (Dipper–James / Wenzl), so for real q > 1, including q₀ ≈ 1.11, the Jacobson radical of H_n(q) is zero and there is nothing for a modified trace to separate. The GPMT construction is about the ideal of projective objects where the ordinary quantum dimension vanishes, which only happens at roots of unity. So a non-vacuous "GPMT radical separation" has to be stated at a root of unity (or for a non-semisimple quotient), not at q₀. Candidate statement for the owner to accept or reject: "at q a primitive 2ℓ-th root of unity, the GPMT modified trace on the projective ideal of H_n(q)-mod is non-degenerate". Still unscoped until the owner picks; low priority.
