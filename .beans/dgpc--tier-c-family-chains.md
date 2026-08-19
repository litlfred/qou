---
# dgpc
title: 'Tier C: family chains — one chain drains many witnesses'
status: in-progress
type: task
priority: normal
created_at: 2026-08-18T21:00:00Z
updated_at: 2026-08-18T21:00:00Z
---

Parent dgap. 66 witnesses across producers that emit MORE THAN ONE witness. The audit matches
producers by BASENAME, so one `script:` note in one chain claims the whole family — highest
yield per chain authored.

Queue (re-run the categorizer for current counts):
  26  _habiro_coefficient_extract.py
   6  nucleus_real_sdp.py
   4  compute_atom_chi_rust.py
   4  chi_at_q0_via_matrix_m_mpfr.py
   3  bar_pairing_binding_observable.py
   3  chi_via_rust_lossless.py
   2  A_operator_extract_at_level.py / alpha_k_jones_markov_h3.py / _h4.py / others

DONE: canonical_isotope_witness.py (120 shards) — see the worked example in the program doc
for what a composition chain may and may not claim.

---
2026-08-18 PROGRESS. Two families drained (branch claude/dgpc-habiro-family-chain-2026-08-18):
 - canonical_isotope_witness.py  -> 122 witnesses (composition/orchestration chain)
 - _habiro_coefficient_extract.py -> 26 witnesses (genuine symbolic extraction: Phase 5q closed
   form -> u=q^(1/2) rational form -> sequential cyclotomic division into the Habiro basis
   (u;u)_m, with the witnesses' own falsifiable checks all_integral + reconstruction_matches
   + tr_M_at_q0_rel_err = 0)
Trust audit: derivation-backed 7 -> 155; computational-only 2630 -> 1722.

METHOD NOTE (cost me a wrong conclusion, worth recording): I first judged the 27 habiro
witnesses "thin" because a quick check looked for habiro_coefficients under data.{...}. These
witnesses carry it at the TOP LEVEL. The witnesses are rich; the check was wrong. Inspect a
full witness before concluding a family is empty -- and note the two families needed DIFFERENT
chain shapes (composition vs extraction), so shape must be read per family, never assumed.

REMAINING families are small (6, 4, 4, 3, 3, then 2s) -- diminishing yield per chain authored.
After these, tier D (per-compute authoring) is where the bulk sits.
