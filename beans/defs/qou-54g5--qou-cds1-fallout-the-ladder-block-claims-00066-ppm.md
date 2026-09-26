---
# qou-54g5
title: 'qou-cds1 fallout: the ladder block claims -0.0066 ppm at the muon pin; the implementation gives +7.34 ppb'
status: todo
type: task
priority: high
created_at: 2026-08-26T23:21:11Z
updated_at: 2026-09-13T17:30:00Z
---

## What was measured

Calibrating a `qou-cds1` re-derivation probe against the existing ladder
implementation, I checked that my decomposition reproduces the published
five-rung product. It does, **bit-identically** (`|diff| = 0.0` in mpmath at
65 dps, both pins). So the implementation and my re-expression are the same
function.

That function, at the muon pin -- the block's own frame, the one its headline
residual is quoted in -- returns:

    +7.336484 ppb        (proton pin, canonical: +37.70749 ppb)

The block `q-beta-categorical-precision-ladder` claims **-0.0066 ppm**, i.e.
**-6.6 ppb**, at that same pin.

Same order of magnitude, **opposite sign**, and ~11 % apart in magnitude. That
is not rounding.

## Why it matters

The -0.0066 ppm is the number the entire ladder is quoted on. Every downstream
statement about the ladder's accuracy -- including my own framing that "the
whole five-rung product moves Q_A by 0.168 %" -- inherits it. If the block's
figure and the code's figure disagree, at least one of the following is true
and none of them is small:

1. the block's residual was computed against different CODATA inputs than
   `qou_substrate.constants` now carries (`M_E_MEV = 0.51099895069`,
   `Q_NEUTRON_MEV = 0.7823334093099085`);
2. the block's residual predates a change to one of the five rungs;
3. `qbeta_ladder_convention_fee_probe.ladder()` -- which every recent
   convention probe, mine included, has treated as *the* implementation --
   does not faithfully encode the block's formula;
4. the sign convention on "residual" differs between block and code.

(4) alone would not explain the 11 % magnitude difference.

## What this is NOT

Not a fit and not something to tune. **Do not adjust either number toward the
other.** The task is to find which of (1)-(4) holds, by reading the block's own
derivation against the implementation line by line.

## Provenance

Surfaced by `computations/qbeta/qbeta_d_frame_rung_one_rederivation_probe.py`
(9/9), whose `calibration_reproduces_the_blocks_sub_ppb_muon_frame_number`
assertion passes only on the loose `< 100 ppb` bound -- deliberately loose,
because I could not assert the block's stated value without asserting a number
I had just found the code disagrees with.

Noted but NOT chased in that probe: it was opened for the rung-1 re-derivation
and this is a separate defect. Queued rather than pivoted to, per the bean
policy.

## 2026-08-30 — ANSWERED, and the recorded number is itself stale (PR #6103)

**Which hypothesis?** (4), a sign convention — and it is NECESSARY BUT NOT
SUFFICIENT. Probe qbeta_ladder_headline_residual_provenance_probe, 5/5.

  headline (prose)                  -6.6      ppb
  block's OWN table 2, N=3          +6.02     ppb   |ratio| 0.912
  block's OWN table 2, N=4          -0.57     ppb   |ratio| 0.086
  live implementation, muon pin     +7.133937 ppb
  live implementation, proton pin   +37.70749 ppb

The headline matches NO row of the block's own table. Nearest is N=3:
opposite sign AND 8.8 % apart in magnitude, so a pure sign flip does not
close it. Hypotheses (1) CODATA and (3) faithfulness are not needed to
explain it; (2) predating a rung change is folded into the fifth-rung
question below.

**Hypothesis (2) — the q0 pin — is DEAD.** The implementation is POSITIVE at
both pins; changing q0 moves the magnitude 5.3x, never the sign. This also
corrects qbeta_ladder_convention_fee_probe's own docstring item 3, which
says the -0.0066 ppm 'reproduces only at the MUON pin'. It does not: the
muon pin gives +7.13 ppb.

**Not settled here:** which number is RIGHT. That needs the block's
fifth-rung coefficient, which its own .qa.json finding (1) records as
superseded — boxed -(b^2+1/2) = -1.2527 vs context/table-3 3c_3^2+b =
+12.8676, opposite sign, order of magnitude apart. Math question.

## NEW, and it is the reason to re-measure rather than quote

