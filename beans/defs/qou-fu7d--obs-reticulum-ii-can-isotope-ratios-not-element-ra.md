---
# qou-fu7d
title: 'OBS: Reticulum II — can isotope ratios (not element ratios) be resolved in r-II dwarf stars? the elemental/isotopic discriminator is the whole test'
status: todo
pr: 8203
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-obs
created_at: 2026-09-07T13:44:35Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

---

## 2026-09-13 — sibling note: the alpha route is dead, THIS one is not

`qou-ultb` (actinide cosmochronometry) is now measured: a bound on
`|d(alpha)/alpha|` converts to a bound on `|dq/q|` by dividing by
`S = |d ln alpha / d ln q| = 6.86193302278`, and at its asserted 2.08e-3 that
is **2.5e5x LOOSER than sigma(q0)** — so the alpha-variation programme cannot
constrain q0 at any achievable precision, formation site or not.

**That negative does NOT carry over to this bean, and should not be quoted as
if it did.** This bean proposes constraining the framework through a DIFFERENT
quantity — nuclear masses and beta-rates far from stability / isotope-vs-
element discrimination — which has its own sensitivity to the substrate and is
untouched by the alpha calculation. Scope (a) on `qou-ultb`'s route only.

Still a title with an empty body; the task needs scoping before it can be
worked.

## Progress (2026-11-16, PR #8203)
- [x] Formalized `elementalObservable`, `hyperfineObservable`, and `elemental_degenerate_but_hyperfine_separates` in `folio/quantum-observable-universe/lean/QOU/Eightfold/RootOfUnityCutoffIsotopeHyperfineBetaCoulombAndSymplecticRoots.lean` + 50-dps mpmath witness (`qou_fu7d_elemental_vs_hyperfine_isotopic_separation`) in PR #8203 (`74a091a53fd300f6f906db42c72c6a5e3e84e7b3`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8203, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
