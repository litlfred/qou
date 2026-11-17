---
# qou-isu5
title: 'DEFECT: the H_3 TR_M weight vector [1,z,z,z2,z2,z3] is NOT A TRACE — not cyclic'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T08:58:36Z
updated_at: 2026-11-17T13:00:03Z
parent: qou-59vq
---

## What is ESTABLISHED (two independent proofs)

The H_3 Markov-trace weight vector used across the corpus,

    TR_M = [1, z, z, z^2, z^2, z^3]

on the NF basis [(), (0,), (1,), (0,1), (1,0), (0,1,0)], is **not a trace**.

**Proof 1 — not cyclic.** With x = T_s0 and y = T_s1 T_s0, computed in the H_3
regular representation:

    tr(xy) - tr(yx) = z (z - q) (q z + 1) / q

which is nonzero: -0.426952471076 at z_C and -0.461171580324 at z_D. A trace is
cyclic by definition. (Note the factor: it IS cyclic exactly at z = q and
z = -1/q, the two degenerate roots -- which is why this can hide.)

**Proof 2 — not a class function.** Solving TR_M = y_3 chi^(3) + y_21 chi^(2,1)
+ y_111 chi^(1^3) over the three irreducible characters returns NO SOLUTION.
By Wedderburn any trace on H_3 must decompose that way.

## The correct value, and where it comes from

From the DEFINING Markov property tr(x T_n y) = z tr(x y) plus the Hecke
relation T^2 = h T + 1:

    tr(T_{s1 s2 s1}) = z * tr(T_{s1}^2) = z (h z + 1)      NOT z^3

`z^3` is what you get from assuming tr(T_w) = z^{len(w)}, which holds for
len <= 2 in H_3 and fails at len 3 because the Hecke relation kicks in. The
comment at hecke_core_symbolic.py:160 says exactly that: "Word lengths
0,1,1,2,2,3".

**Convention-INDEPENDENT.** Both steps hold whatever value z takes, so this is
wrong under C and under D alike. It is not the excision question.

## Cross-check against the corpus's own record

With z(hz+1) the solve reproduces `y-lambda-symbolic-witness.json` EXACTLY at
z_D -- y_(3) = (q^4+1)/(q^2+1)^2, y_(2,1) = q^2/(q^2+1)^2, y_(1^3) = 0. With
z^3 there is no solution at all. So the corpus already holds the correct
weights in one place while computing with the incorrect ones in another.

Corroborating: `h4_markov_weights_closed_form.py` DOES carry Hecke corrections
throughout (h*z^2 + z, h*z^3 + z^2, h^2*z^3 + ...), and its `h*z**2 + z` entry
is precisely z(hz+1).

## Blast radius — MEASURED IN PART, NOT COMPLETE

`substrate/hecke_core_symbolic.py:161` defines TR_M_SYM with z^3 and is
IMPORTED by `shift_from_nf_basis.py`, which computes
`tr_q = sum(nf_list[i] * TR_M_SYM[i])` and describes it as "canonical Markov
via TR_M_SYM".

13 further live files carry the same literal (atom_mass_derived:102,
basis_knot_tables:54, ch-bond-writhe-lp:30, compound_shift_nf:257,
h4_markov_character_decomposition:111, h4_markov_weights_closed_form:111,
hh-trefoil-corrected:51, intermediate_knot_detection:31, jet_knot_invariants:56,
photon_operator_table:60, probes/markov_reduction_h3_to_h4_verify:115,
probes/nucleon-lp-convention-probe:91), plus 14 in _deprecated/.

**NOT established: that every downstream number is wrong.** A use whose words
never reach the 6th basis element is unaffected, and I have not checked which
do. Do not quote "13 broken producers" -- quote "13 live sites carry it;
consumption not yet traced".

## How I found it

Chasing why the convention-D migration of compound_shift_nf moved 95 fields. I
noticed the 6th weight looked wrong, and deliberately did NOT conflate it with
the migration. It turns out to be the larger of the two problems, and it means
the migration measurement was of a doubly-wrong quantity.

## THIS IS THE ROOT CAUSE OF qou-6hm4 PART (i)

`qou-6hm4` (open, 2026-08-22) records the SYMPTOM: the committed
`confinement-topological-proof` Gram is not symmetric, `max|G - G^T| = 0.4269`,
with `G[1][3] = 0.551443` against `G[3][1] = 0.124491`. It attributes this to a
row ordering artefact -- "Rows 3 and 4 are transposed relative to the columns".