This bean recorded **+7.336484 ppb** at the muon pin on 2026-08-26. A fresh
run today gives **+7.133937 ppb** — 0.203 ppb apart, 2.8 %. The committed
qbeta-ladder-convention-fee.witness.json still holds the 7.336484 figure, so
that witness is **substantively stale**, not merely drifted.

I did NOT refresh it in #6103. The movement is main's (the muon anchor's
CODATA-2022 move and whatever else entered the cone), not this PR's, and
committing it here would put a main-caused change to a published number
inside a PR about a different defect. Left as its own item.

Every number above is C-frame; the D-frame ladder is unknown pending the
qou-cds1 re-derivation.

## 2026-08-31 — RESOLVED. It was an index slip, and the headline is correct.

Probe: `computations/qbeta/qbeta_ladder_c5_slot_provenance_probe.py`, **12/12**,
mpmath 50 dps.

### The remaining item was not a math question

This bean recorded the open item as "which fifth-rung coefficient is right,
boxed `-(b^2+1/2) = -1.2527` vs context/table-3 `3c_3^2+b = +12.8676`, opposite
sign and an order of magnitude apart. Math question." It is neither a math
question nor a dispute. The block's own context says so in one line
(`q-beta-categorical-precision-ladder-context.md:29`):

    "The earlier c_4 = b^2 + 1/2 form is superseded: it is 9.5% off the
     empirical value, while c_3 * b^4 matches to 0.9%."

`b^2 + 1/2` is the **retired c_4**. Site by site:

    site                                    c_4          c_5
    boxed formula (.md)                     c_3*b^4  OK  b^2+1/2   <- retired c_4
    ladder() in qbeta_ladder_convention_fee c_3*b^4  OK  b^2+1/2   <- retired c_4
    context, "mixing pattern across rungs"  c_3*b^4  OK  3c_3^2+b
    table-3, N=5 row                        --           3c_3^2+b

The supersession updated rung 4 in the box and **displaced the retired
expression into the rung-5 slot** instead of deleting it. Three sites agree on
`3c_3^2+b`; the two that disagree carry an expression their own prose retires.

### CORRECTION to this bean: they are not opposite in sign

Both are negative coefficients of `u^5` (`-1.2527` and `-12.8676`). The recorded
opposition came from comparing the box's `-(b^2+1/2)` against a bare
`+(3c_3^2+b)` — one with the leading minus folded in, one without. They differ
by **10.27x in magnitude only**.

### The slip is what hid the headline

    block headline         -0.0066 ppm  =  -6.6 ppb  (2 s.f.)
    context c_5, muon pin  +6.6133 ppb  ->  0.0066133 ppm     0.202 % apart
    boxed   c_5, muon pin  +7.1339 ppb                        8.1 % apart

**The headline IS the N=5 muon-pin residual computed with the context c_5**, and
it rounds to `0.0066 ppm` exactly at the two significant figures it is quoted to.

The earlier pass could not see this because the live code carries the retired
`c_4` in the `c_5` slot, pushing its N=5 to `+7.13`; the nearest thing to the
headline then looked like N=3 (`+6.02`, 8.8 % off), which is what made the sign
hypothesis read "necessary but not sufficient". **It was sufficient.** The
residual 8.8 % was an artefact of comparing against the wrong rung.

So of the four hypotheses this bean opened with: (1) CODATA, (2) pin and
(3) faithfulness are all not needed. **(4), a sign convention, is the whole
answer** — and it is now a pure sign with no magnitude gap left to explain.

The sign itself is NOT resolved here. What is resolved is that nothing but the
sign is wrong.

### Reconstruction faithfulness, because the first attempt was not

The probe reproduces the live implementation **exactly** — `+37.70749` ppb
(proton) and `+7.133937` ppb (muon), both matching the values recorded above.
A first draft guessed `w_blind = 0` rather than reading it, and produced an
11.7 % residual, ~70x worse than the block's own "Form A bare" row. A wrong
baseline makes every downstream comparison measure the baseline; the guess is
recorded in the probe so the next reader does not repeat it.

### The fix, deliberately not applied in the probe

Correct the `c_5` slot in both carriers — the boxed formula in
`q-beta-categorical-precision-ladder.md` and `ladder()` in
`qbeta_ladder_convention_fee_probe.py` — from `(b^2 + 1/2)` to `(3c_3^2 + b)`.
That is a correction to match the block's own prose, not a change of claim. It
moves a published number (`37.707 -> 37.187` ppb at the canonical pin), so it
belongs in its own commit with the witness refreshed.

