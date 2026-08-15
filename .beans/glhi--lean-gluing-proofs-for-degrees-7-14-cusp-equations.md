---
# glhi
title: 'Lean gluing proofs: degrees 7–14, cusp equations, and wiring to SatisfiesEdgeEquations'
status: todo
type: task
priority: normal
tags:
    - lean
    - hyperbolic-volume
    - gluing-equations
    - codegen
parent: m015
created_at: 2026-08-10T07:00:00Z
updated_at: 2026-08-10T07:00:00Z
---

The successor to `glnl`, which delivered 312 Lean theorems across 19 manifolds at shape
field degrees 2–6 and is **completed** for that scope. Three things it deliberately did
not do.

## 1. Degrees 7–14

Route 75 verifies these exactly in Python; Lean has nothing for them:

| manifold | degree |
|---|---|
| 9₂ | 7 |
| 10₁, 7₅, 8₂, 8₃ | 8 |
| 7₆ | 9 |
| t12000 | 13 |
| 10₁₀₀ | 14 |

`scripts/gen-gluing-lean.py` handles them in principle — the method does not care about
degree. What grows is the **cofactor size**: each edge equation's certificate is
`(LHS − RHS)/P`, and at degree 14 with 16 equations the emitted `linear_combination`
terms get large. Measure before committing to it; a file that takes an hour to compile is
worse than no file.

## 2. Cusp equations

`glnl` covered **edge** equations only, because those have non-negative exponents and
clear to a polynomial identity. Cusp equations carry **negative** exponents — 5₂'s are
`[-1,0,0, 0,0,1, 0,0,0]` and `[2,0,-3, 1,0,-2, 0,0,1]` — so they need each parameter's
inverse as an explicit polynomial in `θ` (available: the parameters are units in
`ℚ(θ)`, and `sympy.invert` already computes exactly this for the Bézout certificates),
plus `zpow` handling in the statement.

Route 75 verifies all cusp equations symbolically in Python. Lean does not.

## 3. Wire the generated theorems to `SatisfiesEdgeEquations`

`glnl`'s own bean asked for this and it was not done: the generated theorems are
**standalone**, when `QOU/MathlibExt/IdealTriangulation.lean` already has `GluingData n e`
and `SatisfiesEdgeEquations`. Landing them as instances of that structure turns the
generated file from a parallel pile of identities into **certification of the corpus's
existing triangulation objects**, which is what makes it compose with
`FiveTwoVolumeConstant`, `FigureEightTriangulation` and the volume functor.

Note the flat-shape generalisation from `m015`: `SatisfiesEdgeEquations` currently lives
on `IdealTriangulation`, which carries `im_pos`. `QOU/Knot/FlatTetrahedra.lean` added
`ShapedTriangulation.SatisfiesEdgeEquations` over possibly-flat shapes. Wiring should
target the **weaker** one — the generated identities hold for an arbitrary root of the
minimal polynomial, which is exactly the flat-tolerant setting, and pinning them to
`im_pos` would re-import a hypothesis the proofs do not use.

## Method, unchanged and known to work

Verbatim from `glnl`, because it held up: state each identity for an **arbitrary root** of
the minimal polynomial (the verification lives in `ℚ[x]/(P)`, so it holds at every root,
which sidesteps root selection); prove non-vanishing by Bézout certificate; prove each
cleared edge equation by one `linear_combination` with a cofactor from exact polynomial
division. **Do not reach for `field_simp`** — its normal form is unpredictable and cannot
be code-generated.

---
**2026-08-10 — item 3 (the wiring) is DONE, generically. `QOU/Knot/GluingBridge.lean`.**

Sorry-free, standard axioms.

### The bridge, proved once instead of per knot

`GeneratedGluing` proves identities in **cleared** form; `SatisfiesEdgeEquations` is in
**product** form. The passage between them is exactly the `field_simp` step `glnl`
refused to code-generate. Doing it **once, generically**, removes the problem entirely:

| lemma | content |
|---|---|
| `Shape.param_pow_prod` | `z^a·(1/(1−z))^b·(1−1/z)^c = z^a(z−1)^c / ((1−z)^b z^c)` |
| `satisfies_of_cleared_one` | cleared ⟹ product, one tetrahedron |
| `satisfies_of_cleared_two` | cleared ⟹ product, two tetrahedra |

