---
# qou-i229
title: 'AUDIT: 35 published figures have no computational provenance anywhere in the repo'
status: todo
type: task
created_at: 2026-09-05T12:58:18Z
updated_at: 2026-09-05T12:58:18Z
---


Opened 2026-09-05 from `qou-qnqf`. Tool:
`scripts/unsourced-published-figures.py` (selftested, wired into nothing).

## Where this came from

`thm:markov-trace-factorization` published a transfer-matrix readout copied from
**deprecated** code — wrong on every bond — while a merged probe had already
recorded that exact readout as a trap. A defect can sit in a content block while
the correction sits in a probe. That prompted two mechanical questions.

## Question 1: deprecated provenance — answered NO, and the zero is real

**653 decimals live only in `computations/_deprecated/` and never in live code.
None of them reaches `content/`.** So no published figure has deprecated-only
numeric provenance. The readout defect was a *formula*, not a number, which is
why this test does not catch it — worth stating so nobody reads the zero as
covering the class it came from.

The detector selftests against an injected known positive and a fabricated
negative, per `qou-5pgl`: a detector without a known positive can report a whole
class clean, and this one would otherwise have reported exactly that.

## Question 2: no provenance at all — 35 of 333

**ROUNDING IS THE WHOLE DIFFICULTY, and getting it wrong inflates this 4x.**
Exact string matching reports 132; most are false, because a figure published at
one precision and computed at another does not string-match —
`0.00155060213`, `0.00155060`, `0.0015506` are three roundings of one quantity.
Allowing a source value to round to the published figure at its own decimal count
takes 132 → 35.

## THIS IS A CANDIDATE LIST, NOT A DEFECT LIST

The first candidate spot-checked is a **false positive, and correctly so**:
`0.00137748` in `flavor-split-habiro-derivation` is
`Δ_target = (m_n − m_p)/((m_p+m_n)/2)`, the experimental mass split from CODATA
masses. It is not computed anywhere because it should not be. Expect the same of
other AME/CODATA inputs and of values quoted from cited work. **Deciding any
entry needs a human reading its block; do not sweep off this list.**

Heaviest concentrations, as a starting point rather than a verdict:

    q-beta-spectral-bridge-table-data.md        4
    witness-substitution-audit.ts               2
    substrate-consistency-window-table1-data    2   (1.11023043771 / …782 — q-like
                                                     but NOT q0 = 1.10997858…)

The `substrate-consistency-window` pair is the one I would look at first: two
values differing in the 11th digit, both close to but distinct from `q0`, in a
table whose name says it is about the substrate window.

## One entry was mine, and fixing it is the worked example

`1.064088425325` was flagged — my own figure, published in the
`markov-trace-factorization` correction table earlier the same day, printed by a
probe but never recorded in its witness. Adding it and its two siblings to
`no_within_generator_noncommutativity_probe`'s witness took the count 36 → 35.
That is the shape of the fix where the fix is warranted: **witness the figure, do
not delete it.**

- [ ] Triage the 35. Per candidate: read the block, decide input vs computed vs
      stale, and either cite the source, witness the producer, or correct.
- [ ] Consider whether the tool should become a gate once the list is drained.
      It should NOT while the list stands — a gate red at 35 on arrival, with a
      known false-positive class in it, is one nobody can adopt.

## TRIAGE ROUND 1 (2026-09-05): 35 -> 32, and category (b) EXISTS after all

Two entries closed and a real defect found. Probes:
`substrate_consistency_window_q_from_alpha_em_probe.py` (3/3),
`published_figures_carry_a_retired_q0_probe.py` (4/4).

### (c) correct but unwitnessed — CLOSED, worked example

`1.11023043771` / `1.11023043782` in `substrate-consistency-window-table1-data`.
Every `alpha_EM`-inversion module in the tree is deprecated and the block's `.ts`
cites nothing computational, so this looked like the stale case. It is not:
inverting the bare form `alpha^-1 = q[9]_q[10]_q` at 40 dps gives
`1.11023043770666` (CODATA 2018) and `1.11023043781657` (2022) — the published
figures are the correct roundings, and the quoted `1.1e-10` shift is right too.
**Correct, derived, merely unwitnessed.** Producer now recorded.

One overstatement corrected en route: the block called that shift "six orders of
magnitude below the ±0.00002"; it is `1.82e5`, i.e. **five**.

### (b) STALE — FOUND, and it is four figures across two blocks

I wrote "of which none has yet been found". Wrong within the hour.

    q0_retired = 1.1099785955541805752815940796095093779932822799587

lives in eight `computations/_deprecated/` witnesses and one deprecated script,
**nowhere live**, and is neither anchor — proton `1.10997858275…`, muon
`1.10997859564…` — sitting *between* them, which is why nothing looked wrong.

    block                                figure           published        retired q0 gives
    hecke-log-decomposition-table-data   1 + q_0          2.10997859556    2.10997859555418
    hecke-log-decomposition-table-data   log(1 + q_0)     0.74667780313    0.746677803149403
    hecke-log-decomposition-table-data   log(1/hbar_q)    2.31181024982    2.31181024984889
    em-coupling-bring-zero-mode          q[9]_q[10]_q     136.823219654    136.823219654561

`q[9]_q[10]_q` is decisive — the quantum integers amplify, so the retired value
matches 11 significant figures against muon's 9 and proton's 7. On all four the
retired value is closest **by relative error**.

**Not recomputed.** The proton/muon choice is owner-gated (`q_parameter.py`:
"genuinely MIXED", "a blanket flip is WRONG", "do NOT change this default").
Both live values are tabulated in the block caveats; the substitution waits for a
ruling.

### 🛑 THIS CORRECTS THE SWEEP'S OWN HEADLINE

The bean above reports "Question 1: deprecated provenance — answered **NO**".
That answer tested for the literal decimal **string**, and is true at that level.
It is **misleading as read**: a figure that is a *function* of a retired constant
inherits its provenance without ever carrying its digits. Four such figures were
sitting in the corpus while the sweep reported the class clean.

So the string-level test is much weaker than its phrasing suggested, and the
derived-level question is **open, not answered**. The method that works is the
one used here: take a published figure, guess the closed form from its own
caption, and solve for the `q0` that reproduces it.

- [ ] Run the derived-provenance test on the remaining 28. Cheap per figure where
      the caption gives the closed form (`1 + q_0`, `log(1/hbar_q)`, …), and most
      of them do.
- [ ] Owner ruling: which anchor do `hecke-log-decomposition-table-data` and
      `em-coupling-bring-zero-mode` take? Then substitute.

## TRIAGE ROUND 2 (same day): six figures, FOUR blocks — and a discrimination floor

