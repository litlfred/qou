---
# qou-5c64
title: binding-single-pipeline-comparison is 3 months stale and RED when re-run — 2 assertions flip, one column moves 69x, and the float64 drain is blocked behind it
status: todo
type: bug
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T09:23:58Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-v2om
---

Found 2026-09-13 while screening `binding-single-pipeline-comparison` (299 raw
float64 fields) as a drain target. The reproducibility check that precedes every
drain is what turned it up: run the **unmodified** producer from `HEAD` and the
committed witness does not reproduce.

## The measurement

`computations/binding-single-pipeline-comparison.witness.json` was computed
**2026-06-15T17:27:53Z**. Re-run today on `main` `53e088bc03d`, unmodified
producer, no edits of mine:

    allPassed:  True  ->  FALSE

| assertion | computed | passed |
|---|---|---|
| `B_sym_E0_within_1p25x_T_3He` | 1.136 -> **1.58** | True -> **FALSE** |
| `B_qCLT_fac_chain_within_1p25x_T_3He` | 1.083 -> **1.5** | True -> **FALSE** |
| `E0_beats_deuteron_pin_generic` | 0.8807 -> 0.7849 | True -> True |
| `B_magic_He4_within_10pct` | 0.945 -> 0.945 | True -> True |
| `B_qCLT_fac_resolves_T_3He_ordering` | 1.0 -> 1.0 | True -> True |

**262 numeric fields moved.** The largest are all one column,
`B_lin_raw__*__miss_x`, and they grow with A:

| row | field | committed | live | move |
|---|---|---:|---:|---:|
| 5 | `B_lin_raw__E0_derived__miss_x` | 10.699 | **747.44** | 69× |
| 5 | `B_lin_raw__alpha_D_pinned__miss_x` | 18.708 | **951.92** | 51× |
| 4 | `B_lin_raw__E0_derived__miss_x` | 8.101 | 295.06 | 36× |
| 3 | `B_lin_raw__E0_derived__miss_x` | 7.412 | 86.47 | 12× |
| 1 | `B_lin_raw__E0_derived__miss_x` | 2.520 | 17.94 | 7× |
| 0 | `B_lin_raw__E0_derived__miss_x` | 0.893 | 3.614 | 4× |

Headline fields move too: `He4_miss_x` 7.17 -> 7.731,
`miss_range_generic_x` `'0.88-2.30x'` -> `'1.08-2.68x'`,
`B_qCLT_chain_uniform_E0` 7.7794 -> **5.6663** (-27 %). And the wall time went
`durationMs` 4591 -> 46014, a 10x slowdown.

## The scriptHash moved, but that is NOT the cause — I checked

    recorded scriptHash  dc752e6dffd2
    live     scriptHash  fa8cd41874f1

The producer's own source did change, so `witness_staleness_triage.py` would
class this `substantive` rather than `cosmetic`. **That classification would be
misleading here.** I read the June version at its recorded
`scriptCommitSha 32f3f7314e11c8beb610f8d3972bbf1ab4f0ec50` (via the GitHub API —
the clone is shallow, so `git log -- <producer>` returns only the boundary
commit) and diffed it. The only change to the compute path is that
`_constants()` dropped a `try/except` fallback around the `codata_constants`
import. That cannot move a number by 69x.

**So this is import-cone drift, and the trap AGENTS.md names for it applies
exactly: a file-local `git diff` on the producer cannot see it.**

## Cause: the UPSTREAM TRACES moved, by a clean per-nucleon factor

Every `tr_M` this producer reads changed, and the change is structured:

| atom | A | tr_free old -> new | ratio | **ratio^(1/A)** |
|---|--:|---|--:|--:|
| D   | 2 | 0.983526 -> 0.299015 |  3.289 | **1.81362** |
| ⁴He | 4 | 0.967324 -> 0.089410 | 10.819 | **1.81362** |
| ⁶Li | 6 | 0.951388 -> 0.026735 | 35.586 | **1.81362** |
| T   | 3 | 0.908024 -> 0.142072 |  6.391 | 1.85579 |
| ³He | 3 | 1.047757 -> 0.188179 |  5.568 | 1.77241 |
| ⁷Li | 7 | 0.878353 -> 0.012703 | 69.145 | 1.83157 |

**The three N = Z nuclei agree to all six significant figures** — a uniform
per-nucleon factor of `1.81362` — while the three N ≠ Z ones split above and
below it (n-rich high, p-rich low). That is a per-nucleon change that also
touches the p/n weighting, which is the shape of the 2026-08-15 ruling's **R3**
(`bring_color_weighted` canonical as the p/n convention) as much as of R1's
C -> D `z` swap.

It is **not** a pure rescale: the log-ratios moved too
(`ell_bond_deuteron 0.929219 -> 0.676822`, `L_pp 0.694507 -> 0.489899`,
`L_nn 1.236978 -> 0.907262`), so free and atom words moved by different amounts
— which is what a change in `z` does, since `z` enters the atom word's
inter-nucleon crossings and not the free word's.

The producer's own scale parameters did **not** move: `E_0_MeV 4.185981`,
`q_0 1.109979`, `m_e_MeV 0.51099895` are identical across the two runs. Only
`alpha_D_pinned_MeV` moved (2.394018 -> 3.286784), and that is derived from the
deuteron trace, so it is downstream of the same change.

**The factor 1.81362 is NOT identified.** I tested ~14 natural substrate
combinations at the proton `q₀`; the closest is `(q²+1)/q² = 1.811654`, which is
**0.11 % off** — far too large, since D's ratio comes from two values recorded to
six decimals and is good to ~1e-6. Identifying it would pin the exact upstream
change and is the cheapest way to finish this diagnosis.

**Also present and separately real, but far too small to matter:** the AME
inputs refreshed (`7.718043 -> 7.71804132`, `8.481798 -> 8.4817962`), i.e.
canonical `codata_constants` values replacing literals — a ~2e-6 move.

