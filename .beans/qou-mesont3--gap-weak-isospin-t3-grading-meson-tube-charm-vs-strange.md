---
# qou-mesont3
title: 'GAP: weak-isospin T₃ grading of the H₃(q) meson tube (charm vs strange; refines qou-qpj9)'
status: open
type: task
priority: normal
created_at: 2026-08-02T00:00:00Z
updated_at: 2026-08-02T00:00:00Z
---

## Refines `qou-qpj9` (meson-binding braid gate)

The meson-binding braid gate (`qou-qpj9`, J/ψ attack PR #4608) was
re-attacked on the **D meson** `c̄u` (1864.84 MeV) via the symbolic
gg→c̄c operator-selection route (owner redirection). Result: **honest
negative**, sharpened to a precise missing datum. Full analysis:
[`docs/audits/2026-08-02-meson-fluxtube-junction-reduction.md`](../docs/audits/2026-08-02-meson-fluxtube-junction-reduction.md),
PR #4614, sorry-free Lean `MesonFluxTubeReduction.lean`.

## The two obstructions found

1. **Naive Y-junction → single-tube reduction is Vol=0 (scope (b)).**
   The literal reduction takes strands 3→2; `B₂ ≅ ℤ` is abelian, so every
   2-strand closure is `T(2,k)`, Vol=0 (SnapPy-verified k=2..10, incl.
   gluon `T(2,9)`). Strand *removal* cannot build hyperbolic (Brunnian)
   structure. The framework correctly uses the 3-strand `H₃(q)` Hopf-bound
   meson instead — the "3rd strand" is the binding, not a quark.

2. **The `T(2,n)` winding dictionary is charm-degenerate (load-bearing).**
   Meson crossings = n₁+n₂ (`lepton-meson-torus-knot-dictionary.lean`,
   Lean-proved). Charm=5 ⇒ D `{5,3}` = kaon `{3,5}` (8 crossings, IDENTICAL
   multiset); charm=7 ⇒ D `{7,3}` collides with η/φ (10). `windingContent`
   is non-injective (Lean-proved). The operator-selection selects the
   generation-2 (n=5) block = the *strange* block; no charm-specific
   operator exists in the `{γ,σ₀,σ₁,L₊,L₋,e⁻}` basis. So the D-meson braid
   is NOT canonically fixed → no mass check was run (anti-fit).

## The precise missing datum

A **weak-isospin / up-down-type grading `T₃` orthogonal to the generation
winding `n`.** Charm (up-type gen-2) and strange (down-type gen-2) share
`n`; only weak isospin separates them. The up/down distinction lives in
the framework's *weak* generator `T(3,5)` (`force-knot-identification.md`),
NOT in the `T(2,n)` winding dictionary. Until the meson-binding operation
consumes a `T₃` grading (selecting the c̄ block distinctly from the s̄
block), the D-meson braid is under-determined and its mass is only
fittable.

## Next honest step

Derive (or refute) a `T₃` grading of the `H₃(q)` meson tube from the
`T(3,5)` weak-generator up↔down action (or a bar/mirror asymmetry on the
c̄ end). If it canonically fixes the asymmetric `c̄`(5̄)|light(3) braid,
THEN check once against `m_D`. Do NOT hand-pick a braid to hit 1865.

## Side finding (canonical-watcher)

Live corpus inconsistency: charm assigned **T(2,5)**
(`knot-formula-table-table2-data.md` row 11) vs **T(2,7)**
(`knot-notation-convention-table1-data.md` row 9). Resolve independently.
