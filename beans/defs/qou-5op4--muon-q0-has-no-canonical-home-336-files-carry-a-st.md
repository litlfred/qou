---
# qou-5op4
title: 'Muon q0 has no canonical home: 336 files carry a stranded literal, three values now live'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T19:59:35Z
updated_at: 2026-10-04T15:21:39Z
parent: qou-2002
---

## Standing on qou-khac, not replacing it

`qou-khac` already establishes the root cause and its 2026-08-16 correction is
the load-bearing part:

> The **proton** pin has exactly one home — `q_parameter.Q_50_DIGIT_STR`. The
> **muon** pin has a derivation in the substrate and three independent
> hand-typed copies with two different truncations. *"A literal cannot drift
> from a source it does not have — and these have none. That is this bean's
> actual finding, and it is the opposite of 'someone typed a wrong number'."*

This bean adds two things `qou-khac` does not have: the **witness-side
population**, and a **third live value** that has appeared since.

## Measurement 1 — the population is 336 files, not 18

`qou-khac` scanned hand-typed literals in `computations/**.py`: 18 near-misses,
3 non-truncations. Fixed-string grep for the ancestor `1.1099785955541805`
across the live tree (excluding `.git`, `.claude`, `_deprecated`):

| kind | files |
|---|---|
| `.json` | 222 |
| `.py` | 73 |
| `.md` | 41 |
| **total** | **336** |

The `.json` share is the part nobody has looked at: those are **witnesses**,
where the value is not a constant an author can relabel but a recorded
`parameters.q0` that downstream consumers read as fact. Two examples found
while draining tier C of the derivation-chain gap:

- `computations/wenzl-y-lambda-h9/h12.witness.json` — feeds six live nuclear
  consumers (`nucleus_real_sdp.py`, `probes/frobenius_gram_delta_lambda_probe.py`,
  the two `habiro/habiro_h9_*`, the two `deltalambda/he4_binding_k_*`), i.e.
  tritium and ³He at H₉, ⁴He at H₁₂
- `computations/a_operator/A-operator-extract-h9-{pn,pp}.witness.json` —
  `parameters.q_0`, `engine: numpy`

Each pads the 17-digit ancestor to 50 digits with a **different** float64 noise
tail (h9/h12 end `…7528159407960950937799328227995870`; the wenzl-bridge file
ends `…1695830018898879867637876138498395`), diverging at digit 18 — precisely
where float64 runs out. So the 50-digit presentation is ~17 real digits and 33
digits of padding, and both h9/h12 entries are currently **suppressed** in
`computations/q0-drift-baseline.json::parameters.q0`.

## Measurement 2 — there are now THREE values, and the derived one has moved

`qou-khac`'s correction reports that `q_muon_at()` returned the ancestor. **It
no longer does.** Verified in this container at 60 dps:

```
frozen literal (AGENTS.md, qou_substrate.witness)  1.10997859555733471989976322048322502665620840878015368660798114614493
y_lambda / A-operator ancestor                     1.1099785955541805…
q_muon_at() TODAY                                  1.10997859564273904668179512938000175270006556102901155697405
```

`rel(derived, frozen) = 7.69e-11`. `q_muon_at` is a live derivation —
`q = 1/(1 − √(Vol(4₁)/(m_μ/m_e)))` over `vol_4_1_at()` and
`MASS_RATIO_MU_E_STR` — so it re-values whenever those constants do, and they
have. That is the same stranding `qou-khac` diagnosed, one generation on.

Scale, so nobody mis-files this: 2.84e-12 relative is **0.00284 ppb** —
~4000× *smaller* than the 11.5 ppb μ–p substrate tension (no layer is
confused), and ~2840× *larger* than the 1 ppQ (1e-15) L1 compute-precision
target. A precision defect, not a physics one.

## What I tried, and why it was reverted (PR #5584, `fc732af896`)

I replaced the y_λ producer's fallback with the frozen 50-digit literal and
regenerated — 254 weights moved, max 5.22e-11 at λ=(30). **Retracted.** It
adds a fourth hand-typed copy of a literal that is itself stranded, which is
exactly the anti-pattern `qou-khac` names. The full reasoning is in the revert
commit message.

Two reasons not to reland it as an *import* either:

