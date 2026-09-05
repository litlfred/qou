---
# qou-zgg2
title: 'build_atom_nf misuse: four genuine, plus the no-durable-home claim that hid two'
status: todo
type: task
priority: high
created_at: 2026-09-05T06:26:13Z
updated_at: 2026-09-05T06:27:17Z
---

AUDITED 2026-09-05 (corpus-grepper subagent, read-only, branch/gating resolved
per call site rather than read off grep). Follows origin/main 30b3568404, which
warned that "any probe reasoning from build_atom_nf_mp to a claim about the
framework's binding is reasoning about the wrong object". THE WARNING IS
DIAGNOSTIC, NOT PROSPECTIVE: it has already happened, four times.

## THE META-DEFECT FIRST — it is why nobody looked

Three artifacts assert the finding has nowhere to have propagated:
  docs/audits/2026-09-04-full-tower-ruling-vs-the-h3-mass-surface.md:34-36
  .beans/qou-tower:676
  .beans/qou-hu1f:22-23
all saying build_atom_nf_mp "appears in ZERO files under docs/ or content/".

MEASURED on the same tree:
  build_atom_nf_mp in docs/    claimed 0  ACTUAL 4 files (3 predate the claim)
  build_atom_nf_mp in content/ claimed 0  ACTUAL 0  <- correct
  the NF ROUTE in content/                ACTUAL 3 blocks (mba-chain-map:7,
                                          mba-step01:58, mba-step02:59,63,64)
  the NF route in .lean                   ACTUAL 2 files

The audit reasoned about THE NF ROUTE while measuring ONE FUNCTION NAME WITH AN
_mp SUFFIX, concluded there was nothing durable to check, and items 1.2 and 1.3
sat in content/ the whole time. Same shape as the trap 30b3568404 itself
records: a grep answered a narrower question than the sentence it supported.

## (1) FOUR GENUINE MISUSES

1.1 "the corpus never leaves H_3" — THE STRONGEST, live in FIVE artifacts.
    Origin qbeta_level_k_operator_and_real_decays_probe.py:2-3,10-22 (no
    correction banner, unlike its Step-26/27 siblings). Propagated to
    qbeta-level-k-operator-and-real-decays.witness.json assertion
    corpus_atom_model_is_H3_valued_at_every_A, passed:true, caveats:null,
    computedAt 2026-09-03 — REGENERATED TWO DAYS AFTER its own correction; to
    qbeta_discriminant_curve_in_q_probe.py:80,461,623; to that witness's
    hecke_tower_adds_no_eigenvalue_by_branching, passed:true; to
    docs/audits/2026-08-31-qbeta-discriminant-curve-in-q.md:98-104 §3
    (uncorrected); and to qou-cds1 Steps 25-26.
    FALSE TWO WAYS: the canonical route builds genuinely H_{3A} objects
    (2H->11=p(6), 3He->30=p(9), 4He->77=p(12)); AND the corpus refutes it
    internally ten lines away — qbeta_level_k_binding_operator_probe.py:64-72
    proves Delta_bind is "genuinely H_6-valued".
    ARITY DEFECT: a universal closure ("every corpus object") established by
    checking ONE function's return length.
    THE EXISTING CORRECTION IS ALSO WRONG: four artifacts replace it with "H_3
    is where the production chain can OBSERVE it" — precisely what 30b3568404
    retracts. So five artifacts carry the original and four carry a wrong fix.
    BLAST RADIUS: no number moves. What moves is the closure of the qou-cds1
    convention-D c_k ladder arc — live S1 science. Does NOT reach Lean
    (DiscriminantCurveInQ.lean carries genus/2pi-3 theorems only) or content/.