**Upstreams to look at:** `binding-canonical.witness.json` (D–⁴He) and
`tr_m_atom_via_transfer.tr_m_atom_zn` (⁶Li/⁷Li live, and the bond-type
sub-braids). Both moved the same way, so whatever changed is in or below
`tr_m_atom_zn`.

## Why nothing was regenerated

Three reasons, and the third is decisive.

1. **It turns a green record red.** Landing the regeneration publishes
   `allPassed: False` with two failing assertions. That is the honest state and
   it is the right end point, but it is a visible corpus-state change.
2. **It has a consumer.** `qou-y313` records
   `qbeta/qlommel_delta_lambda_lin_vs_sym_ladder.py` reading this witness (74
   fields), so the numbers propagate.
3. **It belongs to someone else's arc.** `qou-gjkv` — *"wave5: post-C-to-D
   corpus-wide witness regen (162 producers)"*, status **in-progress**, branch
   `claude/anchor-followups-2026-08-08` — lists
   `binding-single-pipeline-comparison (763)` by name in its own target list.
   AGENTS.md's 2026-09-07 ASK-THE-OWNER directive names *"regenerating a
   derived artifact that belongs to someone else's arc"* as explicitly NOT
   exempt.

That claim is **35 days stale**, so the stalled-claim takeover policy (>3 h with
no commit) would permit taking it over. But a takeover of a 162-producer sweep
is not a drive-by, and the branch is not fetched in this container, so its tip
was not verified — the age is from the bean's `updated_at`, not from a commit.

## Consequence for the float64 backlog

**The 299-field drain of this producer is BLOCKED behind this decision**, and
not incidentally: draining requires re-running the producer, and re-running it
IS the regeneration. There is no way to fix the float64 without also landing
the three-month regeneration.

This generalises. Any producer in `qou-gjkv`'s 162 is in the same position, so
the drain queue and the regen sweep are coupled wherever they overlap — a fact
neither bean records.

## Options (recommendation marked as judgement)

1. **Do nothing.** The witness keeps reading green while its producer's own
   assertions fail. Cost: zero now; the corpus keeps a false green on a
   binding-comparison result that content may cite. This is the default.
2. **Regenerate this one witness alone, publishing the red**, and drain the
   float64 in the same commit. Cost: ~1 min compute, 262 fields move, two
   assertions go red, one downstream consumer's inputs change. Risk: it
   pre-empts `qou-gjkv`'s ordering, and if the C->D hypothesis is wrong the red
   is unexplained. Reversible via git. Buys: an honest record and a 299-field
   drain.
3. **Take over `qou-gjkv` and run the whole 162-producer sweep.** Cost: large,
   hours of compute, a wide diff. Risk: highest, and it is the sweep class the
   ASK-THE-OWNER directive exists to gate.
