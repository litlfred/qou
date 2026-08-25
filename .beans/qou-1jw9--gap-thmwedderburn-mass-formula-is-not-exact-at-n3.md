---
# qou-1jw9
title: 'GAP: thm:wedderburn-mass-formula is not exact at n=3, its own claimed exactness point'
status: todo
type: task
priority: normal
created_at: 2026-08-25T07:10:47Z
updated_at: 2026-08-25T07:11:20Z
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
