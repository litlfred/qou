---
# qou-7p7d
title: 'Motivate reading (B): where does Geom(K) x trace come from, and what in the lit justifies pairing an algebraic invariant with a geometric one?'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-08-26T03:16:39Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-v2om
---

ANSWERED 2026-08-26. (B) has NO motivation; do not declare it.

Three independent corpus sources, all one-K:
1. canonical-derivation-cheat-sheet 5, quoted in the vol-usage audit:
   m(K) = m_e * VolDensity(K,q0); VolDensity(K,q) = Vol(K)/hbar_q^2 * linking_weight(K,q).
   One K in BOTH factors. Chain likewise: braid -> tr_M -> J_K -> omega -> Geom(K),
   with J_K = tr_M of K's OWN braid.
2. docs/audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md TL;DR calls a Vol
   that does not belong to the traced object 'the bug' -- 64 atom-touching scripts,
   87 uniform vs 2 per-knot, error budget m_p +2.89% .. 56Fe +3.86%. Triggered by
   OWNER pushback: 'thought we determined this knot-dependent and should not be
   uniform'.
3. Literature IS the volume conjecture -- >=8 library sources (arxiv-1002.0126v1,
   arxiv-1203.2182v1, arxiv-1003.4808v2, ...), conj:kashaev-volume-conjecture,
   QOU.Kashaev.VolumeConjecture. But it relates J_K and Vol(K) for ONE K, as
   tr_M ~ exp(Vol) -- the cheat sheet's own words: 'Volume is NOT the carrier, it
   is the exponential of it.' A correspondence, not a product, and no licence to
   take Vol from one object and tr from another.

THIRD READING (C), which the evidence supports and I had not considered: the
framework intends ONE K per atom, being the atom's own braid word (cheat sheet:
'proton B_3, deuteron beta_D via atom_braid_word_3A(1,1)'). That object is NOT a
link (PR #5765, measured), so it has no volume, and production substitutes the
Borromean one. The pairing is the SYMPTOM of an unsatisfiable spec, not a design.

Note the inconsistency inside that one parenthesis: the proton's K is a genuine
LINK, the deuteron's is a HECKE ELEMENT. Different kinds of object; only one has
a volume.

My Addendum-4 elimination stands only as far as it goes: (A) is refuted in Lean.
'Therefore (B)' does NOT follow -- (C) was always available and is better
supported. Corrected in the audit.

2026-08-26: Lean-proved the per-letter spectral fact (AveragedLetterSpectrum.lean, 6 decls, sorry-free, axiom-clean) — averaged letter is ([2]_q/2)*eps with eps^2=1; a scaled generator matches +/-t only at Q=1. Addendum 12 unpacks the satellite vocabulary and audits my 'one move gives three things' claim: closed-braid SURVIVES (pure topology), satellite carrier is a TARGET not a construction, bar-invariance-by-construction WITHDRAWN (rested on the type-B fold that 11b falsified). Open: a pattern that is a closed braid, has Z+N JSJ pieces, AND is bar-invariant structurally. No candidate mechanism for the third.

2026-08-26 addendum 13: COLOUR averaging splits the 2A+1 letters into 2A symmetric (Q=1) + exactly ONE colour-weighted p-n interface (Q=1.0000715145). 11b's count objection is wrong; type B has one T_0 and there is one such letter. Route still pruned, now by a sorry-free invariant: exteriorSquareDim N = 1 <-> N = 2 (VolumeConstraintForcesFibreTwo.lean, on main) pins the fibre dimension, so no single-algebra fold reaches a third row. weak_volume_reading_admits_three shows N=3 IS admitted by the weak reading. deuteron-real-sdp's indefinite Gram is convention C (11 nonzero entries; D gives 4 positive + 7 zero, no negatives at n=3,6,9,12) -> singularity not indefiniteness, qou-cds2. Third channel = third ROW; bar-fixed sector leaves the D support exactly at A=2 (deuteron), which is also the first isotope with a colour letter. Groupoid reading is the corpus's own open item (su5-hypercharge-n3-gate, conj:sm-gauge-truncation). No route claimed.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `(none)` → `qou-v2om`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

- **Round 88 (`https://github.com/litlfred/qou/pull/8405`, head `094b162d955cf25f57c026bb5dce25006b9627d4`)**: Formalized theorem + 80-dps witness (`status: in-progress`).