### Still open, and still not to be closed by fitting

- The **sign** convention (hypothesis 4).
- **Table 3's column**: neither `c_5` reproduces its `+0.04` ppb at N=5. Scope
  (a) — a scope-limited negative about this reconstruction, NOT a claim that
  table 3 is wrong. What is established is that the `c_5` slot is not the cause
  of that gap either.
- The **stale witness** `qbeta-ladder-convention-fee.witness.json` (holds
  7.336484; live gives 7.133937), unchanged from the previous entry.

Every number here is C-frame. The D-frame ladder does not exist — and per PR
#6282 plus its correction, all three legs of the C instrument fail to transport,
so this resolves the C-frame block on its own terms only.

## 2026-08-31, same session — RETRACTING "RESOLVED". I had the count backwards.

The entry above says "three sites agree on `3c_3^2+b`; the two that disagree
carry an expression their own prose retires", and calls it an index slip. **Both
halves are wrong.** They rest on a grep that only searched the two files I had
already opened.

### The full count

    -(b^2 + 1/2)                              3c_3^2 + b
    -----------------------------------       -------------------------------
    boxed formula (.md)                       context, "mixing pattern" line
    ck-extraction-from-algebraic-rules.md     table-3, N=5 row
    conj-qbeta-c-k-closed-forms.md
      (+ the Lean class it formalizes)
    ladder() in convention_fee probe
    ladder() in headline_residual probe
                                    6 sites                           2 sites

### And it was not a displacement

`q-beta-gamma-gamma-canonical-derivation.md:48` gives `b^2+1/2` at **c_4** with
the categorical reading "Kashiwara + half-Hopf mixed".
`conj-qbeta-c-k-closed-forms.md` gives it at **c_5** with **the same reading**
and a recorded **2.4 % empirical residual**, inside a coherent family
(`c_4 = c_3 b^4`, `c_5 = -(b^2+1/2)`, `c_6 = c_3^2 b^2`, `c_7 = c_3^3`) that
already carries the updated c_4.

So when c_4 was superseded, `b^2+1/2` was **deliberately reassigned to c_5**,
carrying its interpretation with it, and was empirically checked there. That is
an intentional claim. My "the supersession displaced it and nobody noticed"
story required the carriers to be stale on c_4 — they are not; they carry the
new c_4 and the old expression at the new slot, on purpose.

### What actually survives, and it is worse than a slip

The measurement stands and is unaffected:

    block headline         -0.0066 ppm = -6.6 ppb (2 s.f.)
    context c_5, muon pin  +6.6133 ppb    0.202 % apart
    boxed   c_5, muon pin  +7.1339 ppb    8.1 % apart

**The published headline was computed with a c_5 that only two sites in the
corpus carry, while six sites — including a conjecture block and the Lean class
it formalizes — claim a different one.** Those cannot both be right. That is a
substantive inconsistency about what the framework claims, not a typo.

Separately, `q-beta-gamma-gamma-canonical-derivation.md` is stale at the other
end: its table still publishes the retired `b^2+1/2` at **c_4**. Third defect.

### NO FIX APPLIED, and the previous entry's proposed fix is withdrawn

That entry proposed correcting "both carriers" to `3c_3^2+b`. With the count the
other way, that means rewriting **six** sites to match **two**, on one
2-significant-figure number. That is a change of claim, not a documentation fix.

What would settle it, in order:

1. Read the conj block's 2.4 % empirical residual for `-(b^2+1/2)` at c_5
   against the context's derivation of `3c_3^2+b`. Same slot, different
   provenance; one is wrong.
2. Find what produced table 3's column. If it used `3c_3^2+b`, the two-site form
   is the computed one and the six-site family is stale.
3. Only then edit, in whichever direction the math gives.

Bean stays **open**. The status is: cause identified and localized, direction
undetermined.

### Note on how this was caught

By running the grep I should have run before writing "RESOLVED" — the corpus-grep
discipline exists for exactly this, and I skipped it because the context line
read like a complete answer. A line that explains a finding is not the same as
having measured its extent.

## 2026-08-31 — DIRECTION SETTLED, and it is the reverse of how I posed it

