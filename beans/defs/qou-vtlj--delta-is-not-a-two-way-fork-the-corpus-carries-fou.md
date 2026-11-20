---
# qou-vtlj
title: 'Delta is not a two-way fork: the corpus carries FOUR net values, and the "13 crossings" sentence contradicts its own block'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T02:49:11Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-10v9
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


## 2026-08-29 (cont. 5) — the blocker is PRECISION, not mathematics

Following the structured residual to its end.

**The residual is real.** corpus − constructed, on the best of 240 variants:

    gamma    -0.018837071     <- 376.7x the table's rounding
    sigma0   -0.0039162
    sigma1   -1.49e-5   ~0
    L_plus   -1.83e-5   ~0
    L_minus  +0.0189
    e_minus  -2.66e-5   ~0

So a term IS missing, and it lives entirely in {γ, σ₀, L₋}.

**Its shape is clean.** Normalised by γ the residual is
`(1, 0.2079, ~0, ~0, -1.0033, ~0)` — i.e. `c·(1 + h·σ₀ − L₋)`, and since
`σ₀² = h σ₀ + 1` that is

    c * (sigma_0^2 - sigma_1 sigma_0)  =  c * (sigma_0 - sigma_1) * sigma_0

with `c = −0.0188371`.

**But the shape cannot be confirmed.** The table is quoted to 4 dp, so each
entry carries ±5e-5. Propagating that:

    sigma0/gamma  = 0.20790 +/- 0.00271   vs  h = 0.20906   ->  0.43 sigma
    L_minus/gamma = -1.00334 +/- 0.00376  vs  -1            ->  0.89 sigma

**Both within the table's own rounding.** The residual is *consistent with*
`c(σ₀−σ₁)σ₀` and **not distinguishable from it**.

**And the disagreement sits exactly where the corpus records least precision.**
γ is quoted to 2 significant figures (0.52 % relative) and L₋ to 3 (0.27 %) —
the two components that disagree. The two the construction matches, e⁻ (6 s.f.,
0.005 %) and L₊ (4 s.f., 0.023 %), are the tightest recorded.

**No higher-precision source exists.** Searched the committed witnesses; none
carries the neutron NF vector. `tbl:categorical-neutron-table-data` at 4 dp is
the only record.

## What would settle Delta

Re-run whatever produced that table and record the neutron NF at 50 dps. Then
either the residual collapses — the construction is right and the table was
merely rounded, giving Delta directly — or it resolves into an identifiable
term and Delta follows from that.

Until then the derivation is blocked on **data precision, not on mathematics**,
which is a materially different and much smaller obstacle than "which of four
values". That producer is not identified yet; finding it is the next concrete
step.


## 2026-08-29 (cont. 6) — MORE PRECISION FOUND, and it EXCLUDES hecke_core at every z

Owner asked how to get more precision. The answer was already in the corpus:
the γγ block's **Step 6** quotes

    Delta tr_M(n-p) = +0.0445860283      <- TEN significant figures

on the same two objects — against the NF table's four decimals. Using it:

**hecke_core is excluded by an exact bound, not a scan.** Its Δtr_M as a
function of the Markov parameter is a quadratic

    A z^2 + B z + C,   A = -0.10681446,  B = -0.021853104,  C = -0.10453015

with **A < 0**, so it has a *maximum*: **−0.103412421104**, at z = −0.1022947.
Its range over ALL real z is `(-inf, -0.1034124211]`. Both **+T and −T lie
above that maximum.**

So **no Markov parameter whatsoever** makes `hecke_core`'s element produce the
γγ number. This is qualitatively stronger than every previous comparison: not
"disagrees under convention D", but **impossible under every convention**.

**The constructed model reaches it**, at z = **0.4983656269** — **0.191 % from
z_C** (0.4993203342). Consistent with the γγ derivation being a
convention-C-frame calculation, which is what AGENTS.md records the whole c_k
ladder to be. (Sign: my n−p is negative where the block writes +T, so a sign
convention differs; the magnitude is what is tested.)

### Standing position on Delta