Those are exactly the two values of the 6th Markov weight, at that witness's
own q0 = 1.1099785955541805 and z_C:

    z(h z + 1) = 0.551443419919830   -> qou-6hm4's G[1][3] = 0.551443
    z^3        = 0.124490943129969   -> qou-6hm4's G[3][1] = 0.124491
    difference = 0.4270              -> qou-6hm4's max|G - G^T| = 0.4269
    and the cyclicity defect z(z-q)(qz+1)/q = -0.42695248 at the same point

Three independent figures agreeing to six significant digits.

**The mechanism.** G_{ij} = tr(b_i b_j) is symmetric ONLY because tr(ab) =
tr(ba). The z^3 functional is not cyclic, so G comes out asymmetric, and the
asymmetry is precisely the amount by which z^3 differs from z(hz+1) on the
words that reach the longest element. It is not a row swap: it is the weight
vector not being a trace.

That also explains qou-6hm4's other observation -- that permuting rows to
(0,1,2,4,3,5) makes it "exactly symmetric" while leaving the RANK wrong (6
instead of the required 5). A permutation can hide an asymmetry without fixing
the underlying functional, and the rank is the tell that it was never a trace
form.

So qou-6hm4 part (i) should be re-scoped from "wrong row order in one 2026-05-02
witness" to "the H_3 weight vector is not a trace, corpus-wide". This bean is
that cause; qou-6hm4 is one of its symptoms.


## 2026-08-30 — BLAST RADIUS MEASURED (not inferred)

Method: perturb ONLY the 6th weight (z^3 -> z^3 * 1.5) at each live site, in a
detached worktree, and see whether the producer's output moves. MOVES = the 6th
basis element is genuinely reached.

### CONFIRMED AFFECTED — 8

    ch-bond-writhe-lp.py:30
    compound_shift_nf.py:257
    h4_markov_character_decomposition.py:111        (also exits 0 -> 1)
    hh-trefoil-corrected.py:51
    intermediate_knot_detection.py:31
    probes/markov_reduction_h3_to_h4_verify.py:115  (also exits 0 -> 1)
    probes/nucleon-lp-convention-probe.py:91
    substrate/hecke_core_symbolic.py:161            -> via shift_from_nf_basis.py

The last one needed a second measurement and is the important one. Run
standalone it reports "no-move", because it is a DEFINITION module -- executing
it computes nothing. That is the same harness artefact that made qbeta_utils
look INERT earlier in this bean, and I nearly recorded it the same way.
Perturbing the definition and running its CONSUMER, `shift_from_nf_basis.py`,
gives MOVES. So the core module's defect does propagate.

### CARRIES THE LITERAL BUT DOES NOT REACH IT — 3

    basis_knot_tables.py:54
    jet_knot_invariants.py:56
    photon_operator_table.py:60

Still worth fixing (the literal is wrong and will bite the next reader), but no
committed number depends on it.

### NOT MEASURED — 1

    atom_mass_derived.py   (timeout at 240 s)

### So the count is 8 affected, 3 inert-but-wrong, 1 unmeasured

NOT "13 broken producers", which is what a grep alone would have suggested, and
not "1 live file", which is what my first too-narrow grep suggested. Two of the
eight also FAIL outright under perturbation (exit 0 -> 1), which means their own
assertions are sensitive to this weight -- those are the two most likely to
reveal what the correct value does.


## CORRECTION 2026-08-30 — this was NOT a new finding

Two claims made when this bean was opened were re-derivations of corpus-held
facts, and the corpus-grep checklist should have caught both:

- `docs/audits/2026-05-19-trm5-markov-bug.md` (2026-05-19) already states the
  defect, the `h*z^2 + z` derivation and the "not a trace" reasoning.
- `computations/probes/confinement_b3_enumeration_recheck_probe.py` already
  records the qou-6hm4 link: "stale power rule -> max|G-G^T| = 0.46, rank 6 ...
  qou/6hm4 first diagnosed it as one [a row-ordering bug] -- a coincidence in
  the numbers."

## What IS this bean's contribution

TRAP, and the durable half: `trm5_zcubed_live_producer_audit.py` checked a
hardcoded five-file LIVE_SITES list and printed "all five fixed: True" while
SEVEN other files on the same H_3 NF basis carried the bug. Two of the seven
(`z ** 3` inside np.array; `z * z * z`) were in spellings no pattern in the
guard could match. Guard now backed by a shape-keyed corpus scan with a
--selftest that fails unless all four spellings are detected.

12 sites total; all 12 correct as of f1047c2f9c. Rust (gram.rs:146) was already
correct -- the pyhecke test docstring claiming otherwise was stale.

