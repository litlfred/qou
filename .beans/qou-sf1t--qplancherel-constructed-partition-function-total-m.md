---
# qou-sf1t
title: 'QPlancherel: constructed partition function + total mass one (retroactive claim for merged PR #5372)'
status: completed
type: task
priority: normal
created_at: 2026-08-21T16:05:17Z
updated_at: 2026-08-21T16:06:29Z
---

RETROACTIVE CLAIM. Opened 2026-08-21 *after* the work merged, because it was
done without a bean. Recorded as unclaimed rather than quietly backfilled: the
merge agent for PR #5372 flagged "this merge was not claimed by a bean" and it
was right — AGENTS.md work-plan policy asks that durable work carry a claim, and
this did not until now.

WHAT LANDED (PR #5372, rebase-merged):
  e9696f45095  lean(QPlancherel): construct the partition function, prove total mass one
  22fd14fde5e  docs(Z-defect): the "no total-mass theorem" line is superseded

The Lean, in content/quantum-observable-universe/lean/QOU/MathlibExt/QPlancherel.lean:
  qPartitionFunctionOn    Z_q(s) = Sum_{lam in s} d_q(lam)^2 as a DEFINITION over
                          an explicit Finset -- previously HasPartitionFunction.Z
                          was an opaque class field whose "= Sum d_q^2" identity
                          lived only in a docstring.
  measureOn               d_q^2 normalised by that constructed sum.
  sum_measureOn_eq_one    TOTAL MASS ONE. Needs no ordering on R.
  qPartitionFunctionOn_pos  Z_pos DERIVED, not assumed.
  measureOn_nonneg        each weight nonnegative.
  sum_measure_eq_one_of_Z_eq_sum   the exact missing axiom: IF the opaque Z k
                          equals the constructed sum THEN the module's own
                          `measure` has total mass one.
  unitQDimension / badPartitionFunction / measure_total_mass_ne_one_of_bad... /
  exists_lawful_Z_with_total_mass_ne_one
                          the non-vacuity witness: a LAWFUL HasPartitionFunction
                          instance (Z = 2 > 0, satisfying every constraint the
                          class imposes) for which `measure` sums to 1/2. The
                          missing content is a VALUE constraint, not a sign one.

VERIFIED: lean-direct exit 0 (~4.6s), run three times by the merge agent -- once
pre-rebase and once after each of two rebases. #print axioms clean on all six new
declarations ([propext, Classical.choice, Quot.sound], 0 sorryAx). 0 sorry and 0
axiom in the file. No lake build was ever run; the olean cache stayed intact at
6990 Mathlib oleans. check-sidecars clean (the new sections are generic over
{R'}; the only concrete ring is the Q counterexample).

SCOPE -- what this does NOT establish. sum_measureOn_eq_one is one line from
Finset.sum_div + div_self, because normalising a family by its own sum gives
total mass one BY CONSTRUCTION. It is evidence about the constructed object only
and is NOT evidence that Sum_lam d_q(lam)^2 is the canonical normaliser for the
Ocneanu weights w_lam(q) = d_q^2/[n]_q!. This is stated in the module text and
repeated in the audit note so no later reader cites it as more than it is.

FOLLOW-UPS (queued, not done here):
  1. The #5365 addendum on main says "which normalizer is canonical ... is
     exactly what remains open". That OVERSTATES it: the owner ruling of
     2026-08-16 in notation/notation-collisions.md already rules that
     w_lam(q) = dim_q^2/[n]_q! has Sum w_lam(q) != 1 at q != 1 by design
     ("Never write a normalisation claim on bare w_lam"; 0.987 at n=3, 1.051 at
     n=8, ~1.51 at n=12 -- matching this audit's own table). The register was not
     grepped when the addendum was written; only the Lean side was.
  2. library/arxiv-0911.4494v2 (Webster-Williamson, "The geometry of Markov
     traces") constructs a geometrically-defined trace whose character expansion
     is given by MOLIEN SERIES via B_Delta-equivariant intersection cohomology --
     the shape of the owner-gated S^1-equivariant-index item. Needs a lead doc,
     with the Tr_Gamma vs Jones-Ocneanu identification flagged as OPEN
     verification (the paper says "analogous to", and coinciding with Gomi's
     trace, while the abstract calls it an interpretation OF Jones-Ocneanu).
