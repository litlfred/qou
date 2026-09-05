# Q_β: which functional evaluates Δ — the decision, with options, costs and downstream

`qou-99qc`. **This is a decision document, not a finding.** The findings are in
[`2026-08-26-qbeta-epsilon-is-inadmissible-under-convention-d.md`](2026-08-26-qbeta-epsilon-is-inadmissible-under-convention-d.md)
and [`2026-08-29-delta-fork-at-admissible-parameters.md`](2026-08-29-delta-fork-at-admissible-parameters.md);
what neither contains is an enumeration of what can be *done*, which is what
this adds. Nothing here is wired, no content block is edited, no `c_k` proposed.

---

## 1. The situation in six sentences

The framework publishes a closed form for the neutron β-decay Q-value:

    Q_β = m_e · |q₀² − 2q₀ − 1| · (q₀+1) / (2q₀³)  ≈ 0.784 MeV,  0.17 % from CODATA

Structurally that is `Q_β = |ε(Δ)| · E₀`, where `Δ = 𝓑_n − 𝓑_p` is a difference of
nucleon braid elements in `H₃(q)`, `E₀ = m_e/(q(q−1))` is a base energy, and `ε`
is a linear functional. **Two different functionals are written `ε` in the
corpus** — the *augmentation* `σ ↦ q` (an algebra map) and the *coordinate sum*
`net` (weight every basis element by 1, i.e. the Markov trace at parameter
`z = 1`). The owner ruling of 2026-08-15 made convention D canonical, and under
D the corpus's own GNS proof places the theory in the Temperley–Lieb quotient,
where a functional is only meaningful if it annihilates the discarded block.
**The augmentation does; the coordinate sum does not.** And the published closed
form is *exactly* the coordinate sum — measured, not inferred.

## 2. What is now settled (each measured, none assumed)

| # | fact | where |
|---|---|---|
| 1 | The published closed form solves to **`z = 1`** exactly over ℚ(q); the other branch is `z = h−1`. Neither is admissible. | `qbeta_published_form_is_the_inadmissible_z1_probe.py` (15/15) |
| 2 | Admissibility is one linear condition. Roots of the `(1³)` weight numerator: **`z = q`** (which *is* the augmentation) and **`z_D = q³/(q²+1)`**. `z = 1` is not one. | `ConventionDAdmissibleRoots.lean`, sorry-free |
| 3 | Admissible **traces** form a 2-dimensional space, and the two Markov points already **span** it. Relaxing "Markov trace" to "trace" adds no new direction. | `qbeta_admissible_functional_hierarchy_probe.py` (13/13) |
| 4 | Dropping the trace condition gives 5 of 6 dimensions — but a non-trace functional is not a Markov trace and carries no link invariant. | same |
| 5 | No convex or affine combination reproduces `net`: `rank{aug, tr_D, net} = 3`. | `qbeta_admissible_span_prune_probe.py` (8/8) |
| 6 | No parameter-free admissible **base** correction exists; the `√(1−h)` near-match is the forbidden `z = 1` returning in disguise. | `qbeta-d-frame-admissible-base-correction-search` |
| 7 | **Bracketing is not evidence** — *both* candidate elements bracket the measured value. | `2026-08-29-delta-fork…` |

### The grid, complete

`Δ_S` is the normal-form vector; `Δ_L` is the 11-crossing word difference.
`qou-avt5` established these are **different elements**, and the question of
which is the nucleon difference is *open and independent of this one*.

| | `z = 1` **(published, inadmissible)** | `z = q` (augmentation) | `z = z_D` (Markov, D) |
|---|---|---|---|
| **Δ_S** | **+0.168 %** | +12.470 % | −43.157 % |
| **Δ_L** | +24.776 % | +39.324 % | −15.451 % |

**Best admissible cell in the whole grid: +12.470 %.** Two orders of magnitude
worse than the inadmissible one.

### Two facts that should temper the reading

