---
# fwr4
title: 'mass-theory carries the paper''s long-range ordering problem'
status: open
type: task
priority: normal
created_at: 2026-08-09T21:35:00Z
updated_at: 2026-08-09T23:10:00Z
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

---

**Analysis done (`SP/fwr4-analysis.md`); application still open.**

Two findings settle the shape of the fix.

**The chapter's block-level `uses` graph is acyclic** — 746 blocks, 771
same-chapter edges, Kahn sort covers all 746. An ordering with *zero* forward
references provably exists, so none of these is a logical constraint; every one
is a placement artefact. That does not license a topological sort — three rounds
of narrative review on the within-section pass showed how much ordering the
prose carries that the graph does not — but it does mean each defect is a real
editorial question with an available answer.

**It is not two chapters.** The four faces are internally coherent
(217/207/147/48 internal edges), and 26 of the leaks come from just 19 blocks in
the algebraic face. Splitting would convert them to cross-chapter references and
resolve nothing.

**Recommended, not yet applied — four thematic consolidations, 15 blocks, 16
edges cleared including the paper's two longest jumps (543 and 477), zero
created:** pentagon/quantum-torus (7), Geom(K) (4), quantum-Bloch-group hoist
(3), LP → SDP (2). These are cross-section moves, so they need the same
narrative review the within-section pass got — that review is the remaining work
here, not more analysis.

**Deliberately not done:** the 49-block vertex-factorisation chain (H1). The
manifest records at line 425 that it was consolidated in from `climax-volume-mass`
in May 2026 and landed mid-chapter, and three section intros still narrate the
pre-consolidation order. Moving it back is a viable alternative. Author's call.

**Five edges want fixing as edges, not as order** — chasing them with moves
optimises toward a wrong fact. Two I verified directly against the text:
`prop:gram-determinant-plancherel-ratio` → `rem:gram-matrix-spectral-connection`
(497 positions) runs backwards — the target opens "*Remark (where the Gram matrix
fits…)*" and itself cites `prop:frobenius-gram-matrix`, while the source never
names it; and `prop:markov-pair-z2` → `rem:mass-endomorphism-jet-tower` is a
parenthetical "(cf. …)". Also reported: `rem:motivic-mass-rationale` (512) should
point at the cross-chapter statement rather than the in-chapter restatement,
`prop:frobenius-s-classification` (447) at `thm:wedderburn-mass-formula`, and the
two-row definitions (149/150) want `foreshadows:` for the notational `y_λ`.
Deletions and retargetings both need the adversarial second read that fwr1 used.