| | net (4 dp) | NF vector (6 comp) | γγ Δtr_M (10 s.f.) |
|---|---|---|---|
| constructed | 0.7975664 ✓ exact | **3/6** exact | **reachable**, 0.19 % from z_C |
| hecke_core | 1.1132 ✗ | **0/6**, e⁻ = 0 exactly | **impossible at every z** |

Three independent tests, increasing in precision, all pointing the same way.

### Archaeology on the table's producer — BLOCKED, and why

`categorical-neutron-table-data.ts` carries **no** `computation.script` or
`computation.witness`; it is tagged `extracted-table`, i.e. extracted rather
than produced. `git log --follow --diff-filter=A` returns 2026-08-26 — but the
clone is **shallow (336 commits)**, so that is the fetch boundary, not the
creation date. Exactly the hazard AGENTS.md records for `scriptCommitSha`.
Deepening the clone is the next step.


## 2026-08-29 (cont. 7) — the EXACT parabola: the exclusion is a THEOREM in q

Owner asked whether the difference is due to the SDP/ILP being integer, and
whether the exact parabola vertex is obtainable. **Yes to the vertex; no to
integrality being the cause.**

### The exact objects

`hecke_core`'s (n−p) coordinates, exactly in ℚ(q):

    gamma   = (1 - q^2)/(2q)                = -h/2
    sigma0  = sigma1 = -(q^2-1)^2/(4q^2)    = -h^2/4
    L_plus  = -(q^2-1)(q^4+1)/(4q^3)
    L_minus = 0          <-- vanishes identically
    e_minus = 0          <-- vanishes identically

    A = -(q-1)(q+1)(q^4+1)/(4q^3)
    B = -(q-1)^2(q+1)^2/(2q^2)
    C = -(q-1)(q+1)/(2q)

    z*  = -q(q-1)(q+1)/(q^4+1)
    max = -(q-1)(q+1)(q^2+1)^2 / (4q(q^4+1))

Numerics check out: z* = −0.10229469281 and max = −0.103412421104, matching
the measured values exactly.

### The exclusion upgrades from a measurement to a theorem

`max`'s numerator factors as **−(q−1)(q+1)(q²+1)²**, strictly negative for
**every q > 1**. So

> `hecke_core`'s Δtr_M(n−p) < 0 for ALL real z AND ALL q > 1,
> while the γγ anchor is POSITIVE (+0.0445860283).

Not "disagrees at q₀ under convention D" — **impossible across the entire
substrate range and every Markov parameter.** All three coefficients are
−(positive) for q > 1, so the quadratic is negative-definite.

### Answering the ILP question directly: integrality is NOT the cause

The corpus's *"integer LP dual enumerates all feasible gluon combinations and
selects the configuration minimizing |tr_M|"* selects among **gluon
configurations**, not among z. And the vertex z* = −q(q²−1)/(q⁴+1) is
**negative** — nowhere near any admissible Markov parameter (z_C 0.499,
z_D 0.613, q 1.110), so the ILP's minimisation is not happening there either.

The actual cause is structural and visible in the coordinates: **L₋ and e⁻
vanish identically**. With them gone the `z(hz+1)` term disappears entirely and
the z² term is L₊ alone, leaving every surviving coefficient negative. It is
the vanishing of two NF coordinates — the Hopf-link and trefoil channels — that
makes the whole quadratic sign-definite.

Which is the same fact as the NF-vector comparison, now in closed form: the
gluon and trefoil channels are simply not in the object `hecke_core` traces.


## 2026-08-29 (cont. 8) — archaeology: BLOCKED at the clone boundary, and I nearly reported the boundary as the answer

Owner asked to keep going and find the table's producer by commit archaeology.
Result: **cannot be determined from this clone**, and the way it fails is worth
recording because I walked into it.

**Deepened** 338 → **14,679** commits (`git fetch --deepen=3000`).
`git fetch --unshallow` did **not** complete in the time available; the repo is
still shallow with **6 grafts**.