Method: read each caption's own closed form and solve for the `q0` that
reproduces it. Two more confirmed, two more blocks.

    block                                  figure          published              retired matches
    q-beta-form-a-n1-symbolic-table-data   1 + hbar_q^2    1.009817188513479      15 sig figs
    q-beta-spectral-bridge-table-data      h^2             0.04370621823290131    10 sig figs

`1 + hbar_q^2` is the sharpest figure in the whole sweep — 15 significant figures
to the retired value, against muon's 10 and proton's 8. Running total: **six
figures, four blocks, one retired constant.**

### THE METHOD HAS A FLOOR, AND IT MUST BE QUOTED WITH THE RESULT

The muon and retired values differ by a relative `7.98e-11`, so a figure needs
about **12 significant digits** to separate them. Two flagged figures fall under
it:

    q^10 - q^-10              2.48662110   (9 digits)   INDETERMINATE
    h^2/[q dq(9) dq(10)]      7.30870098   (9 digits)   INDETERMINATE

These are **not clean** — the test has no resolving power there and says nothing.
Worth stating loudly because in a results table "no hit" and "no resolving power"
look identical, and reading the second as the first is how a sweep reports a
class clean.

### TWO CAPTIONS I READ WRONG, RECORDED SO THEY ARE NOT RE-GUESSED

Taking the captions literally, `ln(1 + z h)` and `1/z + (z-1)h/(2z)` reproduce
`0.09929139859972778` and `1.897907634269324` at **no anchor at all** — 0
significant figures everywhere, not a near miss. So either the caption is not the
whole computation or another input enters. That is a statement about my reading,
not about those figures' provenance, and it is deliberately not dressed up as
"indeterminate".

- [x] Run the derived-provenance test on the remaining figures — **done for
      every caption carrying an explicit `q0` closed form.**
- [ ] The rest need their producers identified rather than their captions read:
      `tr_M(deuteron, q_0) = 0.17743692421`, the Frobenius Gram eigenvalues, the
      `q-beta` bridge quantities above, `E_{0,N=1} = 4.22707538`.
- [ ] Owner ruling: which anchor do the **four** affected blocks take? Then
      substitute all six figures at once.

## ANCHOR ANALYSIS (2026-09-05): the question was mis-framed, and correcting it collapses most of it

Full write-up:
[`docs/audits/2026-09-05-anchor-choice-for-the-four-retired-q0-blocks.md`](../docs/audits/2026-09-05-anchor-choice-for-the-four-retired-q0-blocks.md).

**I called this an owner-gated proton-vs-muon decision. It is not.** The six
figures carry the **CODATA-2018 vintage of the MUON anchor** — the anchor the
two-layer convention already says canonical blocks should use. Verified by
inverting the CAL-2 pin `m_μ/m_e = Vol(4₁)/ℏ_q²`:

    m_mu/m_e = 206.7682830  (CODATA 2018)  ->  q0 = 1.1099785955541805753   <- published
    m_mu/m_e = 206.7682827  (CODATA 2022)  ->  q0 = 1.1099785956427390467   <- live muon

The first matches the published constant **to twenty digits**. So the choice is
which *vintage*, not which anchor.

### It is collateral of a known, already-fixed defect

`qou_substrate/codata.py`: `206.7682830` was carried under a "CODATA 2022"
comment **across 138 sites**, fixed 2026-08-15 by reading the NIST table instead
of transcribing it. **That fix reached `computations/` and `tools/` and not
`content/`.** Same shape as today's transfer-matrix readout: correction lands in
compute, block keeps the old value, nothing walks between them. The discrepancy
is `1.451 ppb` = `0.065σ` — physically nothing, which is why it survived.

### The corpus already rules on three of the four

`q0_anchor_manifest.json` tags **six of its nineteen `ideal_muon` producers as
`qbeta_*`**, and two of the four blocks are Q_β blocks. Sharper still: **Q_β *is*
the CAL-2 proxy**, and CAL-2 is what the muon pin pins — anchoring a Q_β table on
proton makes it a prediction from a prediction and folds in the μ–p tension.

### Magnitudes

`q0` moves `7.98e-11` refreshing the vintage, `1.15e-8` switching to proton —
**145× larger**. About 11 published digits survive the refresh; ~8 survive the
switch. Nothing physical moves either way.

### The one I would not decide alone

`em-coupling-bring-zero-mode` sits under `predicted-spectra/`, which the
two-layer rule reads as Physical-Observations → proton; but its quantity is
`q[9]_q[10]_q`, the *bare* coupling, a derivation input. Placement and content
point opposite ways and no manifest entry covers it. **Genuinely ambiguous — a
question about what that block is for.**

### Recommendation

Refresh the three canonical blocks to the current muon anchor; ask on
`em-coupling-bring-zero-mode`. Treating a data refresh as an occasion to
re-decide a convention is how conventions drift.

- [ ] Owner: confirm the refresh, and rule on `em-coupling-bring-zero-mode`.
- [ ] **Stale comment found en route**, not changed: `q_parameter.py` says the
      corpus is "genuinely MIXED (279 proton + 455 muon)"; the manifest now reads
      **906 proton / 19 muon / 15 ambiguous**. Misleading to anyone reasoning
      about balance from it. Left alone because that file is anchor-selection
      machinery under an explicit "do NOT change this default".
- [ ] **The real gap neither gate covers:** both defects found today are a
      correction landing in code while a block keeps the old value. Nothing walks
      that boundary. The unsourced-figure sweep found this one only because the
      figures had no provenance at all — a stale figure that still matches *some*
      producer stays invisible.

## COMMIT ARCHAEOLOGY (2026-09-05): the open question is closed, and I was wrong twice

Addendum in the same audit doc.

**1. `em-coupling-bring-zero-mode` was never ambiguous — the block says muon.**
Line 26: *"Evaluation at `q_0 = 1.109978595554181…` **(muon pin, 16 dps)**"*. I
called it "the one genuine ambiguity" by reasoning from its directory
(`predicted-spectra/` → physical → proton) without reading its own label.
Placement is a weaker signal than a declaration and I invoked the first without
checking the second.

`df13e845cee` (2026-08-21) put that label there and states the identification
independently: *"solving CAL-2 for CODATA-2018 `m_μ/m_e` gives
`1.1099785955541805753…` … **The defect was the label.**"* Digit-for-digit what I
re-derived — so the provenance finding is confirmed, not merely mine.

**2. "Refresh to the current muon anchor" presupposed an open ruling.**
`qou-po7i` catalogues **three** muon values:

    A canonical q-pinning  1.1099785955573347...  FROZEN
    B in the witnesses     1.1099785955541805...  the REVERTED derivation's value
    C q_muon_at() live     1.1099785956427390...  drifts with CODATA

The published figures carry **B**, and that bean closes with *"needs a ruling on
which of A and C a 'muon-anchored' quantity uses"*. My Option A quietly assumed
that ruling.

