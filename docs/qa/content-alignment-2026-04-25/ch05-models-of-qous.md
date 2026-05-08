# Chapter 5 — Models of QOUs — QA Report

**Review Date:** 2026-04-25
**Chapter Directory:** `content/quantum-observable-universe/models-of-qous/`
**Coverage:** 39 .md, 12 .lean, ~40 .ts (Part A only — Part B Descartes is now its own chapter)

## Inventory

59 blocks across 5 sections (Part A only):

| Section | Blocks |
|---|---|
| Physical interpretation and main result | 6 |
| Archimedean specialisations | 21 |
| Non-Archimedean models | 4 |
| Lifting via Formal Groups and Witt Vectors | 5 |
| Finite fields and Jones polynomials | 3 |

## Section-to-content alignment

All sections align. Sec 1 sets up `S_q[∇]` and the YM mass-gap categorical conjecture; Sec 2 develops K3, ALE, Calabi-Yau, instantons, Seiberg-Witten; Sec 3 introduces $p$-adic via Drinfeld; Sec 4 lifts $\mathbb{F}_p \to \mathbb{Q}_p$ via formal groups + Fresse skew-Poisson; Sec 5 finite-field realisation + braid stub.

## Section-to-chapter alignment

Intent (Part A): QOU axioms admit realisations over different ground fields. Verified arc complete. Part B (Bring's surface, $\chi(A) = -6$) lives in `descartes-universe/`.

## One-voice violations

Grep for editorializing blacklist + person violations: **0 matches**. Heisenberg epigraph in `heisenberg-commutator.md` is an attributed historical quote (allowed).

## Notational alignment

| Pattern | Status |
|---|---|
| `\mathcal{C}` (should be `\mathbf{C}`) | ✓ none |
| `E_q` for elliptic curve (should be `\mathcal{E}_q`) | ✓ none |
| Deprecated 5-tuple `(M, θ, G, P, E)` | ✓ none |
| `\mathfrak{m}` for mass | ✓ 8 occurrences, all correct |
| `\omega` (10 occurrences) | ✓ all are geometric forms (`\omega_I, \omega_J, \omega_K`, contact forms), not fibre functor |
| Numerical $q$ values | ✓ none |

## Substrate-q vs finite-field-q collision

Audit clean. $q > 1$ = substrate parameter (continuous); $q \in \mathbb{F}_p^\times$ when used = root of unity in finite field. Context disambiguates everywhere. No collision.

## Expository simplification opportunities

1. **Sec 3 (Non-Archimedean)** — compressed; add motivating paragraph on why $p$-adic geometry is needed (currently jumps straight to Ostrowski).
2. **Sec 4 (Witt vector lifting)** — notation-heavy (F-crystals, unit-root, Kummer filtration). Add a roadmap diagram for the three-step lift $\mathbb{F}_p \to \mathrm{Dist}(H) \to \mathbb{Q}_p$.
3. **Sec 2 (Archimedean, 21 blocks)** — largest section; consider sub-sectioning out "Contact geometry foundations" (Reeb decomposition, spatial realization, contact form) before Seiberg-Witten and instantons.
4. **Sec 1 (Main commutative diagram)** — add a diagram legend block explaining each vertex (algebra $A$, Kähler manifold, $\mathbb{P}^1$ fibre) before diving into commutativity.
5. **Sec 5 (jones-polynomials.md)** — currently a stub deferring everything to Ch 10. Expand to 1-2 paragraphs sketching why $\mathrm{SU}_q(2)$ reps produce Jones invariants and how $q$ interacts with crossing number.

## Issue tally

| Severity | Count |
|---|---|
| Blocker | 0 |
| Major | 0 |
| Minor | 0 |
| Simplification | 5 |
| **Total** | **5** |