**The trap.** With the deeper clone, `git log -S"1.0109"` and
`git log -S"0.0445860283"` both bottom out at the *same* three commits —
`c43d8b253d`, `a41b592e50`, `a3e3f5e4fa`, all 2026-06-12 — which looks exactly
like a co-introduction. It is not: **`.git/shallow` lists those very commits as
grafts**, and `git rev-list --max-parents=0` returns precisely the six graft
points as if they were roots. The "earliest" result *is* the fetch horizon.

**Third time this session** a "found the origin" answer was the boundary: the
`scriptCommitSha` class AGENTS.md warns about, then the first `--diff-filter=A`
attempt, now this. The tell is always the same — several independent searches
agreeing on one suspiciously round date.

**What IS established about the table, independent of history:**
`categorical-neutron-table-data.ts` carries **no** `computation.script` and no
`computation.witness`; it is tagged **`extracted-table`**. So no producer is
declared, whatever the history says. The nearest analogue found — commit
`a41b592e50`, *"conj-table digit fix"* — is a **different** table
(`conj-canonical-knot-id-sdp`, knot volumes) whose stale digits were replaced
by census values, **owner-confirmed**, i.e. hand-edited rather than
regenerated. Suggestive of the same pattern here; **not evidence for it**.

**How much this still matters: less than it did.** The exact parabola gives
infinite precision on the `hecke_core` side, so that exclusion is now a theorem
and needs
## The three open leads, pursued (2026-08-29)

### Lead 1 — pin the reconstruction from a corpus source: PARTLY CLOSED

**The B_3 word is a corpus statement, not my reconstruction.**
`binding-knots-visual-inventory-table1-data.md:12` gives the Borromean as
`(s0 s1^-1)^3`; `categorical-proton-properties.md` Step 1 gives
`s1^-1 = s1 - h`. Together that IS `(s0(s1-h))^3`. I had flagged this as an
open reconstruction DOF. It was pinned all along, in a table I had not read.

**A selection rule EXISTS, and I had reported it absent.** The previous probe
listed all eight quark-generator assignments because "the corpus does not say
which". Wrong: `ilp-solution-count-unwrap.md` states a parameter-free
tie-break — *"The proton's 9-crossing element admits N_l = 84 feasible ILP
solutions ... minimizing |tr_M| selects the unique sigma_0 -> sigma_0
solution"* — and `categorical-proton-properties.md` repeats it.

**But it cannot be applied, and that is the new open item.** "Minimize |tr_M|"
is monotone in the gluon count, so unconstrained it returns k=0 — the bare
element both blocks call infeasible. The rule is meaningful only over a
feasible set, and the corpus never defines that set machine-checkably. The
obvious reading — Frobenius positivity as "every NF channel coefficient >= 0",
which is the neutron block's own phrasing since it names the *sigma_0 channel*
— is **refuted by the corpus itself**: under it k=1 is infeasible for the
proton, while the proton block states *"a single Hopf link L_- = sigma_1
sigma_0 is the minimum additional structure capable of restoring stability"*.

So no gluon count is claimed. Under the naive reading the rule would pick k=2
(proton) / k=3 (neutron); those are NOT published, because the predicate that
produced them contradicts the corpus. Finding A is neither confirmed nor
withdrawn by this route.

**Restated blocker** (materially different from before): not "the corpus is
silent on which configuration", but "**Frobenius positivity has no
machine-checkable definition**". It must be the Gram/LP condition
`G(q) x >= 0` over operator SELECTIONS rather than sign-positivity of one
element's NF coefficients — no block pins it.

Probe: `computations/qbeta/qbeta_nucleon_selection_rule_probe.py`, 4/4.

### Lead 2 — a producer for the neutron NF table: BLOCKED BY LEAD 1

Confirmed again that no producer exists (all six basis rows tested; the one
apparent `1.0109` match is at the wrong basis element). Writing one requires
the exact element, which requires the gluon count and the quark assignment —
and Lead 1 shows the rule that would fix the gluon count cannot be evaluated
until Frobenius positivity is defined. **So Lead 2 is not independently
actionable**; it unblocks exactly when Lead 1's predicate is pinned.

### Lead 3 — the mpmath split: CLOSED, it is not a staleness axis

