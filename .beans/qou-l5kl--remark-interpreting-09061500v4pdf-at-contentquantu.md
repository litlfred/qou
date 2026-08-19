---
# qou-l5kl
title: Remark interpreting 0906.1500v4.pdf at content/quantum-observable-universe/lean/QOU/OneLoopEdgeLa…
status: todo
type: task
created_at: 2026-08-08T16:13:01Z
updated_at: 2026-08-08T16:13:01Z
---

Record why the refutation in qou-fl4t is a defect of the |det J| route and not of the torsion itself: the adjoint torsion is a well-defined invariant with an independent CW-level computation, so the negative is scope-(a) (this construction, as computed, is not invariant) and not scope-(b) (the quantity does not exist). Prevents the refutation from over-narrowing the search.

**From the source**
- Theorem 14 + eq. (32), §8, p.23 — Duality with sign: Delta^{phi (x) Ad.rho}_{E_L}(t^{-1}) = (-1)^b * Delta^{phi (x) Ad.rho}_{E_L}(t) for a link exterior with b boundary components (sign term epsilon = (-1)^{b(b-1)/2} computed in Prop. 16).
  Use here: A proved bar-involution (t -> t^{-1}) parity law for the torsion polynomial, with the parity set by the component count b. QOU's bar-even/bar-odd bookkeeping is currently asserted per-object; this is an external, proved instance of exactly that symmetry on an object the corpus already computes, and it is a falsifiable constraint on any candidate torsion polynomial the corpus produces.

Source: `library/arxiv-0906.1500v4/0906.1500v4.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
