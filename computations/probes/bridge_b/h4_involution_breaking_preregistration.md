# H4: search for a datum that breaks u ↔ d (pre-registration, 2026-11-16)

Written before any candidate is evaluated.

## What is already proved (Lean, `NucleonIsospinExclusions.lean`)

The intertwiner `P` between the proton-type and neutron-type weight spaces of `(C²)^{⊗3}` is
`q⁻¹` times the block of the total lowering operator `F₃` (coproduct `Δ(F) = F⊗1 + K⁻¹⊗F`,
the one commuting with the Jimbo Ř). Any weight-preserving operator commuting with `F₃` has
equal plain traces on the two spaces and restricted quantum traces in ratio `q²`
(`commutant_trace_eq`, `commutant_restrictedTrace_ratio`).

So a candidate can matter only if it **fails to commute with `F₃`**.

## Question

Does the corpus contain an object that (i) does not commute with `F₃`, and (ii) has a size fixed
by the framework rather than imported? That is the Higgs role: a vacuum or boundary choice
that picks a direction in the isospin doublet.

## Candidates, listed before evaluation

1. The pivot `K = diag(q, q⁻¹)` used in the quantum trace. It does not commute with `F`
   (`K F K⁻¹ = q⁻² F`). Size is derived, but known: the factor `q^{∓2}`.
2. A reference (vacuum) vector in V: a highest-weight state `e₁`, or a cup/cap with a fixed
   vector. Its projector breaks the symmetry; ask whether any corpus construction selects it.
3. A boundary condition on an open strand end (Dirichlet-type fixed vector).
4. The chiral projector or weak vertex `L±` (weak-vertex thread; not evaluated here).
5. The corpus Higgs blocks (`categorical-higgs-mechanism`, `weinberg-angle-categorical`,
   `electroweak-higgs-torus-link-triplet`, `g-action-on-substrate`): is any of them an
   operator on the isospin doublet, and does it commute with `F₃`?
6. Equivariant structures, recorded as expected nulls: ev/coev (module maps), the twist θ
   (central), Jones–Wenzl projectors, the KZ connection, the Reeb direction (Bridge A2).

## Classification of each candidate

- **breaks?** Does it commute with `F₃`? Check exactly, where it is an explicit operator.
- **size**: derived (fixed by the framework, no free number), input (a free number), or
  undefined (the corpus does not specify the object as an operator).

A **hit** is a candidate that breaks and has a derived size other than the pivot `q^{∓2}`.

Expected result: no hit. The pivot is the only derived breaker, and its size, a relative
1 − q⁻² ≈ 18.8 %, is far from the comparison value (Δm/m ≈ 0.14 %). That comparison is
physics, and it is the only physics in this note.

No fitting. A candidate is not promoted because its number is closer.
