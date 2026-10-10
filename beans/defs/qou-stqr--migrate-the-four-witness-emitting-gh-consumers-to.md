---
# qou-stqr
title: Migrate the four witness-emitting G.h consumers to gram.h_mp() -- needs witness regeneration
status: completed
type: task
priority: normal
created_at: 2026-08-18T21:10:08Z
updated_at: 2026-08-18T22:12:04Z
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


## 2026-08-18 — RESOLVED, and 3 of the 4 listed consumers needed nothing

The bean listed four witness-emitting `G.h` consumers. Reading each (rather than
trusting the grep that produced the list) shows only ONE was a real violation.

**Already fixed, independently, before I filed this:**
* `mass_at_3A_proper.py` — a prior agent fixed it at the source under a
  "NO FLOAT64 (owner directive)" banner: exact crossings via
  `mpf(str(Q_50_DIGIT_STR))` inside `workdps(60)`, plus a `reject_float64_q`
  guard. Measured there: deuteron 1.024e-16 -> 3.229e-50. **My grep hit its
  comment explaining the removal.**
* `qbeta_lorentzian_gram_offset_probe.py` — likewise already migrated from a
  `gram_at_h` that mutated `_gram.h` to `gram_matrix_mp(q=...)` at mpmath
  precision. **Again a docstring describing its own fix.**

**f64 BY DESIGN, not a violation:**
* `all_nuclides_sdp_admissibility.py` — `build_nf` declares "native f64 if
  available" and feeds `np.asarray(gram.TR_M, dtype=float)` into numpy/Clarabel,
  which cannot take mpf. This is the sanctioned "cast at your own boundary,
  where the loss is visible" case.

**The one real violation, now fixed:**
* `h6_deuteron_free_word_chi_lambda_probe.py` — had
  `h = float(gram_h); q0 = (h + math.sqrt(h*h + 4.0))/2.0`: the float64 module
  constant, then q0 recovered from it by inverting h = q - 1/q through a float64
  `math.sqrt`. The inversion is also backwards — q0 is the primitive the corpus
  publishes at 50 digits; h is derived. Now taken in the canonical direction
  inside `workdps(60)`, and the witness's substrate block serialized with
  `_precision.fmt`.

**A trap I fell into en route, worth recording.** My first attempt used
`mp.mpf(str(Q_50_DIGIT_STR))` at the probe's ambient dps — which is mpmath's
default 15. That bakes in a 15-digit q0 (3.0e-17 error) which `_precision.fmt`
then PADS to 60 digits: strictly worse than the float64 it replaced, because the
float was honest and the padded value is not. `mass_at_3A_proper.py` documents
this exact trap at its own `workdps(60)`. Fixed by matching that pattern.

**Witness regenerated and diffed:** 37 numeric fields moved, largest relative
5.19e-14 (a ~1e-16 h error amplified through the H_6 characters). Two ratchet
effects, both improvements, both committed: `q0-value-drift` now records q0 at
60 digits instead of 16, and `witness-raw-float64` drained_files 35 -> 36.


## Correction (2026-08-18, post-close) — h6's PAYLOAD was still float64

I closed this bean reporting h6 fixed. The fix was **cosmetic**: it corrected
the q0/h ENTRY POINT while the characters still came from
`build_seminormal_matrices_cached` + `chi_lambda_of_word`, which are float64
by construction — `math.sqrt` against a fixed 1e-15 threshold, and
`float(np.trace(...))` over a numpy matrix. An mpf q0 does not survive contact
with numpy. The witness then serialised a 50-digit substrate beside a float64
payload, which is the exact failure the directive names.

Two further leaks were live on the same path: `float(v)` on every Wenzl y_lambda,
and `0.0` trace seeds.

Fixed properly by new module `computations/hoefsmit_mpmath.py` (BlockCacheMP with
mp.sqrt and a precision-scaled threshold, seminormal_matrices_mp,
chi_lambda_of_word_mp), same SYT ordering as the cached builder. The float64 path
still runs as a MEASURED cross-check: max relative gap on chi_bound = 8.71e-15,
recorded as the float64 floor rather than as a disagreement (rule 4). Values
unchanged to that floor, now at full precision. 1.7s for the H_6 sweep.