Probe: `computations/qbeta/qbeta_ladder_c5_slot_provenance_probe.py`, **15/15**.

The retraction above left the direction undetermined and listed the step that
would settle it: "find what produced table 3's column". Done.

### `3c_3^2 + b` lives in exactly one place: a deprecated producer

    computations/_deprecated/precision-ladder-superseded/
        precision_ladder_ck_symbolic_probe.py:79
            5: mpf("4") * 3 + b,      # c_3^2 * 3 + b = 12 + b

Its coefficient family there is **identical to the live conjecture family at
c_4, c_6 and c_7** and differs **only at c_5** — so c_5 is precisely what the
supersession that retired this producer changed.

### The SDP extraction decides it

`computations/qbeta/qbeta_decay_sdp_full_ck.py` — the conjecture block's own
declared producer, with a witness — records:

    c_5 extracted        -1.2229
    -(b^2 + 1/2)         -1.2527     2.44 % off        <- 6 sites, CURRENT
    3c_3^2 + b          +12.8676   1152 % off, WRONG SIGN  <- 2 sites, SUPERSEDED

No plausible refresh of that extraction moves it from `-1.22` to `+12.87`.

### So the 0.202 % agreement means the opposite of what it looked like

It is **not** evidence that `3c_3^2+b` is right. It is evidence that **the
published headline was computed by the deprecated producer and never recomputed
when c_5 changed.** Same for table 3, whose N=4/N=5 rows the block's declared
producer (`probe_q_beta_operator_valued_N3.py`) **cannot generate** — it stops
at N=3, and carries no c_5 at all.

**The stale sites are the HEADLINE, TABLE 3, and the context's mixing-pattern
line.** The six carriers are current. My first proposed fix — rewrite the two
carriers to `3c_3^2+b` — would have propagated a superseded coefficient into the
framework's formalized coefficient family and its Lean class.

### On the "opposite sign" I corrected in the retraction

Both readings were right about different objects, and the bean's original was
the one that mattered. **As ladder coefficients** (with the box's leading minus
folded in) both are negative — that is what I checked. **As quoted in their
sources** they are opposite: `-(b^2+1/2) = -1.2527` against a bare
`+(3c_3^2+b) = +12.8676`. The quoted forms are what compare against the
extraction, so the original "opposite sign" reading was the useful one. Recorded
so the retraction is not itself over-read.

### Status

Cause identified, localized, and **direction settled**. What remains before any
edit:

1. **The SIGN of the headline** (hypothesis 4) — unresolved. Correcting the
   headline means recomputing a published number with the live c_5, and the sign
   convention has to be settled first or the recomputation just re-publishes the
   ambiguity.
2. **A producer that reaches N=5.** The block's declared one stops at N=3. Table
   3 and the headline need recomputing together from something that can actually
   produce them.
3. `q-beta-gamma-gamma-canonical-derivation.md` still publishes the retired
   `b^2+1/2` at **c_4**, where the supersession replaced it. Separate defect.
4. The stale `qbeta-ladder-convention-fee.witness.json` (holds 7.336484; live
   gives 7.133937), unchanged.

Bean stays open on (1)-(4). Everything here is C-frame.

## 2026-08-31 — (A) SETTLED and (B) ANSWERED. The sign is POSITIVE; the producer did not exist.

Producer: `computations/qbeta/qbeta_precision_ladder_n5.py`, **29/29**, mpmath,
convention C, registered `physical_proton`. PR #6424.

### (B) No producer reached N=5, and the DECLARED one is a different ladder

