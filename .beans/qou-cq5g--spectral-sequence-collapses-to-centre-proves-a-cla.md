---
# qou-cq5g
title: spectral_sequence_collapses_to_centre proves a class-field projection, not the collapse
status: todo
type: task
priority: normal
created_at: 2026-08-25T21:16:54Z
updated_at: 2026-08-25T21:17:48Z
---

`QOU.WedderburnMass.spectral_sequence_collapses_to_centre`
(`content/quantum-observable-universe/mass-theory/spectral-sequence-collapse.lean`)
has conclusion

    forall i : I.central_idempotents, I.e i * I.e i = I.e i

and body `fun i => I.e_idem i`. It re-exports a class field. It does not mention
E_infinity, does not mention a filtration, and **never uses its own
`[WhiteheadHH R A]` instance** — the hypothesis the whole result is supposed to
turn on. The docstring immediately above states the E_infinity result, so the
gap is docstring-vs-type, the §3b-cond item-5 self-assuming shape.

The block's `.ts` carries `validation: "not_checked"`.

**It is not in `docs/audits/lean-vacuity-review-ledger.json`** — grepped
2026-08-25, no entry — so no agent verdict has ever been recorded against it.
That is the actionable part: it is a library-adjacent declaration whose shape is
exactly what the ledger exists to catch, and it has never been seeded.

**Honest dispositions** (per the AGENTS.md rubric), in preference order:

1. Rename to what it proves (`centralIdempotent_idem` or similar) and let the
   collapse be stated separately — cheapest, and removes the mis-citation
   without asserting anything new.
2. State the real proposition with `sorry` + `-- Ref:` and mark `has_sorry`.
3. Demote the collapse to a `conjecture` carrier alongside `WhiteheadHH`.

**Do not "fix" it by proving the collapse.** Mathlib has no Hochschild-cohomology
framework (the file says so), and — separately and more fundamentally — the
filtration whose collapse is asserted is not defined: all three corpus readings
of `J^bullet` are excluded (`2026-08-16-three-gb-filtrations-one-name.md`). There
is no spectral sequence here yet to collapse.

Analysis: `docs/audits/2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md` §2.
