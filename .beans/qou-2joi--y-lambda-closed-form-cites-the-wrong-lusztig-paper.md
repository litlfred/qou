---
# qou-2joi
title: y_lambda closed form cites the wrong Lusztig paper; BLM is absent and the DOI contradicts itself
status: in-progress
type: task
priority: normal
created_at: 2026-08-24T13:20:20Z
updated_at: 2026-08-24T13:33:23Z
---

## Survey: are the Delta_lambda / y_lambda assertions Lean-proved?

211 declarations across 219 files mention Delta_lambda or y_lambda.

    sorry            0        `: True` conclusions   0
    axioms           0        empty Prop carriers    0
    theorems       136        of which conditional on a CONJECTURE class: 2
                              (17 more are ordinary [Field K]/[DecidableEq], not conjectures)
    classes          8        all content-bearing; 7 have NO instance = honestly open

So the file-level answer is clean, but it splits:

- **Delta_lambda: PROVED, unconditionally.**
  `QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional` takes no class
  hypothesis, is sorry-free and general-n.
- **y_lambda: NOT proved.** The closed form is a conjecture class,
  `QSchurYLambdaClosedFormClaim`, with the real content as a field
  (`closed_form_holds : forall lam q, ySchurClosedForm lam q = qSchurWeight lam q`)
  and **no instance**. That is the honest open state, correctly encoded.

## Need lit? YES — and the provenance was pointing at the wrong paper

The class docstring said the conjecture is "equivalent to the Lusztig 1990 /
BLM identity" and carried one `-- Ref: [lusztig1990]`. Three problems:

1. **`lusztig1990` is the wrong paper.** It is *Canonical bases arising from
   quantized enveloping algebras* (JAMS 3) — canonical bases, not a q-Schur
   Markov-trace weight identity.
2. **BLM was absent entirely.** `grep -c 'q-schur' references.ts` = 0; the only
   "Beilinson" in the bibliography is the p-adic Beilinson conjecture paper.
   Added as `blm1990`, explicitly marked **UNVERIFIED** — fields are from recall,
   egress is blocked, and the paper is not in `library/`.
3. **Two DOIs, one key.** `references.ts` says `10.2307/1990961`;
   `OptionE/CrystalDeltaLambdaScaffold.lean` and `IwahoriHecke/TypeA.lean` both
   say `10.2307/2152736`. NOT resolved here — guessing is what produced it.

## What is actually holdable, measured

| key | title | ingested? |
|---|---|---|
| wenzl1988 | Hecke algebras of type A_n and subfactors | **NO** |
| jones1987 | Hecke algebra representations of braid groups | **NO** |
| orellana1998 | Weights of Markov traces on Hecke algebras (1999) | YES `arxiv-math-9806163v1` |
| lusztig1990 | Canonical bases... | NO |
| blm1990 | A geometric setting for the quantum deformation of GL_n | NO |

**The one ingested paper is the wrong type.** Orellana's weight formula is type
B_n/D_n — double partitions (alpha,beta) with a second parameter Q. The QOU
y_lambda is type A: single partition, one parameter. Do not read the section
"5. The Weight Formula" as settling the type-A claim; that is the same
object-vs-object slip as the (2,1)-vs-(1^3) conflation.

The type-A sources that WOULD settle it — Wenzl 1988 and Jones 1987, both
already cited by the file — are **not ingested**, so nothing in this repo can
check the identity. That is the actionable ask: ingest those two.

Minor: `orellana1998` is keyed 1998 but the entry is 1999 (Crelle 508). Left
alone — a key rename is corpus-wide.
