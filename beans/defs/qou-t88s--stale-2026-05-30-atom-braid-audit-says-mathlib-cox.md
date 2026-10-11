---
# qou-t88s
title: 'STALE: 2026-05-30 atom-braid audit says Mathlib CoxeterSystem API is in flux — it is 1612 lines across four stable files at the pin'
status: completed
type: task
priority: low
tags:
    - reorg-2026-10-04
    - 8f-lean
created_at: 2026-09-04T09:08:25Z
updated_at: 2026-10-10T07:26:38Z
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


## ENACTED and COMPLETED 2026-10-10

The stale clause is removed from
`docs/audits/2026-05-30-atom-braid-categorical-proof-feasibility.md` (bullet 1 of
"Why a single-session attempt won't close"), replaced by a dated correction note.

**A stronger, locally-checkable fact than the one this bean recorded.** The bean
argued from Mathlib line counts and from `IwahoriHeckeAlgebra.lean` using
`CoxeterSystem` as a positive control. The sharper evidence is one line up:
that file's **line 3 is `import Mathlib.GroupTheory.Coxeter.Basic`** — the corpus
*compiles against* the API, and an API you build against is not in flux. That
settles it without needing any line count.

**What is NOT re-measured here, stated so nobody inherits it as fresh.** The
1612-lines-across-four-files figure against pinned mathlib `f897ebcf72cd` is
carried from this bean's 2026-09-04 measurement. Mathlib source is **absent from
this container** — which `IwahoriHeckeAlgebra.lean` itself notes is normal
("the source is not present in every container"). The import argument does not
depend on the figure, which is why the correction leads with the import.

**The rest of the bullet stays, and the correction says so explicitly**, because
the risk in fixing a stale sub-clause is that a reader takes the whole bullet as
discredited: KLR algebras, Hoefsmit seminormal basis, Kashiwara crystals and
Type-B folding still do not exist in Mathlib, and the load-bearing blocker is
Step 4, not the Coxeter API.
