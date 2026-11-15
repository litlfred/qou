---
# qou-c3ey
title: 'GAP: typed σ_shell literal 5.889176e-3 (y·σ at A_magic=2) has no owning witness, and under convention D y_(3,2,1)=0'
status: todo
type: task
created_at: 2026-11-15T11:08:03Z
updated_at: 2026-11-15T11:08:03Z
parent: qou-s4ws
---

Owner asked for this bean 2026-11-15 ("3 y").

## What
`5.889176e-3`, labelled `y_shell·σ_shell` at A_magic = 2, is typed into three producers and owned by no witness:
- `computations/d_from_scratch.py` (`SIGMA_SHELL_BARE_AT_Q0_AMAGIC2`; its witness records the caveat). It contributes Δm_shell = 0.029880 MeV to B(D) = 2.41223 MeV.
- `computations/unified_low_isotope_predictor.py:330`
- `computations/categorical_q_decay_ba_low_isotopes.py:167` (comment: "A_magic=2: y·σ ≈ 5.9e-3")

Grep of `computations/**/*.json` finds it only in `d-from-scratch.witness.json`, the consumer. No producer was found. `sigma-shell-A2-closed-form.derivation.json` carries C_(3,2,1) = 0.0374882414…, a different quantity.

## Why it matters now
#7849 (merged `6ae2616b7cc`) proved `sigma_shell_staircase_vanishes_conventionD`: under convention D the staircase weight y_(3,2,1) = 0 (every three-row Ocneanu weight vanishes at z_D). If this literal really is y_(3,2,1)·σ, then under the canonical convention it should be **0**, not 5.9e-3. In that case the three consumers carry a convention-C value, and the 0.030 MeV shell term in d_from_scratch is a C-frame artifact.

## Next honest step
1. Find where 5.889176e-3 was first computed (`git log -S5.889176`) and in which convention and word.
2. If it is y_(3,2,1)·σ under C: the D value is 0. Changing the consumers moves B(D) by −0.030 MeV and needs an owner decision, since it changes a compared number.
3. If it is a different quantity: give it an owning witness and a producer.

Default if nobody acts: the literal stays, with the caveat in d-from-scratch.witness.json.
