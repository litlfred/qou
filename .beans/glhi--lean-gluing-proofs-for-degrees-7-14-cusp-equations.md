---
# glhi
title: 'Lean gluing proofs: degrees 7–14, cusp equations, and wiring to SatisfiesEdgeEquations'
status: completed
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

---
**2026-08-10 (later still) — 16 manifolds certified, generated. Item 3 is DONE.**

`QOU/Knot/GeneratedCertified.lean` — **16 `SatisfiesEdgeEquations` certifications**,
machine-generated from the `SixOneCertified` template, sorry-free on standard axioms:
4₁ 5₂ 7₂ 6₂ 8₂₀ 9₄₂ 7₄ 12n242 v3227 s776 m371 7₇ 8₂₁ 6₃ 7₃ 8₁. Emitter added to
`scripts/gen-gluing-lean.py` as `emit_certification`.

The generated identities from `glnl` are no longer standalone: each now certifies a
`ShapedTriangulation` the rest of the corpus can consume.

### ⚠ My proposed "generator improvement" was WRONG, and I checked before building on it

The previous entry recommended emitting the cleared identity as a `Finset` product to
delete the bridging step. **That does not work**: the ∏ form still indexes the shapes by
`Fin n`, so the `Matrix` application survives and the reduction problem is unchanged. The
recommendation is withdrawn; the validated flattened-plus-bridge template is what shipped.

### ⚠ THE TRAP THAT COST THE MOST, and it hides at exactly n = 5

A curated `simp only [Matrix.cons_val_zero, cons_val_one, cons_val_two, cons_val_three,
…]` works perfectly **up to n = 4** and then silently stops:

- Mathlib names `cons_val_zero/one/two/three` and **no `cons_val_four`**;
- `cons_val_succ` does **not** fire on a literal `4 : Fin 5`, because that is not
  syntactically a `Fin.succ`.

So the matrix application survives into the goal and the proof fails with a bare
**"ring failed, ring expressions not equal"** — which reads as a *wrong cofactor*, sending
you to check the arithmetic, when the arithmetic is fine and a `simp` is stuck.

**This is the second time in this bean that an unreduced `simp` disguised itself as a
`ring` failure.** The first was `fin_cases` leaving `⟨0, ⋯⟩`. Both were found only by
dumping the goal; neither error message points anywhere useful.

Fix: **full `simp`, not `simp only`**. Measured — `n ≤ 4` passes either way, `n ≥ 5`
needs it. Recorded as a comment at the emission site, since a future editor "tightening"
it back to `simp only` would break every `n ≥ 5` manifold and get a misleading error.

### A process note

The first generation run emitted 23 lines and I nearly missed it: I had piped stderr to
`/dev/null`, so a `KeyError: 'edges'` — my emitter assumed a key the real `build()` does
not return — vanished silently. **Suppressing stderr on a code generator turns a crash
into an empty file.**

### Remaining on this bean

1. **Degrees 7–14** — untouched.
2. **Cusp equations** — untouched.
3. ~~Wiring~~ — **done**: generic bridge, hand-validated template, 16 generated.
   The three manifolds with `n = 9` (9₃₅, o9_00000) and `n ≥ 9` generally are **not**
   emitted: Mathlib stops at `Fin.prod_univ_eight`, and the emitter says so rather than
   emitting something broken.

---
**2026-08-10 — item 2 (cusp equations) DONE. `QOU/Knot/GeneratedCusp.lean`.**

**42 cusp theorems across 17 manifolds**, machine-generated, sorry-free on standard
axioms. Emitter added as `emit_cusp`.

### The negative exponents never became `zpow`

This bean assumed cusp equations would need "inverses as explicit polynomials plus `zpow`
handling". They do not. Every edge parameter is a unit, so

    ∏ paramᵉ = 1   ⟺   ∏_{e>0} paramᵉ  =  ∏_{e<0} param^{−e}

and **both sides now have natural exponents**. Clearing denominators turns the whole
thing into one polynomial identity — exactly the edge case — so the same exact-division
cofactor works. `zpow` appears nowhere, and no invertibility bookkeeping is threaded
through the statements.

That is a strictly simpler design than this bean anticipated, and worth recording as the
reason cusp equations turned out cheap rather than expensive.

### ⚠ Three of forty-two need a different tactic shape, and it is not visible in advance

When the cofactor is **0** the cusp identity is a plain ring identity, and the preceding
`simp only [zⱼ]` closes the goal outright — so a bare `linear_combination` fails with
**"No goals to be solved"**. Measured: 3 of 42.