My "566/449" was wrong. Measured over live witnesses: **1160 at 1.3.0, 829 at
1.4.1, 2 at "0.0.0"** (that last a real defect — version not captured), total
1991.

The corpus cannot settle it: five producers have witnesses under both
versions, but none has a *same-named* witness under both — they are producers
whose different SUBJECTS were computed at different times, so a difference is
the subject, not the version. No in-corpus control exists.

Tested directly instead: both versions as pinned wheels, the framework's
load-bearing primitives at 60 dps compared at 55 significant digits. **All ten
byte-identical**, including `Vol(4_1) = 2*Cl2(pi/3)`, the q_0 root-solve,
polylog, hyp2f1, besselj, zeta, gamma. The split is not a reason to re-run
anything. Concern was mine; retired.

Method note, now asserted as check 1 so it cannot recur silently: the
container's INSTALLED mpmath is **1.4.1**, not 1.3.0. My first attempt
compared the installed interpreter against a 1.4.1 wheel — 1.4.1 against
itself — and returned "0 differences", which is indistinguishable from a real
agreement.

Probe: `computations/audits/mpmath_version_staleness_probe.py`, 3/3.

## RETRACTION: "Frobenius positivity has no machine-checkable definition"

**That claim was wrong, and I put it to the owner as needing a ruling.**
`stable-atom.md` (`def:stable-atom`) defines it, and precisely:

> Let `G(q)` be the Frobenius Gram matrix of the primitive Wedderburn-block
> operators `{e_λ}`. Decompose `T_w = Σ_λ x_λ · e_λ` with `x_λ ∈ ℤ_{≥0}`. The
> atom is **stable at q** iff `∃ x ∈ ℤ_{≥0}^N` with `G(q) x ≥ 0`
> coordinatewise.

One grep on the exact phrase found it. I had searched the two properties
blocks and the ILP block, found the phrase used but not defined there, and
concluded it was undefined corpus-wide — without grepping the phrase itself
across `content/`. The definition block was one hop away.

**Two things in that sentence are load-bearing and I dropped both:** the
inequality is on `G x`, **not** on `x`; and `x` are coordinates in the
**primitive Wedderburn basis** `{e_λ}`, not the normal-form basis `{T_w}` my
probe used. So my "naive reading" was not a plausible-but-unconfirmed
interpretation — it was a different predicate on a different basis.

### Formalised: `QOU.ParticleInteractions.FrobeniusPositivityPredicate`

Sorry-free, `lean`-direct exit 0, zero warnings, `#print axioms` clean on all
8 declarations.

| declaration | content |
|---|---|
| `frobPos_of_entriesNonneg` | `G` entrywise ≥ 0 ⟹ the naive reading is sound |
| `exists_coordPos_not_frobPos` | ONE negative Gram entry already separates them — witness is the indicator of that column, so they part company on the basis |
| `coordPos_imp_frobPos_iff_entriesNonneg` | the naive reading is sound for *every* selection vector **iff** `G` is entrywise nonnegative |
| `naive_reading_unsound_of_neg_entry` | contrapositive, in the form to check |
| `frobPos_zero` / `_add` / `_smul` | the feasible set is a convex cone |
| `stableAt_trivial` | the **relaxed** predicate is trivially satisfied for every `G` |

`stableAt_trivial` is a *sharpness* result: the corpus's condition carries
content only through what the relaxation drops — that `x` be the
primitive-basis decomposition of the given `T_w` with nonnegative **integer**
coordinates. A formalisation that omits it proves nothing about stability.

So my probe's verdict (k=1 infeasible for the proton, contradicting
`categorical-proton-properties.md`) is exactly the unsoundness
`naive_reading_unsound_of_neg_entry` describes. **The corpus was right.**

### The open item, restated and narrowed — NOT an owner ruling

The predicate is pinned. What is missing to evaluate it for `H_3` is
**computable, not conventional**:

1. the Frobenius Gram matrix `G(q)` of the primitive Wedderburn-block
   operators `{e_λ}`, `λ ⊢ k`, `k ≤ k_max`; and
