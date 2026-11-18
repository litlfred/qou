---
# qou-9f4h
title: 'GAP: derive a structural per-partition truncation selector lambda -> k_lambda, or prove none exists (the rule in the compute is FITTED)'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T18:19:11Z
updated_at: 2026-10-11T07:50:29Z
parent: b9cj
---


Opened 2026-10-10 on owner instruction relayed from the project thread
("add bean to derive"). Evidence verified at source before writing this, not
transcribed from the relay.

## The gap

Derive a **structural** per-partition truncation selector `λ ↦ k_λ` for the
brane tower, or prove no such selector exists. This is the open part of
`conj:brane-tower-z-habiro`, and it is **not** closable by any rule selected
against the data.

## Why this is open rather than done: the rule in the compute is FITTED

The live catalogue uses *"`k_λ = 1` on one block, 2 elsewhere"*, published as a
"max-|μ| selector" that "closes all 3 atoms". All three parts of that are
wrong, and the primary source is the rule's own originating probe.

**Origin.** PR #639 cycle 5b, `probe_phiq_per_partition_klambda.py`. Read it
commit-pinned:

    git show 0763606e4f^:_deprecated/probes/probe_phiq_per_partition_klambda.py
    git show 0763606e4f^:_deprecated/probes/probe-phiq-per-partition-klambda.witness.json

🛑 **Cite the pinned form.** The `_deprecated/` tree is **no longer on `main`**
(removed 2026-10-10; it survives on branch `cat/cat-harness/fsh-guts`). A live
`_deprecated/...` path in a docstring or audit doc now resolves to nothing.

**1. It is a fit.** The probe's own docstring states the rule under test:

> *"Candidate rule under test: `k_λ = 1` if λ is the **maximum-|contrib|
> outlier** for the atom; `k_λ =` atom-uniform-`k` otherwise."*

Selection by maximum-|contrib| is selection of the Wedderburn block that
**dominates the quantity being reproduced**. AGENTS.md §"NO FITTING, EXCEPT
CAL-1/2/3": *"Selection against the target — choosing an object because the
choice reproduces the measured value — is a fit even though no continuous
parameter is tuned."*

**2. The "max-|μ|" label is wrong, and the probe's own data refutes it.** For
tritium the flipped block is **`[6, 3]`** (`/data/dominant_partitions/tritium/lambda`),
while the same probe's docstring puts T's `max|μ| = 8.23` at **`[4, 3, 1, 1]`**.
Two different partitions: the rule selected by *contribution* and was later
relabelled by *eigenvalue magnitude*. At one live site the relabel could not
even have been evaluated — `derived_chi_catalogue_build.py` hardcodes
`k_lambda=1` beside `mu_eigenvalues=["?", "?"]`.

**3. "Closes" meant `|tower| < 2` and was never compared to AME.** The probe's
closure print reads *"atoms collapse to small-magnitude towers (|tower| < 2)"*.
It records `ame_MeV` beside each atom and does not test against it. Recomputed
from its committed witness:

| atom | flipped block | tower (fitted) | AME `B` (MeV) | miss |
|---|---|---:|---:|---:|
| deuteron | `[2,2,1,1]` | 0.8764 | 2.2246 | **−60.6 %** |
| tritium | `[6,3]` | 1.9370 | 8.4818 | **−77.2 %** |
| ³He | `[5,4]` | 1.0659 | 7.7181 | **−86.2 %** |

The criterion is satisfied by driving the tower **toward zero**, while the AME
bindings are 2.22 / 8.48 / 7.72 — so the closure test is **anti-correlated**
with the data it was taken to close.

## What has already been ruled out

From `docs/coordination/2026-05-10-non-calibrated-q-beta-mass.md`, the PR #639
cycle ledger — six candidates are in the refuted table of
`docs/audits/2026-06-17-refuted-ansatz-lemmas.md` (scalar-eigenvalue family;
per-eigenvalue operator-valued at uniform `k`; Type-B fold; multiplicity-refined;
pair-knot product-volume; pair-knot Markov-trace), plus from the ledger:

- **LP cost argmax** — refuted (1/3)
- **SDP with diagonal Gram** — refuted (1/3)
- **Hoefsmit content-spread** — refuted
- **Type-B fold depth** — partial (2/3)

## The one route the May ledger never tested

