---
# qou-hkwd
title: 'RENAME TRANCHE: the atomic object is a Hecke word, not a braid word — 5 mathematically-false lines, not a 672-file rename'
status: todo
type: feature
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T12:25:33Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-mub3
---

Owner instruction 2026-09-06: "do a separate rename tranche. coordinate with all
open PRS relevant."

ROOT (issue #6941 §10). atom_braid_word_3A returns (c, d, gen_idx) and d takes
FOUR values at the proton q0:
    d = 0                     -> sigma       positive crossing        BRAID
    d = -h  = -0.2090602988   -> sigma_inv   negative crossing        BRAID
    d = -h/2 = -0.1045301494  -> averaged    (sigma+sigma^-1)/2       NOT
    d = -0.1044582478         -> averaged_wt colour-weighted          NOT
0 of 14 atoms protium->Fe-56 is free of the last two, so the object lives in
H_n(q) and outside the image of B_n. Its closure is not defined.

WHY NOT A RENAME. "braid word" appears in 2169 files; atom_braid_word_3A in 672.
MOST ARE CORRECT -- the trefoil really is sigma_0^3 in B_2, the Borromean rings
really are (sigma_0 sigma_1^-1)^3 in B_3. A blanket rename would corrupt true
statements to fix false ones.

THE ACTUAL DEFECT is much smaller: lines asserting the ATOMIC object lives in a
BRAID GROUP. That is wrong as MATHEMATICS, not naming. Detector:
computations/audits/braid_vs_hecke_word_audit.py, 3/3.

  5 DEFECTS
    mass-theory/per-braid-mass-tower.md:1              "W in B_{3A} the atomic braid"
    mass-theory/graded-hecke-energy-truncation-bound.md:1  "the CLOSURE of B_K in B_n"  <- sharpest
    mass-theory/conj-atom-braid-exterior-algebra.md:2  "T_w(Z,N) in B_{3A}"
    mass-theory/sigma-shell-from-beta-chain-derivation.md:1
    mass-endomorphism/conj-rho-k-pair-gen-canonical-form.md:2
  1 SIBLING-OWNED, not touched
    mass-endomorphism/atomic-mass-gb-nf.md:3  -> PR #6821
  24 lines / 7 files VERIFIED CORRECT and left alone

DETECTOR BLIND SPOT, found and fixed before shipping: v1 keyed on the word
"atom" and missed graded-hecke-energy-truncation-bound, which says
"the closure of $\mathcal{B}_K \in B_n$" and never says "atom". The symbol IS
the subject. 4 -> 5 defects after the fix.

COORDINATION: #6821 owns the strand-count question on the same object and has a
three-way decision with the owner. Braid-vs-Hecke is PRIOR to it: whichever
count wins, "in B_n" is wrong on the GROUP.

## 2026-09-06 SELF-CORRECTION — this is a DRAIN, not a discovery

The producer's own docstring has carried the correction since 2026-08-25
(PR #5765), verbatim:

    NAME IS A MISNOMER - this does NOT return a braid word (2026-08-25, PR #5765).
    A rename was considered and rejected: 685 call sites across 382 files.

So: the corpus already knew; the rename was already weighed at 685/382 -- close
to my independent 672 -- and already REJECTED; and PR #6359 already acted on it,
correcting "the closure" out of its body, its probe and a Lean docstring.

I framed this as a root-level discovery in #6941 §10 and did not run corpus-grep
path 3 on the producer docstring before doing so. I read canonical_braid_crossings
and never read atom_braid_word_3A's own header.

WHAT SURVIVES, and it is the only real contribution here:
  * the measurement (0 of 14 atoms protium->Fe-56) quantifies a known fact
  * the 5 CONTENT-BLOCK lines still asserting `in B_n` for the atomic object --
    the docstring fixed the PRODUCER, nobody drained the BLOCKS
  * the detector, so it does not re-spread

REFINEMENT I had wrong, from #6359: the branch count is 2^(2A+1), not my 2^k,
and it is NOT a free choice in the way I implied -- an averaged letter and BOTH
its resolutions project to the SAME transposition, so the component partition,
non-interaction and strand blocks are branch-INDEPENDENT. Some topology is
readable; volumes, crossing numbers and genus are not.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-06 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — pointer

Tracked under carrier M9 (qou-jgg0) of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.


## 2026-11-21 — expo-chapter drain (session https://claude.ai/code/session_01Qmmkt5JeUvGF2FboRQJbLN, issue #8826)

Re-measured on main 2ae54ab40. The detector `computations/audits/braid_vs_hecke_word_audit.py` grepped `content/`, which no longer exists after the content/ -> folio/ move, so on main it reported 0 defects and 0 correct sites (1/3 assertions): a silent gate, not a clean one. Pointed at `folio/` it found 3 lines. One was real and new since 2026-09-06: `mass-theory/rho-k-h3a-refinement.md:3` ("braid word B_K in B_{3A}"). Two are the notation-register A vs B_K entry, which states B_K in H_{3A}(q) and quotes the old B_{3A+Z} wording only as history (adjudicated correct). PR #6821 has merged, so `atomic-mass-gb-nf.md:6` is no longer sibling-owned; it still said "nuclear-core braid B_K in B_n" and is fixed too. Both now read "nuclear-core Hecke word B_K in H_n(q)", per the register. Branch `claude/expo-chapter-drain-2026-11-21` (269b643c0, 1ae09428d); detector now 3/3, 0 defects, 10 correct files. Residual, not done: `rho-k-h3a-refinement.lean:55` docstring says `β_K ∈ B_{3A}` (needs lean-direct). Status stays todo until the PR merges.
