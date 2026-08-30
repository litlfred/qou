---
# qou-0y6h
title: 'B3: invariant Gram bilinear form on cell modules; Schur element = hook/content product (reuse WenzlSchurElement.schurElement); det(Gram)=∏ Schur (Geck-Pfeiffer)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-24T16:21:38Z
updated_at: 2026-08-30T07:56:22Z
---

## 2026-08-29 — this is closer than the standing plan implies (from qou-0ubf)

The Schur-element NON-VANISHING half is **already proved for all n**:
`WenzlSchurElement.schurElement_ne_zero` (line 231) is sorry-free, hypotheses
`1 < Q` and `X <= 0` only, no class hypothesis. And `semisimple_of_substrate`
already composes it into all-rank semisimplicity — but conditionally, on
`[SchurElementCriterion Q X ss]`, which has NO INSTANCE (verified by grep over
content/**/lean/QOU on main @ df81b22be4).

So this bean's remaining content is **exactly** Geck-Pfeiffer Thm 7.2.6 — 'every
Schur element nonzero => semisimple'. Formalising it turns `semisimple_of_substrate`
from class-conditional into an outright theorem at every rank, which discharges the
`WenzlCriterion` hypothesis of PNeqNpEquivalence for real.

Note the 2026-07-25 status audit §5 item 1 sends you to build the T_w/Matsumoto
basis + the symmetrizing-trace Gram determinant instead. That route is still the
honest Mathlib gap for the DETERMINANT approach and is worth doing on its own
merits, but it is NOT on the critical path to all-n semisimplicity. Corrected in
place in that audit; full re-measurement in
docs/audits/2026-08-29-pneqnp-gap-inventory-refresh.md.

Crosses no barrier — semisimplicity is a magnitude-axis fact. It removes one of the
two remaining cited classes from the conditional chain.

## 2026-08-29 (later) — CORRECTION: this is DOWNSTREAM of the T_w basis, not an alternative to it

My own note above, and the audit §3 ranking it came from, presented this bean and
the T_w/Matsumoto basis as **alternatives** — `0y6h` ranked #1 'chippable', the
T_w basis ranked #5 'no longer P!=NP critical path'. **That is wrong.**

Measured: `WenzlSchurElement.schurElement` is **purely combinatorial** — a
hook/content product over ℝ. A grep of the whole file for
`IwahoriHecke|HeckeAlgebra|Algebra|Module|Basis` returns **nothing**. No algebra
is attached to it anywhere.

So `SchurElementCriterion` silently bundles TWO obligations:
  (i) the combinatorial formula *equals* the algebra-theoretic Schur element, and
  (ii) Geck-Pfeiffer 7.2.6 proper (all Schur ≠ 0 => semisimple).
Both need the algebra side: a **basis** of H_n(q) to state det(Gram) against, plus
the symmetrizing-trace/Wedderburn theory. For H_n(q) that basis is T_w.

The downstream half of the chain already exists and is fine —
`RegTraceGram.isSemisimpleRing_of_regTraceGram_det_ne_zero` and the
`TraceFormSemisimple` keystone give det(Gram) ≠ 0 => semisimple. What is missing
is precisely 'Schur ≠ 0 => det(Gram) ≠ 0', i.e. det(Gram) = ∏ Schur, and that
cannot even be *stated* without the basis.

**What remains true:** `semisimple_of_substrate` does give all-n semisimplicity
without the T_w basis — but only CONDITIONALLY, on the unproved criterion. The
distinction I blurred is between an all-n *conditional* statement (no T_w needed,
true) and an all-n *discharge* (T_w needed, which is this bean).

**Verdict: not chippable in isolation. Genuine Mathlib-scale, gated on T_w
(qou-lrz1 / qou-twwf).** Do those first or accept the conditional.
