---
# qou-0xrn
title: 'GAP: spin-involution-lp-dual-invariance (24 errors) blocked by a SUPERSEDED self-assuming sibling class'
status: todo
type: task
priority: normal
created_at: 2026-09-04T02:43:55Z
updated_at: 2026-09-04T02:44:35Z
---

The 24-error outlier of the sibling sweep (`qou-e7xv`). NOT 24 defects — 19
of the 24 are one cascade, and the root is a name that does not exist.

## What fails

`mass-theory/spin-involution-lp-dual-invariance.lean` uses
`FrobeniusTraceAlgebra`, which Lean auto-binds as an implicit because it is
not in scope — hence 19 × "Function expected at FrobeniusTraceAlgebra … but
this term has type ?m.1", plus the cascade through `SpinInvolution` (declared
in that same file, so it never gets declared once line 50 fails).

The file imports `QOU.BraidKnot.FrobeniusSelfDualityForcesLPDualExtraction`.
That LIBRARY module does not declare `FrobeniusTraceAlgebra`. The name is
declared in a *different content-block sibling*,
`mass-theory/frobenius-self-duality-forces-lp-dual-extraction.lean` — and
siblings cannot import siblings (outside the Lake globs, no module path).
Same structural blocker as `ReebBundle` in `qou-xdwp`.

## The part that matters: the two objects have DIVERGED, and the sibling is the bad one

    LIBRARY  structure FrobeniusSelfDualityForcesLPDualExtraction (A) (R)
               τ : A → R ;  tau_cyclic ;  tau_add ;  nondegenerate
             def  Obs (a) := fun b => F.τ (a * b)
             theorem Obs_eq_pairing ... := rfl          -- DERIVED

    SIBLING  class FrobeniusTraceAlgebra (R)
               algebra : Type ; trace ; obs_frame ; frob_map
               obs_eq_frob   : obs_frame = frob_map     -- ASSUMED
               obs_bijective : Function.Bijective obs_frame  -- ASSUMED

The block's `.md` says the Observation Frame is **defined** as
`Obs_τ(a) := τ(a · −)`. The library does exactly that and gets
`Obs_eq_pairing` by `rfl`. The sibling carries `obs_frame` and `frob_map` as
two independent fields and then ASSUMES they are equal — assuming, as an
axiom field, an identity that is definitional in the correct version. It also
assumes `obs_bijective` rather than deriving it from `nondegenerate`. That is
the §3b-cond item-5 shape.

The block's `lean.ref` names the LIBRARY declaration
(`qou:QOU.BraidKnot.FrobeniusSelfDualityForcesLPDualExtraction`), so the ref
itself is right. But §0a resolves a ref sibling-FIRST **by file**, so a reader
following it opens the sibling and meets the superseded class.

**The superseded sibling COMPILES CLEAN** (0 errors; it is not in the sweep's
failure list). Nothing flags it. Its only two referrers are itself and the
broken file.

## What to do — a judgement call, hence a bean and not a patch

Port `spin-involution-lp-dual-invariance.lean` onto the library structure.
Not mechanical: the sibling bundles the carrier as a FIELD (`FA.algebra`)
while the library takes it as a PARAMETER (`A`), so every use site changes
shape, and `SpinInvolution` (declared in the failing file) has to be
re-parameterised too. Then delete the superseded sibling, or reduce it to a
docstub, so the §0a sibling-first path stops reaching a self-assuming class.

Do NOT "fix" the 24 errors by declaring `FrobeniusTraceAlgebra` locally —
that would propagate the assumed-conclusion class instead of retiring it.
