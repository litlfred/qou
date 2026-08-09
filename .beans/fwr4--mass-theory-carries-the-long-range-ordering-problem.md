---
# fwr4
title: 'mass-theory carries the paper''s long-range ordering problem'
status: open
type: task
priority: normal
created_at: 2026-08-09T21:35:00Z
updated_at: 2026-08-09T21:35:00Z
parent: fwr1
---
After the block moves (`fwr2`) and transpositions (`fwr3`) are taken out, 177
forward references remain. They are not spread evenly: **the fifteen longest
jumps in the paper are all in `mass-theory`**, from 304 to 543 positions.

| positions | edge |
|---|---|
| 543 | `conj:hoefsmit-scattering-pipeline` (128) → `conj:geom-yekutieli-alignment` (671) |
| 512 | `rem:motivic-mass-rationale` (10) → `prop:mass-endomorphism-tower` (522) |
| 497 | `prop:gram-determinant-plancherel-ratio` (84) → `rem:gram-matrix-spectral-connection` (581) |
| 477 | `rem:sdp-degeneracy-at-metallic-coincidence` (125) → `prop:confinement-sdp` (602) |
| 447 | `prop:frobenius-s-classification` (40) → `prop:confined-knot-binding` (487) |

Distance spread of all 177: 52 at 1–10 positions, 61 at 11–50, 33 at 51–200,
**31 at 200+**.

A chapter of ~770 blocks where 31 edges reach more than 200 positions ahead is a
sequencing question, not a set of edge fixes: several of these are cases where a
mid-chapter block computes with apparatus the chapter only sets up near its end
(`def:two-row-projection` at 150 sources `$y_\lambda$` by name from 500;
`rem:sdp-degeneracy-at-metallic-coincidence` at 125 runs its whole analysis on
dual variables set up at 602). Worth deciding whether `mass-theory` should be
split, or resequenced around the apparatus it shares.

Every edge here was confirmed by a reader as a genuine dependency — these are
real, not artefacts. The list is regenerable from `detangler-no-forward-ref`.
