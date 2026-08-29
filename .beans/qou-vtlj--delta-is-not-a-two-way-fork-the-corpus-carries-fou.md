---
# qou-vtlj
title: 'Delta is not a two-way fork: the corpus carries FOUR net values, and the "13 crossings" sentence contradicts its own block'
status: in-progress
type: task
priority: normal
created_at: 2026-08-29T02:49:11Z
updated_at: 2026-08-29T03:25:06Z
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


## 2026-08-29 (cont.) — WHY hecke_core is 0.34 off: its word has no Hopf link

Chasing the largest gap collapsed it. `hecke_core`'s crossing multisets:

    proton  {(s0,0):6, (s0,-h/2):1, (s1,-h):3, (s1,-h/2):1}
    neutron {(s0,0):5, (s0,-h/2):2, (s1,-h):4}

A Hopf link is `L_- = sigma_1 sigma_0` (or `L_+ = sigma_0 sigma_1`); either
way it requires a **sigma_1 crossing at shift d = 0**. **NEITHER nucleon word
contains one** — proton 0, neutron 0.

So the words `Delta_L` is built from **lack the gluon** the blocks call
*"strictly required by the LP dual"* and *"the minimum additional structure
capable of restoring stability"*. The 0.34 discrepancy is not ordering and not
convention: it is a **missing factor**.

(A first hypothesis — that `hecke_core`'s grouped `_G0`-then-`_G1` storage
loses the interleaving of `B_3 = (s0(s1-h))^3`, and that `net` being
order-sensitive explained the gap — was **refuted**: the multisets themselves
differ, so it is not merely a re-ordering. Recorded because the refutation is
what led to the right answer.)

Corroborating the decomposition: `B_3` contributes exactly `3x(s0,0) +
3x(s1,-h)`, and `hecke_core`'s proton contains exactly `3x(s1,-h)`. So `B_3`
IS in there; what is absent is the gluon.

## Consequence for the adjudication

Of the four values, **the constructed one is the only one with a derivation
behind it**: the blocks' own recipe contains the Hopf link and reproduces the
stated neutron net exactly at 11 crossings, while `hecke_core`'s word does not
contain it and misses by 0.32.

Still **scope-(a)** — this is stated as a finding, not an adjudication.
Nothing is wired, `hecke_core` is untouched. But `qou-bg3w` is now a much
smaller question than it was: not "which of four" but "is the missing Hopf
link in `hecke_core` a defect, or is the block's Hopf-link requirement wrong?"


## 2026-08-29 (cont. 2) — the missing Hopf link is NOT a one-crossing slip [REFUTED]

Natural next hypothesis: `hecke_core` has the RIGHT shift multiset but assigns
every pure crossing to `sigma_0`, while the Hopf link needs one on `sigma_1`.
Confirmed on the multiset side —

    hecke_core proton, minus B_3's 3x(s0,0)+3x(s1,-h):  3 pure + 2 half
    blocks' proton,    minus B_3:  quark{1 pure, 2 half} + Hopf{2 pure} = 3 pure + 2 half

same shift multiset, differing only in generator assignment. So: does moving
ONE pure `sigma_0` crossing onto `sigma_1` — the minimal repair that gives the
word a Hopf link — reproduce the stated nets?

**No, at any position.**

    proton   target 1.0065   closest of 6 edits = 1.007188697   |err| 6.9e-4
    neutron  target 0.7976   closest of 5 edits = 0.799581945   |err| 2.0e-3

So `hecke_core`'s word is **not one crossing away** from the blocks'
construction; the divergence is structural, not a mis-assigned generator.
A tempting route, closed. Recorded as a negative because the next reader will
reach for exactly this.

## Standing summary of the Delta push

**Derivable:** the CONSTRUCTED Delta, from the blocks' own recipe
(`B_3 = (s0(s1-h))^3`, typed quark shifts, one Hopf `L_-`), 11 crossings.
Reproduces the stated neutron net **exactly**; net = −0.2137638.

**Not derivable from the corpus:** `Delta_L`. Its word lacks the Hopf link the
blocks call strictly required, and is not one edit away from having it.

**Still open, and now the whole question:** the proton. No generator
assignment reproduces the stated 1.0065 (closest 1.0067901, err 2.9e-4),
while the neutron's 0.7976 is reproduced exactly by two of eight. That
asymmetry — neutron exact, proton never — is the sharpest remaining lead.