Searched the whole tree including `_deprecated/`. Three near-misses, none of
which evaluates the block's boxed product:

  * `probe_q_beta_operator_valued_N3.py` — the block's **declared** producer.
    Stops at N=3, no c_5. **And it never generated table 2 at all**: its own
    witness records `eps_N1 = 674.83 ppm` and `eps_N2 = 602.24 ppm` against
    table 2's `+73.79` and `+1.24` ppm, because its first rung is
    `cos(alpha_N1)`, `alpha_N1 = -0.0447444`, not the box's
    `cos(alpha - b*hbar^2/2)`, `alpha = (z-1)h/2 = -0.0404858`. This is a
    fourth defect, and it is upstream of the earlier entries' framing: the
    block's `computation.script` has been pointing at a different ladder.
  * `qbeta_ck_truncation_order_analysis.py` — DOES iterate k = 3,4,5 (so the
    previous entry's "no producer reaches N=5" was too strong), but it seeds
    `Q = Q_N2` from that same witness, so its column starts ~602 ppm, and it
    uses the superseded `c_5`.
  * `_deprecated/.../precision_ladder_ck_symbolic_probe.py` — carries the
    superseded c_5, computes no residual.

The new producer evaluates N = 0..5 at both pins over all four documented
(c_4, c_5) assignments and emits a witness.

### (A) The SIGN — settled, three ways, and the published minus is wrong

**A1. The convention is `(pred - CODATA)/CODATA`** — i.e. exactly
`qbeta_ladder_convention_fee_probe.ppb`. Not assumed. Read off table 2's own
coarsely-quoted rows at the MUON pin:

    table 2 N=0   +1677.5 ppm      computed  +1677.53852 ppm
    table 2 N=1     +73.79 ppm     computed    +73.7975604 ppm

At the proton pin N=1 is +73.828, which does not round to 73.79 — the table is
muon-frame, confirming the bean's earlier reading. (N=2's `1.24` is 3 s.f.,
where the 7.133 ppb epoch offset below is visible, so it is checked against its
published-epoch value instead and is not evidence about the convention.)

**A2. The ladder descends to CODATA from ABOVE.** Q_A sits +1677 ppm above
CODATA and every live rung factor `1 + c_k u^k` has `c_k < 0`, hence `< 1`. A
negative residual requires overshooting zero.

**A3. It never overshoots.** Over both pins and all four assignments the most
negative N=5 residual is **+6.5046 ppb**:

              c_4      c_5            N=3         N=4         N=5
    proton   live     live       43.72672   37.763639    37.70749
    proton   live     superseded 43.72672   37.763639   38.340392
    proton   retired  live       43.72672   37.134339   37.078191
    proton   retired  superseded 43.72672   37.134339   37.711093
    muon     live     live       13.153171   7.1900855   7.1339366
    muon     live     superseded 13.153171   7.1900855   7.7668394
    muon     retired  live       13.153171   6.5607857   6.5046368
    muon     retired  superseded 13.153171   6.5607857   7.1375396

**=> the corrected headline sign is POSITIVE.** Scope (a): scope-limited to the
boxed ladder under the four documented assignments at the two documented pins.
No proved invariant, so this is not a structural exclusion.

### Why the tables show negatives anyway — an input epoch, not a sign flip

Table 2's N=3 row (+6.02 ppb, 3 s.f., the tightest constraint in the block)
sits **7.1332 ppb below** the recomputed N=3. An input change shifts
`Q_A/Q_CODATA` by one relative amount and moves every rung by it, so one row
calibrates the column. Calibrated on N=3, the offset then predicts **two rows
it was not fitted to**:

    published-epoch N=4, RETIRED c_4   -0.5724 ppb    table 2's N=4:  -0.57
    published-epoch N=4, LIVE    c_4   +0.0569 ppb    (does not)
    published-epoch N=2                 1.24176 ppm   table 2's N=2:   1.24

So **table 2's N=4 NUMBER predates the c_4 supersession its own LABEL column
already carried** — the same failure mode as the c_5 slot, one rung earlier.

And the load-bearing consequence: under that offset the published-epoch N=5
lies in **[-0.629, +0.634] ppb** over all four assignments. **-6.6 ppb is
unreachable at the published epoch too**, so the minus is not an epoch
artefact. Table 3's published +0.04 ppb sits inside that window.

NOT FITTED: the *cause* of the 7.133 ppb offset is **not** identified. It is
not the stored `Q_AME` (0.78233355931 vs today's 0.7823334093099085 — a 191.7
ppb gap, and in the wrong direction), and not the CODATA-2018 -> 2022 m_e move
(1.35 ppb). Recorded as unexplained rather than tuned to anything.

### The headline's MAGNITUDE has no provenance — correcting the previous entry

The 2026-08-31 entry above reported `context c_5, muon pin = +6.6133 ppb` as
`0.202 %` from the headline and read that as the headline's provenance. **That
agreement is coincidental and should not be quoted as provenance.** It is a
*today's-inputs* number, while the headline is a published-epoch one; at the
published epoch the same quantity is `-0.520 ppb`. Nothing in the block's own
ladder produces `6.6 ppb` at the epoch the headline was written in, under any
of the four assignments. The magnitude is unrecoverable, so the correction
replaces it from the live producer rather than reconciling with it.

