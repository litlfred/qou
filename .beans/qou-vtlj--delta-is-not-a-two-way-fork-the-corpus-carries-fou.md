---
# qou-vtlj
title: 'Delta is not a two-way fork: the corpus carries FOUR net values, and the "13 crossings" sentence contradicts its own block'
status: in-progress
type: task
priority: normal
created_at: 2026-08-29T02:49:11Z
updated_at: 2026-08-29T06:50:15Z
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


## 2026-08-29 (cont. 3) — the proton is where Delta breaks, and the stated value is the likely error

The neutron/proton asymmetry, pursued to a conclusion.

**Derived target.** If the exact neutron net (0.797566438888) and the stated
Delta net (−0.2089) are both right, then `net(p)` **must** be
**1.00646643889** — which does round to the stated 1.0065. So the corpus's own
pair is self-consistent, and this is a verification target, not a fit.

**96 variants, no hit.** 8 quark-generator assignments x 2 Hopf orientations
(`L_-`, `L_+`) x 6 compositions (`BQG`/`BGQ`/`QBG`/`GBQ`/`QGB`/`GQB`). Closest
is **1.00679010515**, |err| **3.2e-4** — against a NEUTRON match exact to
~1e-30. The asymmetry is structural, not numerical.

**The required correction is not a corpus quantity.** The proton differs from
the neutron only in the uu crossing's shift, which the block reads as 0.
Solving for the shift that would make `net(p)` match gives **−0.004756809789**.
Against 18 corpus-shaped candidates (`0`, `±h`, `−h/2`, `−h/4`, `−h/8`,
`−h/16`, `−h/32`, `−h²`, `−h²/2`, `−h²/4`, `−h²/8`, `−h³`, `−h³/2`, `−h⁴`,
`q−1`, `−1/q`, `−(q−1)²`, `−(q−1)³`) the nearest is **−h³/2 at 3.96 %
relative error**. Nothing matches.

**Weight of evidence: the stated PROTON net is wrong.** The same block family
already carries one demonstrated error — its "13 crossings" sentence, refuted
by its own neutron number. The proton value is unreachable by 96 readings of
the block's own recipe and is not one recognised correction away from it.

**Which makes the derivable Delta the CONSTRUCTED −0.2137638306**, from the
assignment that reproduces the neutron exactly.

**NOT proved.** An incomplete reading of the recipe remains open — the
composition order and the quark-generator assignment are both my
reconstruction, not corpus statements. What is established is that no reading
I can find reaches the stated value, and the gap is 1000x the neutron's
residual.


## 2026-08-29 (cont. 4) — WHERE THE GLUON WENT (owner question)

Owner asked: *"what happened to the gluon... shouldn't we see it in proton? it's
in the γγ production history, no?"* — and that is the right question, because
the γγ block's central identification **is** the gluon:

- `c_3 = -2 = J_Hopf(q=1)` — *"classical-limit Jones polynomial of the
  **Hopf-link substructure**"*
- `c_4 = b^2 + 1/2` — *"Kashiwara + **half-Hopf** mixed"*
- its own open question: *"formalising the 3-fold Markov closure →
  **Hopf-link substructure** identification"*

So `c_3`, which the whole published ladder rests on, IS the Hopf link.

### Answer: the gluon is a NORMAL-FORM TERM, not an added factor

`categorical-proton.md`: *"$B_3 = (\sigma_0\sigma_1^{-1})^3$ … **$B_3$ natively
carries Hopf link content. This constitutes the intrinsic gluon field**"*.
`categorical-neutron-properties.md`: *"establishing intrinsic Hopf link content
**without an independent $L_H$ factor**"*.

**This corrects my earlier framing.** I looked for the gluon as a *factor in
the word* and reported "hecke_core's words contain no Hopf link". The corpus's
own account is that the Hopf content lives in the `L_±` **coordinates of the
reduced element** — the basis IS `[γ, σ₀, σ₁, L₊, L₋, e⁻]`.

### And the corpus PINS the whole vector — `tbl:categorical-neutron-table-data`

| basis | | corpus | constructed | hecke_core |
|---|---|---|---|---|
| **1** | γ | −0.0096 | +0.0092 | 0.4894 |
| σ₀ | | −0.0481 | −0.0442 | 1.2978 |
| σ₁ | | 0.0461 | **0.0461 ✓** | −0.1845 |
| σ₀σ₁ | **L₊** | −0.2206 | **−0.2206 ✓** | −0.4894 |
| σ₁σ₀ | **L₋** | +0.0189 | 0.0 | **0.0** |
| σ₀σ₁σ₀ | **e⁻** | +1.0109 | **+1.0109 ✓** | **0.0** |

Sums to 0.7976 = the stated net. **This is a six-component target, not one
scalar** — a far stronger constraint than anything used before.

**Construction: 3/6 exact** (240 variants scanned: 8 quark assignments × 5
gluon words incl. `L₊L₋` × 6 compositions). max|err| 0.0189, and the residual
is *structured* — the same 0.0189 displaced between γ and L₋.

**hecke_core: 0/6, max|err| 1.35.** Decisively: its neutron has
**e⁻ = 0.0 EXACTLY** — zero weight in the trefoil channel the block says
*"dominates both nucleons"* at ≈ +1.0 — and **L₋ = 0.0**.

### So, to the owner's question

The gluon **is** in the corpus's proton/neutron — as `L₊`/`L₋` NF terms, both
nonzero, exactly as the definition says. It is **absent from the word
`hecke_core` traces**, along with the entire dominant trefoil channel. That is
why `Delta_L` sits 0.34 from the blocks: not a convention, not an ordering, not
a missing factor I could add — a different object.

Which strengthens the standing conclusion: the derivable Delta is the
constructed one. It now matches 3/6 components of a pinned vector; `hecke_core`
matches none.

**Still open:** the 0.0189 γ↔L₋ displacement and the 0.0039 on σ₀. No variant
of 240 closes them, so one more structural element is unaccounted for.
