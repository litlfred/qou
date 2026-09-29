---
# qou-tc8y
title: 'BUILD: give BlochWigner_unit_circle its body (Cl_2) — the opaque seal is stale and collides with the proved def'
status: todo
type: task
priority: high
created_at: 2026-09-04T09:07:54Z
updated_at: 2026-09-04T09:07:54Z
parent: qou-8lxd
---

**BUILD.** `QOU/Archimedean/BlochWignerUnitCircle.lean:67` declares

    noncomputable opaque BlochWigner_unit_circle (_θ : ℝ) : ℝ

with a sealed body. Its own docstring (lines 58-62) gives the reason: *"sealed pending
the canonical Clausen-function integration (Phase 3 research-grade closure)"*.

**That closure landed, and the corpus records it two files away.** The candidate body
is already written, sorry-free, at `QOU/Archimedean/BlochWignerMathlibFiller.lean:60`:

    noncomputable def BlochWigner_unit_circle (θ : ℝ) : ℝ := Cl_2 θ

over `Cl_2` at `ClausenFunctionMathlibFiller.lean:80`. The filler's own changelog
records `Cl₂` derivative, series↔integral bridge, continuity and boundary lemmas
**CLOSED 2026-07-19**, and the duplication formula **CLOSED 2026-07-26** — all
sorry-free in `QOU/Knot/Clausen.lean` (`hasDerivAt_clausen:87`, `clausen_eq_series:441`,
`continuous_Cl_2:112`, `Cl_2_two_pi_sub:451`, `Cl_2_pi_div_three_pos:490`).

**It is also a fully-qualified-name collision (the `qou-kfcl` class).** Both files open
`namespace QOU.Archimedean` (`BlochWignerUnitCircle.lean:53`,
`BlochWignerMathlibFiller.lean:53`), so both declare
`QOU.Archimedean.BlochWigner_unit_circle`. The collision is currently dodged by
**commenting the real definition out**: `QOU/Archimedean.lean:30` imports
`BlochWignerUnitCircle`; `QOU/Archimedean.lean:36` is
`-- import QOU.Archimedean.BlochWignerMathlibFiller`. So the sealed stub is live and the
proved definition is disabled.

**Work:** ~5 lines plus import surgery — pick one carrier, give it the `Cl_2` body,
re-enable the import, delete the other. Consumer to re-verify:
`QOU/Archimedean/EmCouplingBringZeroMode.lean` (which at line 241 already quotes
`:= Cl_2 θ` as the intended body).

Do NOT edit .lean in the audit session that filed this — it was read-only.

Source: `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §B1, §F5.