**The number is not a fit.** The ansatz appears in audit docs from **2026-05-01**;
convention D was ruled canonical on **2026-08-15**. The 0.17 % was produced ~3.5
months *before* the constraint that now excludes its functional. This is a
convention change invalidating a standing result — not a quantity tuned to an
anchor. *(Chronology from authored filename dates; `git log` dates are
rebase-rewritten in this repo and are not a valid signal.)*

**The premise is strong.** The GNS/TL embedding is registered as a
**proposition**, and its own status note reads *"Established, not conjectural —
this is the Jones–Wenzl subfactor construction."* It is textbook mathematics,
not a framework posit. Any option that attacks it is attacking standard theory.

---

## 3. The options

Seven, and they are not equally serious. Each is given the same frame.

### Option A — Keep the published value; disclose and reclassify it

**What it means.** Q_β's 0.17 % stays in print, relabelled as a **pre-D,
convention-C-frame result**, conditional and awaiting re-derivation — exactly
the treatment AGENTS.md already gives the `c_k` ladder (`qou-cds1`). It stops
being quoted as a live parameter-free prediction under the canonical convention.

**Cost.** Label edits at ~8 content blocks carrying the closed form, the
AGENTS.md cheat-sheet line, and the L2 dashboard row. No re-derivation, no
compute re-run, no number moves.

**Risk.** Low and reversible. The live risk is *presentational*: a reader who
skims sees "0.17 %" and infers a strength the framework does not currently
claim. Mitigated only if the label is applied at **every** site — and this
corpus's own history (the `4.66e6` and `963.6×` drains) says partial labelling
is the normal failure.

**Commits to.** Nothing. It keeps every other option open, including B, C and E.

### Option B — Adopt the augmentation (+12.470 %)

**What it means.** Declare `ε` = the augmentation. It is the unique multiplicative
admissible functional — genuinely canonical, not a choice.

**Cost.** The `c_k` ladder is re-derived from a new base (`c₃` is *extracted*
from `Q_β^exp` relative to the base, so it moves), `q*` in `rem-qstar` moves with
it, and the L2 dashboard Q_β row is rewritten. Several content blocks change
their headline number from 0.17 % to 12.5 %.

**Risk.** Presenting a **12.5 % miss** as the framework's decay-sector
prediction is a materially weaker public claim than the current one, and it is
not obviously more honest — it swaps "right number, wrong functional" for "wrong
number, right functional".

**Commits to.** The claim that the decay Q-value *is* the augmentation of Δ,
which nothing independently supports beyond admissibility.

### Option C — Adopt the Markov trace at `z_D` (−43.157 %)

**What it means.** Declare `ε` = `tr_M` at the canonical convention-D parameter.
This is the option most continuous with the mass channel, which uses `tr_M`.

**Cost.** Same as B.

**Risk.** A **−43 % miss**. On Δ_S this is the worst admissible cell in the grid.
It is defensible only as "the mass channel's functional, applied uniformly", and
that uniformity is itself contradicted by
`decayLadder_zC_threeRow_ne_zero`, which makes the C-frame ladder and the mass
channel's three-row forcing mutually exclusive.

**Commits to.** Uniformity of functional across mass and decay channels — a
substantive physical claim, currently unargued.

### Option D — Deny that the decay channel lives in the TL quotient

**What it means.** Accept the GNS embedding but argue it constrains the *mass*
channel only, leaving the decay channel in full `H₃(q)` where any functional is
available.

**Cost.** An argument, not a computation.

**Risk.** **This is the option I would expect a referee to attack first.** The
quotient is by the radical of the trace form; if the decay channel is not in the
quotient, the framework owes an account of what space it *is* in and why the
same `q₀`, the same `H₃(q)` and the same braid elements appear in both. And the
gain is smaller than it looks — see §4.

**Commits to.** A two-space framework, with a stated boundary between them.

### Option E — Derive a different element Δ

**What it means.** Keep an admissible functional and find the element it should
act on. This is the route `qou-99qc` names as honest option (ii).

**Cost.** Real research. Unbounded.

**Risk.** None to the corpus — it is additive. The risk is that it does not
close.