**No per-knot cofactor is ever needed again.** A generated cleared identity plus
non-vanishing now gives the product form by `rw` and `div_self`.

⚠ **A trap inside the bridge itself.** The obvious proof — `simp only [param_*]` then
`field_simp` — fails, leaving `(1−z)⁻¹^b * (1−z)^b` uncancelled: `field_simp` does not
cancel an inverse against a power when **the exponent is a variable**. The fix is to
rewrite each parameter to an explicit quotient *first* (`div_pow`), so the inverses become
single atoms. Recorded in the proof, since the failure mode is invisible from the
statement.

### Worked instance: the trefoil, certifying the structure

`trefoil_satisfiesEdgeEquations : trefoilTriangulation.SatisfiesEdgeEquations trefoilGluing`

The identities stop being standalone and start certifying a `ShapedTriangulation` — which
is what this bean asked for. The trefoil is the right first case *because its shapes are
flat*: it exercises the flat-tolerant structure that an `IdealTriangulation` cannot
represent at all, confirming the design note above that the wiring must target `Shape`
rather than `IdealTetrahedron`.

### Remaining on this bean

1. **Degrees 7–14** — untouched.
2. **Cusp equations** — untouched.
3. ~~Wiring~~ — **done generically**; what is left is *applying* it to the 19 manifolds in
   `GeneratedGluing`, which needs a `Shape` per tetrahedron (the `z_j_ne_zero` and
   `one_sub_z_j_ne_zero` lemmas are already generated for exactly this) and an
   `n`-tetrahedron composition lemma beyond the `n = 2` case written here.
   `Finset.prod_div_distrib` makes that routine; it was not needed for the trefoil.

---
**2026-08-10 (later) — the path is validated end to end on a GENERATED manifold. 6₁ is
certified.**

`QOU/Knot/SixOneCertified.lean`, sorry-free, standard axioms:

    satisfiesEdgeEquations : (triangulation ht).SatisfiesEdgeEquations gluing

for an arbitrary root `t` of `x⁴ − 3x³ + 6x² − 5x + 2`. Four tetrahedra, four edges, all
four generated identities consumed. The 312 theorems now have a demonstrated route from
standalone equations to structure certification.

Two general lemmas added to `GluingBridge`:

- `satisfies_edge_of_cleared` — cleared ⟹ product, **at any `n`**, via
  `Finset.prod_div_distrib`;
- `satisfiesEdgeEquations_of_cleared` — the whole edge system from the cleared identity
  at every edge.

### ⚠ Two traps, both invisible from the statements

**1. `fin_cases` breaks the exponent matrix.** Under `fin_cases k` the index becomes
`⟨0, ⋯⟩`, on which `Matrix.cons_val_zero` and friends **do not fire** — so the exponent
matrix never reduces and `linear_combination` is handed an unreduced goal with the entire
`GluingData` literal still in the exponent. It fails with a bare "ring expressions not
equal", which reads like a wrong cofactor rather than a stuck `simp`. Adding `Fin.isValue`
and `Fin.mk_zero` did **not** help.

Fix: prove one cleared lemma **per literal edge index**, where the matrix application
reduces, and only then `fin_cases` and `exact` them. This is why `SixOneCertified` has
four `private theorem cleared_k` rather than one tactic block.

I found this only by dumping the goal with `trace_state`. The failure message points at
`ring`, which is the wrong place to look.

**2. `field_simp` and variable exponents** — recorded with `param_pow_prod`: it does not
cancel `(1−z)⁻¹^b` against `(1−z)^b` when `b` is a variable. Rewrite to explicit quotients
via `div_pow` first.

### Generator improvement this exposes

`GeneratedGluing` emits the cleared identity **flattened**; the whole
`simp only [Fin.prod_univ_four, …]` step exists only to bridge that to the `∏` form.
**Emitting it directly as a `Finset` product would delete that step**, and with it trap 1
— there would be no `Matrix` application to reduce. Worth doing before generating the
remaining 18, since it removes the fiddliest part of the template.

### Remaining

1. Degrees 7–14 — untouched.
2. Cusp equations — untouched.
3. The other 18 manifolds — now **mechanical**: `SixOneCertified` is the template, and
   the generator can emit it. Recommend the `∏`-form change above first.