2. the primitive-basis decomposition of the nucleon normal form, with
   nonnegative **integer** coordinates.

With those two, the selection rule (`minimize |tr_M|` over the feasible set)
becomes evaluable, and Lead 2 — the neutron NF table's missing producer —
unblocks with it.

## Owner-authorised content corrections (2026-08-29)

Owner selected all four options offered. Applied:

1. **Neutron crossing count 13 → 11** (`categorical-neutron-properties.md`).
   The block contradicted itself in consecutive paragraphs: para 2 says *a
   single* Hopf link `L_-` restores stability; para 3 said *two* Hopf links,
   4 gluon crossings, 13 total. Its own printed `+0.7976` is the
   **eleven**-crossing value (k-ladder: 9 → 0.788010, **11 → 0.7975664**,
   13 → 1.235859, the last appearing nowhere in the corpus). The 4-versus-2
   proton asymmetry claim does not survive and was dropped; the `tr_M` depth
   comparison it rested on is kept. Settles `qou-im4m` — it is the prose.

2. **`N_ℓ = 84` marked unsourced** (`ilp-solution-count-unwrap.ts` author
   note) and the **dead citation repaired** in
   `docs/audits/2026-05-27-mass-formula-uniqueness-argument.md` §C5. The cited
   `mass-endomorphism.witness.json` exists but carries zero fields equal to 84
   and zero ILP-related keys; its subject is a Φ_q tower endomorphism
   recording a 407 % error. Not a claim that 84 is wrong — a claim that
   nothing now reproduces it.

3. **σ₀ vs L₋ stabiliser disagreement flagged** on both
   `stable-atom-properties.ts` and `categorical-proton-properties.ts`.
   Same crossing count (2), different operator, neither block citing a
   computation. Recorded, not adjudicated.

4. **2-vs-3 crossings kept OUT of content**, per the owner's choice — it
   rests on my reading of `(Gx)_γ` rather than on the corpus's arithmetic.
   It stays here and in `qbeta_adjunction_ilp_probe.py`.

Verification: `run-validate.ts` **✓ Valid**, 13 issues, all pre-existing on
main (zero added — none of the four edited blocks appears in any warning).
Render-QA preflight on the edited `.md`: `$` balanced (90), braces balanced,
no `\operatorname`, no align-family env, no list-hijack inside `$$`.

**A near-miss worth recording.** These edits were first written while the
dispatched prepare-merge agent was mid-rebase. Worktrees share refs, so the
branch tip moved ~100 commits forward under my working tree, and `git status`
showed **2229 modified + 350 deleted** files — my stale tree read as a revert
of all of main. Committing then would have reverted main wholesale. Caught by
checking status before staging; edits were saved aside, the tree restored to
HEAD, and each edit re-applied against the post-rebase base after verifying
0 lines would be lost. Lesson: after dispatching a worktree agent onto the
SAME branch, treat the local tree as stale and re-check HEAD before staging.



## 2026-09-03 — my own caveat on rem:categorical-neutron-properties was WRONG; retracted

The note I landed on 2026-08-29 said the $(Gx)_\gamma = tr_M(e_\gamma . T_w)$
reading "reproduces this chapter's own claim that the bare 9-crossing element
violates positivity, with exactly one negative channel", and concluded no
two-gluon adjunction is feasible for the proton (minimum three). Three defects,
found by the corpus-grep I should have run before writing it:

1. **The corroboration cites STRUCK text.** "This chapter's own claim" is the
   sentence one paragraph up, struck through since 2026-08-24 by `qou-jqjx`:
   the bare element's instability is an artefact of the retired weight
   `tr_M(e-) = z^3`, retired 2026-05-19. That bean is `completed` and predates
   my note by five days. Reproducing a withdrawn number is evidence AGAINST a
   reading.

2. **The numbers never reproduced it anyway.** The withdrawn claim is
   `tr_M(T_w) < 0` (retired-weight -0.0059 / -0.1322). My probe's gamma=1
   channel gives **+0.5444** = `qou-jqjx`'s corrected live **+0.544370**, to
   the digit. So it agreed with the CORRECTION and I wrote it up as agreeing
   with the BUG.