**It is now moot: A and C have converged.** Re-running
`muon_pin_three_values_probe.py` today gives `A == C == 1.1099785956427390466…`,
which is also what the canonical witness `q-pinning-50-digit.witness.json`
carries; B is `<not found>`. One live muon value, and B is the lone outlier at
`0.0798 ppb`. So Option A is unambiguous after all — refresh target
`1.1099785956427390466817951293`.

**Side effect, not fixed here:** that probe now FAILS (`allPassed: False`)
because it asserts a three-way split that no longer exists. The failure is how
the convergence surfaced, but a permanently-red probe decays into noise. It
belongs to `qou-po7i`.

**3. A figure in the record is mis-attributed.** `df13e845cee`, `qou-q0lp` and
`docs/audits/2026-06-24-q0-layer-migration-scope.md` all say the published value
"sits **0.0028 ppb** from the current muon pin and 11.53 ppb from the proton
pin". The proton figure is exactly right (I measure 11.53 independently). The
muon one is `B−A` — the gap to the **frozen** pin — while the gap to the current
pin is `C−B = 0.0798 ppb`, **28× larger**. The number is real; its attribution is
not. It matters mildly: that sentence is the stated justification for *labelling
rather than refreshing*, and it understates the gap it justifies by 28×.

### Revised recommendation

**Option A for all four blocks**, target `1.1099785956427390466817951293`.
Nothing physical moves; this is the 2026-08-15 CODATA fix reaching content.

- [ ] Owner: confirm. No ambiguity remains to rule on.
- [ ] `qou-po7i` owns re-pointing `muon_pin_three_values_probe.py` to the
      converged state.
- [ ] The `0.0028 ppb` attribution should be corrected where it is durable
      (`qou-q0lp`, the 2026-06-24 audit).

## REFRESH ATTEMPTED AND REVERTED (2026-09-05) — the unit is the block, not the figure

Acting on my own recommendation, I substituted the six figures at the converged
muon pin, then **reverted**. Addendum 2 in the audit doc.

**Why: each table carries `q₀`-derived SIBLINGS the sweep never flagged**, because
the sweep only looks for figures with *no provenance* and these have some:

    block                      flagged figure        un-flagged sibling      sibling pin
    hecke-log-decomposition    1+q0, log(1+q0), …    hbar_q, h               B
    q-beta-form-a-n1           1 + hbar_q^2          hbar_q 0.099081726435699 B
    q-beta-spectral-bridge     h^2                   h 0.2090603219955937    A

Refreshing only the flagged ones leaves `1 + ℏ_q²` at the new pin beside an `ℏ_q`
at the old one **in the same table** — worse than the stale value, because the
reader can no longer recompute one column from another.

### NEW DEFECT: `q-beta-spectral-bridge` was already internally inconsistent

    prose q_0   1.109978595557335   = pin A exactly
    h           0.2090603219955937  = pin A
    h^2         0.04370621823290131 = pin B

**Its `h` and `h²` are at different `q₀`.** `h² ≠ (h)²` as published; the table
does not close on itself, and that predates today. Refreshing `h²` alone would
have made it three-way mixed, which is how I found it.

This also revises "all six figures carry B": five do, but this block's prose pin
and `h` carry **A** while its `h²` carries **B** — it straddles two muon vintages
internally.

### And the pin string is stale in six MORE blocks

`1.109978595554181` also appears in `delta-skein-substrate-identity`,
`knot-particle-dictionary`, `g-q-closed-form`, `flavor-split-substrate-proof`,
`physics-names-knot-operations`, `particle-nf-table` — residue of
`df13e845cee`'s labelling pass, which labelled 22 sites and refreshed none.
**Not touched**: their siblings are at the old pin, so changing the quoted pin
alone would make them say something false.

- [ ] Refresh **per block, all `q₀`-derived quantities together**. Needs each
      block's derived set identified by reading, not grepping.
- [ ] Resolve `q-beta-spectral-bridge`'s A/B straddle FIRST — refreshing a table
      that does not close on itself buries the inconsistency.
- [ ] The six pin-string blocks are the same job, one level out.

## 🛑 RETRACTION + a much bigger finding: the bridge table and its witness compute DIFFERENT z

Probe: `the_qbeta_bridge_table_and_its_witness_compute_different_z_probe.py`, 6/6.

### First, I was wrong

I recorded `q-beta-spectral-bridge` as "already internally inconsistent: `h` at
pin A, `h²` at pin B, so `h² ≠ (h)²`". **Withdrawn.**

    h published        0.2090603219955937
    (h published)^2    0.043706218232901319
    h^2 published      0.04370621823290131     differ by 9.0e-18

The table closes on itself exactly, and every value reproduces from its own
quoted `q₀` with the proposition's own `z`. I got there by matching `h²` against
closed forms at three candidate pins and reading the bucket; at `h²` the pin-A
and pin-B values differ near the tenth digit and the bucketing could not separate
them. **Second instance today of the same lossy-metric error** — the first should
have taught me to try the simple explanation (`h²` is `h` squared) before
reaching for a cross-pin story.

### The real defect is larger, and it runs the OTHER WAY

The block's closing sentence claimed its values were "the displayed digits of the
50-dps witness … regenerated from the canonical CAL-2 pinning". **Every clause is
false.** The witness contains none of them and declares `q0Anchor: proton`.

                       block                 witness
    q0                 1.109978595557335     1.1099785827513808…  proton
    z                  0.4993203340335613    0.6126880371464652…
    ln(1 + z h)        0.09929139859972778   0.1205248238414840…
    predicted bridge   1.897907634269324     1.5660730493910099…

Each side reproduces its own numbers exactly. **Two different computations,
diverging by 21.2 %** — not a vintage, not drift.

**And the block is the side that matches its proposition.**
`prop:q-beta-spectral-bridge` *defines* `z := 1/(√q + 1/√q)`, which the table
uses; `q_beta_spectral_bridge_witness.py` computes `q³/(q²+1)`. For once the
**compute** has drifted from the stated definition, not content lagging compute.

**What hid it: a name collision.** The proposition calls its `z` "the
Markov–Jones parameter"; the producer's field holding the *other* formula is
named `z_markov_jones`. Anything grepping the name sees agreement.

**And CI is green.** Both witness assertions PASS — a producer checking itself
against itself cannot see that it has drifted from the block it names in
`contentBlock`. That is the structural gap: nothing compares a witness to the
block it declares.

### Not decided

Which `z` is correct. The proposition defines one and the producer computes the
other; the `Q_β` MeV figures differ by ~0.05 MeV between them. Producer,
proposition and table values all left untouched — only the false provenance
sentence corrected.

- [x] `q-beta-spectral-bridge` straddle — **there was none.** Retracted, and a
      21 % publication/producer divergence found instead.
- [ ] Author: which `z` does `prop:q-beta-spectral-bridge` intend?
- [ ] **The general gap this exposes:** a witness declares `contentBlock`, and
      nothing checks that the block's numbers are the witness's. That is
      mechanically checkable and would have caught this, the transfer-matrix
      readout, and the retired-`q₀` figures.

