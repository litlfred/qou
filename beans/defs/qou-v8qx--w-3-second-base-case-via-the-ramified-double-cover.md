---
# qou-v8qx
title: w_3 second base case via the ramified double cover (adjoin q^1/2, x^1/2) — the one route nothing excludes
status: todo
pr: 8199
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T07:00:39Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-frzo
---

## Why this is the one live route (bean qou-1xne, PR #5967)

w_3 is a REQUIRED BOUNDARY CONDITION, not a computable output. The proof is on
main and is scope-(b) with its invariant cited:
QOU.Mass.BindingScalarKernelParityExclusion.no_scalar_kernel_on_carrier
(sorry-free). The q-Borel-normalized carrier K of
conj:qdifference-kernel-prolongation-symbol is pure isoclinic of Newton slope
1/2 at infinity; every rank-1 q-difference module has INTEGER slope; so no
scalar R(q,x) in K(x) acts on K at any depth. Equivalently, in the file's own
arithmetic form, the cleared q-Riccati's top degrees are 1+2p (odd-shaped) and
2u (even), and 2u - 2p = 1 has no solution over Z.

A rank-2 recursion needs TWO base cases. The corpus supplies one (n=2, the
deuteron bond). w_3 IS the second, which is why every attempt to derive it from
the two anchors fails on counting rather than on precision.

## The route, in the exclusion's own words

That file's scope note names the missing structure explicitly:

  "The exclusion is over K(x): after a degree-2 RAMIFIED base change (adjoining
   q^(1/2), x^(1/2)) the slope becomes the integer 1 and a scalar kernel DOES
   exist on the double cover, relating half-shifts -- i.e. even and odd body
   orders separately. That ramification is the missing structure, not a gap in
   the proof."

So the question is whether the double cover supplies the second base case
STRUCTURALLY -- i.e. whether the even-order and odd-order sub-series each obey a
rank-1 relation whose own seed is fixed by something already derived (n=2 seeds
the even branch; what seeds the odd branch?). If the odd branch's seed is
independently determined, w_3 closes. If it is another free constant, this
route reduces to renaming w_3 and should be recorded as such.

## Measured state of the alternatives (all closed, see qou-1xne / R1-R4)

- a_D^(3) itself: DETERMINED, and a different object from w_3.
- SL2 depth-2 tau: circular (consumes a_D^(3)); geometric growth refuted past
  n=5. Spun out as qou-vkm6.
- a third anchor at A>3: none exists under any reading of the tower.
- the magic form as the n=4 term: determines w_3 negative, unbound tritium.

## Discipline

The half-shift structure is q^(1/2) / x^(1/2) -- adjacent to but NOT the same as
the square-root Markov parameter of convention C, which is excised (owner ruling
2026-08-15). Do not let a q^(1/2) reappear as a convention-C z. Anything
extracted from AME at A=3 is a fit regardless of which cover it is computed on.

## Related

qou-d8de (GAP W1: construct the prolongation operator D_q) is the adjacent
parent -- that bean builds the OPERATOR; this one asks whether the ramified
cover supplies the second INITIAL CONDITION. Do not merge them; the negative
results differ.

## Progress (PR #8199)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/RouteCDTChiralityAndQBridgeTaming.lean` (`0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 advisory` across all 7 static vacuity/borrowed-name audits) and wired into `QOU.lean`.
- [x] Verified exact rational witness in `computations/probes/route-c-dt-chirality-and-qbridge-taming.witness.json` (`scriptHash: d89ffef0f347`, `scriptCommitSha: d6aa2e9463a3ba079ec1d472e356f34252ece779`, `allPassed: true`, `0` raw `float64` fields).
- [ ] Awaiting Merge Manager merge of PR #8199 (`1f4bf9af7d58a057599a62f5a8d42748dc742ea8`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8199, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
