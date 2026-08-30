---
# qou-54g5
title: 'qou-cds1 fallout: the ladder block claims -0.0066 ppm at the muon pin; the implementation gives +7.34 ppb'
status: todo
type: task
priority: high
created_at: 2026-08-26T23:21:11Z
updated_at: 2026-08-30T04:50:37Z
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
