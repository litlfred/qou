---
# qou-43co
title: 'DEFECT: def:hecke-normal-form asserts confluence that QOU''s own Lean refutes at n=4'
status: in-progress
type: bug
priority: high
created_at: 2026-08-09T18:27:58Z
updated_at: 2026-09-07T18:30:05Z
---

`content/quantum-observable-universe/braids-and-knots/hecke-normal-form.md` says of
the three-rule system (Hecke relation, far commutativity, Yang-Baxter in the
shortlex-decreasing direction):

> This reduction is confluent, making the normal form independent of rule order.

That is exactly the system `heckeRewritingSystem` in
`content/unital-groebner-bases/lean/UGB/GrobnerShirshov/HeckeGS.lean`, and
`NotAGSBasis.hecke_not_gs_basis_four` in that file is a machine-checked
REFUTATION at n = 4: the overlap of the Yang-Baxter rule for (sigma_2, sigma_3)
(lm = s3 s2 s3) with the far-commutation rule for (sigma_3, sigma_1)
(lm = s3 s1) over the word s3 s2 s3 s1 has S-polynomial

    s2 s3 s2 s1 - s3 s2 s1 s3

and both words are irreducible for the system, so the S-polynomial is a nonzero
normal form and the system is not confluent. The Lean module header states this
outright and records that the axiom `hecke_is_gs_basis` was deleted for being
false, not merely unproved.

So the manuscript block asserts, uncited, precisely what the folio's own
sorry-free Lean disproves. Fix the block, do not just add a citation.

WHAT THE REPAIR NEEDS (all three sources agree on the shape):
- HeckeGS.lean:461 names the missing family itself:
  sigma_i sigma_{i-1} ... sigma_j sigma_i -> sigma_{i-1} sigma_i sigma_{i-1} ... sigma_j,
  of which s3 s2 s1 s3 -> s2 s3 s2 s1 is the first instance. That is the
  Bokut-Shiao completion, now citable as [bokut2001].
- [kimlee2018] Prop. 3.1 shows the same shape on the Temperley-Lieb quotient:
  the GS basis needs the two extra families E_{i,j}E_i - E_{i-2,j}E_i (i > j)
  and E_j E_{i,j} - E_j E_{i,j+2} (i > j) beyond the defining relations.
- The q-deformed type-A statement itself is Kang-Lee-Lee-Oh 2002 (see the
  sibling bean); [bokut2001] is a Coxeter-GROUP theorem and does not by itself
  license the H_n(q) claim.

Two acceptable outcomes: (a) restate the block over the COMPLETED rewriting
system and cite the completion; or (b) drop the confluence sentence and say the
normal form is defined by a fixed rule order, with a pointer to
`NotAGSBasis.hecke_not_gs_basis_four` for why order-independence fails. Either
way `def:hecke-normal-form` currently has no `cites` field at all and carries
the `groebner-shirshov` tag.

Surfaced by relevance triage of the nine-PDF batch (library/fd58d8e1...pdf and
library/arxiv-1808.05026v1/1808.05026v1.pdf); ledger rows carry the join.


## 2026-09-07 — repaired via outcome (b), plus two further defects found

PR #7123 (branch `claude/tl-gs-basis-citation-2026-09-07`). NOT closing this
bean until that merges — a fix on a branch is not a fix in the product.

The bean named ONE defect. Measured, there were THREE, and the two new ones
mean the object the block DEFINED was not the object the Lean REFUTES, so
'the Lean disproves the block' needed the rules reconciled before it was even
true. All three are in `computations/hecke_normal_form_confluence_probe.py`
(6/6, exact Laurent polynomials over Z, no float, q never evaluated):

1. CONFLUENCE FALSE (the known one) — re-derived independently of the Lean, by
   executing the rewriting rather than by S-polynomial bookkeeping. s3s2s3s1
   goes to s2s3s2s1 or s3s2s1s3, both irreducible.
2. RULE 2 DOES NOT TERMINATE AS PRINTED — the block wrote far commutation
   symmetrically as |i-j| >= 2, which applies to its own output. Reducing
   s3s1 under the block's own rules runs forever (capped at 4000 steps).
   A reader implementing the block as printed gets a hang.
3. RULE 3 POINTED THE WRONG WAY — printed as s_i s_{i+1} s_i -> s_{i+1} s_i
   s_{i+1} while annotated '(in the shortlex-decreasing direction)'. With
   s1 < s2 < ..., s2s3s2 < s3s2s3, so decreasing is the other arrow, which is
   what HeckeGS.lean uses.

WHY THE FALSE CLAIM SURVIVED, measured: order-dependence is real but rare and
ABSENT in the regime a person spot-checks. All 504 words of length <= 8 over
H_3 are order-independent; the first counterexample needs n >= 4 AND length
>= 4 (1 of 81). At n=5 length 5 it is 25 of 1024. So the claim was true
everywhere it would have been checked by hand — worth saying in the block
rather than just deleting the sentence, and it is now said there.

THE COMPLETION REPAIRS IT — as scope-(a) EVIDENCE, not as a theorem. Adding
the Bokut-Shiao family the Lean names gives 0 of 1652 words order-dependent at
n <= 5, length <= 5, and the mechanism is visible: s3s2s1s3 becomes REDUCIBLE
by exactly the first instance HeckeGS.lean names, so the S-polynomial stops
being a normal form. This is NOT a claim that the completed system is a GS
basis, and must not be cited as one — that needs every S-polynomial of every
overlap at all n. The block states the completion as the known repair and says
the normal form is meanwhile DEFINED by a fixed rule order.

Also done: the block had no `cites` at all; it now cites bokut2001, kang2002,
kimlee2018. `kang2002` did not exist and was added this session — metadata
only, NOT READ, reconciled from two agreeing bibliographies I read directly
(Kim-Lee ref [9] and arxiv-1808.05026 ref [8]), no DOI synthesised, on the
`bokut2001` precedent. So the sibling bean qou-qspu is PARTLY served — the
citation exists and is correctly scoped — but the paper is still not held and
that bean stays open.

Verification: probe exit 0 (6/6); validate exit 0 against platform pin 428ca5c
(8 issues, all pre-existing, none naming this block); qa-sweep 0 critical /
0 major / 0 minor, sidecar refreshed; precision-gates --changed.