**Commits to.** Nothing, and it is the only option that could produce a
*parameter-free admissible* sub-1 % result rather than choosing between existing
misses.

### Option F — Retract Q_β as a prediction

**What it means.** Move Q_β to "not currently derived under the canonical
convention", as the absolute-mass targets were moved by the 2026-08-11 excision.

**Cost.** Same label surface as A, plus removing it from the L2 scoreable set
(taking the count from 1/5 scoreable to 1/4).

**Risk.** Discards a result that may be recoverable by E or by the `qou-cds1`
re-derivation. Precedent exists (the absolute-mass excision) but that ruling
rested on a *structural* argument — double-counting the calibration — which has
no analogue here.

**Commits to.** Reopening it later would be a reversal.

### Option G — Use a non-trace admissible functional

**What it means.** Exploit the 5-of-6 dimensions available once the trace
condition is dropped.

**Cost.** Low to compute.

**Risk.** **Fatal, and it should be struck rather than weighed.** Without the
trace property the value depends on the *braid word*, not the link — so
`Δ_S` vs `Δ_L` would no longer be a question about which element is right but a
permanent ambiguity. A 5-dimensional space with one anchor is also a 4-parameter
fit. Listed for completeness only.

---

## 4. Downstream impact — the thing that makes this smaller than it sounds

**No calibration moves under any option.** AGENTS.md is explicit: *"Q_β
reproduced from q₀ is a 0.17 % **cross-check**, not a fourth input."* CAL-2 is
`𝔇_β`, pinned numerically through `m_μ/m_e` in the ideal layer and `m_p/m_e` in
the canonical experimental layer. **q₀ does not move. m_e, m_π, the mass channel
and the binding channel are all untouched.**

What *does* depend on the choice:

| consumer | affected by | note |
|---|---|---|
| `c_k` ladder (`c₃` onward) | B, C, E | `c₃` is extracted relative to the base, so a new base moves it. **Already C-conditional and awaiting re-derivation** (`qou-cds1`) — so this cost is largely pre-paid. |
| `q*`, `rem-qstar` | B, C, E | root-found on `S(q) = c₃(q) + Vol(4₁)`; moves with `c₃`. Already flagged as **(H1)-conditional**. |
| L2 dashboard Q_β row | all | currently 1279 ppb / 164× at the deepest *derived* rung. |
| ~8 content blocks + AGENTS.md cheat sheet | all | label or number edits. |

**And one hope that is already dead.** It would be convenient if passing to the
TL quotient collapsed `Δ_S` and `Δ_L` into one class, settling the element
question for free. It does not: the augmentation is admissible and gives
**+12.470 %** on `Δ_S` against **+39.324 %** on `Δ_L`, so an admissible
functional distinguishes them. **The functional question and the element
question are independent** — settling either leaves the other open.

---

## 5. Recommendation

**Option A, and it is my judgement rather than a finding.**

Three reasons, in order of weight:

1. **The number is not a fit, and A is the only option that says so accurately.**
   It predates the constraint that excludes it by three and a half months. B and
   C both replace a correct-but-inadmissible number with an admissible-but-wrong
   one, which trades a precise defect for a vague one.
2. **The blast radius is near zero** — Q_β is a cross-check, not an input — so
   there is no forcing reason to decide now, and A is the only option that
   preserves every other.
3. **The corpus already has this exact pattern and it works.** The `c_k` ladder
   is labelled C-conditional and queued for re-derivation rather than deleted or
   restated. Q_β sits in the same frame, for the same reason, and should get the
   same treatment.

**What I would not do:** adopt B or C. Publishing a 12 % or 43 % miss as *the*
decay-sector prediction is a weaker and less informative claim than "a standing
result in a superseded frame, re-derivation queued".

**Where the real work is:** Option E — derive the element — and the `qou-cds1`
convention-D re-derivation. Those are the only routes to a *parameter-free
admissible* result. Everything else redistributes an existing miss.

