---
# qou-8qby
title: 'GAP: braid-action-tensor.lean has 2 unproved diagram chases after Mathlib drift (was 5 errors)'
status: completed
type: task
priority: normal
created_at: 2026-09-03T22:26:44Z
updated_at: 2026-09-04T05:06:42Z
---

## State

`content/quantum-observable-universe/braids-and-knots/braid-action-tensor.lean`
does NOT compile. Found by a sweep compiling every content-block sibling
`.lean` — these sit outside the Lake globs (`globs = ["QOU", "QOU.+"]`), so
`lake build QOU` never sees them, and CI here is dispatch-only. Nothing was
checking them.

    before this session:  exit 1, 5 errors
    now:                  exit 1, 2 errors

## Fixed (both verified to reduce the error count)

1. `MonoidalCategory.whiskerRight_comp` -> `comp_whiskerRight`. Mathlib
   rename; confirmed against the pin with `#check @comp_whiskerRight`
   (`(f ≫ g) ▷ Z = f ▷ Z ≫ g ▷ Z`). Two sites.
2. `structure BraidRepB3`'s `braid_rel` field carried the default
   `:= yang_baxter_braiding V`, whose type is stated in `sigma1 V`/`sigma2 V`
   while the field's type is in the sibling fields `gen1`/`gen2` — which are
   opaque in the field's TYPE even though their own defaults are those terms.
   Result: "Type mismatch" at the structure and "Fields missing: braid_rel"
   at the one construction site. Default dropped; `braid_action_tensor` now
   supplies `gen1`, `gen2` and `braid_rel` explicitly.

## Still open — 2 rewrites, both associativity bracketing

    :96  `sigma2_is_iso`            rw [Iso.inv_hom_id_assoc]
    :126 `sigma12_eq_alpha_braiding` rw [← hex]   (hex = BraidedCategory.hexagon_forward V V V)

Both fail with "Did not find an occurrence of the pattern". The mathematics
is not in doubt (both are standard braided-monoidal facts, Kassel Ch. XIII);
the proofs were written against a Mathlib whose `Category.assoc` normal form
differed. Tried and did NOT help: `simp only [Category.assoc] at hex` before
the rewrite (inert, reverted to keep the diff minimal). Likely routes:
`reassoc_of% hex`, `slice_lhs`/`slice_rhs`, or `coherence`/`monoidal` tactics.

NO `sorry` was added — AGENTS.md §Zero-sorry default. The statements already
exist and are simply unproved; reporting the gap is the honest disposition.

## Scope note

A full sweep of all 908 sibling `.lean` files is running. A partial
single-threaded pass found 1 failure in 36 (2.8 %), so expect roughly 25
broken siblings corpus-wide — do not fix them one at a time before the sweep
reports; the causes seen so far are Mathlib drift (this file), a
Lean-notation token used as a binder name (`Σ` = Sigma; that class is drained,
0 remaining), and a missing `Mathlib.Data.Real.Basic` import for `Inhabited ℝ`
under `opaque … : ℝ`.
