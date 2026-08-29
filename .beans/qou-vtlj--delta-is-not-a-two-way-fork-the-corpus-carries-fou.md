---
# qou-vtlj
title: 'Delta is not a two-way fork: the corpus carries FOUR net values, and the "13 crossings" sentence contradicts its own block'
status: in-progress
type: task
priority: normal
created_at: 2026-08-29T02:49:11Z
updated_at: 2026-08-29T02:49:58Z
---

## Measured, `qbeta_delta_net_four_values_probe.py`, 6/6

Pushing on "derive Delta" produced a negative that is sharper than the
question. Delta is **not** underdetermined by a two-way fork; the corpus
carries **four** values for the same quantity, and no two agree.

| source | net(p) | net(n) | Delta net |
|---|---|---|---|
| `deuteron-binding-dressing-proton-net` (short model) | 0.89547 | — | **−0.1872072** |
| `categorical-*-properties` blocks, as STATED | 1.0065 | 0.7976 | **−0.2089** |
| those blocks' own recipe, as CONSTRUCTED (k=1) | 1.01133 | **0.7975664 ✓** | −0.2137638 |
| `hecke_core` words (= `Delta_L`) | **1.34644** | **1.11324** | **−0.2331977** |

Spread 0.04599 — **24.6 %** of the value the published ladder consumes
(`epsNPq = h²/2 − h`). `net(p)` alone takes **three** values.

`hecke_core` misses the content blocks by 0.34 and 0.32 — not rounding.

## Finding A — the "13 crossings" sentence is the error, not the code

`categorical-neutron-properties.md:11` says the LP dual "selects L₊ → L₋
(two Hopf links, 4 gluon crossings)… This yields a total of 13 crossings".
Built from the block's own recipe — `B₃ = (σ₀(σ₁−h))³`, typed quark shifts
(uu→0, ud→−h/2, dd→−h), Hopf `L₋ = σ₁σ₀` — the k-ladder is:

    k=0  ( 9 crossings)  0.788010
    k=1  (11 crossings)  0.7975664   <-- the block's stated +0.7976
    k=2  (13 crossings)  1.235859     <-- appears NOWHERE in the corpus
    k=3  (15 crossings)  1.466228

**The stated 0.7976 is the ELEVEN-crossing value.** So the count is 11, the
sentence is wrong, `hecke_core` is right on the count, and
`q-beta-gamma-gamma-canonical-derivation.md:33`'s "11 typed crossings each"
is correct.

**This CORRECTS `qou-im4m`**, which established the prose/code mismatch and
framed it as the corpus deriving 13 against a code implementing 11. The
block's own number settles which side is wrong — and it is the prose.

## Anti-fit discipline

The quark-crossing generator assignment is not given by the corpus, so all
**eight** are reported, not the best one. **2 of 8** reproduce the stated
neutron net, so the match is a property of the construction rather than a
selected fit. Note also that **no** assignment reproduces both stated values
at once — the closest on the proton, (1,1,0) at 1.006790, gives 0.802107 on
the neutron.

Also measured: `net(B₃) = 0.9996006`, where the block states **+1.0000** at
four quoted decimals.

## Not adjudicated

No net is declared right. `hecke_core` untouched, no content block edited, no
`c_k` proposed. The finding is that **the Delta question cannot be closed by
choosing between two candidates**, which is how it has been framed
(`qou-bg3w`). Whoever adjudicates now has four numbers to choose among and a
constructive recipe that reproduces one of them exactly.
