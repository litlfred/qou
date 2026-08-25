---
# qou-xi16
title: 'GAP: KS primitive wall-crossing <-> quantum pentagon link is unformalized (WallCrossing placeholder axiom)'
status: todo
type: task
priority: normal
created_at: 2026-08-21T21:02:22Z
updated_at: 2026-08-21T21:02:58Z
---

Found draining the small-category vacuity tranche (qou-h3ly), PR #5408.

**Two linked placeholders in QOU/Mathlib/WallCrossing.lean:**

1. `KontsevichSoibelman.primitive_wall_crossing` — the KS axiom field is
   `∀ (_W : Wall L) (_Zp _Zm : CentralCharge L), True`, with the real
   content ('multiplicities differ by ±⟨γ₁,γ₂⟩·Ω(γ₁)·Ω(γ₂)') living only in
   a comment. So the class does not constrain any instance.
2. `primitive_KS_is_pentagon : True := trivial` — REMOVED in #5408. It
   claimed to link the rank-2 KS formula to the quantum pentagon identity
   `E(e₁)E(e₂) = E(e₂)E(e₁+e₂)E(e₁)`, said to be the content of
   `QOU.BraidKnot.QRogersPentagonArchimedean`. WallCrossing.lean does not
   import that module and nothing consumed the declaration.

**Why it could not be restated in place:** the pentagon identity needs the
quantum torus algebra and the `E(·)` dilogarithm operator (absent here);
the obligation on the other side of the link is itself a placeholder; and
the file is `sorry`-free, so the state-and-queue route would have added
the first `sorry` to a clean file (Strict Lean Discipline §2).

**Real work required:** give `primitive_wall_crossing` a genuine Prop field
(the multiplicity-jump formula over a quantum torus), then either import
`QRogersPentagonArchimedean` and derive the rank-2 reduction, or state it
as a §3b conditional. Do not restore a `True`-valued link.