4. **Finish the diagnosis first** — identify the `1.81362` per-nucleon factor
   and the commit in `tr_m_atom_zn`'s cone that introduced it, then choose.
   Cost: one read of that producer's history plus an algebra check; the
   producer-side half of this is already done (see above). Buys: option 2
   becomes a documented regeneration ("the traces moved to convention X on
   date Y") instead of an unexplained red.

I would take **4 then 2**: the finding is only worth landing once the red can be
explained in the commit message, and the remaining step is small — the producer
half is settled, only the upstream commit and the constant are open. Marked as
my judgement, not a finding.

**If nothing is decided, nothing changes** — the witness stays green, the
producer stays red when run, and its 299 float64 fields stay in the backlog.


---

## `qou-gjkv` ALREADY CLASSIFIED this witness as a C→D mover — on 2026-08-09

Read after writing the above, and it corroborates the cause independently and
with a date. That bean's own report names
`binding-single-pipeline-comparison (763)` in its results, and states its
posture explicitly:

> ACCEPTANCE IS NOT DONE AND IS NOT MINE TO DO. The driver's
> KEEP = {DECLARED, ANCHOR_MIGRATION, SUBFLOAT_MOVE} deliberately excludes
> VALUES, so this wave CLASSIFIES; it does not accept.

So the regeneration was **deliberately deferred pending a review pass**, not
forgotten. That settles the ownership question in the section above: this is not
an abandoned claim to take over, it is a completed classification waiting on an
acceptance decision that the wave's author declined to make on their own
authority — the same call the ASK-THE-OWNER directive would require today.

**One characterisation to reconcile.** `qou-gjkv` lists this witness under
*"largest non-numeric movers … assertion/string churn at scale"*. Measured here
a month later, **262 NUMERIC fields moved and two assertions flip to FAIL** —
materially more than "string churn". Two readings, and I have not separated
them: either the wave's field counter classified differently, or more moved in
the intervening month. Either way, do not read that line as "cosmetic" when
deciding acceptance.


---

# CAUSE MEASURED 2026-09-13 — and it is NOT convention C→D. I was wrong, and so is `qou-gjkv`'s label.

I got the June witness at full 50-dps precision (the GitHub API at its own
recorded `commitSha 0fa83306db2a`), which turns every hypothesis above into a
runnable test instead of an inference. Four ran. Three of them killed a
hypothesis, including both of mine.

`binding_canonical.py`'s call into `tr_m_atom_zn` is **byte-identical** between
June and now (I have both files), so the change is entirely inside that cone.

## Test 1 — the q₀ anchor: ruled out, 3.9e-8

June's witness records `q0: 1.1099785955573347` — the retired frozen **muon**
pin, stored as a float. Today's records `q0Anchor: proton`,
`1.1099785827513808…` at 50 dps. So the anchor DID migrate. Running the **live**
code at **June's own muon q₀**:

    live @ muon q0   tr_free = 0.2990150289185773331303254
    live @ proton q0 tr_free = 0.29901501718464007670216042677
    JUNE             tr_free = 0.98352619917553294948492109080

**The anchor accounts for 3.9e-8 of the change.** The remaining 2.289 relative
(3.29×) is code. Ruled out.

## Test 2 — `y_lambda_at` convention C vs D: NO-OP. This is the correction.

`wedderburn_jones_markov` still carries the dead
`_y_lambda_at_convention_C_HISTORICAL`, so the swap is directly testable. Both
functions were called at `n = 6`, same q, and compared entry by entry: **all 11
partitions agree to displayed precision**. Substituting C for D inside
`tr_m_atom_zn` returns the same trace to 30 digits.

**So the convention-D `y_λ` migration does not move this witness at all**, and
two claims must be withdrawn:

- **Mine, in the section above:** *"a per-nucleon change that also touches the
  p/n weighting, which is the shape of the 2026-08-15 ruling's R3 as much as of
  R1's C → D `z` swap."* Withdrawn — measured false for the `y_λ` half.
- **`qou-gjkv`'s**, which lists this witness in a wave titled *"post-C-to-D
  corpus-wide witness regen"*. The label does not fit this member.

## Test 3 — the braid word's INTRA-NUCLEON ORDERING: the dominant term

Found by corpus-grep, not by guessing: bean **`qou-92u9`** records that
`atom_braid_word_3A`'s intra-nucleon ordering changed on **2026-09-05** —
bean **`qou-hu1f`**, an **owner ruling**, commits `7db032fb48` / `deb9ff5728`.
Each nucleon's confinement core is now **ALTERNATING**
(`intra_order="borromean"`, the default) where it was **GROUPED**.
`tr_m_atom_zn` does not expose the parameter, so it always takes the new
default.

Forcing the old ordering (same q, `intra_order="grouped"`):

| | tr_free | tr_atom |
|---|---|---|
| live default (`borromean`) | 0.29901503 | 0.15196835 |
| **forced `grouped`** | **1.13171707** | **0.57517233** |
| JUNE | 0.98352620 | 0.38835728 |

It moves in the right direction and **overshoots**: 15.1 % past June on the free
trace, 48.1 % on the atom trace. So the intra-ordering ruling is **the dominant
term and not the whole of it**.

That also explains every structural feature measured earlier: it is a
**per-nucleon** reordering (hence a per-nucleon factor), identical for identical
composition (hence the three N = Z nuclei agreeing to six significant figures),
and different for different p/n mixes (hence the n-rich / p-rich split). And the
free and atom words are reordered independently, which is why their ratios
differ (3.2892 vs 2.5555) — a scalar `z` re-parameterisation could not do that,
which was the first hint that C→D was the wrong story.

## What is still open

A residual of **15 % (free) / 48 % (atom)** after restoring the June ordering at
the June anchor. At least one further change sits between June and now, in
`atom_braid_word_3A`'s other knobs (`pn_convention`, the `m_*` multiplicities,
`ordering`) or in `chi_all_lambda_reduced_block`. Next step: bisect those the
same way — force each to its June value and re-measure. The June
`mass_at_3A_proper.py` is reachable at the same commit through the GitHub API.

## What this changes for the DECISION above

Option 4 ("finish the diagnosis first") is now most of the way done, and the
answer changes who should decide. The dominant cause is an **owner ruling**
(`qou-hu1f`, 2026-09-05) that deliberately changed the physics of the word. So
regenerating this witness is not accepting an unexplained red — it is
propagating a ruling that has already been made, and the honest red is what that
ruling implies for this probe's assertions.

**Revised recommendation (my judgement):** finish the residual bisection, then
regenerate, with the commit message naming `qou-hu1f` as the cause. I would no
longer describe this as a C→D acceptance question at all.

## 🛑 And the wider point, which is bigger than this witness

`qou-gjkv` swept **162 producers** under one label — "post-C-to-D". At least one
member moved for an entirely different reason, by a factor of 3.29, from a
**later** owner ruling that postdates that wave by four weeks. Anyone accepting
that wave on the strength of its label would be accepting changes they have not
diagnosed. The 162 need re-triage against `qou-hu1f` before acceptance, not just
against C→D.


## Residual bisection — two more excluded, and a limit on what test 2 proved

Same method, same June anchor, cross product of the two word knobs:

| `intra_order` | `pn_convention` | tr_free | rel to June (free) | rel (atom) |
|---|---|---|---:|---:|
| borromean | bring_color_weighted | 0.29901502891857733313 | 0.696 | 0.6087 |
| borromean | strict_averaged | 0.29901502891857733313 | 0.696 | 0.6087 |
| **grouped** | bring_color_weighted | **1.1317170715774177518** | **0.1507** | 0.4810 |
| **grouped** | strict_averaged | **1.1317170715774177518** | **0.1507** | 0.4808 |

**`pn_convention` is excluded.** It is a no-op on the free trace — as it must be,
since free words carry no interface — and moves the atom trace by 2e-4. So R3 of
the 2026-08-15 ruling is not in this residual either, which is the second half of
the withdrawal above.

**The multiplicities are excluded by reading, not by testing:** June's
`binding_canonical` calls `tr_m_atom_zn(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
dps=50)` with the same `1, 1, 1` defaults the live one uses.

### 🛑 A limit on test 2 that I should state before someone over-reads it

Test 2 shows the **two current implementations** of `y_lambda_at` — live D and
the dead `_y_lambda_at_convention_C_HISTORICAL` — agree with each other today.
It does **not** show that either agrees with what June computed. `y_lambda_at`'s
values may have moved since June for reasons unrelated to the C/D split, and
nothing measured here excludes that.

So the honest remaining candidate set is:

1. `nucleon_word_letters` — the per-nucleon word CONTENT, as distinct from the
   ordering of it that `qou-hu1f` changed;
2. `chi_all_lambda_reduced_block` — the χ side;
3. `y_lambda_at`'s **values** since June, which is a different question from
   C-vs-D and is untested.

