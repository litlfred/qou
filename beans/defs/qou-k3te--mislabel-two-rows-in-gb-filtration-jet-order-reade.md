---
# qou-k3te
title: 'MISLABEL: two rows in gb-filtration-jet-order-reader name knots their braid words do not close to'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T15:30:55Z
updated_at: 2026-11-16T19:56:39Z
parent: qou-trd0
---

computations/gb-filtration-jet-order-reader.witness.json:41 names a row 'deuteron 6_2 sigma_1^-1 sigma_2 sigma_1^-1 sigma_2^2 in H_3'. That word closes to a 2-COMPONENT LINK (det 8). 6_2 is a KNOT (1 component, det 11). The row two below it, 'tritium 8_11 sigma_1^-1 sigma_2 sigma_1^-2 sigma_2^3', is also 2-component; 8_11 is a knot. The adjacent figure-8 row '(sigma_1 sigma_2^-1)^2' IS correct (1 component, det 5), so the file's notation convention is the standard one and these two rows are genuinely wrong rather than differently-conventioned.

Deuteron repair looks like a single exponent: sigma_1^-1 sigma_2 sigma_1^-1 sigma_2^3 (one more sigma_2) gives 1 component, det 11 -- exactly 6_2. NO repair proposed for the tritium row: two nearest-neighbour candidates (sigma_2^4, sigma_1^-3) restore a knot (det 23, det 25) but neither was identifiable as 8_11 from what was computed, so only the arity mismatch is claimed there.

Scope-(b) structural exclusion on a proved invariant: the number of components of a braid closure is a permutation invariant, hence independent of every crossing sign and every convention. A 2-component closure cannot be a knot. Needs no determinant table.

BLAST RADIUS (c), small. max_grade and filtered_basis_size are computed FROM the word, so they are correct facts about the word; the NAME is what is wrong. Risk is a reader taking 'max_grade = 3' as a jet-order fact about 6_2.

Measured with computations/probes/deuteron_braid_closure_identification.py (exact: permutation cycle count + reduced Burau over Z[t,t^-1]; no floats). SnapPy is not installed in this container, so nothing was checked against the census programmatically.

Found while amending docs/audits/2026-08-21-deuteron-knot-assignment-adjudication.md §8.2 (bean qou-e5jf, PRs #5350 / #5363). Distinct from qou-r0dn, which is wrong NUMBERS under right names; this is a wrong WORD under a right name.

## Progress Update (Round 50 — PR #8178)

- Added exact $S_n$ permutation cycle counter `closure_component_count(n, word)` to `computations/gb_filtration_jet_tracker.py`.
- Fixed the `deuteron 6_2` 3-braid word from `[-1, 2, -1, 2, 2]` (2-component link, det 8) to `[-1, 2, -1, 2, 2, 2]` (`\sigma_1^{-1} \sigma_2 \sigma_1^{-1} \sigma_2^3`, 1-component knot $6_2$, det 11) and relabelled the 2-component `\sigma_1^{-1} \sigma_2 \sigma_1^{-2} \sigma_2^3` row honestly so it no longer claims to be the 1-component knot $8_{11}$.
- Added `gb_filtration_knot_named_rows_have_single_component` / `gb_reader_knot_named_rows_have_single_component` assertions and `--self-test` to both `gb_filtration_jet_tracker.py` and `gb_filtration_jet_order_reader.py`, lifted `speedup_estimate` to `mpmath.mpf` serialized via `_precision.fmt`, and regenerated `gb-filtration-jet-order.witness.json` and `gb-filtration-jet-order-reader.witness.json` (`0` raw float64 fields).
- PR: https://github.com/litlfred/qou/pull/8178 (`6465362ef2e7902778c4f8796f81286e3aeb81bc`)
