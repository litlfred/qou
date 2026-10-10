---
# qou-85cg
title: 'Retire the chernSimons_volume_correspondence tautology (NonAbelianStokes.lean:738): ∃ vol, ∀ h, vol h = vol h is witnessed by the zero function; the honest §3b carrier VolumeBridge already exists, so retire rather than add a second carrier'
status: completed
type: task
created_at: 2026-09-06T10:36:09Z
updated_at: 2026-09-06T13:37:57Z
---

## Done (2026-09-06)

`QOU/Mathlib/NonAbelianStokes.lean`: the docstring + `theorem chernSimons_volume_correspondence ... := ⟨fun _ => 0, fun _ => rfl⟩` are replaced by a `/-! ### Retired -/` block pointing at `QOU.MassEndomorphism.VolumeBridge` (non-degenerate §3b class, `volTerm = descTrace + transient`, no instance) as the existing honest carrier, citing [kashaev1997] and [murakami-murakami2001]. No second carrier added. lean-direct `-DautoImplicit=false -s 65536`: exit 0, 0 sorry, only the pre-existing dupNamespace linter warnings; the name survives only in the retirement comment. The 07-12 audit's §G6 request (a CS ↔ volume statement) is discharged by pointing at VolumeBridge rather than by a new declaration. Audit: docs/audits/2026-09-06-bring-cs-lawson-dialog-assessment.md.