1.2 mba-step02-gs-reduction.md:83 — "EVERY downstream algorithm consumes NF(w),
    not the raw braid". FALSE for the canonical binding route, which consumes
    atom_braid_word_3A and never calls the reducer. Plus mba-step01:58,
    mba-chain-map:7 (status "proved"), and mba-chain-map:8 presenting
    qou_mass.compute_tr_M and pyhecke.nf_tr as interchangeable entry points for
    one step when they are different objects. INTERNAL CONTRADICTION in the same
    84-line block: §Output says NF(w) is indexed by w in S_n (n! elements); the
    API it names returns 6 for every A.
    BLAST RADIUS: largest of the four and PROCEDURAL — this appendix is the
    STRICT maintenance contract enforced by four skills, and rows 9a/9b sit
    downstream of rows 2-3. No number moves; what moves is which producer the
    chain map declares canonical, and a false universal an agent will act on.

1.3 hadron_knot_table.py:11-14 — "the H_3(q) NF captures ALL the information
    needed for mass formulas and Q-value predictions". Live at :174 for every
    non-nucleon row. The content block it fed
    (appendix-knot-operations/hadron-level-knot-table.md:1-3) makes a WEAKER and
    defensible claim (a compression claim between two H_3 objects); the Python
    sufficiency claim is the over-claim. BLAST RADIUS small: no numerical mass
    or binding producer reads that witness.

1.4 def:universal-ilp-algorithm — "the same LP at every level" on a state
    x in H_3(q), with an explicit energy claim. Already caught on the PRODUCER
    axis (four authorNotes, computation.status demoted to error, producer raises
    NameError before Level 4, witness unreproducible). NOT caught on the OBJECT
    axis: nothing records that x is the collapsed NF.

## (2) LEGITIMATE USE — and two are PRIOR ART for 30b3568404

atom_vhyp_closure_matrix_m.py:1-15 draws exactly this distinction, correctly,
owner-confirmed 2026-06-09 — FIFTEEN WEEKS EARLIER, on the Delta_lambda arc.
StrandLayoutForcesChain.lean:44-50 scopes it in Lean. The
all-nuclides-sdp-admissibility witness reaches the right inference unprompted:
"per-nucleus binding richness must live in the tower / Delta_lambda, not the
H_3 operator selection". Also gs_filtration_jet_shape_magic_probe,
nf_inter_nucleon_is_a_count_not_a_graph_probe, LaurentWalkCompute.lean.

TWO RESIDUAL CONTAMINATIONS inside otherwise-fine files, where the retraction
sits BELOW the uncorrected claim: tower_walk_magic_replication_probe.py:24-26
and gamma_chain_tower_magic_probe.py:14-26.

## (3) AMBIGUOUS — and 3.2 is the highest-value next measurement in the area

3.2 compound_shift_nf.compound_shift().categorical_mass (:663) is
    Sigma nf_i * tr_w_i on the COLLAPSED NF, named "categorical_mass",
    serialised uncaveated. No consumer reads it today.
    WHAT WOULD DECIDE: run tr_m_atom_zn(Z,N) for the same six atoms (A=2..6,
    seconds) and compare. Agreement => faithful order-zero rendering, only the
    NAME is loose. Disagreement => the witness carries a "mass" that is not the
    framework's. This is exactly the measurement qou-hu1f names as unmeasured,
    restricted to the cheap range.

3.1 all-nuclides-sdp-admissibility-mp analysis.dual_discriminates_magic:false —
    a magic-number negative over 4932 rows. NOT NF-derived (the NF never reaches
    the LP), so not category (1), but the LP's channel space IS the 6 NF
    channels and this witness, unlike its v1, carries no finding text saying so.
3.3 jet_knot_invariants.py:6-14 — same premise as 1.1 but as an ASSUMPTION of
    the file; build_atom_nf imported at :50 and never called. One sed decides.
3.4 .beans/qou-tower — corrections are on the last 35 of 728 lines; a reader
    stopping at §THE FINDING gets the uncorrected version.

## RANKED

1. 1.1 — a passed:true assertion regenerated after its own correction, closing
   a live S1 arc on a premise the corpus refutes in the next probe along.
2. 3.2 — the one cheap measurement that converts "different objects" into
   "agree / disagree".
3. 1.2 — no number moves, but it is the STRICT maintenance contract.
4. the meta-defect — until "no durable home" is corrected, the next agent
   re-derives this sweep and reaches the same wrong conclusion.

NOTHING EDITED. Read-only audit.
