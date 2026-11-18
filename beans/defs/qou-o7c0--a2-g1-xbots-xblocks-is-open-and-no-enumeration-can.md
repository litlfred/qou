---
# qou-o7c0
title: 'A2: G1 (Xbot(s) <= Xblock(s)) is OPEN — and no enumeration can ever settle it'
status: in-progress
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-10-10T07:03:49Z
updated_at: 2026-11-18T07:54:48Z
parent: qou-3e6w
---

Parent epic `qou-3e6w`.  Split out of `qou-hok7` on 2026-10-10 so the arc's one *unresolved
inequality* is a bean rather than a paragraph inside a 1,967-line ledger.

## The claim

`Xbot(s) ≤ Xblock(s)` for every `s`.  It is what licenses the `e_∞` join (#7335) to substitute
`Xbot := Xblock`.

## Status: OPEN — neither proved nor refuted

## 🛑 No enumeration can ever settle it

Every table in the arc is a maximum over a **capped** class, hence a **lower** bound on its own
supremum — and a lower bound can only **refute** an inequality, never prove it.  This is the single
most important fact about G1 and it is why the arc's strategy (task A1) is to **remove G1 from the
argument** rather than prove it.

## 🛑 Its only recorded supporting evidence was an ARTIFACT

An earlier entry read *"measured EQUAL for `s ≤ 12`; top higher by `0.01982` at `s = 13`"* and
treated the second clause as a data point in G1's favour.  **It is not one.**  `Xbot` is tabulated
by enumerating bottom profiles with a cap of `BMAX = 9` **rows**.  The bottom maximisers are **flat
and long** (≈ one row per unit of `s`) where the top's are **steep and short** — at `s = 8` the top
winner is `[3,2,1,1,1]` (5 rows) and the bottom winner `[1,1,1,1,2,1,1]` (7 rows), *worth exactly
the same to all 40 digits*.  So the bottom class exhausts its row budget first, and from there
`Xbot` understates its own supremum.  Vary the cap and the break point moves with it; at **every**
setting the winner at the break uses exactly `BMAX` rows.

Past `s = 16` the bottom winner is cap-saturated, so **`s ≥ 17` is undetermined**, not settled in
the top's favour.  `s ≤ 16` covers the certified join window's argmax `s_b = 8` comfortably; it
does **not** cover the full window `s_b ≤ 27`.

## 🛑 And the one-sided sweep nearly produced a FALSE refutation

At `BMAX = 12` the **bottom overtakes the top** — which is also not a refutation, for the mirror
reason.  The comparison G1 actually asks for is **symmetric** (equal caps on both classes), and
even an equal cap is not a *fair* cap, because the two classes spend rows at different rates.
Probe checks `G1f` (the symmetric comparison) and `G1g` (the row-count asymmetry) exist for this;
the witness field is deliberately named `agreement_widest_cap_ONE_SIDED` with a `_note` saying it
is **not** a G1 verdict, so the next agent cannot read the one-sided number as one.

## Structural context worth keeping

`staircase_beta(k, L)` is **two different environments glued at a wall**, and the bottom block
straddles the junction:

    rows i ≤ k :  b0 = k + L − 1 − 2i      an AP of GAP 2   (the top edge's world)
    rows i > k :  b0 = L − 1 − i           consecutive, GAP 1   (the bottom wall)

So the two edges are **not the same problem in different coordinates**, and their agreement at
small `s` is not a symmetry of the frame.  Read from the bottom with `j = 0` the last row:
`b0(j) = j` for `j < pe`, `2j − pe` for `j ≥ pe`; `lin_w(pe, j) = pe − j` for `j < pe` else 0.

The bottom edge also carries two terms the top edge simply does not have: a one-body
`fi(β) − fi(b0)` (identically **zero** for `ap_value`, since `β ~ 2k` saturates `F`) worth up to
`eps(1) = 1.6695` per unit of displacement at the wall, and a linear cost
`lin = Σ_{i>k}(i−k)u_i` worth `ln(q₀)·lin`, reaching `1.0434` over the enumerated class.  Against
an `Xbot` of ~2.16 neither is perturbative.

## What would actually settle it

An **upper** bound on `Xbot` compared against a **lower** bound on `Xblock` — i.e. task A1's
machinery, pointed at the inequality instead of at the window.  Which is why this bean is
**low priority**: A1 makes the arc not need it.

**Do not close this bean, and do not record a capped table as a G1 verdict.**

## Round 84 Progress (PR #8393)
- Branch: `feat/round84-colourdisc-fixedratio-comptrace-zeroslope-equidcap-43c1`
- Commit 1 (code + probe): `02a557115ca6d2779725ccfdca969ee6ef80dff4`
- Commit 2 (witness): `f21ac2e565e6a27158e92746366f1616c0d9fd98` (`scriptSha256 = 930736b7600cb1fb1ca87062021ff390088ea82549e2ac7bf6e2fad10cdf9749`)
