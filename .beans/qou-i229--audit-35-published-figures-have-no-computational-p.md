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