### What was changed

    q-beta-categorical-precision-ladder.md      headline: -0.0066 -> +0.0071 ppm
                                                (muon pin; +0.0377 at proton),
                                                convention now stated inline
    ...-table2-data.md, ...-table3-data.md      recomputed, live c_4/c_5, muon pin
    ...-ladder-context.md                       mixing-pattern c_5; "N=3 is first to
                                                beat 7.80 ppb" -> N=4; the Delta S
                                                paragraph; open question 2; a new
                                                "Provenance of the tables" section
                                                keeping the as-published column
    ...-ladder.ts                               computation.script -> the new producer;
                                                authorNotes status entry
    q-beta-gamma-gamma-canonical-derivation.md  retired b^2+1/2 at c_4 -> c_3*b^4

### FLAGGED FOR THE OWNER, not changed: the non-monotonicity claim

With the live `c_5 = -(b^2+1/2)` the column is **strictly decreasing at both
pins** — every factor is below 1. The "N=4 -> N=5 non-monotonicity (the
residual ticks back up)", which the context block and **AGENTS.md's own c_k
banner** both cite as *the experimental signature that c_k>=3 are q0-dependent
near-matches*, was produced by the superseded **positive** `c_5 = +12.87`,
whose factor exceeds 1. It does not survive that supersession.

The context block now says so. **AGENTS.md was NOT edited** — that is an owner
call, and the banner's tiering conclusion is independently supported by the
q0-anchor swing, which is untouched. Only the numerical signature is gone.

### Also noticed, NOT chased (out of remit, no provenance found)

Table 1's c_5 row publishes a `99.9 %` empirical match. The conj block records
a 2.4 % residual for the same coefficient, i.e. `97.6 %`. Left alone: fixing it
would mean re-litigating the c_5 question the task ruled settled.

### Still open

  * `qbeta-ladder-convention-fee.witness.json` still holds 7.336484 against a
    live 7.133937. NOT refreshed — that producer was not touched here, and the
    movement is main's.
  * The 7.133 ppb epoch offset's cause.
  * The headline's original magnitude — unrecoverable, now superseded.

Everything here is C-frame.

## 2026-09-13 — THE OWNER-FLAG ABOVE IS STALE, and it points the wrong way

Re-ran `computations/qbeta/qbeta_ck_c5_slot_and_size_mismatch_probe.py` on
`main` `1660c49f2f`: **4/4, exit 0, and it reproduces its committed witness
BYTE-IDENTICALLY** (clean tree after the run), so this is a current reading,
not a stale one.

### What the flag says, and what is true

The 2026-08-31 entry's **"FLAGGED FOR THE OWNER, not changed: the
non-monotonicity claim"** reports that with the live `c_5 = -(b^2+1/2)` the
column is **strictly decreasing at both pins**, and concludes that the
N=4 -> N=5 non-monotonicity — which AGENTS.md's `c_k` banner cites as *the
experimental signature that `c_k>=3` are q0-dependent near-matches* — "does
not survive that supersession".

**The probe names that conclusion and contradicts it, in its own assertion
text:** *"the OPPOSITE of what my PR #6424 concluded, which read the SIGNED
column"*. Measured:

    N      |resid| live        |resid| superseded
    3       2.6662082e-6       2.6662082e-6
    4          6.1698258          6.1698258
    5          6.2259747           5.555129

So by **magnitude** the live family INCREASES across N=4 -> N=5 (signature
HOLDS) and the superseded one decreases (does not). #6424 read the signed
column, where `-6.1698 -> -6.2260` is *decreasing*, and that is the whole
disagreement.

### AGENTS.md has already been corrected, in that direction

The banner now carries two retractions — the original "a convergent series
with exact `c_k` would be monotone" argument (unsound as a general
statement) and its own replacement size-mismatch argument (computed on the
superseded `c_5`; `|c_5 u^5| = 0.577` ppb tracks `+13.71`, not `-1.2527`).
It now rests on the **magnitude** crossing. So the flag asks the owner to
consider removing a claim that has since been re-established on a different
and better argument.

**The flag should not be actioned as written.** Leaving it is what risks the
damage: an owner reading this bean cold is told the signature is gone.

### NOT explained, and I am not asserting it is

