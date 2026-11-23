# H4 result: what breaks u ↔ d (2026-11-16)

Pre-registration: `h4_involution_breaking_preregistration.md`. Criterion: a hit is an object that
does not commute with the total lowering operator `F₃` and has a framework-fixed size other than
the pivot `q^{∓2}`.

**Result: no hit.**

| # | candidate | commutes with F₃? | size | verdict |
|---|---|---|---|---|
| 1 | pivot `K = diag(q, q⁻¹)` in the trace | no (`KFK⁻¹ = q⁻²F`) | derived: `q^{∓2}`, relative 1 − q⁻² ≈ 18.8 % | breaks, but it is the known pivot, so not a hit |
| 2 | a reference (vacuum) vector in V | no | the corpus selects one only through #5 | see #5 |
| 3 | boundary condition on an open strand | no, for a fixed vector | no corpus construction found | undefined |
| 4 | chiral projector / weak vertex `L±`, `P_L`, `P_R`, `J`, `Δ_S` | **yes**: polynomials in Ř (weak-vertex thread, symbolic) | none | excluded by `commutant_trace_eq`; agrees with ε-L1 and ε-TR1 (draft PR #8104) |
| 5 | corpus Higgs vacuum `ϱ_Φ`, idempotent `e_H` (`conj:g-action-on-substrate`, G-3/G-4) | no: `e_H` projects onto one weight vector of the doublet | direction set by `Q·ϱ = 0` with the Higgs hypercharge `y = 1/2` **assigned** in Table 1; norm `v²/m_e²` **empirical**; quark coupling unspecified | breaks, size input, so not a hit |
| 6 | ev/coev, twist θ, Jones–Wenzl, KZ, Reeb | yes (module maps / central / Casimir-built) | none | expected nulls, confirmed earlier (H2, A2) |
| — | Coulomb insertion `Σ Q_aQ_b`, `Q = T³ + Y/2` (weak-vertex ε-EM1; Bridge B EM1) | no (diagonal, not F₃-equivariant) | asymmetry exactly `2Y`; `Y = ±1/3` is a labelled conditional input (bean qou-99qc) | breaks, size input |

## What #5 shows

The Higgs role is already written into the corpus as a conjecture, and it does the right
structural thing: a rank-1 projector on one weight line of the doublet. As a single-strand
diagonal operator it is `a + b·h` with `b ≠ 0`, so by `ud1` its first-order effect on n − p is a
word-independent constant `−2b` times its unspecified coupling. Its direction comes from an
assigned hypercharge, and its norm comes from the measured VEV.

Two tensions in that block, reported here and not edited (content changes wait on the owner):

1. **G-3 asks for a non-zero morphism `𝟏 → A^{(H)}` with `A^{(H)}` the spin-½ irrep.** In
   `Rep(SU_q(2))` that Hom-space is zero (Schur), so no such morphism exists inside the
   equivariant category. This is the categorical form of the no-go: a VEV is a vector that is
   **not** a module map, so it has to be adjoined from outside `Rep(U_q)` (a fibre-functor or
   boundary datum that forgets the symmetry). The corpus has not specified that datum.
2. **G-2/G-4 give `dim_q(e_H·A^{(H)}) = [2]_q` for a rank-1 projector.** With the pivot `K`, the
   quantum dimension of a weight line is `q` or `q⁻¹`, never `[2]_q = q + q⁻¹`. `[2]_q` is the
   dimension of the whole doublet.

## Consequence

Inside the framework as it stands, the only derived u ↔ d breaker is the pivot, and its size is
fixed. Every other breaker found (the corpus Higgs idempotent, the Coulomb insertion, a mass term
`diag(m_u, m_d)`) carries an imported number: `Y`, `v`, or a coupling. A derived n − p splitting
therefore needs a new object: a non-equivariant datum adjoined to `Rep(U_q)`, with its direction
**and** size derived. This is an open problem, scope (b) relative to the equivariant class (proved
invariant: commuting with `F₃`).
