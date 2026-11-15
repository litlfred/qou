---
# qou-ev2b
title: 'GAP: compound_shift_nf is convention C while both sources it claims to match are D — migration moves TR_M by 22.7-50.6%'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T09:20:48Z
updated_at: 2026-10-10T07:47:21Z
parent: qou-cdx1
---


## The finding

`computations/compound_shift_nf.py:67` claims the NF basis "matches
pyhecke.gram & hecke_core_symbolic conventions". Measured 2026-08-30, **both
named sources are convention D and this module is convention C**:

| file | z | since |
|---|---|---|
| `tools/pyhecke/python/pyhecke/gram.py:199` | `q0**3/(q0**2+1)` — **D** | 2026-08-15 |
| `computations/substrate/hecke_core_symbolic.py:105` | **D**, "Was convention C ... excised" | — |
| `computations/compound_shift_nf.py:271` | `1/(sq + 1/sq)` — **C** | still |

**This is the SECOND instance of the same defect shape in this one file.** The
first was the TR_M[5] Markov bug (`qou-looi`, fixed on PR #6058): the file
claimed to match `pyhecke.gram` and returned `z**3` where the recursion gives
`h*z**2 + z`, three months after gram.py was fixed. The claim at line 67 is
load-bearing and has now been wrong twice, in two different ways.

## Why it was NOT migrated on sight

Measured blast radius at the substrate pin — this is not drift:

    z_C = 0.499320334184   z_D = 0.612688037146   ratio 1.227

    TR_M[0]  1.0          -> 1.0            0 %
    TR_M[1]  0.499320334  -> 0.612688037   +22.7 %
    TR_M[2]  0.499320334  -> 0.612688037   +22.7 %
    TR_M[3]  0.249320796  -> 0.375386631   +50.6 %
    TR_M[4]  0.249320796  -> 0.375386631   +50.6 %
    TR_M[5]  0.551443414  -> 0.691166478   +25.3 %

Three reasons to decide rather than swap:

1. **A z-swap is not always a valid migration.** `qou-cds1` records that the
   C-frame ladder and the mass channel's three-row forcing are mutually
   exclusive (`QOU.QBeta.decayLadder_zC_threeRow_ne_zero`, sorry-free), so
   substituting z_D into a C-derived object can be incoherent rather than
   merely different. Whether that applies to the compound shift specifically
   is exactly what needs establishing.
2. **This module's constants are convention-FROZEN, and a prior agent already
   found that they LOOK convention-independent.** Lines 128-134 (qou-cds1,
   2026-08-24): `SHIFT_NF_PROTON_H3` / `SHIFT_NF_NEUTRON_H3` are TRANSCRIBED
   from `shift-from-nf-basis.witness.json`, so this module's own witness showed
   "0 fields moved" under the D conversion — "which read as
   convention-INDEPENDENT and is actually convention-FROZEN". So a post-swap
   "nothing moved" result here would be evidence of nothing.
3. It moves committed numbers by up to 50 %, on a PR that is otherwise ready.

## Next step

Establish whether the compound shift is C-derived in the sense `qou-cds1`
means, or merely evaluated at a z. If the latter, migrate and re-run; if the
former, it needs the same re-derivation the ladder does. Re-read
`shift-from-nf-basis.witness.json` rather than trusting the transcribed
constants, per the in-file warning.

## RESOLVED ON MAIN 2026-08-30 — a sibling made the call and migrated it

Superseded before it was worked. `main` now carries `compound_shift_nf.py` with
BOTH halves:

    :320  z = q0 ** 3 / (q0 ** 2 + 1)          <- convention D
    :322  out = [..., h * z ** 2 + z]          <- the TR_M[5] fix

So the desync this bean reported is closed: the module now agrees with
`pyhecke.gram` and `hecke_core_symbolic` on the convention, which is what the
line-67 claim asserted all along. The bug documentation is retained in the file.

Taken from `main` wholesale on the pre-merge integration rather than reconciled,
since main's version is strictly ahead of this branch's on both axes.

`markov_trace_weights_wenzl.py` moved the same way (:291 and :497 are now
`q ** 3 / (q ** 2 + 1)`), which invalidated this branch's ledger entry for it —
pruned rather than rehashed, because the site no longer carries convention C at
all.

Worth recording the shape: this bean asked for a decision on a 22.7-50.6 %
numeric move, and the answer arrived from a parallel agent while the question
sat open. The measurement was still the right output — it is what made the
incoming migration checkable rather than something to take on trust.


## 2026-10-10 re-audit verdict: **CLOSE** (bean `qou-am5t`)

`compound_shift_nf.py:321` now reads `z = q0 ** 3 / (q0 ** 2 + 1)` —
convention D. The module also carries a C-vs-D determinant comparison table at
`:301-304` naming `z_D / h.z^2+z` as 'the true D form'. The bean's claim
('both named sources are D and this module is C') is measurably false; the
module migrated. It appears in no convention-C binding report.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.
