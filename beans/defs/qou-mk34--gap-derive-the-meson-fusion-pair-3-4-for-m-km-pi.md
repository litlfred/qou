---
# qou-mk34
title: 'GAP: derive the pair (3,4) in m_K^2/m_pi^2 = [3]_q[4]_q from a definition of K and pi (currently scan-selected)'
status: completed
type: task
priority: normal
created_at: 2026-11-20T08:13:33Z
updated_at: 2026-11-28T10:56:30Z
tags:
    - compute-accuracy
parent: qou-3l2l
---

**Open, by six-path corpus-grep 2026-11-20** (audit docs/audits/2026-11-20-mk-mpi-derivation-status.md §2, PR #8529).

What is proved (QOU.BraidKnot.MesonFusionIndexSelection, sorry-free, generic CommRing):
- qCG_unnormalised_general: [m]_q[m+d]_q = sum_{k<m}[d+1+2k]_q for all m,d. The credited
  meson_qCG_3x4 is its m=3,d=1 instance (meson_qCG_3x4_is_family_instance), so the Lean credit on
  the strong core carries no selection information.
- scanPair_four_not_dictionary_index: 4 is not a quark torus-knot index (all odd) nor a meson
  total crossing (6,8,10) of the lepton-meson dictionary; kaon constituents are (3,5). Scope (b)
  for the index reading only.

Measured (computations/meson/mk_mpi_derivation_status_probe.py, 70 dps, proton q0): core alone
-101553.36 ppb (385.26x miss); in {[a][b]: a<=b<=12} (3,4) ranks 1/78 at 203.10 ppm, runner-up
(2,6) at 26742 ppm; local gap 7.61 %, chance-within-deviation ~0.53 %. Dictionary-indexed
readings miss by 27-89 %.

What would close it: a definition of K and pi as Hecke/Wedderburn objects (strands, partitions,
quark content s vs u/d) from which [3]_q[4]_q follows without reference to PDG. Choosing another
pair because it fits better is forbidden (selection against target). Until closed, the row
m_K/m_pi is not parameter-free regardless of the alpha_em sorry.

**2026-11-27 (compute-accuracy C5, PR #9449, branch claude/mk-mpi-status-2026-11-27).** Still open; label **Selected**.
New Lean `QOU.EightfoldWay.MesonRatioSelectionStatus` (generic Field, sorry-free): every function of the pion/kaon
clasp words agrees at q = 1 (`clasp_reading_pion_eq_kaon`), so no polynomial ratio N/D with N(1) = D(1) != 0 equals
[3]_q[4]_q as an identity in q (`unit_ratio_reading_ne_p34`). Scope (b), invariant = q=1 odd-clasp collapse vs
[3]_1[4]_1 = 12. Does NOT exclude a chosen channel (dim_q(V2 x Sym2 W3*) = [3][4], 2026-11-24); choosing it is the
premise this bean asks to derive. Audit docs/audits/2026-11-27-mk-mpi-selection-status.md.

## 2026-11-27 — option 2 (channel choice), PR #9477

Channel choice does NOT select `[3][4]`. The `sl₂ × sl₃` isotypes of classical dim 12 are exactly five. The four coloured ones (`V₂⊗6̄`, `V₂⊗6`, `V₄⊗3̄`, `V₄⊗3`) all have `dim_q = [3][4]`. The colourless `V₁₂` has `[12]`. Lean: `MesonTwelveDimChannels` (sorry-free). Remaining premise: classical multiplicity 12 and a coloured channel. Still Selected. Open: derive 12 (or `[3][4]`) from a definition of K and π. The quark labels (3,3)/(3,5) supply no map to 12 in the corpus.

## 2026-11-27: Hecke-object route (PR #9502)

Carl took the recommended route. The result is a negative of scope (a), and the row stays Selected.

- **Clasp-word traces.** On the clasp words, every block trace and every Markov trace gives a kaon/pion ratio of 1 at q=1.
- **Label embeddings.** `MesonLabelEmbeddings.lean` tries four ways for the quark labels to enter. Their ratios are 1 (clasp exponents), 5/3 (colour dimensions), 4/3 (strand count) and 56 (Hecke dimension). None is 12.
- **General exclusion.** `classical_ratio_ne_p34` rules out any reading whose classical ratio is not 12.
- **Where 12 does appear.** Only as the product of the half-sums, 3·4. That is the post-hoc V₃⊗V₄ reading.

Still open: a definition of K and π in which the labels enter additively, are halved, and are then multiplied. A card for the alternatives is posted in the thread.

- 2026-11-27 (PR #9502, second commit): `no_meson_total_ratio_twelve`: for labels in {3,5,7}, no ratio of label sums (max 14/6) and no ratio of label products (max 49/9) between two mesons is 12. Still open: the additive/halved/multiplied reading.

Closed post-merge: landed on `origin/main` in PR #9502 (`32c51829a9dc6887adc237c6d5c4eb243331cda5`).