**SDP with the full off-diagonal Gram.** Still recorded `UNTESTED | next probe`
in that ledger, five months on. It means computing Gram entries
`tr_M(b_i · b_j)` *across distinct Wedderburn blocks* via Hoefsmit matrix
products; the diagonal simplification is already refuted, so the off-diagonal
structure is where any remaining signal would be. The ledger's second surviving
route is a **Hoefsmit hook-content asymptotic along a reduced braid word**
(`(q, β)`-aware).

## 🛑 The constraint that makes this hard

**No selection against AME.** A selector chosen because it reproduces a binding
is the defect this bean exists to replace, not a solution to it. Per AGENTS.md
§NO FITTING, rank by derivational cleanliness first and treat accuracy as a
diagnostic: *"a more accurate fitted route is worth LESS than a less accurate
derived one."* A documented honest miss from a derived selector is the
deliverable; a better number from a chosen block is not.

Also note the **discrete-choice trap**: "it is only an integer per block, not a
continuous parameter" is explicitly named as fitting in the same section
("Sweeping a discrete parameter for accuracy"). One free choice per block is
`p(n)` free choices.

## Live state

`k_λ` is emitted by three witnesses and **read numerically by nothing** —
`derived-chi-catalogue`, `derived-chi-catalogue-sweep`, and
`delta-lambda-categorical-verification`. 🛑 **The third is a different object**:
a *jet-prolongation* order (that producer's own docstring, line 18), not a
truncation order. The shared name is a collision, not a third consumer. A
rename to `jet_order_k` was suggested but **not done** — it is a witness field,
so it is a schema change with its own blast radius, and it was offered as a
suggestion rather than an owner pick.

All three producers now label the field a fit in place, and the two documents
that published "closes" / "max-|μ|" are corrected (PR #7586).

## Status

**`todo`, and it stays `todo`.** Per AGENTS.md §13a — *"NEVER close a bean
whose subject is an open conjecture"* — recording that the current rule is a fit
is not deriving a selector. This closes only when a structural `λ ↦ k_λ` is
derived, or its non-existence is proved.

---

## 2026-10-11 — the May towers rest on HARDCODED inputs; the off-diagonal-Gram route is excluded in the block basis; my own table used |tower|

Findings relayed from a sibling session at ofri's request. **Separated below
into what I verified from the repo and what I am carrying on relay**, because
three of them bear on numbers this bean and PR #7586 already published.

### VERIFIED HERE, from the primary source

**1. My own table used `abs(total_tower)`, hiding a sign.** The witness's
signed `total_tower` for tritium is **−1.9370**, against an AME binding of
**+8.4818**. That is the **wrong sign**, not a "77.2 % shortfall" — a different
and worse statement. D (+0.8764) and ³He (+1.0659) are positive; only T flips.
This was my error, in the figures written into three producers and two docs.

**2. Three of the May probe's nine dominant-block entries were never
computed.** `DOMINANT_PARTITION` is a hand-written literal dict:

    "deuteron": {"lambda": [2,2,1,1], "contrib_k1": 0.0,    # negligible
                                      "contrib_k3": -65.0,  # approximate
    "tritium":  {"lambda": [6,3],     "contrib_k3": -27.0,  # approximate

**For deuteron this voids the result.** The rule sets `k_λ = 1` on the cut
block, so the tower is `non_dominant_sum + contrib_k1(cut)`, and the witness
records exactly `0.87640 + 0.00000 = 0.8764`. **The rule's entire effect on
deuteron was a literal `0.0` annotated "negligible".** The deuteron "closure"
is the non-dominant sum alone — it never measured the rule at all.

**3. Under convention D, deuteron's cut is provably a NO-OP** — and this needs
no compute. `[2,2,1,1]` has **four rows**, and
`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows` (sorry-free,
general `n`) gives `y_λ = 0` for every shape with a third row. So under the
canonical convention the block the rule flips for deuteron carries **zero
Ocneanu weight**, and changing its truncation order cannot move the tower. T
`[6,3]` and ³He `[5,4]` are two-row and survive. Structural, and independent of
every number below.

### RELAYED, arithmetically consistent, NOT recomputed here

Sibling session, 60 dps, two independent routes agreeing to 2e-58, rebuilt from
the braid word at `e2204a4a5d55` with Hoefsmit σ and Wenzl `y_λ`. Full report
cited as `/mnt/project-files/mass-endomorphism/klambda/recheck-tower-precision.md`
(not readable from this container).

- **May setup** (convention C, muon CODATA-2018): **D 0.2550**, **T −1.9719**,
  **³He 1.0656**; D's real `contrib_k1` = **−0.62148**, not 0.
- The uncomputed `k=3` entries: **D −32.94** (hardcoded −65), **T −23.50**
  (hardcoded −27).
- The PR #638 witness's `y_λ` are wrong by up to **1.15e-4** relative at `n = 9`.
- **Convention D at the proton pin**: **0.2222 / 2.8116 / −0.0098** — so
  **tritium fails `|tower| < 2`**, i.e. the closure criterion itself fails under
  the canonical convention.
- `argmax|μ|` differs from the cut block for **all three** atoms — D `[3,3]`,
  T `[3,3,3]`, ³He `[3,3,3]`. So the "max-|μ|" mislabel is broader than the
  one-atom discrepancy recorded above; the rule was max-|contrib| throughout.

**The one consistency check available to me without recomputing:**
`0.87640 + (−0.62148) = 0.25492` against the relayed `0.2550`. ✓

### 🛑 The route this bean named as the last untested one is now EXCLUDED — scope (b), in the block basis

This bean's §"The one route the May ledger never tested" named the **full
off-diagonal-Gram SDP**. Relayed exclusion, with its invariant named: the `e_λ`
are **central orthogonal idempotents**, so `tr_M(e_λ e_μ) = δ_λμ · tr_M(e_λ)`
and the Gram is **diagonal by construction** — measured max off-diagonal
`1.7e-52`. The LP then degenerates to "pick the cheapest block" and agrees with
the fitted rule **0 / 3**.

**But scope it, and do not over-read it.** That is an exclusion *in the block
basis*. The ledger's own phrasing is `tr_M(b_i · b_j)` over **braid-word**
elements `b_i`, which are not idempotents and whose Gram need not be diagonal.
So what is excluded is the idempotent/block-basis reading of that sentence, not
every reading of it. Per AGENTS.md §"Before declaring refuted", this is a
legitimate **(b)** for the stated basis and **not** a (b) for the route as the
ledger words it. Before calling the route dead, re-state it — and the sibling
route (Hoefsmit hook-content asymptotic along a reduced braid word) — in the
basis each is meant in.

### What this leaves

The ten refuted candidates stand. The seventh (the live fitted rule) is now
known to rest on invented inputs as well as on selection against the target, and
to be a no-op for deuteron under the canonical convention. The block-basis SDP
is excluded. **No derived selector exists, and the search space is smaller than
this bean recorded yesterday.**

The sibling session reports it is now (a) re-running on the current braid word
under convention D and (b) **pre-registering q-only truncation rules before
scoring them** — which is the right shape under §NO FITTING, since
pre-registration is what makes a rule a prediction rather than a selection.

**Still `todo`.** Nothing here derives a selector; most of it narrows the space
and corrects the record.

---

## 2026-10-11 (later) — the CURRENT word fails both May claims, and the obstruction may not be the selector at all

Relayed from the sibling session at ofri's request. Their compute is marked
relayed; the corroboration below is **verified here from the May probe's own
source**, and it sharpens the account of the mislabel.

### RELAYED — the current production word, convention D, proton pin, 60 dps

`atom_braid_word_3A`, borromean intra order (`7db032fb48`), colour-weighted p-n
letter; cross-checks agreeing to ≤ 1e-52. Report cited as
`/mnt/project-files/mass-endomorphism/klambda/current-word-D/current-word-D.md`
(not readable from this container).

| atom | k=1 | k=2 | k=3 | fitted |
|---|---:|---:|---:|---:|
| D | 0.451 | 181.2 | 1281 | **10.29** |
| T | 3.689 | 161.4 | 1621 | **31.85** |
| ³He | 1.505 | 24.76 | 41.31 | **2.53** |

**Neither May claim survives on this word.** The cut block is not `argmax|μ|`
for D or ³He, and **all three fitted towers fail `|tower| < 2`** — by 5×, 16×
and 1.3×. So the rule does not even reproduce its own recorded verdict once the
word and the convention are brought current.

**7 of the 14 live blocks have an eigenvalue within 0.007 of a Φ_q pole**
(corrected from 8 — see the 06:39Z relay below; the May word is not pole-free
either, it has 1)
`μ = q^j`, by `min_j |1 − q^{−j} μ|`; the closest is T `(7,2)` at **8.9e-4**.
Near-pole amplification is roughly **1000×**.

### VERIFIED HERE — the May probe already named this mechanism, and the "max-|μ|" label was a FALSE POST-HOC OBSERVATION inside it

Three quotes from
`0763606e4f^:_deprecated/probes/probe_phiq_per_partition_klambda.py`:

1. **Line 35-39** — ³He's cut block `[5,4]` is *"structurally over-twisted — the
   partition [5,4] … carries the dominant **near-pole** multiplicity that broke
   the 2-input rules"*.
2. **Lines 210, 251** — `m_near_pole` was already one of the **2-input rule
   parameters that failed** at uniform `k`.
3. **Line 255, and this is the one that matters** — *"Numerical signal: outlier
   partitions are the **max-|μ|** ones in `ρ_λ(β_atom)`."*

**So the origin of the "max-|μ|" label is quote 3: a post-hoc numerical
*observation* about the outliers, not the selection rule.** The rule selected by
max-|contrib| (its own "Candidate rule under test"); the probe then remarked
that the outliers "are the max-|μ| ones"; and that remark was promoted into the
rule's identity downstream, where it reached the catalogue as *"1 iff λ is the
max-|μ| partition"*.

**And the observation is false.** Measured (relayed, float64 data): `argmax|μ|`
differs from the cut block for **all three** atoms — D `[3,3]`, T `[3,3,3]`,
³He `[3,3,3]`. So the mislabel is not a careless rename between files; it is a
**wrong claim inside the probe** that nothing re-derived. That is the same class
as everything else in this arc: a conclusion written into prose where no
consumer re-checks it.

### What the near-pole finding suggests, and how to hold it

Quotes 1-2 show the May probe had near-pole structure for **one** block and used
`m_near_pole` as a failed scalar input. The relayed measurement puts **7 of 14** (corrected from 8)
blocks near a pole, with ~1000× amplification. If that holds up, **the
obstruction is not the choice of truncation order at all** — it is that `Φ_q` is
being evaluated close to its own poles, where any truncation is
ill-conditioned and a one-block integer flip is the wrong instrument.

🛑 **Hold this as a hypothesis, not a finding.** Scope (a) at best: it says this
*construction* is ill-conditioned on this word, and no invariant is yet named
that would make it scope (b). The sibling reports two open threads that would
decide it — whether the pole proximity is **structural or accidental**, and
**which of the two word changes causes it** — plus the **pre-registered q-only
rules**. Pre-registration is the right shape under §NO FITTING: it makes a rule
a prediction rather than a selection.

**Do not re-derive their numbers from this bean.** Nothing here is independently
recomputed; the three source quotes are.

**Still `todo`.** This removes a candidate and proposes a mechanism. It derives
no selector.

---

## 2026-10-11 (06:39Z + 06:41Z relays) — the pole proximity is ACCIDENTAL, and all 7 pre-registered q-only rules FAIL

Two relays from the sibling session, recorded at ofri's request. The second
contains the finding that reframes this whole arc, so read §Finding 1 first if
reading only one thing. **Verified-here items are marked; everything else is
their compute, labelled relayed.**

### Correction to the figure I published: 7 of 14, not 8 — and the May word was not pole-free

Corrected above in place. The report's own §3 tables list **seven** blocks below
0.007. And the May word has **1** near-pole — its ³He `(5,4)` block sits at
**0.00197** (`j = 2`) — so the contrast is **1 → 7**, not *none → 8*.

### CAUSE — isolated with the producer's own kwargs, and it is an owner-ruled correctness fix

🔎 **Verified here.** `computations/mass_at_3A_proper.py:456`
`atom_braid_word_3A` does take exactly the two parameters needed to separate the
changes — `intra_order: str = "borromean"` and
`pn_convention: str = "bring_color_weighted"` — so the split is done with the
producer's own switches, not a reconstruction. Relayed: May = `grouped` +
`strict_averaged`, matching the `e2204a4a5d55` word to **9.7e-62**.

**The `intra_order` change alone (grouped → borromean) produces the current
spectra and all 7 near-poles.** The colour-weighted p-n letter alone shifts pole
distances by **≤ 8 %**.

🛑 **WHY IT IS NOT A FIT — and "the owner ruled it" is NOT the reason.** My
earlier wording here cited the 2026-09-05 owner ruling (`qou-hu1f`) as the
reason the change was not selection against data. **That is not evidence**, and
it is withdrawn as the argument. The actual evidence is a measurement in the
*preceding* commit, and it is far stronger.

🔎 **Verified verbatim in `82860c4f317` (2026-09-05).** That commit measured the
borromean word and found it makes agreement **WORSE**:

> *"the two-level character ratio telescopes to `tr_M(W_atom)`, giving **2H
> +254.53 %**, 3H +74.49 %, 3He +53.87 %, 4He −33.60 %. It does not work, and is
> **worse than the grouped word** below A = 4. Recorded as the answer, not
> repaired — **the grouped column's +4.07 % at 2H is agreement produced by a
> word that is not β_Bor.**"*

**The change was adopted while the measurement said it made the numbers worse,
and the commit says so in those words.** A fit would have gone the other way —
it would have kept the +4.07 %. That sentence is itself a textbook anti-fit
statement: it rejects the better-agreeing word *because the agreement came from
the wrong object*. **That** is why `7db032fb48` is not a fit.

**Two things this does NOT establish, and they were conflated in my earlier
wording.** The `5e-60` Lean match shows only that the code now equals the Lean
**definition** of `β_Bor`; it does **not** show that `β_Bor` is the right
nucleon word. And whether *"nucleon = Borromean word `(σ₀σ₁⁻¹)³`"* is itself
**derived or chosen is UNVERIFIED** — record it as open, not settled. The
ordering of events was: measurement (`82860c4f317`), then the ruling, then the
change (`7db032fb48`), with the commit noting the edit touched 685 call sites.

### ACCIDENTAL, NOT STRUCTURAL — this retracts the hypothesis I recorded above

My 06:29Z append said *"the obstruction is not the choice of truncation order at
all — `Φ_q` is being evaluated close to its own poles, where any truncation is
ill-conditioned."* **Withdrawn as a mechanism.** Relayed, holding for all 10
`(eigenvalue, j)` pairs with `d < 0.01` on the current word, where
`d(q) = |1 − q^{−j}μ(q)|`:

- `d(q)` **drifts smoothly** when the word is rebuilt at each `q`.
- Each crossing is a **simple zero away from `q₀`**: `q*/q₀ − 1 ∈
  [−8.3e-3, +1.6e-2]`; closest is T `(7,2)` `j=2` at **−1.340e-3**.
- **`μ ≠ c·q^j`**: `dlog μ / dlog q` runs **1.40–3.94**, so the eigenvalues are
  not tracking the pole locus.
- `|μ/q^j| − 1 ~ 1e-3`, **not ~1e-60** — i.e. near, not on.
- Proton → muon pin changes `d` by **≤ 8.8e-6** relative, so it is not an
  artefact of the anchor either.
- Only `k = 1` towers are stable: **0.45 / 3.69 / 1.51**.

**Unresolved in their own report:** the ³He `(6,3)` `j=2` crossing (the secant
did not converge), and poles with `j ≥ 4`. 🔎 That last one is real and I
checked it: at the proton pin `q⁴ = 1.517953`, against D `(4,2)`'s quoted
`max|μ| = 1.514` — a gap of **0.0040**, so `j ≥ 4` poles are genuinely in range
and the sweep is incomplete there.

### The 7 PRE-REGISTERED q-only rules: ALL FAIL, on both words, under both unit maps

**The discipline here is right and should be the template.** `PREREGISTRATION.md`
sha256 `3d3f628a2318b0c4790bedc785d4fea3f74e33d73b211f581db01c69d9cbd832`,
frozen **2026-10-11T05:41:29Z, before any tower was computed**. That is what
makes these predictions rather than selections, per §NO FITTING.

Rules: **R1a/b/c** pole index `⌊log_q max|μ|⌋` (per block / per eigenvalue /
ceiling); **R2** cyclotomic termination; **R3** Garoufalidis–Zagier optimal
truncation; **R3′** smallest-term truncation; **R4** a Habiro-degree bound —
flagged by its author as **the agent's own construction, because the corpus
defines no Habiro selector**.

🔎 **The criterion is the conjecture's own, verified verbatim** at
`folio/quantum-observable-universe/mass-theory/brane-tower-z-habiro.md` §52-60:
compare with AME `{2.224566, 8.481798, 7.71806}` MeV, and *"A candidate rule
closing all three to within ∼5 % **without per-atom retuning** constitutes the
empirical signature."* The anti-fit clause is in the conjecture itself.

**Result: all 7 rules fail on all 3 atoms**, on the current and May words, under
both unit maps (M1 = tower as MeV; M2 = `m_e`·tower). The uniform `k = 1/2/3`
baselines and the fitted May rule fail too. **Best cell anywhere: 26 %** (M2,
³He, `k=2`, May word) against a 5 % target. Each failure is **scope (a)** for
that rule alone.

### 🛑 Finding 1 — truncation is cutting a CONVERGENT product, and this is the finding

`Φ_q^{[≤k]}(μ) = Π_{j≤k}(1 − q^{−j}μ)^{−1}` **converges** at `q₀ > 1`. 🔎
Verified here, and it is elementary: `q > 1` ⇒ `q^{−j} → 0` geometrically ⇒ the
factors → 1 and `Σ|q^{−j}μ| < ∞`, so the product converges absolutely. Relayed:
the **untruncated** tower is `~1e8–1e9` for every atom.

**So the truncation order is not regularising a divergence — it is cutting a
convergent product short.** Every q-intrinsic rule picks `k_λ = 2…22` and lands
at `1e2–1e9`; **only `k ≈ 1` gives an O(1) tower.**

**Why that is decisive under §NO FITTING, and it is the sharpest thing in this
bean:** if no rule derivable from `q` reaches `k ≈ 1`, and only `k ≈ 1` produces
a number of the right order, then *"the right `k`"* is **not a function of the
mathematics** — it is whatever makes the output small. That is selection against
the target **by construction**, and it explains why every candidate for five
months has been a fit rather than a derivation. The failure is not that the
right invariant has not been found yet; it is that the quantity being chosen is
fixed by the answer.

### Finding 2 — a GAP IN THE CONJECTURE'S OWN STATEMENT

**R2 cannot fire at all**: `q₀` is not a root of unity, and no eigenvalue sits
*on* a pole. More than that — `Φ_q` is **not a class in any `R/(P_k)`**, since
`P_∞ ≡ 0` there. So the conjecture's *"cyclotomic projection evaluated at
`z = μ`"* is **undefined at generic eigenvalues without an extra choice**. That
is a defect in the statement, not in a candidate rule, and it belongs on
`conj:brane-tower-z-habiro` rather than here.

### Unsettled, and stated as such

- **The conjecture never specifies the dimensionless → MeV map.** M1 vs M2 is
  the agent's choice, so every MeV comparison above inherits an unstated
  convention. This should be pinned before any further scoring.
- The **`n⋆` claim** in the conjecture **gets no support** from any of this.
- The **Cauchy-limit claim is untouched** — not tested, not refuted.

**Still `todo`.** Five months of candidates, ten refuted ansätze, one fitted
rule now known to rest on invented inputs, a block-basis SDP exclusion, and
seven pre-registered q-only rules all failing. What this arc has produced is a
well-documented negative and one structural reason to expect it (Finding 1). It
has not produced a selector.

### Cross-reference (2026-10-11)

The two **statement** defects — the undefined cyclotomic projection and the
unspecified dimensionless → MeV map — are split out to **`qou-f1wk`**, since
they are defects in `conj:brane-tower-z-habiro` rather than in any candidate
rule. The content block is **not** edited; both are owner decisions.

### Cross-link (2026-10-11)

same defect class one file over: `closed_form_tau_M.py:79` restates a conditional's antecedent as settled ("IS derived"), as the May k_λ probe did with its own "max-|μ|" remark. Record: [`2026-10-11-atom-word-provenance.md`](../../docs/audits/2026-10-11-atom-word-provenance.md).

## Round 74 Progress (PR #8509)
- De-vacuified and proved genuine Lean 4.24.0 theorems in PR `litlfred/qou#8509` (C1 `ffa6f4009ea1d8bfb9fcdb4c0721e486e42a5dca`, C2 `521dae553af743d7b8435ff34bef6f8099a8afcf`, 80-dps mpmath witness verified, 0 static audit findings).
