---
# qou-gpwk
title: q0 proton layer agrees only to ~1e-16, four orders coarser than the muon layer's 9.111e-20
status: completed
type: bug
created_at: 2026-08-08T18:48:54Z
updated_at: 2026-08-08T18:48:54Z
---

Follow-up from qou-n1c4. With every leg on the proton pin, chi_dual_path_xref_audit reads 3.4e-17 (proton) .. 2.0e-16 (He-4). The muon layer used to reach 9.111e-20 at n=9 and n=12, so proton is ~4 orders coarser and the floor looks like an f64 leak.

Prime suspect: canonical_braid_crossings._avg_color_delta is documented to reach only ~5e-16 because it reads the float64 q_parameter.Q rather than the 50-dps string; AGENTS.md says deep-1ppQ callers should call flavor_split_leading(local_q0_50dps) directly.

But that is probably NOT the whole story: proton and neutron have no inter-nucleon crossing, so no colour-weighted delta at all, and they still sit at 3.4e-17 / 6.8e-17. Something common to every leg is capping at ~1e-16.

Worth checking: the muon q-pinning witness carries 70 digits while q_parameter.Q_50_DIGIT_STR carries 50 -- but 50 digits should still give ~1e-50, not 1e-16, so a float64 is being crossed somewhere in the proton path.

Acceptance: chi_dual_path_xref_audit reaches ~1e-19 or better on the proton layer, matching what the muon layer achieved.


## RESOLVED — it was float64, in two places, at source

Not a q0-precision problem at all. The braid word itself was float64.

1. **`pyhecke.gram.h` is a Python float** (2.61e-16 relative vs the 50-dps
   closed form) and was used directly as `h_loc` in BOTH
   `nucleon_gen_chains` (intra-nucleon crossings) and `atom_braid_word_3A`
   (inter-nucleon). `atom_braid_word_3A` then cast everything through
   `float()` on the way into the word — including `c`/`d` values that were
   already exact ints.

2. **δ came from `_avg_color_delta()`**, which evaluates at the float64
   `q_parameter.Q` and reaches ~5e-16. Small term, dominant once the crossings
   were exact: δ enters as −h(½ − δ/4), so δ/4 is ~6.9e-4 of the offset and
   1e-16 in δ lands at ~7e-20. The tell was three DIFFERENT atoms sitting at
   an IDENTICAL 3.476e-20.

A third bug surfaced only after the casts were removed: an mpf carries the
precision of the OPERATION, not just its operands, so `-h_loc / 2` formed
outside the precision context was rounded to the ambient dps — 15 for the
module-level `_PROTON_G0` constants built at import. All templates are now
constructed inside one guard.

    layer straddle        1.704e-07
    layers aligned        1.024e-16
    exact crossings       3.476e-20
    + exact delta         3.229e-50      (deuteron)

Final, all six atoms AGREE: proton 6.376e-51, neutron 3.030e-50, deuteron
3.229e-50, tritium 6.329e-50, helium-3 7.099e-50, helium-4 6.740e-50 — thirty
orders past the muon layer's old 9.111e-20.

`reject_float64_q()` now refuses a float64 `q` at the word builders, including
the laundered `mpf(str(q_parameter.Q))` form (detected by float64 round-trip),
with `allow_float64=True` as an explicit escape. That closes the hole whereby
any caller could undo the source fix from outside — three did.
