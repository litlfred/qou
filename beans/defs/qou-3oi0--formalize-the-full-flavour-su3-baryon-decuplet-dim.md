---
# qou-3oi0
title: Formalize the FULL flavour-SU(3) baryon decuplet (dim Sym^3 = 10, needs N = 3) -- blocked by qou-j3w6 (split from nmib)
status: in-progress
type: task
priority: normal
tags:
    - 8f-flavour
    - reorg-2026-10-04
    - split-from-nmib
created_at: 2026-10-10T08:27:45Z
updated_at: 2026-10-10T08:28:05Z
parent: qou-8lxd
blocked_by:
    - qou-j3w6
pr: 8229
---

Split out of `qou-nmib` on 2026-10-10. **Blocked by `qou-j3w6`, and the block is
proved rather than assumed.**

`qou-nmib` bundled the `Δ` isospin quartet with the full flavour-`SU(3)`
decuplet. They have different dimensional requirements, so they are different
beans:

| `N` | `dim Sym³(k^N) = C(N+2,3)` | multiplet |
|---:|---:|---|
| 2 | **4** | the `Δ(1232)` quartet `Δ⁺⁺, Δ⁺, Δ⁰, Δ⁻` — **ungated**, tracked at `qou-nmib` |
| 3 | **10** | the full decuplet, adding `Σ*, Ξ*, Ω⁻` — **this bean** |

`Ω⁻` is `sss`: strange, so it cannot exist at `N = 2` on any route. Hence this
half needs flavour `SU(3)` with `N = 3`, which is exactly the arc's gate.

## The gate, and why it is a proof and not a preference

`qou-j3w6` — owner decision, asked 2026-09-03, dismissed, still open. Every
single-fibre route to flavour `SU(3)` is closed by a proved invariant: the
missing object needs `Λ³W = 1`, which condition 5 (`Λ²V = 1`, `N = 2`) forbids
for `V`. Options A (keep `N = 2`, add a second fundamental `W` — recommended
there) / B (weaken to epimorphism — breaks the convention-D forcing chain, 10
consumers) / C (top-power `Λ^N V`, forces the multi-universe picture) / D
(nothing). Frame: `docs/audits/2026-09-03-eightfold-axiom-5-decision-frame.md`.

`folio/quantum-observable-universe/lean/QOU/Eightfold/RowCapObstruction.lean`
proves **sorry-free** that at `N = 2` the alternating channel
`dim V_(1³) = C(N,3)` **vanishes** — no singlet, hence no `8 ⊕ 1` and no `η′`,
for **any** `q`. Scope-(b), invariant cited (the Schur-Weyl row cap). It excludes
`N = 2` from *hosting* the decomposition; it says nothing against a route that
*produces* `N = 3`.

## Content state

`prop:borromean-decuplet`
(`folio/quantum-observable-universe/eightfold-way/borromean-decuplet-derivation.md`)
already tabulates `Δ⁺⁺(uuu)`, `Δ⁺(uud)`, `Δ⁰(udd)`, `Δ⁻(ddd)` and `Ω⁻(sss)` with
`I₃` and strangeness. Its `lean.ref` is
`qou:QOU.Eightfold.RowCapObstruction.eightfold_channels_at_three` — i.e. it
points at the **obstruction**, which is the honest current state: the block
describes a decomposition the substrate is proved not to host at `N = 2`.
Measured: no `Delta baryon` / `DeltaBaryon` / `delta_baryon` declaration exists
anywhere in the Lean tree.

## What NOT to do

**Do not start this before `qou-j3w6` is answered**, and do not route around it
by assuming `N = 3`. Formalising a `Sym³` at `N = 3` without a derivation that
produces `N = 3` would construct the representation of a fundamental the
substrate is not shown to have — the axiomatisation-is-not-a-proof failure, with
a proved obstruction sitting one file away.

**Default if unanswered: option D of `qou-j3w6` — nothing changes and this stays
parked.** That is the safe no-op.

**Blast radius when it unblocks:** `prop:borromean-decuplet`,
`QOU/Eightfold/RowCapObstruction.lean`, and whatever `8f-flavour` lands.

## Implementation Note (PR #8229)
- Implemented in `folio/quantum-observable-universe/lean/QOU/Eightfold/SkeinResolutionQuarkWritheBalanceWorpitzkyDecupletOrderedContentAndGenerationFilters.lean` and `computations/probes/skein_resolution_quark_writhe_balance_worpitzky_decuplet_ordered_content_and_generation_filters_probe.py` (witness `computations/probes/skein-resolution-quark-writhe-balance-worpitzky-decuplet-ordered-content-and-generation-filters.witness.json`, `f1cdc284e299c69db7b5cdefc55f5ba3d747a9ab`).
