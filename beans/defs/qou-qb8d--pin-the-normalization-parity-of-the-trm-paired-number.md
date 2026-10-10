---
# qou-qb8d
title: 'Pin the normalization: bar-parity of the tr_M-paired NUMBER, not the class'
status: completed
type: task
priority: normal
created_at: 2026-08-08T09:30:00Z
updated_at: 2026-08-08T10:15:00Z
---

## RESULT (2026-08-08): NOT trace-blind; the paired number is MIXED with a
## nonzero bar-ODD part. The HH^1 carrier SURVIVES the bar-parity screen.

Ran it. `computations/hh1_outer_class_trace_paired_parity.py`; witness
`hh1-outer-class-trace-paired-parity.witness.json`; audit
`docs/audits/2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md`
§Successor result.

Both pins ended up structural, so the anti-fit guardrail was satisfied:
- generator: He-Nie min-length class reps (e, s1, s1s2), ASSERTED to project
  to a basis of HH_0;
- trace: Ocneanu/Markov Jones spec, with z held SYMBOLIC and bar-EVEN --
  which sidesteps the q^{1/2} branch AND the open Ocneanu-parameter question.
  ASSERTED: tr_M kills all 36 commutators.

| point | x | S_even | S_odd | parity |
|---|---|---|---|---|
| q=i    | s1   | z/3  | -i/3            | MIXED |
| q=i    | s1s2 | 2/3  | 2iz/3           | MIXED |
| q=zeta_6| s1s2| -z   | sqrt(3)i(1-z^2)/3| MIXED |

Cross-checked at the SPECIALIZED Jones z (guards against a formal-z artifact):
z = sqrt(2)/2 and sqrt(3)/3, both REAL (independently verifying the
bar-evenness hypothesis). Bar-odd parts survive: -i/3, sqrt(2)i/3, 2sqrt(3)i/9.

Readings:
1. The clean scale-invariant prune (tr_M . Delta = 0) DOES NOT occur.
2. The pairing carries a nonzero bar-ODD component -- the parity c_3's swing
   needs. The bar-parity obstruction that closed every real route does NOT
   close this one.
3. Asymmetry: at zeta_6 the units of Z[zeta_6] contain no parity flipper, so
   an integrality pin WOULD fix parity there; at q=i the units +-i flip it.
   Integrality is a point-dependent pin, not a general one.

NOT ESTABLISHED (the gap is wide): a nonzero bar-odd COMPONENT is not a
bar-odd EIGENVECTOR (the number is MIXED; isolating the odd part needs further
structural justification); MAGNITUDE is completely untouched -- nothing here
reproduces c_3's value or its anchor swing; n=3 is the mechanism, the Bring
fibre is H_5 at zeta_5.

Successor: qou-qb8e (magnitude channel -- the actual open question).
Nothing wired. No fit. c_3/Q_beta gap unchanged and open.

---

Successor to qou-qb8b, which established that the bar-parity of the HH^1 outer
class acting on the cocenter is normalization-dependent (Hilbert 90 over
Q(zeta)/Q(zeta)^+) and therefore carries no information. See
docs/audits/2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md.

The fix is to stop asking about the CLASS and ask about a NUMBER. The c_3 swing
S is a scalar, and bar-parity of a scalar IS well defined. So pin the whole
construction:

    S_candidate = < tr_M , Delta(x) >    for a canonical generator x in HH_0

where Delta is the induced outer action (class-canonical, already computed) and
tr_M is the Markov trace, which factors through HH_0 by the merged
CocenterTraceFactor.lean. Then read bar(S_candidate) vs -S_candidate.

The whole difficulty transfers to pinning TWO things, and neither may be chosen
to taste (that would be a fit):
1. the normalization of the outer representative D -- candidate: require D to
   preserve a Z[q,q^{-1}] lattice, leaving only unit scalings +/- q^k;
2. the canonical generator x in HH_0 -- candidate: the min-length conjugacy
   class basis of He-Nie (already cited in CocenterTraceFactor; this is the
   qou-dilv machinery).

ANTI-FIT GUARDRAIL (load-bearing): choosing the normalization or the generator
so as to make the parity come out bar-ODD is a FIT and must be labelled one and
not wired. The normalization must be pinned by a structural requirement stated
BEFORE the parity is read. If no structural pin exists, report that -- an honest
"the construction is not canonical" is the correct output, not a tuned choice.

Order of work: (2) first via qou-dilv (the He-Nie basis is a real structural
pin), then (1), then read the parity. If (1) cannot be pinned structurally,
stop and report -- do not pick a normalization to taste.
