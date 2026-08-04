# T3b assessment: distinct-fibre groupoid for flavour SU(3)

**Date:** 2026-08-04
**Bean:** `qou-dwsh` (T3b), epic `qou-8lxd`

## Status: OPEN RESEARCH PROBLEM

The multi-fibre groupoid construction for flavour SU(3) is genuinely
open. No construction exists in the corpus. This note records the
constraints any construction must satisfy.

## 1. The constraints

Any candidate 3-dimensional object W in the multi-fibre groupoid must:

1. **Pass the Sym² gate** (T3a): Sym²(W) must be irreducible (no
   invariant symmetric bilinear form), i.e. W must be non-self-dual.
2. **Not be a tensor power of V**: The single-fibre V is 2-dimensional
   (Descartes condition), so V^⊗n has the Schur-Weyl commutant
   U_q(gl_2), which drops the (1^3) partition at n=3.
3. **Be categorically constructible**: W must arise from the groupoid
   structure of the framework, not be postulated ad hoc.
4. **Be compatible with the mass pipeline**: If W changes the Hecke
   algebra structure used for mass computation, the mass predictions
   must not break (T3f finding: N=2 is structurally tied to masses).

## 2. Available construction directions

### 2a. Octonionic G₂ stabilizer (T3d — partly built)

**Status:** Discrete skeleton machine-checked. The Günaydin-Gürsey
decomposition 7 = 1 ⊕ 3 ⊕ 3̄ provides a non-self-dual triple from
SU(3) ⊂ G₂ = Aut(𝕆). Passes the Sym² gate.

**Gap:** This gives **colour** SU(3), not flavour. Whether colour and
flavour can be identified, or whether they require separate constructions,
is untested.

### 2b. Inter-fibre morphism space

The groupoid G has objects (fibres) and morphisms (gauge transformations).
If G has 3 inequivalent fibre types, the morphism space between them
could provide a 3-dimensional representation. But:
- What forces exactly 3 fibre types?
- Do the inter-fibre morphisms carry the right tensor structure?
- Is the resulting representation non-self-dual?

No corpus content addresses these questions.

### 2c. Schur-Weyl at N=3 via Ocneanu parameter (T3f)

The T3f audit found that the Ocneanu trace parameter a = q^{N-1} is
free. Setting a = q² (N=3) in the HOMFLY-PT would give gl_3-weighted
invariants and the full eightfold-way decomposition. But the mass
pipeline is structurally tied to N=2, so this can't be a global
substitution — it would have to be a separate "flavour channel"
parallel to the "mass channel."

This is the most promising direction: it requires no new construction,
only a separation of the N=2 mass channel from an N=3 flavour channel
on the same Hecke tower. Whether this is categorically coherent is
the question.

## 3. Recommendation

This bean should remain **open** with status **todo**. No construction
can be responsibly authored without resolving the flavour/colour
separation (open problem §4 of the eightfold-way chapter). The most
promising short-term step is:

1. Formalize the separation: can the Hecke tower H_n(q) support BOTH
   an N=2 Jones trace (for mass) and an N=3 HOMFLY trace (for flavour)
   simultaneously, as two different functors on the same algebraic object?
2. If yes: the eightfold-way follows from Schur-Weyl duality at N=3
   applied to the HOMFLY trace, while masses use the Jones trace at N=2.
3. If no: the multi-fibre groupoid or octonionic G₂ route is the only
   remaining direction.