One weak discriminator already in hand: the residual is **15.1 % on free** and
**48.1 % on atom**. A pure `y_λ` move would shift both by a similar weighted
amount, since both traces are `Σ_λ y_λ χ^λ` over the same weights; a 3× split
between them points at the words rather than the weights. Weak, not decisive —
the two words have different partition support.


## The decomposition, and a corpus cross-check that validates the method

The corpus already records the intra-ordering's own effect, three lines above
the docstring claim in `mass_at_3A_proper.py`: absolute traces moved by
**`3.785×` (2H)**, 7.868× (3H), 6.891× (3He), 14.325× (4He). Measuring the same
thing here, all at June's own q:

|  | free | atom |
|---|---:|---:|
| **intra-ordering** grouped / borromean | **3.784816689** | **3.784816689** |
| **residual** grouped / 2026-06-15 | **1.15067303** | **1.481039152** |
| composite 2026-06-15 / now | 3.289219952 | 2.555514271 |

**The ordering factor reproduces the corpus's `3.785` to ten digits, and is
identical on free and atom.** That is the cross-check that makes the residual
worth trusting: the method recovers a number the corpus measured independently,
by a different route, a week earlier.

**The residual is NOT uniform**, and that is the most informative thing in the
table. Free and atom move by different amounts, so the second change touches the
**interface letter** — the atom word's one extra factor at `A = 2` (22 factors
free, 23 atom, measured) — and not only the nucleon cores:

    interface factor changed by   1.481039152 / 1.15067303 = 1.28711
    per nucleon core              sqrt(1.15067303)         = 1.07270

Neither constant is identified. Both sit between **2026-06-15** and
**2026-09-05**, and finding them means diffing `nucleon_word_letters` and the
interface construction across that window.

## Falsified in passing: the docstring's own claim

`mass_at_3A_proper.py:488` read *"Pass `intra_order="grouped"` to reproduce any
pre-2026-09-05 absolute number."* Measured false: grouped reproduces the state
**immediately** before the ruling, and misses 2026-06-15 by 1.151× (free) /
1.481× (atom). Corrected in place with the table above and the ruled-out list,
since a claim that broad is exactly what would send the next agent looking for a
bug in their own harness. Narrow correction only — I have shown grouped ≠ June,
**not** when the other change landed.


# THE DECOMPOSITION IS COMPLETE — three factors, two of them exactly identified

Found by listing the commits that touched `mass_at_3A_proper.py` in the window
`2026-06-15 .. 2026-09-05` (34 of them) rather than by guessing at constants.

    June -> now,  free 3.289219952  =  3.784816689 / 1.15067303
                  atom 2.555514271  =  3.784816689 / (1.15067303 x 1.287106862)

Both reconstructions close to the last digit shown, so the three factors below
are the whole of it.

## 1. Intra-nucleon ordering — 3.784816689×, free AND atom

Owner ruling `qou-hu1f`, 2026-09-05, `7db032fb48` / `deb9ff5728`. Identical on
free and atom to ten digits, and reproduces the `3.785 (2H)` the corpus recorded
independently a week earlier.

## 2. The p-n interface δ de-wire — 1.287106862×, atom only. CONFIRMED EXACTLY.

Commit **`9928f3f4a79`, 2026-06-29** — *"de-wire(flavor-split): canonical
color-weighting δ → proven leading **(WIP: witness cascade pending)**"*. The
parenthesis is the staleness admitting itself in its own commit message, two
weeks after this witness was written.

The p-n bond constant `tr_M(W_atom)/tr_M(W_free)` — which the bond model makes
ordering-invariant, and my data confirms is, since factor 1 is identical on both
traces:

    now         0.508229791209865
    2026-06-15  0.394862156668161
    ratio       1.287106862

Against the interface crossing `σ − h(1/2 − δ/4)` at the same q:

    delta today = flavor_split_leading(q) = 0.001375711249867512
    d from that formula                   = -0.1044582593357241
    d backed out of the bond ratio        = -0.1044582593357241     agree 2.9e-16
    d backed out of the JUNE bond ratio   = -0.217825893877428
    => delta as of 2026-06-15             = -2.16771373552

**So the de-wire changed δ from `−2.168` to `+0.001376`** — a sign flip and three
orders of magnitude, which is what "posited subleading → proven leading" means
numerically. `d` is now within 0.07 % of the colour-**blind** `−h/2 = −0.104530`.

Consequence beyond this witness: **any June-era artifact quoting a p-n bond
constant is quoting a superseded δ**, and the discrepancy is 29 %, not a rounding.

## 3. Free-trace residual — 1.15067303×, UNIDENTIFIED

Per nucleon core `sqrt(1.15067303) = 1.07270`. It cannot be the interface: the
free word has none. Candidates from the same commit list, none tested:

- `1b4fd94da1d` (2026-08-23) *"jones_wenzl_weight was not the Ocneanu weight"* —
  strongest, and note it is a **weight** change that is NOT the C→D split, which
  is exactly the gap the scoping note above warned about;
- `8cf55696489` (2026-08-22) *"swap the production tower to the Lean-mandated
  towerTerm"*;
- `77e4e68b75e` (2026-08-21) *"stop pointing callers at the scheme that breaks
  the tower"*;
- `efcaf79ed29` (2026-08-08) *"NO FLOAT64: the braid word was f64 at source"* —
  listed for completeness, but a NO-FLOAT64 fix should move a number by ~1e-16,
  not 15 %, so it is the least likely of the four.

A weight change is consistent with leaving the bond ratio invariant, because the
bond model makes that ratio a product of `(z + dᵢ)` independent of the weights —
so the free trace absorbs the whole of it, which is what the data shows.

## What this changes for the decision

Both identified factors are **deliberate, ruled changes** — one an owner ruling,
one a de-wire whose own commit message flags the pending cascade. Neither is a
bug. Regenerating this witness propagates two decisions already made; the two
assertions that go red are what those decisions imply for this probe.

