---
# qou-isu5
title: 'DEFECT: the H_3 TR_M weight vector [1,z,z,z2,z2,z3] is NOT A TRACE — not cyclic'
status: todo
type: task
priority: normal
created_at: 2026-08-30T08:58:36Z
updated_at: 2026-08-30T09:00:27Z
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