Fix: emit `all_goals linear_combination …`, which succeeds on zero goals, so **one
emission shape covers both cases**. Recorded at the emission site.

This is the third time in this bean a generated proof failed for a reason that is a
property of the *tactic state* rather than the mathematics:

1. `fin_cases` leaving `⟨0, ⋯⟩` unreduced → looked like a wrong cofactor;
2. no `Matrix.cons_val_four`, so `simp only` silently stops at n ≥ 5 → looked like a
   wrong cofactor;
3. cofactor 0 closing the goal early → looked like a broken emission.

In all three the mathematics was already correct and asserted exact in the generator
*before* emission. **That assertion is what made each one cheap to diagnose** — it ruled
out the arithmetic immediately, leaving only the tactic state.

### Remaining on this bean

1. **Degrees 7–14** — the only item left untouched. Route 75 verifies them in Python;
   Lean has nothing.
2. ~~Cusp equations~~ — done.
3. ~~Wiring~~ — done.

Cusp equations are the **completeness** condition on the cusp, not the edge condition;
satisfying them still says nothing about whether any of this is a triangulation *of* a
knot complement.

---
**2026-08-15 — item 1 (degrees 7–14) DONE. All three items are now closed.**

`QOU/Knot/GeneratedGluingHigh.lean` — **180 theorems across 8 manifolds**, degrees 7
through 14: 9₂ (7), 10₁ 7₅ 8₂ 8₃ (8), 7₆ (9), t12000 (13), 10₁₀₀ (14). Sorry-free; all
180 verified `#print axioms` = `[propext, Classical.choice, Quot.sound]`;
`lake build QOU.Knot.GeneratedGluingHigh` exit 0 with the `.olean` deleted first.

### ⚠ THIS BEAN'S CENTRAL PREDICTION WAS WRONG, and the number is the interesting part

The bean said: "the cofactors grow and the emitted file would be large … **Measure before
committing to it; a file that takes an hour to compile is worse than no file.**" The
measurement was the right precondition and I did it first. It came out the other way:

| what | size | `lake build` |
|---|---|---|
| degrees 7–9, 6 manifolds | 91 KB | **95 s** |
| t12000, degree 13 | 56 KB | **60 s** |
| 10₁₀₀, degree 14, 14 tets | 384 KB | **131 s** |
| all eight together | 532 KB | **264 s** |

`10₁₀₀` alone is **2.5× the character count of the entire degree 2–6 module** and carries
a single `linear_combination` cofactor **30,193 characters long** — and it compiles in
about two minutes.

**Why the extrapolation from degree 9 overshoots.** Cost tracks the *number* of `ring`
normalisations far more than the size of any one of them. `10₁₀₀` has 14 equations of
enormous individual width; six degree-8/9 manifolds have 40 equations of moderate width,
and cost more per byte. So "cofactor size" — the quantity this bean identified as the
thing that grows — is **not** the quantity that predicts compile time. That is the
generalisable lesson: for `linear_combination`-shaped proofs, count the calls, not the
characters.

Nothing in the 7–14 range needed abandoning. The degree ceiling for this method is not
where this bean placed it, and no ceiling was found at all within the range Route 75
covers.

### Unchanged scope, and one real limit

Edge equations only, at an **arbitrary root** — flat shapes permitted, hyperbolicity not
established (that needs `Im z > 0`). Nothing says any of this is a triangulation *of* a
knot complement.

`10₁₀₀`'s **14 tetrahedra exceed the `SatisfiesEdgeEquations` certification template**,
which stops at 8 because Mathlib provides `Fin.prod_univ_{two..eight}` and no further —
the same limit already recorded for 9₃₅ and o9_00000. The standalone identities are
unaffected; only the certification wrapper is. Lifting it needs iterated
`Fin.prod_univ_succ`, and that is a separate job from this bean.

### Method note

Nothing about the method changed with degree, which is worth stating because it was the
open question: still exact polynomial division with residual asserted zero *before*
emission, still one `linear_combination` per equation, still Bézout certificates for
non-vanishing, still no numerics at any step. Degree 14 uses the identical generator path
as degree 2.

### Status

All three items delivered — degrees 7–14, cusp equations, and the wiring. Setting
**completed**. Two things deliberately left for successors, neither a defect of this
bean's scope:

1. `Fin.prod_univ_succ` iteration to certify `n ≥ 9` triangulations (9₃₅, o9_00000, 10₁₀₀).
2. Degrees beyond 14 — untested, and now worth testing, since the ceiling this bean
   predicted did not appear where expected.