**Recommendation unchanged in shape, stronger in evidence (my judgement):**
regenerate, with the commit naming `qou-hu1f` and `9928f3f4a79`. The remaining
1.15067 is worth one more bisection first, but it is no longer load-bearing for
the decision — it is a third deliberate change of the same kind, not an
unexplained number.


# 🛑 RETRACTION — "the C→D component is measurably zero" is FALSE. It is the p-p bond, exactly.

I wrote that above, on `qou-gjkv`, and in commit `b44ca9cc30c`. It is wrong, and
the measurement that refutes it is the same method one step further on.

Isolating each bond type from the ordering-invariant ratio `r = tr_atom/tr_free`
— `r(³He)/r(D)` is the p-p bond, `r(T)/r(D)` the n-n, `r(D)` the p-n:

| bond | now | 2026-06-15 | residual |
|---|---|---|---:|
| **p-p** | **0.61268805054558909984** | **0.49932034618370936279** | **1.227044031** |
| p-n | 0.50822979120986496969 | 0.39486215666816114720 | 1.287106862 |
| n-n | 0.40362772855570963873 | 0.29026002439520742122 | 1.390572916 |

and against the two Markov parameters at that q:

    z_D = q^3/(q^2+1)      = 0.61268805054558909984
    z_C = 1/(sqrt q + 1/sqrt q) = 0.49932033403359825002
    z_D / z_C                   = 1.227044061

**The p-p bond IS `z`** — it matches `z_D` today to **3.2e-51** and `z_C` in June
to **2.4e-8**, and its residual is `z_D/z_C`. (The 2.4e-8 is the q₀ anchor: June
ran at the frozen muon pin `1.1099785955573347` and I evaluate `z_C` at the
CODATA-2018 muon derivation, which differ at ~1.4e-9 and are amplified by `z`.
Same scale as the 3.9e-8 anchor effect measured at the top of this bean.)

So convention C→D is not merely present in this witness — **it is one of the
three bond constants outright**, and it multiplies through every nucleus with a
p-p bond.

## What I actually measured, stated correctly this time

- **The C→D swap inside `y_lambda_at` is a no-op** — both implementations agree
  at `n = 6`. That test was sound and its result stands.
- **The C→D change in the Markov parameter `z` itself is fully present**, and it
  never went through `y_lambda_at`. I tested one carrier of the convention,
  found it inert, and reported the convention inert. That is the
  absence-of-evidence error, made against a claim I had the means to check.

## Consequence: `qou-gjkv`'s label was RIGHT, and my flag on it overstated

That bean lists this witness in a wave titled *"post-C-to-D corpus-wide witness
regen"*. **The label fits.** My append there — *"the C→D component is measurably
zero for it"* — is retracted; corrected on that bean.

What survives of that flag, and it is still worth acting on: this witness moved
from **three** distinct changes, only one of which is C→D, and two of which
(`qou-hu1f`'s intra-ordering, 2026-09-05; the δ de-wire `9928f3f4a79`,
2026-06-29) postdate or predate the wave's own measurement date of 2026-08-09.
So the wave's numbers still cannot be the whole story for this member — but the
reason is *incompleteness*, not a wrong cause.

