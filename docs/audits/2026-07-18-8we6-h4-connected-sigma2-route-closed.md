# 8we6: the connected (σ₂) subtracted-object route is closed — the H₄ baryon family is walled for c₄^even

**Date:** 2026-07-18 · **Branch:** `claude/pr-3660-merge-pipeline-ephmw4` ·
**Bean:** `8we6` (genuine c₄ rungs → Casoratian W₃ sign test), session `qou-8u91` ·
**Probe:** [`qbeta_h4_connected_sigma2_probe.py`](../../computations/qbeta/qbeta_h4_connected_sigma2_probe.py) (+ witness) ·
**Tier:** exact (sympy s-series; no fit) · **Scope:** (a) — the H₄ 4th-strand
baryon family, any constant coupling.

## What this closes

The [2026-07-13 Route-A gate-fail audit](2026-07-13-8we6-h4-route-a-three-framings-gate-fail.md)
killed nine hand-built H₄ objects and named exactly one surviving design
direction: *"a subtracted/connected object built to cancel the u²/u³ dressing
— a construction whose low-order cancellation is derived, not arranged."* The
[crossing-locus probe](2026-07-18-8we6-h4-crossing-locus-no-derivable-4th-strand.md)
(merged #3833) then showed no **constant coupling** of the full 4th-strand
baryon passes the gate. This probe tests the **connected/subtracted** object
directly — and it too is walled.

## The canonical (non-fit) subtraction

Split the symbolic H₄ 4th-strand baryon (couplings α = b–u, β = b–d) by the
**support of its reduced normal-form words** — a canonical projection, no tuned
coefficient:

- **disconnected** = words in σ₀, σ₁ only (H₃-word content; route-B-pruned to be
  H₃-determined);
- **connected** = words that *touch* σ₂ (the genuinely-4-strand content).

`Δ(net)₄ = Δ_disc + Δ_conn` (verified: the split reconstructs the full object).
The connected part is the "subtracted object" the audit asked for — obtained by
subtracting the H₃-word dressing, not by arranging a cancellation.

## Result — the connected part carries the c₂ leak

| object | ord\_{q=1} | ladder |
|---|---|---|
| H₃ `Δ(net)₃` | 1 | baseline |
| **connected σ₂ part** | **1** | **leaks at c₂** — no derivable coupling zeroes both φ₄, φ₆ |
| disconnected part | 2 | more suppressed than H₃ |

- The **connected part sits at the leading order** (ord 1, same as H₃) and its
  screen coefficients are nonzero at every natural coupling: `φ₄ = 9, 31/4, −27,
  1897/64` at `(α,β) = (0,0), (½,½), (1,1), (1,0)` (the `(0,1)` value is the
  `α−β+1=0` pole, guarded per the crossing-locus catch).
- The **disconnected part is *more* suppressed** (ord 2), so subtracting it
  cannot remove a c₂ leak that lives in the connected part.
- **Cross-check:** connected `φ₄(0,0) = 9` equals the full-object `φ₄(0,0) = 9`
  from the merged crossing-locus probe — consistent (the disconnected part is
  order-2 suppressed, so full ≈ connected at c₂ order), confirming this is not a
  projection artifact.

**Verdict (scope-a):** the route-B prune **extends to the connected part**. The
σ₂-supported (maximally connected) object also leaks at c₂, so no
constant-coupling H₄ 4th-strand baryon — full *or* connected — yields a genuine
`c₄^even` rung.

## Bean 8we6 status after this probe

The H₄-Hoefsmit **baryon** route to `c₄^even` is now closed across all three
sub-routes the audits enumerated:

1. Route B (λ⊢4 re-decomposition of the unchanged element) — structurally pruned
   (2026-07-03).
2. Route A (nine hand-built σ₂ objects) — all GATE-FAIL (2026-07-13), on a
   screen since **verified** (#3833).
3. Constant-coupling family (crossing-locus) + connected/subtracted object (this
   probe) — walled.

The only possibility the audits named that remains open is a **q-dependent
(higher-Taylor) coupling** or a **non-baryon** H₄ object — both "new framework
content, owner call, not agent ansatz" (route-B prune §"design choices"). Bean
8we6 item 1 is therefore an **honest framework wall**, not a tooling gap: the
Casoratian W₃ test stays gated on a c₄^even rung that this object family cannot
supply.

**Discipline:** canonical projection (no tuned coefficient) ⇒ not a fit; `auditOnly`;
no `c_k` wired; registry untouched; scope-(a).

## Cross-references
- Route-A nine negatives: [`2026-07-13-8we6-h4-route-a-three-framings-gate-fail.md`](2026-07-13-8we6-h4-route-a-three-framings-gate-fail.md)
- Route-B prune: [`2026-07-03-8we6-h4-route-b-structural-prune.md`](2026-07-03-8we6-h4-route-b-structural-prune.md)
- Constant-coupling wall + screen verification: [`2026-07-18-8we6-h4-crossing-locus-no-derivable-4th-strand.md`](2026-07-18-8we6-h4-crossing-locus-no-derivable-4th-strand.md), [`2026-07-17-8we6-h4-screen-calibration-verified.md`](2026-07-17-8we6-h4-screen-calibration-verified.md)
- Casoratian W₃ endpoint: [`2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md`](2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md)