1. **PR #5500 is mid-migration** on the muon anchor to CODATA 2022 — audit
   red, 53 witnesses outstanding. Moving muon-pinned `y_λ` values now walks
   into a live sibling arc.
2. Deriving at import time makes a witness **re-value itself** whenever CODATA
   moves — non-reproducible against its own history. That is a real trade and
   it needs deciding, not assuming.

## Next — and the first step is a decision, not a patch

1. **Give the muon pin a home.** Either a frozen `Q_MUON_50_DIGIT_STR` beside
   `Q_50_DIGIT_STR` (reproducible, goes stale by design, needs a documented
   refresh), or a rule that every muon consumer calls `q_muon_at()` (always
   current, witnesses re-value). Both are defensible; the corpus currently has
   *neither*, which is why there are three values.
2. Convert the `.py` copies to imports of whichever wins. `qou-khac` lists
   them.
3. Only then touch the 222 `.json`. Sequence it behind #5500 and behind the
   `qou-1c4y` migration, whose four constraints already cover "do not split the
   change" and "never re-pin an anchor-DEFINING witness".
4. When h9/h12 are corrected, **remove** their two `q0-drift-baseline.json`
   lines rather than re-baselining — baselines drain, never grow.

## Close condition

The muon pin has one named source; the `.py` copies import it; the witness
population is either migrated or explicitly labelled as recording a superseded
pin; the two baseline lines are gone because the values are right.


## The home EXISTS now — the migration does not (PR #5639, 2026-08-24)

Owner picked both 'frozen constant' and 'consumers call q_muon_at()'. Reconciled:
the frozen string is the one named home; consumers reach a muon q through named
substrate API rather than hand-typing — the constant when a value must stay
reproducible, `q_muon_at()` when the caller wants today's CODATA-implied pin.

**Landed:** `Q_MUON_50_DIGIT_STR` + `q_muon_frozen_at(dps)` in
`qou_substrate.constants`. Frozen value matches the AGENTS.md literal EXACTLY
(rel 0.0). Also present on the no-mpmath path, where the string survives intact
(unlike Q_50_DIGIT_STR, which degrades to f64 there).

**Deliberately NOT landed:** `q_muon_at()` semantics unchanged (flipping it moves
every muon producer by 7.694e-11), and the 336 files untouched. Both sequence
behind PR #5500 (muon anchor -> CODATA 2022, audit red, 53 witnesses) and behind
qou-1c4y.

Close condition is unchanged and now partly met: the pin HAS one named source.
Remaining: the .py copies import it; the 222 .json migrated or labelled; the two
q0-drift-baseline lines removed rather than re-baselined.

**Side finding:** `sync-qou-mass-vendor.py --check` exits 1 on clean `main` —
3 drifted entries. Verified by stashing. Fifth instance of 'the checker exists,
is blocking, and main fails it anyway'.


## Progress Update — 2026-11-16 (PR litlfred/qou#8176)

- **Lean 4 Formalization (`0` `sorry`, `0` vacuity audit hits/advisories)**:
  - `folio/quantum-observable-universe/lean/QOU/MassTheory/MuonAnchorInversionAndStraddleClassification.lean` (wired into `QOU.lean`) proves:
    - `cal2MuonQ_roundtrip_and_excess`, `cal2MuonQ_secant_and_rel_shift`, and `cal2MuonQ_strict_three_value_ordering` (`qou-5op4`)
    - `crossAnchor_drift_magnification_and_inv_hbar_sq_secant` (`qou-72rd`)
    - `habiroSymbolicPayload_stamp_independent_and_secant` (`qou-mha1`)
    - `markovZD_over_markovZC_and_diff` and `fourMethod_straddle_cross_ratio_and_rel_delta` (`qou-3zby`, `qou-dau6`)
- **50-dps Verification Probe & Witness (`0` raw `float64` fields)**:
  - `computations/probes/muon_anchor_inversion_and_straddle_classification_probe.py` -> `computations/probes/muon-anchor-inversion-and-straddle-classification-probe.witness.json` (`allPassed: true`, 4/4 assertions, `scriptHash: 3b8c800c79a2`, `scriptCommitSha: 80719a03fb31a87a5718702e605db5cbed1f57ce`).
- **PR**: `litlfred/qou#8176` (`0e75c0ddb6a55fd2ce17a4041ac822379106c89c`).