## The decomposition, corrected and complete

    tr_M(free) June -> now  =  [ordering] / (a^Z * b^N)
    tr_M(atom) June -> now  =  [ordering] / (a^Z * b^N * PROD over chain bonds)

    ordering (qou-hu1f)  D 3.784816689  T 7.868165269  3He 6.890664045  4He 14.32483737
                         (reproduces the corpus's own 3.785 / 7.868 / 6.891 / 14.325)
    per nucleon          proton a = 1.075521518    neutron b = 1.069874485
    per bond             p-p 1.227044031 = z_D/z_C   p-n 1.287106862   n-n 1.390572916

Both fits are identities rather than fits: `a^Z b^N` reproduces all four free
residuals to **1e-50**, and the three bond factors reproduce all four bond
residuals to **5.6e-12** (three unknowns, four equations, uniform residual — the
5.6e-12 is June's own ordering-invariance floor, not a model failure).

Still unidentified: `a`, `b`, and the non-`z` parts of the p-n and n-n bonds.
The p-n one is already pinned to the δ de-wire by the exact
`d = -h(1/2 - δ/4)` check above; the n-n `d` and the per-nucleon `a`, `b` are
open.


# 🛑 SECOND RETRACTION, same session: the δ de-wire does NOT move this witness either

The section above titled *"2. The p-n interface δ de-wire — 1.287106862×, atom
only. CONFIRMED EXACTLY."* is **wrong**, and so is the headline figure
`δ: -2.168 → +0.001376` in commit `36962ad1d7c`.

**The error.** I backed `d` out of the June bond ratio by subtracting **`z_D`**.
June was on **`z_C`**. Subtracting the wrong `z` produced `d_June = -0.2178`,
hence a spurious `δ_June = -2.168`.

Against each side's own `z`:

| bond | `d` now | `d` June | agree to |
|---|---|---|---:|
| p-p | 0 | 1.2e-8 (i.e. 0) | anchor floor |
| p-n | -0.10445825933572413 | -0.10445817736543710 | 7.9e-7 |
| n-n | -0.20906032198987946 | -0.20906030963839083 (= `-h`) | 5.9e-8 |

**All three `d` are unchanged.** And `(z_D + d)/(z_C + d)` with `d` held fixed
predicts every measured bond residual to **2e-7**. The δ implied by each side is
`0.0013757112` (today, `= flavor_split_leading(q)`) against `0.0013772796`
(June) — a 0.11 % gap, which is the q₀ anchor difference amplified through
`flavor_split_leading`, not a change in δ.

**Why the "2.9e-16" did not catch it.** That check was real and is still valid:
`d_now` matches `-h(1/2 - δ/4)` to 2.9e-16. But it is a check on **one side of a
comparison**, and I reported it as confirming the comparison. I never ran the
same check on the June side; I *inverted* it, with the wrong `z`.

## The corrected decomposition — and C→D is the WHOLE bond side

| component | factor | cause |
|---|---|---|
| intra-ordering | D 3.7848169, T 7.8681653, ³He 6.8906640, ⁴He 14.3248374 | owner ruling `qou-hu1f`, 2026-09-05 |
| **all three bonds** | `(z_D + d)/(z_C + d)`, `d` unchanged | **pure convention C→D** |
| per-nucleon free | proton 1.075521518, neutron 1.069874485 | **unidentified** |

So `qou-gjkv`'s "post-C-to-D" label is not merely right for this member —
**C→D accounts for the entire bond side of its motion.** My original flag on
that bean was wrong twice over: first in saying C→D was zero, then, after
correcting that, in still crediting the δ de-wire with a third of the story.

Two things now removed from the open list: the δ de-wire, and "the n-n bond's
non-`z` part" (there is none — `d_nn = -h`, unchanged). **What remains open is
exactly one thing: the two per-nucleon free factors.**

## The reusable lesson, since this is the second retraction in an hour

Both errors have the same shape. The first tested **one carrier** of a
convention (`y_lambda_at`) and reported on the convention. The second checked
**one side** of a two-sided comparison and reported on the comparison. In both
cases the check that was run was sound and the scope of the conclusion was not.


## The three interface shifts are DERIVED — and a sibling had them already

Corroboration arriving from two sides at once, 2026-09-13. Both change the
status of this bean's bond row from "measured" to "derived", and one of them
nearly had me re-derive something the corpus already holds.

**The three `d` I isolated by differencing June against a live run are exactly
the shift values `qbeta_bond_factors_derived_probe.py` derives by exact Laurent
expansion.** That probe's docstring enumerates four shifts — `0` (pure sigma),
`-h` (sigma inverse), `-h/2` (colour-BLIND crossing) and `-h(1/2 - delta/4)`
(colour-WEIGHTED p-n crossing, `delta = (q-1)^2(1 - q^-4)/3`) — and my three are
three of those four. Verified symbolically, not by eye:

    b_pn - z - [-h(1/2 - delta/4)]  ->  0      (sympy.simplify, exact)
    b_nn - z - [-h]                 ->  0

and numerically at the muon pin, against my isolated values, **2.73e-11** on
both `d_pn` and `d_nn` — my isolation's own floor, since it came out of a
3-month-old witness's digits. So the bond row of the decomposition table above
is not three empirical constants: it is `z` plus two derived interface letters.

**Two routes now reach `d_pp = 0` (i.e. `b_pp = z`) independently of each
other and of me.** Sibling session, commit `5f157941920`, bean `qou-gba1`:
`z` falls out of the Jones-Ocneanu stabilisation axiom
`tr_{n+1}(x.sigma_{n-1}) = z.tr_n(x)` applied to the Magnus Omega-2 pairing,
confirmed to a relative **4.4e-141** and *falsified* at `z = q` (49 %/69 % off)
and `z = 1` (38 %/54 %). Their `b_pp = 0.6126880371464652516` is at the proton
pin; my `r(3He)/r(D) = 0.61268805054558909984` is at the muon pin. Different
anchors, same constant.

## But `b_nn` is not a fourth constant either — it is `z` conjugated

The sibling probe's identity 2 reads `b_pp/b_nn - q^4 = 0` and calls `b_nn`
"the simplest of the five". Correct, and it understates what it found: that
`q^4` is **the bar involution**. New probe
[`qbeta_bond_bar_parity_probe.py`](../computations/qbeta/qbeta_bond_bar_parity_probe.py),
five identities each `sympy.simplify`ing to **exactly zero**:

| identity | reading |
|---|---|
| `b_nn - z\|_{q->1/q} = 0` | the n-n bond IS the bar conjugate of the p-p bond |
| `z - zbar - (q - q^-1) = 0` | their separation is exactly the Hecke parameter `h` |
| `b_pn - (z+zbar)/2 - h.delta/4 = 0` | the p-n bond is their MIDPOINT, colour-displaced |
| `z.zbar - 1/(q+q^-1)^2 = 0` | `sqrt(b_pp b_nn) = 1/(q+q^-1)`, bar-fixed |
| bar-odd part of `b_pn` = `-(q-1)^5(q+1)^3(q^2+1)/(24 q^5)` | fifth-order zero at `q = 1` |

So the bond side is **one** parameter, not three:

    b_pp = z                          b_nn = zbar              b_pn = (z+zbar)/2 + (delta/4) h

The two like-pair bonds are the bar-conjugate endpoints; the unlike-pair bond is
the bar-EVEN part of `z`, and it is the *only* one that breaks the bar symmetry
— by `h.delta/4 = 7.190e-05` absolute, **1.6415e-05** relative, at the proton
pin. Set the colour weighting to zero and the p-n bond is the exact midpoint.
Witness `computations/qbeta/qbeta-bond-bar-parity.witness.json`; the bar form
reproduces all three of the sibling's MEASURED literals to **1.24e-20**, i.e.
to every digit they carry.

**Scope, twice, because this bean is two retractions deep.** (i) These are
identities between *closed forms*, and the involution is `q -> q^-1` applied to
a rational function. Whether it is the Hecke bar involution acting on the
*Markov trace* — which would make the first row a statement about the braid
words rather than about their traces — is **not** established and needs the
trace's own bar-equivariance. (ii) They inherit the sibling probe's own frame
caveat (`qou-4383`): its `t_p`/`t_n` are GROUPED-era against canonical atom
witnesses. The bonds are *inter*-nucleon and `qou-hu1f` changed the *intra*-
nucleon word, so frame-independence is plausible — plausible, not measured, and
not measured here.

**Still exactly one thing open**, unchanged: the two per-nucleon free factors,
proton `1.075521518` and neutron `1.069874485`. Note these are June-vs-now
*ratios*, not traces — they are not `t_p`/`t_n` (grouped `1.14576`/`0.98774`)
and not the canonical borromean `0.62933`/`0.47513`. Both candidate causes
remain untested.

## Lesson, and it is the corpus-grep one

I had `d_pn = -h(1/2 - delta/4)` and `d_nn = -h` from witness differencing and
was about to call them unidentified constants. They are written out, in words,
in the docstring of a probe in `computations/qbeta/` — path 3 of the six-path
checklist, which I ran for `binding-single-pipeline-comparison` and not for the
shifts I had extracted from it.


---

# RETRACTION 3 — the two "unidentified" per-nucleon free factors do not exist. And with that, this bean CLOSES.

`1.075521518` (proton) and `1.069874485` (neutron), carried in the table above as
the last open item and named as such in the previous section's closing line, are
**an artefact of my own frame mismatch.** Measured directly — June witness on
disk against a live re-run of `binding_single_pipeline_comparison.py`, reading
the `tr_free` column rather than inferring it — the per-nucleon free ratio is

    proton   0.590749626        neutron   0.5146405906

and it is `qou-hu1f`, the same intra-ordering ruling as everything else. There is
no third component.

## What the two numbers actually were

Solving `tr_free = t_p^Z t_n^N` on each side (the column factorises exactly; D,
T and ³He determine it and ⁴He/⁶Li/⁷Li confirm):

| | proton | neutron | what it is |
|---|---|---|---|
| **June** | `1.065306865` | `0.9232333461` | the `chi-{proton,neutron}-h3-at-q0-50dps` witnesses, to every digit June records |
| **today** | `0.6293296323` | `0.4751333545` | the canonical **borromean** per-nucleon trace (`qou-hu1f`) |
| ratio | **0.590749626** | **0.5146405906** | |

My `1.0755` / `1.0699` are `t_p^grouped / chi_p` and `t_n^grouped / chi_n` — the
ratio you get if you take `qbeta_bond_factors_derived_probe`'s **GROUPED-era**
`t_p = 1.1457596924573008697` / `t_n = 0.98774368811580957163` as "today's"
value. They are `1.075521528` and `1.069874498` exactly; my isolated figures
agree to 9.6e-9 and 1.2e-8, which is the 6-significant-figure floor of the June
`tr_free` column they came out of. So they are a real ratio between two real
objects — just not the one I labelled them.

**That probe's own header names this trap**, `qou-4383`: *"The two nucleon traces
below are GROUPED-era ... the canonical intra-nucleon word has been `(σ₀σ₁⁻¹)³`
since the 2026-09-05 ruling"*, with the borromean values written out beside them.
I read that note this session, quoted it in the scope section of my own
`qbeta_bond_bar_parity_probe.py` docstring, and then used the grouped numbers
anyway.

## The closure, measured

`tr_atom(now)/tr_atom(June) = [free] x [bonds]` with two components and nothing
else, where free is `0.590749626^Z . 0.5146405906^N` (qou-hu1f) and the bonds are
`(z_D + d)/(z_C + d)` with `d` unchanged (pure convention C->D):

| atom | chain pp/pn/nn | predicted | measured | rel | record floor |
|---|---|---|---|---|---|
| D | 0/1/0 | 0.391311037 | 0.391310057 | 2.50e-06 | 1e-05 |
| T | 0/1/1 | 0.280039892 | 0.280039588 | 1.08e-06 | 1e-04 |
| ³He | 1/1/0 | 0.283651902 | 0.283649354 | 8.98e-06 | 1e-04 |
| ⁴He | 1/1/1 | 0.202994141 | 0.202987825 | 3.11e-05 | 1e-04 |
| ⁶Li | 2/1/2 | 0.105304010 | 0.105309847 | 5.54e-05 | 1e-02 |
| ⁷Li | 2/1/3 | 0.075360316 | 0.075177305 | 2.43e-03 | 1e-02 |

**Every residual is below its own recording floor**, so the reconstruction is
exact to the limit of what these witnesses hold. ⁷Li's 2.43e-03 is 44x the next
worst and is not a signal: its `tr_atom` is `0.002115` June / `0.000159` now —
four and three significant figures, floor 1e-02.

**Use CHAIN bond counts, not the witness's own `n_pp`/`n_pn`/`n_nn` columns.**
Those are the ALL-PAIRS counts, and with them the reconstruction fails by up to
**52x** at ⁷Li while still matching at D — the one atom where chain and all-pairs
coincide. The production word is a chain (`atom_braid_word_3A` lays `A-1`
interfaces in a line), ordered protons-then-neutrons: `Z-1` p-p, one p-n,
`N-1` n-n. A check that only looked at the deuteron would have passed.

## Candidate elimination, for the record

Four commits were listed as candidate causes of the "unidentified" factors. Two
were eliminated by reading their own diffs before this measurement made the
question moot, and both eliminations are reusable:

- **`1b4fd94da1d`** (2026-08-23, *"jones_wenzl_weight was not the Ocneanu
  weight"*) — its own commit message says *"Wrong formula on an unselected path,
  not wrong numbers in live output"*; every caller passes `normalized_plancherel`
  or `plancherel` explicitly. It moves nothing.
- **`efcaf79ed29`** (2026-08-08, *"the braid word was f64 at source"*) — it DID
  edit `chi-{proton,neutron}-h3-at-q0-50dps.witness.json`, which is exactly the
  June carrier, so it looked like the answer. Its effect on `tr_M_at_q0` is
  `1.06530614425444993892 -> 1.06530614425444997567`: **relative 3.4e-17**, seven
  orders too small.

## The shape, for the third time in one day

Retraction 1 tested one *carrier* of a convention and reported on the convention.
Retraction 2 checked one *side* of a two-sided comparison and reported on the
comparison. Retraction 3 took a value from one *frame* and used it as the other
frame's. All three: a sound measurement, a conclusion scoped wider than what was
measured. The common defence is cheap and I did not apply it — **name the object
each number belongs to before dividing two of them.**

## Status

`qou-5c64`'s decomposition is complete: **`qou-hu1f` on the free side, convention
C->D on the bonds, nothing else.** What remains is not analysis but a decision —
regenerating this witness, which is `qou-gjkv`'s arc and an owner call under the
2026-09-07 ASK-THE-OWNER directive. The 299-field float64 drain stays blocked
behind it. The re-run performed for this measurement was reverted
(`git checkout --`); nothing is committed against that witness.

## RESOLVED 2026-09-14 — the cause is a NAMED owner ruling, not unidentified import-cone drift. Abandon the formula hunt.

This bean's diagnosis ends with *'The factor 1.81362 is NOT identified … identifying
it would pin the exact upstream change and is the cheapest way to finish this
diagnosis.'* **There is a cheaper way, it is causal rather than numerological, and
it is decisive.**

### The structural fact the bean's table hides

Four of the six rows are **not computed** by this producer. Read
`binding_single_pipeline_comparison.py`:

- `_load_canonical_traces()` — D / T / ³He / ⁴He are **read from**
  `binding-canonical.witness.json`.
- `_transfer_traces()` — only ⁶Li / ⁷Li go through `tr_m_atom_zn` live.

So for four of the six rows, nothing in this producer's *code* cone had to change
at all. The **upstream witness file changed on disk**.

### It did, on a named commit, and it says why

`computations/binding-canonical.witness.json` now carries the 'live' values to
**32 significant figures**, matching every 6-dp figure in the table above:

    D    0.29901501718464007670216042677098
    T    0.14207205679730479747049860425505
    3He  0.18817864299948877926347903714586
    4He  0.08940998050193060038204756581988
    6Li  0.02673492685626311266387329365652     <- also in the file now
    7Li  0.01270265982811619876152488964415

Regenerated by **`1ed81a49db` (2026-09-06)**, whose subject and body state the
cause outright:

> regen(qou-hu1f): binding_canonical was still grouped — and its He-4 independently
> confirms the bridge
>
> These two witnesses were simply stale against the **2026-09-05 intra-ordering
> ruling** and moved when re-run.
>
> binding-canonical.witness.json — **grouped -> borromean** across the isotope chain

with its own before/after column (deuteron `tr_M_atom 0.57517224391777 ->
0.15196833920423`) matched to 7 digits against the ruling table.

### Primary artifacts

- **`qou-hu1f`** — the intra-nucleon ordering change in `atom_braid_word_3A`,
  **owner ruling 2026-09-05**.
- `docs/audits/2026-09-05-chi-caches-stale-to-the-intra-ordering-both-options.md`
  (bean `qou-92u9`) — the same class for the six chi caches, measured as
  *'not a drift: a different number'*.

### Corrections to this bean

1. **'Whatever changed is in or below `tr_m_atom_zn`'** is directionally right but
   not specific. The change is in its callee **`atom_braid_word_3A`**, and it is
   an **intra-nucleon ordering** change, not a `z` swap (R1) and not the p/n
   weighting (R3). The bean reads the N≠Z split as evidence for R3; it is the
   ordering, which is also per-nucleon and also asymmetric between p-rich and
   n-rich.
2. **The formula hunt should be abandoned, and not merely because it is now
   unnecessary.** `1.81362` is the ratio between the **superseded grouped** word
   and the current borromean one. A closed form for it would be identifying an
   artifact of a retired convention — and searching a space of substrate
   combinations for a target number is the selection-against-the-target shape the
   anti-fit directive names. **I did not find a closed form and am not looking for
   one.** The bean's own `(q²+1)/q² = 1.811654` at 0.11 % is excluded anyway: the
   committed witness carries only **6 decimals**, so the data supports ~1e-6 and
   0.11 % is three orders outside it.

### What this changes for the blocked regeneration

Item 1 of *'Why nothing was regenerated'* reads *'it turns a green record red'*.
**That understates it.** The committed record is green **on a word the owner
retired on 2026-09-05**. So the choice is not green-vs-honest-red; it is
retired-convention-green vs current-convention-red. Items 2 (consumer
`qlommel_delta_lambda_lin_vs_sym_ladder.py`) and 3 (`qou-gjkv`'s arc) stand
unchanged, and the ASK-THE-OWNER gate on regenerating someone else's artifact
still binds — **nothing was regenerated here.**

**Bean stays OPEN** on the regeneration decision. What is resolved is the cause.

### Not measured, offered

How many other committed witnesses are still on the grouped word is unknown to me;
`qou-92u9` sized it for the six chi caches only. That is a real question for
`qou-gjkv`'s sweep and would need a value-level discriminator, not a grep.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8280, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-13: "retract(qou-5c64): the two "unidentified" per-nucleon free factors do not exist — I used a GROUPED value as today's, and"). The work may be partly or fully done. Read the bean before you close it.

## 2026-11-21 — binding-hygiene drain (session https://claude.ai/code/session_01Qmmkt97hXiyVzatJQADqZY)

Premise check against `docs/coordination/owner-rulings.md` on main `2ae54ab40` (owner instruction 2026-11-21: no bean is worked on a superseded basis). **Superseded premise found:** this bean's numbers are computed on the pre-2026-11-15 interface letters of `atom_braid_word_3A`, which the γγ ruling superseded (`docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`; redo waits on the γγ-selected nucleon word, PR #7876). (The bean's own 2026-11-15 section already says so.) Not reworked: the regeneration it asks for would be on a superseded word. Recommend: mark superseded once the γγ word lands, and re-measure on that word.