**If nothing is decided:** the current state persists — the published 0.17 %
keeps being read as a live prediction, the inadmissibility stays recorded only
in audit docs and a bean body, and the next agent re-derives it. That has
already happened once (PR #5893 independently re-encountered the functional
mismatch this bean had diagnosed). **The default is not stable**, which is the
one argument for acting on A sooner rather than later.

## 6. 🟥 SUPERSEDED — the anti-fitting directive lands on §5, and I withdraw Option A

**Added the same day this document was written, by its author.** `AGENTS.md`
gained **§NO FITTING, EXCEPT CAL-1/2/3 (owner directive, 2026-09-05)** on `main`
in `af1368d43ed`, after §5 above was drafted and while this branch was open.
**§5's recommendation does not survive it.** §§1–4 are untouched — every
measurement there stands, and §3's option inventory is still the right map.

### Which clauses collide

Two of the directive's clauses hit §5 directly.

> **Selection against the target.** Choosing an *object* — a knot from a
> census, a partition, a truncation order, **a branch** — because the choice
> reproduces the measured value. No continuous parameter is tuned and it is
> still a fit.

> **Accuracy is not evidence of correctness here, and a more accurate fitted
> route is worth LESS than a less accurate derived one.** … Corollary: **do not
> recommend consolidating onto the most accurate route.**

`z = 1` is a **branch** of the Markov family, selected from outside the
admissible set — its `χ_(1³)` coefficient `c(1) = q²(q−1)(q³−q²−1)/…` is
nonzero, so it does not annihilate the block the GNS/TL quotient kills — and its
entire case is that it lands at 0.17 %.

### What each §5 reason was, and what is left of it

1. **"The number is not a fit … it predates the constraint by three and a half
   months."** — **Withdrawn.** The directive does not ask whether the author was
   fitting *when the number was written*; it asks whether the route the paper
   publishes *today* derives or selects. Under convention D this one selects.
   Provenance is a fact about history, not a defence of a route.
2. **"B and C trade a precise defect for a vague one."** — **Inverted by the
   directive**, which ranks a less accurate derived route *above* a more
   accurate fitted one. B and C are the derived routes; that is the property
   that now decides, and the 12 % / 43 % misses are the honest output of it.
3. **"The blast radius is near zero, so there is no forcing reason to decide
   now."** — **Still true, and still the reason this is cheap.** It is an
   argument for deferring, never an argument for A.

The line **"What I would not do: adopt B or C"** is the specific sentence the
directive's corollary forbids, and it is retracted.

### What the directive decides, and what it leaves open

It **eliminates one option** and **forbids one method of choosing between the
rest**. It does not pick an answer.

| functional | `β` on the admissible line | Q_β | vs CODATA `0.7823334` MeV |
|---|---|---|---|
| `z = 1` — published (Option A) | *not on the line* | `0.7836458` | +0.168 % — **eliminated** |
| `z = q`, augmentation (Option B) | `0` | `0.8798906` | **+12.470 %** |
| `z_D = q³/(q²+1)`, convention-D Markov trace (Option C) | `q²/(q²+1)²` | `0.4447004` | **−43.157 %** |

Choosing B over C *because* 12 % beats 43 % would be the same defect one level
down, and is equally forbidden. The choice has to come from what `ε` **means**
in `Q_β = |ε(Δ)|·E₀` — the augmentation (an algebra map, `σ ↦ q`) or the
coordinate sum `net`/`epsNPq` — which is bean `qou-99qc`'s original question and
is untouched by the directive.

**Revised recommendation, marked as judgement rather than finding.** If `ε` is
the Markov trace in the canonical convention, the 2026-08-15 ruling names `z_D`
and the answer is **Option C, −43.157 %**. If `ε` is the augmentation, it is
**Option B, +12.470 %**. Nothing measured distinguishes them; I do not have a
derived basis for preferring one, and picking by residual is precisely what is
banned. **Options D, E, F and G are unaffected**, and Option E — derive the
element — remains where a parameter-free admissible result would come from.

**If nothing is decided:** unchanged from §5, except that the default now also
leaves a published number the directive classifies as selected-against-target.
