---
# qou-1n7g
title: 'DEFECT: JetOrderIndependence full_rank was discharged by fabricated constant jetPivots = fun _ => (1/4,2,1/8) across ALL orders; the constant extension IS the open conjecture (instance removed PR #4884)'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T22:14:20Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-5p7n
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

## 2026-09-14 — THIRD verification: the two prior entries hold, and this one COMPILED the file

Both entries above read the source; neither built it. On main `2b8206e504` — **69
commits after** the 2026-09-08 entry — the file is byte-unchanged (last non-merge
touch `638f298ffb`, 2026-09-05) and every structural claim re-checks:

- **One `instance`**, `trivialError_bound` at L180. The L405 hit is the word
  "instance" inside a docstring.
- **`jetPivots` at L305 is a plain `def`**, consumed at L312-313 by
  `jetOrder3_certificate` alone. L410/L413 are docstring prose.
- **Zero real `sorry`, zero `axiom`.** The three `sorry` grep hits are the string
  "sorry-free" in docstrings at L250, L259, L414 — the `qou-0a0z` false-positive
  shape, unchanged.

### What this entry adds that the other two did not

**1. The instance search was CORPUS-WIDE, not file-scoped.** Both prior entries
say "the only instance left **in the file**", which leaves open the one thing
that would resurrect the defect: an instance supplied from somewhere else.

```
grep -rn "instance.*JetOrderIndependence\|: JetOrderIndependence" --include=*.lean .   -> 0 hits
grep -rn "ofPivots"                                              --include=*.lean .   -> 5 hits
```

All five `ofPivots` hits are in this file, and **four of them are docstring
prose**; the fifth is the definition at L282. So there is **no consumer of
`ofPivots` anywhere in the corpus** — nothing feeds it the constant, and no
`.lean` in the tree (content-block siblings included, the grep walks them)
declares a `JetOrderIndependence` instance at all. The conjecture is carried by a
content-bearing class with no instance, which is exactly the §3b-tax honest state.

**2. It compiles.** `lean -DautoImplicit=false -s 65536` on the file, **exit 0**,
2m49s wall, no diagnostics. Flags per AGENTS.md: a bare `lean` is a weaker check
than `lake build` because it does not read the lakefile's `autoImplicit := false`.

The snapshot caveat AGENTS.md attaches to lean-direct does **not** bite here, and
that was checked rather than assumed. The file's only non-Mathlib import is
`QOU.Archimedean.HyperbolicVolumeIndependence`, whose olean is stamped
2026-09-07 19:46 against a source last changed 2026-09-05 16:29 — the olean
**post-dates its own source**, so the `descartesWtrace` failure mode (compiles
green against a stale snapshot, red against the source it names) cannot apply.

**3. `qou-xc8t` exists and is dormant.** Still `status: todo`, but
`updated_at: 2026-08-09T22:04:32Z` — **five weeks with no entry**. The 2026-09-08
entry is right that the carrier exists; worth adding that nothing has moved on it,
so "tracked separately" currently means tracked, not worked.

### What is still open, and what I did NOT establish

The residue is untouched and is real. `jacobianRank_eq_three_of_base` is an
**abstract** principle over `{r : ℕ → ℕ}` — one line, `le_antisymm (hle N)
(hbase ▸ hmono hN)` — and says nothing about the concrete order-`N` Jacobian. The
file flags this itself at L328-331: discharging `Monotone` / `≤ 3` / base `= 3`
for the concrete Jacobian "is the remaining structural input, **not a lemma proved
in this file**". `jetJacobianBase_rank = 3` is genuine and witnessed
(`det = 1/16`, `Matrix.rank_of_isUnit`); the step to all orders is not there.

Exit 0 is a claim about *this* file against *this* olean cone. It is not a claim
about the rest of the QOU library, and I did not run a sweep.

### Status untouched — and I am not repeating the recommendation as though it were new

The 2026-09-08 entry already recommends closing and letting `qou-xc8t` carry the
residue, and already defers to the owner. I agree with it and add nothing to the
argument, so restating it would just be a second vote dressed as new evidence.
What changed is the evidence under it: the defect is now verified *absent from the
whole corpus* rather than from one file, and the file is verified *to compile*
rather than to read correctly. The no-op remains safe — nothing breaks if this
stays `todo`.

## 2026-09-14 (same session, later) — the constant is not the only stale thing in that file

Working `qou-xc8t` straight after the verification above turned up something the
three verification entries all missed, because all three checked the *shape* of
the discharge and none re-ran the producer.

**`jetJacobianBase` and `jetPivots` do not reproduce.** The Lean's literals and
the committed witness (2026-06-08) agree with each other and disagree with
`jet_order_pivots.py` as it stands today:

| | Lean + witness | live producer |
|---|---|---|
| elimination det | `1/16` | **`−11/4`** |
| LU pivots | `(1/4, 2, 1/8)` | **`(1/4, 1, −11)`** |

Two of three rows moved (`Borromean` is unchanged, and the `h^0` column is
unchanged for all three). Producer drift, not import-cone drift — the producer's
own `scriptHash` is `1eadd3f17d76` against the witness's `380671554d5b`. The
braid words are unchanged and still match the Lean docstring.

**This does not reopen the defect and does not weaken the verification above.**
There is still no `JetOrderIndependence` instance anywhere, `ofPivots` still has
no consumer, and the file still compiles `exit 0` — `−11/4 ≠ 0` the same as
`1/16 ≠ 0`, so every theorem in it remains true. What is no longer true is the
docstring's claim that these literals are *"witnessed from the framework's own
canonical Markov traces"*: they were, three months ago.

Recorded here only so a reader of this bean does not take "verified three times"
to mean the file's numbers were checked — they were not, until now. Full
measurement, the options and the recommendation are in **`qou-xc8t`**, which owns
the discharge routes; nothing is proposed here.

## Round 88 Formalization (`litlfred/qou#8471`)
- Formalized in `QOU.Foundations.BraidPlaceholderResweepArchimedeanMarkerPartitionConditionalEdgeCollisionBaseOrderPivotExtensionInstanceProjectionAudit` (`folio/quantum-observable-universe/lean/QOU/Foundations/BraidPlaceholderResweepArchimedeanMarkerPartitionConditionalEdgeCollisionBaseOrderPivotExtensionInstanceProjectionAudit.lean`).
- 80-dps `mpmath` probe & 2-commit witness (`e47fb91c9186e83c35ba5f8afe823fc02682f7fa` -> `eb5a105f27408ec654ee82cac266aca18e9361f3`, `scriptHash = scriptSha256 = 76b0a54b7612529d0460197f1a503d128d9ca3acb85f7c16e201490dd4b263d6`).
- PR: https://github.com/litlfred/qou/pull/8471

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- Measured: PR #8471 / #8474 / #8481 (2026-11-18, `QOU/Foundations/*` new files) do **not** resolve this bean. Each adds a standalone Lean file whose structures hold the bean's own audit counts as `Int` fields, with a `canonical…` def filling in the counts and theorems such as `x*x = 0 ↔ x = 0`. No corpus file named by this bean is touched, so the defect it tracks is unchanged by those PRs. Read from the PR patches; not merged.
- Superseded-premise check (owner 2026-11-21, against docs/coordination/owner-rulings.md on main 2ae54ab40; list: L± photon, virtual photons, pre-Nov-15 γγ letters, T(2,n_s), convention C, single-term trace, trefoil-primary electron, 'c_2 = −1 PROVED', χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean's premises or in the files it names.
