---
# qou-stqr
title: Migrate the four witness-emitting G.h consumers to gram.h_mp() -- needs witness regeneration
status: todo
type: task
priority: normal
created_at: 2026-08-18T21:10:08Z
updated_at: 2026-08-18T21:11:15Z
---

Follow-up to qou-jtbo (resolved). `pyhecke.gram.h` is the float64 path and is
off from q0 - 1/q0 by 5.0e-17; `gram.h_mp(dps=50)` is the exact counterpart and
already exists.

qou-jtbo migrated the one consumer that emits no witness
(`framing_derivation_attempt_probe.py`) and documented the entry point. These
four remain on the float:

| consumer | witness refs |
|---|---|
| `computations/all_nuclides_sdp_admissibility.py` | 4 |
| `computations/probes/h6_deuteron_free_word_chi_lambda_probe.py` | 3 |
| `computations/probes/qbeta_lorentzian_gram_offset_probe.py` | 3 |
| `computations/mass_at_3A_proper.py` | 1 |

**Why it is not a mechanical sweep.** Each emits a witness, so swapping
`G.h` -> `G.h_mp()` moves the serialized numbers in the low digits. That needs
witness regeneration and a diff review per file, and `mass_at_3A_proper.py` is
on the L2 binding path — its `atom_braid_word_3A` feeds `_bond_type_L` and the
whole chain closed form, so a change there propagates to the binding dashboard.

**Suggested order** (cheapest blast radius first): the two qbeta/h6 probes,
then `all_nuclides_sdp_admissibility.py`, then `mass_at_3A_proper.py` last with
the binding witnesses re-checked.

**Expected size of the move:** ~5e-17 relative per use of h. Below the L1 1 ppQ
(1e-15) target, so this is a provenance/discipline fix rather than an accuracy
one — but the witnesses will still differ textually and must be regenerated
rather than left stale.

**Run `scripts/precision-gates.sh` (full, not --changed) after each.** Note
`--changed` keys on working-tree changes and reports 'skipped' on a clean tree,
which reads like a pass and is not one.
