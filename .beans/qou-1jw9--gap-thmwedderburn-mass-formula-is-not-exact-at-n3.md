---
# qou-1jw9
title: 'GAP: thm:wedderburn-mass-formula is not exact at n=3, its own claimed exactness point'
status: todo
type: task
priority: normal
created_at: 2026-08-25T07:10:47Z
updated_at: 2026-08-25T08:20:18Z
---

MEASURED, commit 933b895f17, computations/wedderburn_Mi_constructor_test.py.

The theorem states its own domain: the three invariants Phi_1/Phi_2/Phi_3
are the three EXTREMAL Wedderburn blocks, so the formula is exact only
where those exhaust the partitions of n. That is n=3 alone, i.e.
deuterium (Z=1, N=1, A=2, n=A+Z=3). D is therefore not one test among
many -- it is the single point the theorem claims exactness at.

The M_i constructor was built literally from the two blocks that define
it (def:atomic-braid + tbl:atomic-braid-table1-data + the theorem's own
"chaining the crossing matrices of all strands j > i" = suffix product
T_i * ... * T_{n-1}).

Spec-selected cell (literal reading, Phi_1-minimizing ordering n-e-p):
  predicted correction  -6.86271790 MeV
  target correction     -2.22459017 MeV  (= -B_total, AME2020)
  residual              -4.63812773 MeV  = 208.5 % of target
Sign CORRECT, magnitude not.

Sensitivity, not fit: the headline is the SPEC cell, not the smallest
residual. Across all 4 readings x 2 orderings the residual floor is
54.2 % and the ceiling 2652.6 %. No reading rescues it.

Scope (a), not (b): this constructor reading, alone, does not reproduce
D as-is. Nothing is excluded.

WHAT THIS SETTLES. Two earlier retractions in this chain were blamed on
feeding the wrong M_i (quark-level nucleon_gen_chains, then a
two-element atom_gen_chains). Feeding the RIGHT M_i does not rescue it.
The gap is in the leading-order truncation, not in the input.

DO NOT, on picking this up:
  - propose a seventh Delta_lambda closure ansatz (AGENTS.md names that
    prohibited by name, and arriving here by a fresh route is not a
    licence to retry it);
  - close the 208.5 % residual with any parameter -- only CAL-1/2/3 are
    admissible inputs (owner, this session);
  - read the sign agreement as partial success. Sign is one bit and the
    magnitude is 3x.

HONEST NEXT STEP, if any: the residual is a statement about the
truncation. The exact route is the Delta_lambda partition sum
(computations/binding_K_direct.py), which deliberately withholds a
prediction because the many-body magnitude is the documented Track A
blocker. Nothing here changes that status.


=== MORE CONTEXT (commit 61d81adaf9) — and a SCOPING CORRECTION to my own claim above ===

I went looking for what the corpus already says about this formula. Three
things turned up, and the third forces me to weaken the headline.

1. THE PUBLISHED TABLE HAS NO PRODUCER, AND ITS WITNESS NEVER EXISTED.
   tbl:mass-table-z1-20-table-data publishes 20 rows (H..Ca). Its backing
   witness `atom-mass-complete-wedderburn` is not merely absent — it never
   existed in git history. Already named a "phantom witness" in
   docs/audits/2026-07-12-exposition-drain-needs-owner-ledger.md. The 20
   values survive ONLY as a hardcoded dict at
   computations/_deprecated/feynman_qou_comparison.py:218, under a comment
   citing that phantom. mass-table-z1-20.md itself already says the rows are
   "not currently reproducible".

2. THE TABLE'S ERROR METRIC DIVIDES BY THE INPUTS, NOT THE PREDICTION.
   The formula's first three terms are INPUTS (absolute-mass excision). The
   whole predictive content is the correction, whose job is to equal
   -B_total. The base is ~99.8 % of the mass, so Delta/m measures the inputs.
   Re-scored on binding:

       metric      range over the 20 published rows
       Delta/m     0.003 % .. 0.19 %     looks excellent
       Delta/B     0.4 %   .. 28 %       the real prediction error

   And H-1 — the BEST-looking row at +0.014 % — is the correction with the
   WRONG SIGN and ~9300x the magnitude (+0.1269 MeV vs a true -1.36e-5 MeV).
   This part is pure arithmetic on published numbers; it does NOT depend on
   my constructor and stands on its own.

   H-1 needed care and I nearly got it wrong: the published masses carry 3
   decimals (+/- 0.5 keV) while hydrogen's binding is 13.598 eV, 37x finer.
   A binding read off that column is rounding, not physics. My first pass
   used it and printed a ratio of -1436; the CODATA-based figure is -9333.
   Use the second.

3. MY CONSTRUCTOR DOES NOT REPRODUCE THE TABLE EITHER.
   mine/true swings 0.47 .. 2.5e5 across H-1..C-12; pub/true sits in a
   smooth 0.78-1.28 band. Given (1), that does NOT refute the constructor —
   the table is not an independent check on anything.

SCOPING CORRECTION. The heading of this bean, and commit 933b895f17, say
"the formula is NOT exact at n=3". Too strong. What is established:
  - no reading of M_i reproduces D (54 % .. 2653 %), AND
  - no construction reproduces the published table, AND
  - the published table has no producer.
The defensible statement is that thm:wedderburn-mass-formula is currently
UNFALSIFIABLE AS WRITTEN: its M_i prose does not determine a unique
construction, and nothing in the corpus can adjudicate between candidates.
Weaker than "the formula is false"; stronger than "my probe failed".

This also explains the two earlier retractions in this chain. I reached for
the wrong helper twice (quark-level nucleon_gen_chains, then the
two-generator atom_gen_chains) not through carelessness alone but because
THERE IS NO RIGHT HELPER — atom_gen_chains returns 2 chains for every (Z,N)
and is an H_3-shaped approximation, explicitly disclaimed for this formula.

TWO SEPARATE DEFECTS FOUND, both actionable, neither fixed here:
  a) content/quantum-observable-universe/observations/
     neutron-proton-mass-splitting-proof.md:35 still asserts
     "**Witness**: atom-mass-complete-wedderburn.witness.json" with NO
     caveat. The sibling wedderburn-mass-formula-proof.md:143 was rescoped;
     this one was missed. A live content block cites a witness that never
     existed.
  b) def:atomic-braid's ground-state rule ("minimize Phi_1 over all
     permutations") is exponential in A: C(40,20) = 1.4e11 for Ca. As
     written the definition is not computable for the table it underwrites.

STILL PROHIBITED, unchanged: no seventh Delta_lambda ansatz; no closing the
residual with any parameter (only CAL-1/2/3 admissible); sign agreement is
one bit and is not partial success.
