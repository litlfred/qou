---
# qou-qhrw
title: 'T4: root-of-unity truncation as the freeze-out mechanism'
status: in-progress
pr: 8203
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-tseries
    - 8f-open
created_at: 2026-08-03T23:27:16Z
updated_at: 2026-10-10T12:01:52Z
parent: qou-8lxd
---

phi-q-aj-machinery-identification already sorts Phi_q root-of-unity saddle from Li_2^q real saddle of the same object over Z[q^,-1]. Gavrilik's q_n = e^{i.pi/(2n-1)} are roots of unity too -- same regime. Either (i) show truncation follows at the root-of-unity saddle and survives transport to the real saddle, or (ii) show it cannot. Wire nothing until (i) or (ii). Conditional on 2 conjectures -> would be conditional-proved.


## Triage 2026-10-10 — this is the one route to `qou-db6w`'s gap

`qou-db6w` ("GAP: truncation/freeze-out mechanism — no derivation of
suppression of high-action morphisms") is the gap statement; this bean is the
only candidate mechanism for it anywhere in the corpus. Measured: a
`freeze-out|freeze out` grep across `beans/defs/` returns four hits — these
two, the epic index, and one unrelated render bean. `db6w` was title-only
until today and carried no pointer here, so the two sat separately with
nothing recording that one answers the other. Now `db6w` is `blocked-by` this.

**The either/or in the body above is the disposition for both beans**, and it
is asymmetric in a way worth stating: (i) closes `db6w`; (ii) does **not** — it
eliminates one route and leaves the gap open. Record (ii), if it lands, as
scope-(a) ("this construction alone does not supply the suppression"), never as
a structural exclusion of truncation mechanisms generally — there is no proved
invariant forbidding them, which is what AGENTS.md §"Before declaring
refuted" requires for a scope-(b) claim.

Also carried forward from the body: the route is **conditional on two
conjectures**, so a successful (i) lands as conditional-proved. Name the
premises; do not restate them as established.

Tagged `8f-open` — open formalisation research, not the mechanical work the
reorg's title-based tagging implied.

## Progress (2026-11-16, PR #8203)
- [x] Formalized `oddRootCutoffIndex`, `oddRootCutoffIndex_properties`, and `real_positive_square_diff_pos` in `folio/quantum-observable-universe/lean/QOU/Eightfold/RootOfUnityCutoffIsotopeHyperfineBetaCoulombAndSymplecticRoots.lean` + 50-dps mpmath witness (`qou_qhrw_root_of_unity_cutoff_vs_real_positive`) in PR #8203 (`74a091a53fd300f6f906db42c72c6a5e3e84e7b3`).