3. **The basis was over-complete, and that is where the negative came from.**
   `def:stable-atom` defines G over the primitive Wedderburn-block operators
   `{e_lambda}_{lambda |- k}`; H_3(q) has THREE. My probe built SIX ("1, E+,
   E-, and 3 central"), which is the same over-completeness I had already
   measured and retracted elsewhere (rank 4 vs augmented rank 5). The single
   negative pairing (-0.02275) lives on the extra elements.

Re-run of `computations/probes/nucleon-lp-convention-probe.py` on 2026-09-03,
convention D: every step of both nucleons is positive.

    proton   min(Gx) = +0.342489, +0.279195, +0.339149
    neutron  min(Gx) = +0.277726, +0.172959, +0.217525

No negative channel anywhere. My "exactly one negative channel" does not
survive, and neither does the "minimum is three gluon crossings" that rested
on it.

### What survives, and it is only the hedge

The note's own hedge -- "that rests on a reading of the predicate rather than
on the corpus's arithmetic" -- was right, and is now the whole content. The
open question is genuinely open and is NARROWER than the note claimed:

* `def:stable-atom` names the **primitive-idempotent** basis;
* `nucleon-lp-convention-probe.py` uses `pyhecke.gram`'s **NF-word** Gram
  (`NF_BASIS = [(), (0,), (1,), (0,1), (1,0), (0,1,0)]`);
* and the partition-indexed decomposition the definition literally asks for
  **does not exist** (rank 4 vs augmented rank 5), so the definition as written
  is not directly evaluable either.

Which object G is, is unanswered. Nothing here answers it; do not read the
positive min(Gx) row as settling it, only as settling that MY six-element
construction was not the definition's three.

### Second note added, on a LIVE tension nobody has struck

The `sigma_0` sentence is already struck, so the "sigma_0 vs L_-" item I
promised to flag is moot in that form. What is NOT struck, and is in tension
with the live convention, is the next sentence: *"The integer LP dual selects
L_- as the minimum-action stabiliser"*. Measured (same probe, same day):
neutron `L+.L-` ranks **26/41** at 0.690056 against bare 0.408267; the
min-|tr_M| optimum is a **single sigma_0 at one crossing** (0.217525); under
the minimum-crossing objective `def:universal-ilp-algorithm` actually states it
is **zero**. Proton likewise (`s0.s0` 10/41 at 0.615273 vs bare 0.544370).

So the selection sentence, the 11-crossing total it feeds, and the m_n - m_p
mechanism resting on it are all in tension. `qou-jqjx` deliberately proposed no
replacement ("the derivation needs re-deriving, not patching"); that judgement
is not revisited. Flagged on the block, not resolved.

Scope-(a) throughout. No observable moves.

### Contamination check

The retracted claim appeared in: this bean, the caveat authorNote (now
replaced), and PR #5958's body. It did NOT reach any `.md` prose, any witness,
or any Lean file -- the note said explicitly it was "deliberately not written
into this block", which is the one thing that limited the blast radius.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-03 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

## Implementation & Witness Progress (PR #8264)
- Branch: `qou-10v9-e58e-gcmn-vbyi-vtlj-xy5f` (`248efc097170676991e07dd557f09bee0827f2bc`), PR: `litlfred/qou#8264`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/BarParityIsospinSplitBppConfoundSingletTensorInvarianceDeltaFourValuesAndOrderingDofShift.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/bar_parity_isospin_split_bpp_confound_singlet_tensor_invariance_delta_four_values_and_ordering_dof_shift_probe.py` -> `computations/probes/bar-parity-isospin-split-bpp-confound-singlet-tensor-invariance-delta-four-values-and-ordering-dof-shift.witness.json` (`allPassed: true`, `scriptHash: e7d87b167c3f`, `scriptCommitSha: 7d111fc9111a5ac911879c633afd63652e0f6384`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8264, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-04: "content(qou-vtlj): RETRACT my own positivity caveat — it cited struck text, and the basis was over-complete"). The work may be partly or fully done. Read the bean before you close it.
