---
# qou-1n7g
title: 'DEFECT: JetOrderIndependence full_rank was discharged by fabricated constant jetPivots = fun _ => (1/4,2,1/8) across ALL orders; the constant extension IS the open conjecture (instance removed PR #4884)'
status: todo
type: bug
priority: normal
created_at: 2026-08-09T22:14:20Z
updated_at: 2026-09-08T04:37:28Z
---


## 2026-08-22 — VERIFIED RESOLVED as a defect; residue is open math (no body existed, so recording it)
Checked on main. The fabricated-constant instance is GONE: the only instance left in
QOU/Archimedean/JetOrderIndependence.lean is `trivialError_bound`; there is no
`instance ... JetOrderIndependence` applying `ofPivots` to the constant `jetPivots`.

`jetPivots : N -> Q x Q x Q := fun _ => (1/4, 2, 1/8)` survives at L305 as a plain `def`, which is
correct and not the defect -- it is the witnessed BASE-ORDER pivot data. The defect was using it to
discharge `full_rank` at every order.

The file documents this at L408-416 in its own words: "the instance fabricated its data ... a
constant extension of the order-3 pivots to every order, thereby asserting full_rank at all N >= 3
-- which *is* the open conjecture", and lists what is retained (jetOrder3_certificate, prod pivots =
1/16 != 0, sorry-free; jetJacobianBase_rank = 3; eliminationDet_ne_zero; ofPivots;
jacobianRank_eq_three_of_base) versus what is dropped (only the step from base-order certification
to all orders). That is the honest disposition the anti-laundering rule asks for.

So there is NO code fix outstanding. What remains is the genuine open conjecture -- extending the
certified base-order full_rank to all N >= 3 -- plus the separate open item noted just above it in
the file: supplying the `E` that comes from the categorical connection still needs a Lean definition
of the transport error. Recommend re-scoping this bean from `type: bug` to a research item, or
closing it and tracking the conjecture separately. Not closed here (owner call).


---

## 2026-09-08 — the defect is INDEPENDENTLY re-verified, and the residue's carrier EXISTS. Status left as-is; the decision is now one keystroke.

The 2026-08-22 entry above ends *"Recommend re-scoping this bean from type: bug
to a research item, or closing it and tracking the conjecture separately. Not
closed here (owner call)."* Two things about that, one confirming and one that
changes the option space.

### 1. Re-verified from the Lean, not from the bean above

AGENTS.md is explicit that a sibling's bean is not a primary source, so this was
checked at the file rather than taken on trust —
`QOU/Archimedean/JetOrderIndependence.lean` on `main` `29126ed0ed6`:

- **`instance` declarations in the whole file: exactly ONE**, `trivialError_bound`
  at L180. There is no `instance … JetOrderIndependence` applying `ofPivots` to a
  constant. The fabricated-constant instance is gone.
- **`jetPivots` survives at L305 as a plain `def`** and is consumed at L312-313
  only by `jetOrder3_certificate : eliminationDet (jetPivots 3) ≠ 0`, i.e. at
  **base order**. That is the witnessed data used where it is witnessed, which is
  correct and is not the defect.
- **Zero real `sorry`.** `grep -c sorry` returns 3 and **all three are the string
  "sorry-free" inside docstrings** (L250, L259, L414) — the same false-positive
  shape recorded on bean `qou-0a0z`. Counting the grep would have been wrong.

So the defect is resolved and there is no code fix outstanding. That half of the
2026-08-22 entry stands.

### 2. What has changed: the recommendation's second option is ALREADY satisfied

That entry offered *"close it and tracking the conjecture separately"* as though
the tracking still had to be arranged. **It does not — the carrier already
exists and is open.** Bean **`qou-xc8t`** (`todo`), title:

> *Discharge JetOrderIndependence honestly: feed `ofPivots` per-order pivots from
> `jet_order_pivots.py` at higher truncation, or prove the column-extension
> linkage for `jacobianRank_eq_three_of_base`*

That is precisely the residue this bean names — extending the certified
base-order `full_rank` to all `N ≥ 3`. Two further beans touch the same file
(`qou-j4mn` on jet algebraic dependence, `qou-09mr`), so the area is not
orphaned.

**Consequence:** re-scoping *this* bean to a research item would duplicate
`qou-xc8t`, not preserve anything. The open mathematics does not depend on this
bean staying open, and AGENTS.md rule 13a is satisfied either way — 13a forbids
closing a bean **whose subject is** an open conjecture, and this bean's subject
is the *fabricated-constant defect*, which is verifiably fixed, while the
conjecture's own carrier stays `todo`.

### Not closed here either — and why

A sibling deferred this to the owner in writing, and the 2026-09-07 ask-first
override says default to asking. So the status is untouched. What this entry adds
is the measurement that collapses the choice: **my judgement is to close this bean
and let `qou-xc8t` carry the residue** — it costs nothing, loses no open item, and
removes a `bug` that no longer describes any live defect. The no-op is equally
safe: nothing breaks if it stays `todo`, it simply keeps re-surfacing on the
completion-candidate queue, which is how it reached me.