## WHICH z? — ANSWERED BY RULING, and it retracts my last turn

Analysis: [`docs/audits/2026-09-05-which-z-does-the-qbeta-spectral-bridge-intend.md`](../docs/audits/2026-09-05-which-z-does-the-qbeta-spectral-bridge-intend.md).

**Answer: D, `q³/(q²+1)`.** The two values are not rival readings of one
definition — they are the corpus's two registered trace conventions, and one is
excised:

    C   1/(q^1/2 + q^-1/2)   0.49932033418…   EXCISED 2026-08-09
    D   q^3/(q^2+1)          0.61268803714…   PRODUCTION

`rem:markov-z-reconciliation` names `1/(√q+1/√q)` as convention C explicitly, and
the trace-convention registry's channel table records `qbeta-decay` definitional
= **D** per the owner ruling of 2026-08-15 ("convention D is convention. excise
convention C"), with C **structurally excluded**. Status:
**agreed-migration-pending**, bean **`qou-cds1`**.

### 🛑 Retraction

I wrote that "for once the compute has drifted from the stated definition rather
than content lagging compute". **Backwards.** The compute migrated to the ruled
convention; the proposition was left behind. Ordinary C→D content lag — the
`qou-5pgl` class. I treated the proposition as the definition of record without
checking whether its convention was current, which is the one question the
registry exists to answer.

The producer is in fact *ahead* of the registry's own row, which still lists
production as C for this channel (naming `qbeta_utils.markov_parameter`,
`qbeta_ck_sseries_exact_rational`, `ZBarParity.lean` — not the spectral-bridge
witness).

### There is a structural argument as well as the ruling

In D: `z₋ = 1/(q(q²+1))`, `z·z₋ = 1/[2]_q²`, framing ratio `a² = q⁴` — a
monomial, which is what makes D the `sl₂` point. C's `z₋` mixes half-integer and
integer powers in one unfactorable numerator. The reconciliation block's own
phrase: *"not convention C being invalid; it is convention C being
structureless."*

### Recommendation

**Migrate to D — but inside `qou-cds1`, not as a one-off.** This block is one
member of a scoped multi-block migration; moving it alone leaves the channel
half-migrated, the registry row wrong, and three named production files still on
C. The `𝔔_β` MeV figures shift ~0.05 MeV, which wants checking rather than
assuming.

**Done now, the safe half:** the proposition is *labelled* — it states that its
`z` is convention C, that D is ruled, and that migration is tracked. Precedent:
`df13e845cee` labelled the `q₀` pins rather than recomputing them, and that is
what let this sweep identify them at all. Labelling an out-of-date convention is
cheap and reversible; migrating one block of a tracked migration is neither.

- [x] Which `z` does the proposition intend — **D, by ruling.**
- [ ] `qou-cds1` owns the migration; this block is a member.
- [ ] The **pin** rides along and is a separate axis: producer on proton, table
      on muon pin A. A pass that fixes `z` and leaves the pin straddling gives a
      table right in convention and wrong in anchor.

## THE STRUCTURAL GAP IS NOW CHECKABLE — `scripts/witness-block-agreement.py`

Every defect this bean has found is one shape: **a correction lands in compute
while a block keeps the old value, and nothing walks that boundary.** The
transfer-matrix readout, the six retired-`q₀` figures, the 21 % `z` divergence.
The unsourced-figure sweep only caught them because those figures had *no*
provenance at all; a stale figure that still matches *some* producer stays
invisible to it.

The sharper question is available and nobody was asking it: a witness already
declares `contentBlock`, naming the block it is evidence for, and **nothing
checks that the block's numbers are that witness's numbers.** A producer's
assertions compare it against itself, so they stay green while publication and
producer drift apart — which is exactly why CI was green on a 21 % divergence.

New diagnostic, selftested against the known positive (`prop:q-beta-spectral-
bridge` must flag on `0.4993203340335613`, the figure measured to diverge; a
detector that cannot see that can see nothing). Scope: 3274 live witnesses, 799
declaring `contentBlock`, 231 distinct blocks.

**Result: 15 blocks publish 79 figures their declared witness does not carry.**

**Wired into nothing**, same as the companion and for the same reason — a gate
red on arrival with known false positives in it is one nobody adopts. Two such
classes are documented in the script and must be read before any row is acted on:
decimals are not significant figures (a `0.000001` residual column is admitted at
one sig fig and the test has no resolving power — `rem:atom-mass-full-hecke` is
entirely this, the same floor that made two 9-digit figures indeterminate in
round 2); and a block's producer need not be the witness naming it.

### 🛑 TRIAGE 1 RETRACTS MY OWN FRAMING, AND FIXES THE CHECKER

I wrote above that `prop:markov-pair-z2` "publishes **both** `z` values … the
same C/D question as the bridge". **Wrong.** That block's line 5 states
`z = q³/(q²+1)` (**convention D**) outright — it is already migrated. Its two
flagged figures are not its `z` at all: they sit inside a retraction blockquote
*as the conflated pair being warned about* (`1/δ = [2]_q⁻¹ = 0.4972905456`
against the excised `z_C = 0.4993203342`, a 0.4 % confusion, bean `qou-98g5`).
I should have noticed the arithmetic before writing it down — 0.4 % is not the
21 % that separates C from D, and that alone rules out the reading.

**The error was the checker's, and it generalises.** A block that quotes a wrong
value *in order to retract it* is indistinguishable from one that publishes it.
This corpus retracts in Markdown blockquotes, so that class is measurable:
**21 of the 79 unmatched figures occur only on `>` lines**, and three blocks are
entirely that —

    thm:markov-trace-factorization    7/7   the deprecated transfer-matrix readout
    prop:wedderburn-weight-canonical  8/8   y_λ values printed to show a premise FAILS
    prop:markov-pair-z2               5/5   the 1/δ vs z_C conflation it warns about

Unpartitioned, the checker was loudest on exactly the blocks where someone did
the right thing and documented a correction — including **my own** retraction
table from earlier today. A diagnostic that penalises the discipline the corpus
runs on gets ignored, deservedly.

**Partitioned, not dropped.** Blockquote is a proxy for retraction, not a
synonym: `calibration-inputs` publishes the live CODATA `206.7682827` inside a
callout, so a blanket exclusion would blind the checker to any stale figure
living in a note — the same failure as reading "no resolving power" as "clean".
The selftest now also requires the known positive to land in the **asserted**
partition, so a partition that swallows real findings fails loudly.

**Report is now 12 blocks / 58 asserted figures**, with 21 quoted-only listed
separately.

## TRIAGE 2: `prop:em-coupling-projection` — the BLOCK is right, the POINTER is wrong

Probe: `the_em_coupling_projection_block_cites_a_producer_that_leaves_no_witness_probe.py`
(14/14). The checker's hardest row — 6 of 7 figures unmatched — and a near-total
miss turned out to be the signature of a misdirected pointer, not a stale table.
That reading is now in the checker's docstring so the next near-total miss is
read the same way.

**The block is correct.** Every figure reproduces at the proton pin from
`alpha_em_form_comparison_probe.py`, the producer the table names *in its own
prose*, and the table's claim that all rows use the proton pin is accurate.

    em_coupling_projection_probe.py     declared contentBlock, computed 1 of 7 rows
    alpha_em_form_comparison_probe.py   computed the other 6, emitted NO witness

Machine-readable provenance covering **14 %** of the block. **Fixed**: the real
producer now emits a witness declaring the block, carrying both pins, all four
registered `α_EM` forms, the residual-ownership analysis, and the three
intermediates the table publishes but nothing exposed (`δ_CS = 0.00155060213`,
the superseded order-2 truncation, the CODATA-2022 input). **Row closed, 6/7 →
0/7**; report now **11 blocks / 52 asserted**.

### Two label defects in the claiming witness — fixed, no number touched

1. `q0Value` and `q0Anchor` correctly said **proton**; four prose sites in the
   producer and three in its witness said "**muon-anchored**".
2. `CODATA_ALPHA_INV = 137.035999206` is the **Morel et al. (2020) Rb-87 recoil**
   measurement — cited under that name in `sec:fine-structure-data` — not a
   CODATA adjustment. Four sites called it CODATA. The block's table compares
   against CODATA 2022 = `137.035999177(21)`, a different quantity.

Both **numerically inert**: Rb-87 vs CODATA 2022 is `2.1e-10` relative against a
`5e-3` tolerance and a `1.55e-3` measured error. Nothing about the verdict moves,
which is exactly why they survived. Same shape as `df13e845cee`'s *"the defect
was the label"*. Two further warnings the regeneration surfaced and did not get
committed as-is: a raw `float64` entering the witness (now carried as `mpf`), and
a downgraded `mpmath` record (1.4.1 restored rather than committing the weaker
provenance).

**The probe asserts the fixed invariant, not the defect.** A probe that asserts a
defect goes red the moment the fix lands — the `muon_pin_three_values_probe.py`
failure this bean already records. Recorded here because I nearly repeated it.

### Cross-block: one quantity, two pins, one retired

    prop:em-coupling-projection       136.823209      proton  (136.823208853583)
    prop:em-coupling-bring-zero-mode  136.823219654   RETIRED (136.823219654561)
                                                      live muon: 136.823219729273

New: this bean already had the retired pin in `bring-zero-mode`, but not that a
**sibling block publishes the same quantity at the production pin**. The two
disagree on one number in the 11th digit — so it is not only stale against the
substrate, it is internally inconsistent across the corpus. Strengthens the
refresh case.

### A hazard found by accident, measured, and deliberately not patched

`136.823219654` is a **truncation** of `136.823219654561`, which *rounds* to
`…655` — it misses my own checker's half-ulp window by 1.12 half-ulps. So a
truncated publication is rejected even against its own producer. Measured across
the whole report, **truncation explains 0 of the asserted unmatched figures**, so
the window is left alone: widening an acceptance test that rescues nothing while
admitting new false negatives is a net loss. Documented in the script so it is
not rediscovered.

## TRIAGE 3: same pattern again — and then measured instead of guessed

`prop:markov-trace-recursive-reducer` is the identical shape. Its two figures —
proton `tr_M(σ₁⁷σ₂⁴) = 1.884319…`, neutron `tr_M(σ₁⁶σ₂⁴σ₁⁻¹) = 1.464034…` — are
richly produced by `markov_trace_recursive.py`, whose witness carries **both**
and declared **no** `contentBlock` at all. The block's pointer sat instead on
`probe_markov_trace_recursive_reducer.py`, which *verifies* that the reducer
agrees with the canonical seminormal engine and carries no trace value. **Fixed**
(one declaration); row closed. Report now **10 blocks / 50 asserted**, from 15/79.

### THE PATTERN IS THE FINDING: the pointer is on the VERIFIER, not the producer

Two for two is an anecdote, so it was worth measuring rather than extrapolating.
Indexing every number in all **3277 live witnesses** and asking, for each asserted
-unmatched figure, whether *any other* witness carries it:

    40 of 50 asserted-unmatched figures (80 %) ARE produced somewhere in the
    repo — by a witness other than the one declaring their block.

So the dominant defect this checker surfaces is not stale content and not missing
computation. It is that **`contentBlock` tends to be attached to verification
probes rather than to producers.** A verifier shows two engines agree; a producer
computes the numbers a block prints. When the pointer lands on the verifier, the
block's actual figures have no declared provenance — and nothing notices, because
the verifier's own assertions pass.

### THE NEGATIVE CONTROL, WITHOUT WHICH THAT NUMBER IS WORTHLESS

Matching 50 figures against a pool of **271 665** distinct witness values will
find coincidences. This bean has recorded two lossy-metric errors already today,
so the floor was measured rather than assumed: perturb each published figure's
last digit — same magnitude, same decimal count, fabricated — and re-run.

    REAL published figures matched somewhere : 80.0 %
    FABRICATED (last digit changed)          : 10.8 %   (40 draws, range 4–18 %)

**7.4× the coincidence floor**, so the aggregate finding holds. But ~5 of the 50
matches are expected to be spurious, and they will concentrate in the
low-precision figures — `rem:atom-mass-full-hecke`'s `0.000001` and `0.000002`
carry one significant figure and are almost certainly among them. **The aggregate
is sound; individual carrier attributions are not**, and no row should be closed
on this evidence alone.

### 🛑 THE CHECKER ITSELF PARSED FLOAT64 — in a repo that forbids it by gate

Chasing an anomaly in the floor measurement found a defect in my own tool.
`rounds_to` parsed both the published figure and the witness values with
`float()`. At 15+ significant digits, float64 spacing (~1.1e-16 near 0.5) is
comparable to the ±0.5-ulp acceptance window, so **the window stops
discriminating at exactly the precision this corpus cares most about**:
`0.508229789376739` matched **31 of 60** fabricated perturbations. Switched to
exact `Decimal` (prec 80). Measured effect: the 12+ floor drops 11.4 % → 8.8 %,
and two spurious matches disappear from the report.

Embarrassing, but the interesting part is that the *rest* of the elevation is
real, and it is a property of the corpus rather than of the tool.

### THE FLOOR IS NOT A NUMBER, IT IS A CURVE — and it inverts at the top

    sig figs     floor       reading
    0-2         100.0 %      ZERO information. Every fabricated value matches.
    6-8           5.4 %      a match is real evidence
    9-11          2.7 %      strongest discrimination available
    12+           8.8 %      RISES AGAIN

The rise is not an artifact. The fabricated hits concentrate on the corpus's
**load-bearing constants** — `w₋ = 0.247297886748035` (14/60), the `q₀` pins
`1.109978595554181` and `…557335` (10 and 9), `z_C = 0.4993203340335613` (9),
`0.508229789376739` (30) — which the repo carries at many precisions and in many
registered variants. A perturbed digit lands on a *real neighbouring variant of
the same constant*.

**So for exactly the figures that matter most, "it matches something in the repo"
is the weakest evidence available.** Attribution there has to come from reading
the producer. This also retro-justifies the 0-2 prediction: `rem:atom-mass-full-
hecke`'s `0.000001`/`0.000002` sit in the 100 % bucket and should never have been
counted.

### WORKLIST: candidate producers, ranked by COVERAGE not by figure count

One witness carrying k of a block's n figures is much stronger than k scattered
per-figure hits. Ranked that way, with declared witnesses excluded:

    block                                     coverage  candidate
    prop:sl2-prolongation-recurrence            8/8     binding-recurrence-spectral-bridge
                                                8/8     sw-period-lw-sl2-qbessel-probe
    prop:q-hecke-seminormal-character-closure   5/5     laurentq-a5-ceiling-measure
                                                5/5     rho-k-leading-order-verification
                                                5/5     witness-float64-padding-audit
    prop:q-beta-spectral-bridge                6/12     the_qbeta_bridge_..._different_z_probe
    prop:confined-knot-binding                  3/6     deuteron-fpn-wlambda-wiring / a-K-via-lp-dual
    prop:frobenius-gram-matrix                  3/5     qbeta-c3-barodd-knot-operator-gram
    conj:im-q-physical-role                     3/4     qbeta-imq-reality-locus
    prop:em-coupling-bring-zero-mode            2/3     published_figures_carry_a_retired_q0_probe
    prop:alpha-em-categorical-trace-ratio       1/4     -- nothing covers it --
    rem:atom-mass-full-hecke                    2/2     (0-2 sig figs: MEANINGLESS)
    rem:beta-decay-energy-scale                 1/1     weak

**Do not auto-declare from this table.** Two reasons, both measured. First, the
three-way 5/5 tie on `q-hecke-seminormal-character-closure` falsifies the
independence assumption behind any p-value here — and one of those three is
`witness-float64-padding-audit`, an **aggregator** that carries numbers without
producing them, which is a distinct false-positive class the coverage score
cannot see. Second, several blocks' figures are the load-bearing constants above,
where the floor is worst.

## TRIAGE 4: `prop:alpha-em-categorical-trace-ratio` — TWO BLOCKS PUBLISH THE TWO SIDES OF ONE IDENTITY AT DIFFERENT PINS

Probe: `two_blocks_publish_the_two_sides_of_one_identity_at_different_pins_probe.py`
(6/6). Taken first *because* nothing in 3277 witnesses covered more than 1 of its
4 figures — the signature of an unproduced figure rather than a misplaced
pointer. It was, and the reason is worse than either.

**The block proves an exact identity and then disagrees with itself across
blocks.** It states

    α_EM = h²/(q·δ_q(T_2,9)·δ_q(T_3,5)) = 1/(q [9]_q [10]_q)

which holds at **any** `q` — `δ_q(T_2,9) = h[9]_q` and `δ_q(T_3,5) = h[10]_q`
cancel the `h²` — verified to `1e-53` at every registered pin. It is algebra, not
agreement. It then cites `prop:em-coupling-projection` for the right-hand side:

    side                        block                 pin      α_EM × 10³
    h²/(q δ₉ δ₁₀)               this block            MUON     7.30870098
    1/(q[9]_q[10]_q)            em-coupling-projection PROTON   7.30870156

**A `7.94e-8` disagreement between two quantities the corpus has proved equal.**
Sharper than the `em-coupling-bring-zero-mode` cross-block finding: there two
blocks merely published the same quantity, here one *derives from and cites* the
other. They cannot both be right.

### The pin determination is unambiguous; the vintage is not, and is not guessed

Rounding test against every registered `q₀`, on all four table figures:

    proton      0/4   DECISIVELY EXCLUDED (residuals 1.0e-7 to 1.5e-7)
    muon live   4/4
    retired     4/4
    frozen A    4/4

The muon family is certain. **The vintage cannot be determined**: the three
variants differ by `7.98e-11` relative, the sharpest published figure carries 9
significant digits, and separating them needs ~12. Stated explicitly in probe,
witness caveat and block, because this bean has twice recorded that "no resolving
power" and "clean" look identical in a results table.

### Why the sweep found no carrier — and a false provenance sentence

The block cited `delta-q-decoration.witness.json` with *"The witness assertion
validates this match."* That witness declares a **different** block
(`def:delta-q-decoration`), carries Markov-trace machinery rather than any of
these four quantities, and is anchored `q0Anchor: proton`. It validates nothing
here and disagrees on the pin. So the live compute for this quantity follows the
sibling onto proton, and no carrier exists anywhere — exactly what the
coverage sweep saw. Sentence corrected; **labelled, not recomputed**, since
choosing between the two blocks is the anchor ruling, not a substitution.

Report now **9 blocks / 46 asserted**, from 15/79.

- [ ] **Owner: this one needs a ruling more than the others.** Elsewhere a stale
      pin is a data-refresh question; here two blocks publish the two sides of a
      proven identity and one of them must move.
## TRIAGE 5: `prop:sl2-prolongation-recurrence` — the pattern a third time

The coverage worklist was right. Both 8/8 candidates carry **all nine** of the
block's figures — both columns of its table — which at the 9–10 sig-fig floor
(2.7 % per figure) is ~1e-14, not coincidence.

Distinguishing producer from sibling took reading, not scoring:
`sw_period_lw_sl2_qbessel_probe.py` carries `period_table_n2_to_n8` — literally
the block's table — and its two assertions are the block's two claims
(`sl2_depth2_diverges_from_lw_by_n6`, `lw_growth_ratio_exceeds_sl2_lambda_plus`).
`binding_recurrence_spectral_bridge_probe.py` shares the sequence but is about
the spectral bridge (λ₊, det). **Both declared no `contentBlock`**; the block's
pointer sat on `unified_tau_odd_partner_solve.py`, which solves for τ and carries
none of the sequence. Declared the producer, and filled in its **null
description** while there. Row closed.

Worth noting the block itself is sound: its table exists to show the depth-2
recurrence *fails* (−52.21 % by n=8), and the n=4 row is true by construction
because τ is that row rearranged — which the block already says.

Report now **8 blocks / 38 asserted**, from 15/79.

## TRIAGE 6: `prop:confined-knot-binding` — MY OWN witnesses were writing numbers without decimal points

The checker turned on my own work from earlier today and found something worse
than a missing declaration.

`the_nuclear_jet_level_is_the_retired_all_pairs_object_probe.py` is the producer
the block names in its own text. It declared **no `contentBlock`**, and its
witness recorded only two of the six figures the block publishes — the `H₃`
weight table was computed, printed, and then dropped. Ordinary, and the fix is
the one this bean established with `1.064088425325`: *witness the figure, do not
delete it.*

**But adding the table did not close the row**, which is how the real defect
surfaced.

### `gmpy2.digits()` returns a BARE MANTISSA, and I fed it straight into witnesses

    published            0.5054042265039308...
    witness recorded     5054042265039308031875587      <- no decimal point

Every numeric field in those witnesses was **numerically unusable** — not wrong
digits, but wrong magnitude by an unknown power of ten, invisible to a reader and
to every downstream tool. **21 sites across 4 probes**, all mine, all from today:

    the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe.py   12
    the_nuclear_jet_level_is_the_retired_all_pairs_object_probe.py          6
    the_free_energy_reading_has_no_energy_spectrum_probe.py                 3
    the_character_ratio_derivation_path_is_the_bond_model_probe.py          1

Two of those probes **already had** the `s()` formatter I wrote earlier the same
day for precisely this trap (the one that briefly made `[3]_q! = 6.12` read as
`0.612`) — and the witness-emission path bypassed it. I fixed the display and
left the serialisation. The other two never got `s()` at all, so my note that I
had "added it to every affected probe" was wrong.

All 21 sites now route through `s()`; all four probes re-run green (3/3, 8/8,
8/8, 13/13). Row closed. Report **7 blocks / 32 asserted**, from 15/79.

### Scanned for it corpus-wide — and it is only mine

Signature: a pure-digit string of length ≥ 15 in a witness `data` field. Across
**3282 live witnesses**: 6 files, 73 fields, and **every one is a legitimate
large integer** — rational numerators, LCM denominators, `n!` costs, state-pair
counts, Taylor coefficients scaled by `2^(3A)`. No other mangled `mpfr` exists.
So no gate is warranted; the defect was mine and is gone.

### The reason this matters beyond the fix

The two figures that *appeared* to be witnessed before — `0.508229789376739` and
`0.000071511999729` — matched only because they appear in the witness's
**description prose**. The structured data carried neither. A checker reading
`data` alone would have called the block unwitnessed; one reading the whole file,
as this one does, called it witnessed on the strength of a sentence. Both
readings are defensible and they disagree, which is worth knowing before anyone
promotes this checker to a gate.

## TRIAGE 7: `prop:frobenius-gram-matrix` — four false positives and one real digit error, in one block

Probe: `the_gram_block_publishes_a_D_eigenvalue_no_pin_produces_probe.py` (7/7).
The clearest argument yet for reading every row rather than sweeping.

**Four of five flags are a false-positive class the checker had not named.** The
block publishes its Gram spectrum under the production convention **D** *and*
under the excised **C**, side by side and explicitly labelled ("under the excised
convention C"). A producer computing D correctly carries none of the C column.
That is a block doing the right thing, counted as a defect. Named as class 3
now — and unlike the retraction class it sits in ordinary prose, so it is **not
mechanically separable**: the label is a sentence, not a syntax.

### The fifth was real, and it took a computation to tell from a pin difference

The largest **D** eigenvalue read `+4.23033920`. The block's own declared witness
(`q0Anchor: proton`) computes `4.230339225030225` → `4.23033923`, five half-ulps
away. Tempting to call a pin difference: proton→muon moves this eigenvalue by
~`4e-8` against a `2.5e-8` discrepancy, the same order. So it had to be computed.
Rebuilding the whole 6×6 from the block's own symbolic entries:

    proton      4.230339225030226   ->  4.23033923
    muon live   4.230339401101782   ->  4.23033940
    retired     4.230339399892241   ->  4.23033940
    published                           4.23033920   <- NO REGISTERED PIN

**A transcription error.** Corrected; the other five D entries are right at the
proton pin and unchanged.

### 🛑 THE WEAKNESS THAT MATTERS MOST — and I walked into it

Closing this row, I pasted the block's convention-C figures into my new witness
as part of an internal-consistency check. **The row closed.** The C column still
has no producer — convention C is excised, none exists — and the checker had
simply stopped saying so.

Reverted; the row now honestly reads 4/11. But the lesson generalises and is now
in the script's docstring as its most important limitation: **this checker asks
whether a declaring witness *carries* a block's numbers, and a witness that
transcribes them answers yes without adding evidence.** Nothing in it can tell a
computed value from a copied one. That is exactly why
`witness-float64-padding-audit` — an aggregator that scrapes other witnesses —
scored as a top candidate producer for a block it has never computed.

**So the count is a floor on the work remaining, never a measure of it**, and
closing a row means finding or writing the producer, never recording the number
somewhere the checker will look. Anyone promoting this to a gate needs to read
that paragraph first.

Report **7 blocks / 31 asserted**, from 15/79.

- [ ] The four C-column figures stay open deliberately. Closing them would mean
      computing an excised convention, which is the wrong direction; the honest
      resolution is that the checker cannot distinguish "unproduced" from
      "unproducible by policy".
## TRIAGE 8: `prop:q-hecke-seminormal-character-closure` — the largest divergence in this bean, and it feeds `qou-46ab`

Probe: `the_character_closure_block_and_a_lean_file_publish_convention_c_probe.py`
(5/5). Written up in `qou-46ab`, which owns the migration.

**All three top-scoring candidates were wrong, in three different ways** — the
case the checker's docstring says scoring cannot settle:

    laurentq-a5-ceiling-measure        5/5   a WALLTIME BENCHMARK
    rho-k-leading-order-verification   5/5   scriptFile literally reads
                                             "(deferred — producer not in
                                             computations/ tree)"
    witness-float64-padding-audit      5/5   the AGGREGATOR

Reading beat scoring, and found something larger than a pointer problem.

**The table is the excised convention C**, by 7 % to 120 %. The canonical
Hoefsmit + Wenzl bridge computes these same five atoms by the block's *own stated
method* and agrees with none of them; the proton ratio is `qou-46ab`'s own
`0.0755215` C→D signature. **The block's "relative error ~1e-15" column is
agreement between two C-frame paths** — which says nothing about which convention
both are in, and reads as a verification. Largest divergence this bean has found;
previous record was the 21 % `z` gap.

The same C value is live in **Lean** (`MarkovPeelH3.lean`), claiming 4e-16
agreement with a witness it is 7e-2 from — word-for-word the claim `qou-46ab`
already disproved in `computations/`.

**`qou-46ab`'s literal scan could not see either site**: it scanned
`1.06530622861316`; the block renders `…859` and Lean `…592389333`. Zero matches
in a sweep whose whole purpose was to find them. Both sites labelled, nothing
recomputed — the migration is `qou-46ab`'s.

### 🛑 I HIT THE TRANSCRIPTION TRAP THREE TIMES, ONE COMMIT AFTER DOCUMENTING IT

Closing this row, my own probe closed it three separate ways without producing
anything: the block's figures in a `data` field, then in the witness
**description prose**, then as a **prefix** of the Lean value I was quoting as
evidence. Each time the row closed and the figures still had no producer.

Fixed by recording renderings as **suffixes after a shared prefix**, which
carries the finding (three renderings of one quantity) without creating a
matchable literal. Effect: the report went **26 → 31** asserted once the
transcription came out — my own closures had been hiding five figures.

That the author of the warning walked into it three times in twenty minutes is
the strongest evidence that the weakness is structural, not a lapse. It should
be read as a design limit of any checker of this shape: **matching a block's
numbers against text that mentions them cannot distinguish evidence from echo.**
A version reading only computed `data` fields, and only from producers, would be
stricter — and would also have called `prop:confined-knot-binding` unwitnessed
when its two figures sat in prose.

Report **7 blocks / 31 asserted** (honest), from 15/79.

## TRIAGE 9: `conj:im-q-physical-role` — category (c), and it closes a pending vintage item as a NON-DEFECT

Probe: `the_apollonius_circle_from_cal2_reproduces_exactly_probe.py` (4/4). The
first row in this whole triage with **no defect at all**.

Odd shape going in: 4 unmatched against **68** declaring witnesses. Those 68 are
the `Im(q)` reality-locus computations that close candidates (i) and (iii);
candidate (ii)'s Apollonius geometry is a two-line derivation nobody ran
separately. **A large witness count says nothing about coverage of any one
figure.**

CAL-2 is `m_μ/m_e = Vol(4₁)/ℏ_q²` with `ℏ_q = 1 − 1/q`. Over complex `q` the
modulus condition is the Apollonius locus `|q−1| = k|q|`, giving

    k² = Vol(4₁)/(m_μ/m_e)
    centre = 1/(1−k²)   radius = k/(1−k²)   leftmost = 1/(1+k)

All three published figures are the correct roundings, and the table closes on
itself — `centre − radius = leftmost` exactly as printed.

### The vintage does not reach them, which settles a pending item

**No `q₀` enters.** The circle is fixed by `Vol(4₁)` and the mass ratio alone,
because CAL-2 is the equation that *defines* `q₀`. And both CODATA vintages
reproduce all three figures, diverging only at `7.4e-10` relative against 7
published significant digits.

So the `206.7682830` here — one of the three sites this bean left open as "needs
reading rather than relabelling" — **resolves as a non-defect**: the block quotes
CAL-2's own input value rather than asserting a CODATA vintage, and nothing it
derives from that value moves. Two of those three sites remain
(`knot-volumes-verification-table2-data`, and the `witness-substitution-audit.ts`
fixture).

### A note on why closing this row is legitimate

The witness records `206.7682830` as `mass_ratio_input` — a **declared input the
probe consumes**, not a figure copied to satisfy the checker. That is the
distinction the transcription weakness turns on: provenance for a calibration
input *is* recording that the computation took it. The three circle figures are
computed from `mp.clsin` and that input, so recording them is what a producer
does.

Report **6 blocks / 27 asserted**, from 15/79.

## TRIAGE 10: `prop:em-coupling-bring-zero-mode` — a row that MUST STAY OPEN

All three flagged figures are the **retired** `q₀`, consistently:

    figure              retired pin gives      other pins
    1.109978595554181   the pin itself         —
    136.823219654       136.823219654561       muon 136.823219729, proton 136.823208854
    137.035426245       137.03542624535        muon 137.035426320, frozen A 137.035426248

`137.035426245` (`bare + 2/(3π)`, the zero-mode form) separates all four
registered pins and lands on retired exactly. `136.823219654` is the truncation
case documented in the checker — the retired value rounds to `…655`, so it fails
a half-ulp test against its own producer.

**This is the tracked retired-`q₀` refresh, not a new defect.** The block already
declares "(muon pin, 16 dps)" and the refresh is owner-gated.

### The right action is to do nothing, and that is the finding

Nothing live carries retired-pin values, and **nothing should**. So the checker
flagging this block is *correct signal*: these published figures genuinely have
no live producer, which is exactly the problem awaiting the refresh.

I could close the row by declaring
`published_figures_carry_a_retired_q0_probe.py` (it already covers 2 of the 3).
**That would be a defect.** It would make a retired vintage look witnessed and
silence the one automatic signal that this block is stale. Some rows should stay
open, and closing them is worse than the flag — a distinction the count cannot
express, which is another reason this checker must not become a gate on its
count.

Report stays **6 blocks / 27 asserted**.

- [ ] Five blocks left, and at least two should NOT be closed here:
      `prop:em-coupling-bring-zero-mode` (3, awaiting the refresh) and
      `rem:atom-mass-full-hecke` (2, the 0–2-sig-fig class where the method has
      no resolving power — close as *unresolvable*, do not investigate).
      `prop:q-beta-spectral-bridge` (12) belongs to `qou-cds1`.
      So the genuinely-actionable remainder is smaller than 27 suggests.
- [ ] **Worth considering before any gate**: a `data`-only, producer-only variant
      of the checker. Stricter and immune to the echo problem, at the cost of
      flagging blocks whose provenance genuinely lives in prose.
- [ ] Consider whether `contentBlock`-on-a-verifier deserves its own check. The
      signature is mechanical: a witness declaring a block whose assertions are
      all engine-agreement comparisons and whose data carries none of the block's
      figures.

## VINTAGE LABELS: `206.7682830` is CODATA **2018** and two blocks call it 2022

Found by the checker above. The literal survives in six content files. The
compute side is **governed** — all three hits under `computations/` are annotated
historical comments under an existing gate — and content is not.
`epistemic-status-of-calibrations.ts` already records *"The prose said
`206.7682830`, which is CODATA 2018"*; two other blocks published it **labelled
CODATA 2022**. Live value `206.7682827 ± 0.0000046`; discrepancy `1.451 ppb` =
`0.065σ`.

Corrected the labels, **not the values**:

    figure-8-muon-mass-cross-check            (CODATA 2022) -> (CODATA 2018)
    substrate-consistency-window-table1-data  | CODATA 2022 | -> | CODATA 2018 |
    calibration-inputs                        noted; value deliberately unchanged

`calibration-inputs` is the one that must not be substituted: that row **is**
CAL-2, so replacing it moves `q₀` and everything derived from it — the tracked
refresh above, not a labelling fix.

- [ ] The remaining three (`knot-volumes-verification-table2-data`,
      `conj-im-q-physical-role`, and the `witness-substitution-audit.ts` fixture)
      need reading rather than relabelling — check whether each is asserting a
      vintage or merely quoting one.