Downstream consequence worth carrying: the corrected trace WITHDRAWS the
scope-(a) negative published by qbeta_c3_barodd_hs_matrix_resolvent_probe. Its
finding 2 ("the pairing is bar-even") is falsified at mu=0 (BAR-ODD, 18.38 vs
6.86); finding 3's test goes degenerate because the correct Gram is singular.
Not a positive result either -- that probe is still convention C and inverts a
singular Gram in float64. Re-run belongs to qou-cds1.


## 2026-08-30 — the fix has a DOWNSTREAM population this PR has not re-run

Surfaced by the import-cone audit, not by the z³ work itself.

`computations/substrate/hecke_core_symbolic.py` carries the corrected constant:

    -TR_M_SYM = [ONE, z, z, z**2, z**2, z**3]
    +TR_M_SYM = [ONE, z, z, z**2, z**2, h * z**2 + z]        (6b149f4379)

That is a **value change in a symbolic constant**, not a comment. Measured:
**11 direct importers**, and `witness_import_cone_staleness_audit` flags
**121 committed witnesses** whose producer cone reaches it.

**None of those 121 has been re-run.** The z³ tranche fixed the 12 source sites
and verified them; it did not follow the witnesses computed against the old
constant. They are import-cone stale — the class SELF and UPSTREAM cannot see,
so nothing else will report them either.

**Do not bulk-refresh.** AGENTS.md caps witness refreshes per idle pass, several
of the 11 importers are long-compute, and `qou-a2q5` measured that ~77 % of a
cone-stale population can be false positives resolved by reading one module
diff. Here the diff is read and the constant genuinely moved, so the false-
positive argument does NOT apply — but the *cost* argument still does. This
needs a scoped pass with the long-compute members identified first.

Recorded rather than done, and stated on PR #6144 so it is not silently
inherited by whoever merges it.


### 🛑 CORRECTION, same day — "none of those 121 has been re-run" is WRONG

The entry above says the z³ tranche *"fixed the 12 source sites and verified
them; it did not follow the witnesses computed against the old constant."*
**Measured, that is false**, and I published it on PR #6144 before checking.

The commit's diff to `hecke_core_symbolic.py` is **one line of code plus five
lines of comment**:

    -TR_M_SYM = [ONE, z, z, z**2, z**2, z**3]
    +# 6th weight is the Ocneanu value on the longest element … Bean qou-isu5.
    +TR_M_SYM = [ONE, z, z, z**2, z**2, h * z**2 + z]

`TR_M_SYM` is therefore the ONLY changed symbol. Of the 11 direct importers,
**exactly one references it** — `computations/shift_from_nf_basis.py`, 10
occurrences; the other seven import `_phi1_from_ordering_sym`,
`_ground_state_ordering` and similar, none of which the commit touched.

And that one consumer **was re-run in the same commit**:

    shift-from-nf-basis.witness.json  computedAt 2026-08-30T09:19:53Z
    6b149f4379                       committed  2026-08-30T09:21:41Z
    `git log origin/main..HEAD -- <witness>` -> 6b149f4379

Re-ran it again now to confirm: 4/4 assertions, **not one non-ephemeral field
moved**, witness restored rather than committed.

**So the 121 are false positives**, by exactly the mechanism `qou-a2q5`
documents: read the module diff, and a witness-level count collapses. I quoted
that bean's rule in the same PR comment and then failed to apply it to my own
module — I reasoned "the constant genuinely moved, so the false-positive
argument does not apply", which conflates *the module changed* with *the changed
symbol reaches these consumers*.

**No scoped pass is needed. Nothing is owed here.** What the audit flagged is
the module's mtime, not a stale number.

### Progress Update (Round 68 — PR litlfred/qou#8356)
- **PR:** https://github.com/litlfred/qou/pull/8356 (`2c058b5e380e076d0aec9233aad57fa6af43d018`)
- **Lean 4 Module:** `QOU.Foundations.BringCurveHochschildStaleWeightCyclicityThreeCellComparabilityQuadraticRescaling` (`LEAN_EXIT=0`, `0` warnings, `0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 major, 0 advisory` across all directory-mode static vacuity & borrowed-name audits)
- **Numerical Probe & Witness:** `computations/probes/bring_curve_hochschild_stale_weight_cyclicity_three_cell_comparability_quadratic_rescaling_probe.py` & `computations/probes/bring-curve-hochschild-stale-weight-cyclicity-three-cell-comparability-quadratic-rescaling.witness.json` (`COMMIT1 = 8ee314938e6a9bac9ee46faedf9aebdee8b895fb`, `scriptHash = 326bd13833f0`, `allPassed = True`, `dps = 80`)
