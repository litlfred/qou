---
# qou-zm8z
title: 'W2b: the spanning decomposition H_{n+1} = H_n + H_n sigma_n H_n as a content-bearing 3b class (W2''s undelivered third deliverable)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-26T14:05:48Z
updated_at: 2026-08-26T14:11:55Z
---

## Built 2026-08-26 — PR #5827

`HeckeCosetSpanning` in `QOU/Machinery/HeckeTowerBasicConstruction.lean` (its home:
this was W2's undelivered third deliverable, see the finding on qou-2017).

  spanning : forall w : Hn, exists a s b c,
    w = ilow a + sum_{i in s} ilow (b i) * sigma_n n * ilow (c i)

Content-bearing (one real forall-exists equation; not True, not empty). Binds
HeckeBraidedPresentation in its type = the 3b-tax dependency edge, matching the
three existing classes in that file. Independent of the conditional expectation:
mentions neither eps nor the Jones projection, so it can be discharged separately
and a proof needs no trace at all.

Consumer `gwg_trace_of_spanning` (MarkovTowerBridge): with the class plus the two
grounding shape lemmas, the two-generator Markov reduction holds for EVERY w,
not only pre-decomposed ones.

**The conclusion pins the witness to the decomposition** — it asserts both that w
splits and that the reduction holds with the expectation built from THAT split.
A bare `exists Ew, ...` would be weaker in a way that matters: tr = 0 satisfies
it for any Ew (see `markov_axioms_vacuous_of_weight_zero` upstream), so the
existential alone would carry no coset information. Caught and fixed before commit.

Also recorded as a CHECKED fact, not a caveat:
`spanning_shape_holds_for_identity_inclusion` — with ilow = id every w splits
trivially (a := w, empty sum). So the class is CONSISTENT (a degenerate model
exists, which is what makes conditional results non-vacuous) and is WEAKER than a
proper inclusion — an instance carries no information that Hlow is strict.
Anything needing properness must say so separately.

**Still open:** no instance. And the last gap to hgwg proper is `Ew = i (eps w)`,
which needs the Markov property `eps (b * sigma_n * c) = z . (b*c)` — NOT a field
of HeckeConditionalExpectation (it has exactly retract and bimodule). Not added:
that would relocate an assumption, not discharge one.

Verification: lean-direct exit 0 on both modules; #print axioms clean
(spanning_shape needs only propext + Quot.sound); guard rc=0 on 60 entries.