Signed-vs-magnitude accounts for the **direction** flip. It does **not**
account for the **magnitudes**: this bean's table gives proton live/live
N=4 `37.763639` / N=5 `37.70749` ppb, while the probe gives `6.1698` /
`6.2260`, with an N=3 of `2.67e-6` against this bean's `43.72672`. Those are
different quantities, not the same column re-signed. Which base each uses is
**undetermined here**; do not read the two tables as comparable rows.

### The caveat that survives either way

The live crossing is **0.9101 %**, computed with `c_3` hardcoded at the
recorded proton extraction and at the proton pin only. The probe says so
itself. A full settlement re-extracts `c_3` at both pins. So "the signature
holds" is a thin result, not a robust one.

### Unchanged from the previous entry

  * `qbeta-ladder-convention-fee.witness.json` still holds `7.336484` against
    a live `7.133937`. Not refreshed; the movement is main's.
  * The 7.133 ppb epoch offset's cause.
  * The headline's original magnitude — unrecoverable, superseded.

Everything here is C-frame.

### Note on why this was worth a pass

I recommended this bean to the owner twice as *"the ladder block claiming
-6.6 ppb where the implementation gives +7.34 ppb, opposite sign"* — which is
the TITLE. The body records that settled on 2026-08-31 (sign POSITIVE,
headline corrected to `+0.0071` ppm). **I recommended it on its title without
reading its body**, which is the same defect as quoting a stale figure: the
title has not been updated in three revisions of the finding underneath it.

---

## 2026-09-13 — the "stale witness" claim is itself stale, at four sites

This bean states at four places (lines ~99, ~192, ~339, ~479) that
`qbeta-ladder-convention-fee.witness.json` *"still holds the 7.336484 figure,
so that witness is **substantively stale**, not merely drifted."*

**Measured on this tree — the witness holds the LIVE value and does not contain
7.336484 at all:**

| check | result |
|---|---|
| occurrences of `7.336484` in the witness | **0** |
| `/data/MUON_pin_(the_block's_own_-0.0066_ppm_frame)` | `7.1339366413953373436674732111283365208692987644780979634675` |
| `/data/published_frame_err_ppb` | `37.707489855749324657226491936959909548054647606026893018012` |
| recorded `scriptHash` vs live producer hash | `e8a05d91384c` vs `e8a05d91384c` — **MATCH** |
| `computedAt` | `2026-09-04T12:28:14Z` |

So the witness carries **exactly the `7.133937` this bean calls "live"**, and it
is **not stale by the corpus's own definition** — `scriptHash` is the field
`witness_dependency_drift.py` keys self-staleness on, and it agrees to the byte.
The `37.70749` cross-check also matches this bean's own line 22.

### What is settled, and what is NOT

**Settled:** the claim is false *as a statement about the current tree*, at all
four sites. Anyone acting on it would re-run a producer that needs no re-running
— and that is not free: this is exactly the idle-pass waste AGENTS.md's
witness-triage section is about.

**Not settled: whether the witness ever held `7.336484`.** `git log -S "7.336484"`
on the file returns **nothing**, and the only commit touching it in the fetched
history is `87bf883793` (2026-09-07, `qou-k54t`, *"my own probe had a float64 q0,
and my explanation of the residual was wrong"*) — at which the value is already
absent. **Agent clones here are shallow**, so an empty `-S` result is consistent
both with "never held it" and with "the removing commit is outside the fetched
window". This is the same shallow-boundary ambiguity AGENTS.md documents for
`scriptCommitSha`, and it cannot be resolved from this container. I am
therefore **not** claiming the original entry was wrong when written — only that
it has been wrong about the tree for at least the six days since `87bf883793`,
and the bean was never refreshed.

### Correcting my own handling of this bean, twice over

1. Earlier this session I **reported this witness as stale to the user, from this
   bean's text, without opening the witness.** The bean is not a primary source —
   AGENTS.md says exactly that about beans, including recent specific ones — and
   I applied the rule to my own claims all session while suspending it for this
   one.
2. Separately and earlier, I **recommended this bean to the user twice from its
   TITLE without reading its body**, where the sign contradiction had already
   been settled on 2026-08-31 (sign POSITIVE, headline corrected to `+0.0071` ppm).

Both are the same failure: treating a bean's surface as its state.

**No producer was re-run and no witness was committed as a result of this
check** — the only change a re-run would have produced is a provenance
downgrade, and the tree was reverted.
