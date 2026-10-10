---
# qou-t88s
title: 'STALE: 2026-05-30 atom-braid audit says Mathlib CoxeterSystem API is in flux — it is 1612 lines across four stable files at the pin'
status: todo
type: task
priority: low
tags:
    - reorg-2026-10-04
    - 8f-lean
created_at: 2026-09-04T09:08:25Z
updated_at: 2026-10-10T07:16:19Z
parent: qou-8lxd
---

**STALE CLAIM (2026-05-30).**
`docs/audits/2026-05-30-atom-braid-categorical-proof-feasibility.md:25`:

> "**Mathlib has no relevant high-level infrastructure.** No KLR algebras, no Hoefsmit
> seminormal basis, no Kashiwara crystals on Type-A KLR, no Type-B folding functor.
> **Even Mathlib's `CoxeterSystem` order-accessor API is in flux.**"

**The last clause is stale.** Measured 2026-09-04 against pinned mathlib
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7` (v4.24.0):
`Mathlib/GroupTheory/Coxeter/` is **1612 lines across four files** —
`Basic.lean` 516, `Inversion.lean` 483, `Length.lean` 344, `Matrix.lean` 269
(`grep -c '' Mathlib/GroupTheory/Coxeter/*.lean`) — carrying `CoxeterMatrix`,
`CoxeterSystem`, `simple`, `wordProd`, the universal property `lift`,
`simple_induction`(`_left`/`_right`), `simple_determines_coxeterSystem`, plus length and
inversion theory. Whatever was in flux in May 2026 is not now.

**Independent corroboration from inside the corpus.**
`QOU/MathlibExt/IwahoriHeckeAlgebra.lean:8-11` uses `CoxeterSystem` as a **positive
control** for its own negative measurement — *"`CoxeterSystem` occurs in three modules,
`Hecke` in one, and that one is `Mathlib/NumberTheory/FLT/Basic`"* — which is only a
valid control because the API is stable enough to be a reference point. That file also
records a deliberate design choice to take a bare `B → B → ℕ` rather than a
`CoxeterMatrix B`, on the grounds that the Coxeter axioms buy nothing for its
construction. That is a *scoping* decision, not a statement about instability, and the
two should not be conflated.

**The rest of the bullet re-measures as correct** and should stay: KLR algebras,
Hoefsmit seminormal basis, Kashiwara crystals, Type-B folding — none exist in Mathlib
(`Kazhdan` → 0 files; `Specht` → 0; `RSK` → 0; `hookLength` → 0).

**Fix:** strike the "in flux" clause, or replace it with the measurement and its date.
Dated audit docs are historical records and this corpus deliberately leaves them
standing (`qou-3nva` precedent) — so the right shape is probably an inline dated
correction note rather than a rewrite. Author's call.

Source: `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §F8, §H4.
