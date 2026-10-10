---
# qou-ssex
title: 'GAP: 5 computations/ producers carry the TR_M[5]=z^3 bug — a third surface qou-m7py does not list'
status: completed
type: task
priority: normal
created_at: 2026-08-30T07:09:49Z
updated_at: 2026-08-30T07:56:33Z
---

## What is new here, and what is NOT

The `TR_M[5] = z^3` bug is thoroughly known: `docs/audits/2026-05-19-trm5-markov-bug.md`
fixed `pyhecke/gram.py`, and bean **`qou-m7py`** carries a deep treatment of the
Rust crate plus the sequencing constraint. **Nothing here rediscovers that.**

What is new is a **third surface neither covers**: five `computations/` producers
holding their OWN local copy of the buggy weight vector, on the same H_3 NF basis.
`qou-m7py`'s consumer table lists five Python files — `borromean-axial-coupling.py`,
`delta_lambda_master_formula_h3_probe.py`, `delta_lambda_full_variance_phase5e_1.py`,
`bound_state_observable_validator.py`, `audit_frobenius_pairing.py` — and there is
**zero overlap** with the five below. Those are consumers of `gram_inverse`; these
define the trace themselves.

Found while working `qou-t9r1`'s site list; measured before `qou-m7py` was located,
which is why the probe's commit message does not cite it.

## The five

| file | line | symbol |
|---|---|---|
| `computations/compound_shift_nf.py` | 257 | `tr_m_weights_mp` (3 witnesses) |
| `computations/electron_sigma_f_chain.py` | 107 | `TR_M` |
| `computations/jet_knot_invariants.py` | 56 | `tr_basis` |
| `computations/atom_mass_derived.py` | 102 | `TR_M_3` |
| `computations/basis_knot_tables.py` | 54 | `TR_M` |

Each confirmed on the identical basis `[(), (0,), (1,), (0,1), (1,0), (0,1,0)]`
before listing. The 14 further hits under `computations/_deprecated/` are out of
scope. **`jet_knot_invariants` is the sharpest**: it imports FROM `pyhecke.gram`
— the fixed module — and then defines its own wrong `tr_basis`, shadowing the fix
it already had in hand.

## Measured (probe: `computations/probes/trm5_zcubed_live_producer_audit.py`)

Correct/committed = 4.43 under C, 3.01 under D — matching `qou-m7py`'s
independently-recorded "+200.5 %, a tripling".

The coupling `qou-m7py` names is reproduced here on a LIVE producer.
`compound_shift_nf.gram_mp` feeds an LP:

| z | TR_M[5] | det | rank |
|---|---|---|---|
| C | `z^3` (committed) | 0.360801088987 | 6/6 |
| C | `h z^2+z` (correct) | 0.189205219144 | 6/6 |
| D | `z^3` (committed) | 0.152018239085 | 6/6 |
| D | `h z^2+z` (correct) | 1.4e-56 | **5/6** |

So the trace bug **masks the D Gram singularity**, which is why `qou-t9r1`
classified `compound_shift_nf` as a clean z-swap candidate. It is not.

Cross-check: with the correct weight under C its |det| equals
`gram_h3_det_factorization`'s `0.189205219144` to every digit — they are ONE
Gram, and disagreed only because one carries the bug.

## Disposition — NOT a sweep

`qou-m7py`'s sequencing constraint applies verbatim: the trace fix and the
quotient must land together, or a singular Gram drops into a path with nothing
to handle it. Each of the five needs its own answer to "what does this file do
when its Gram loses rank", and `compound_shift_nf` in particular solves an LP
against it.

`qou-m7py` step 1 is already **[OWNER]**-gated on the `gram_inverse` deletion at
a measured 73.3 % re-derivation cost. These five sit downstream of that same
decision and should not be flipped ahead of it.

## Next honest step

Register the five so the standing audits account for them, and pause. Do not
migrate `compound_shift_nf`'s `z` under `qou-t9r1` while its trace is wrong —
that would produce a doubly-wrong Gram that looks healthier than either defect
alone.

## RESOLVED 2026-08-30 (PR #6110) — owner: "Fix all five with the quotient. Real work."

**Correction to this bean's own framing: 2 of the 5 are DEAD constants.** `basis_knot_tables.TR_M` and `jet_knot_invariants.tr_basis` are defined and never read — both move ZERO substantive fields on re-run. Fixed anyway (a wrong constant nothing reads is a trap for the next consumer), but corrected, not repaired.

The 3 live ones: `atom_mass_derived` (103 fields move, 10/10 pass), `electron_sigma_f_chain` (diagonal SDP cost, no Gram), `compound_shift_nf` (127 fields move).

**The quotient work.** Fixing the trace alone broke 5/19 assertions in `compound_shift_nf`, exactly as `pyhecke/gram.py`'s banner predicts. Repair is `_min_norm_lstsq_mp` — a minimum-norm SVD solve, the mpmath twin of `G_PINV`, i.e. the solve on H₃/rad. `mp.qr_solve` RAISES on a rank-deficient system and the old except-branch returned NaN, reporting "no answer" for a system whose answer is merely non-unique.

I patched the DUAL solve first and it did not help — the dual was already fine; the NaN was in the PRIMAL recompute, whose `(Gx)_i = 0` rows are rows of the rank-5 form. 19/19 now pass, duality gaps at the 50-dps floor.
