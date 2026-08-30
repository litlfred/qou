---
# qou-ev2b
title: 'GAP: compound_shift_nf is convention C while both sources it claims to match are D — migration moves TR_M by 22.7-50.6%'
status: todo
type: task
created_at: 2026-08-30T09:20:48Z
updated_at: 2026-08-30T09:20:48Z
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
