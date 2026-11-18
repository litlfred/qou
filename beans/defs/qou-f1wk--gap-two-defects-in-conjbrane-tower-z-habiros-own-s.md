---
# qou-f1wk
title: 'GAP: two defects in conj:brane-tower-z-habiro''s own STATEMENT — the cyclotomic projection is undefined at generic eigenvalues, and the dimensionless-to-MeV map is unspecified'
status: in-progress
type: task
priority: normal
created_at: 2026-10-11T07:00:20Z
updated_at: 2026-10-11T07:00:57Z
parent: b9cj
---


Opened 2026-10-11 on owner pick "1" relayed from the project thread
("write up the two gaps in `conj:brane-tower-z-habiro` as a bean").

🛑 **The relay pointed at a draft at
`/mnt/project-files/mass-endomorphism/klambda/conj-gaps-bean-draft.md` and said
to use the title given there. That path does not exist in this container**, so
the title and wording below are mine, assembled from the findings already
recorded in `qou-9f4h` and in
`docs/audits/2026-06-17-refuted-ansatz-lemmas.md` candidate 7. If the draft
carries a different title or a third gap, this bean needs reconciling against
it.

🛑 **The content block is NOT edited.** Per §ASK THE OWNER, amending a live
conjecture's statement is the owner's call; this bean records the defects and
proposes nothing enacted. Both are defects in the **statement**, not in any
candidate rule — which is why they belong here and not in `qou-9f4h`.

Carrier:
[`folio/quantum-observable-universe/mass-theory/brane-tower-z-habiro.md`](../../folio/quantum-observable-universe/mass-theory/brane-tower-z-habiro.md).

## Gap 1 — the cyclotomic projection is UNDEFINED at generic eigenvalues

The conjecture asks for a *"cyclotomic projection evaluated at `z = μ`"*. Two
problems, relayed from the sibling session's pre-registered rule scoring (rule
**R2**, cyclotomic termination):

- **R2 cannot fire at all.** `q₀` is not a root of unity, and no eigenvalue sits
  *on* a pole of `Φ_q`. So the termination condition the conjecture appeals to
  is never met at the substrate anchor.
- **Worse, the object is not defined.** `Φ_q` is **not a class in any
  `R/(P_k)`**, because `P_∞ ≡ 0` there. So *"the cyclotomic projection evaluated
  at `z = μ`"* requires **an extra choice** that the conjecture does not make,
  at generic eigenvalues.

**What this does and does not touch.** It does not refute the conjecture; it
says one clause of it has no referent as written. A reader cannot compute the
quantity the clause names without supplying a convention of their own — and two
readers may supply different ones and both believe they are testing the
conjecture.

## Gap 2 — the dimensionless → MeV map is UNSPECIFIED

The conjecture's §Falsifiability (verified verbatim, lines 52-60) says:

> *"1. Pick a candidate `n⋆` rule. 2. Compute the projection at `q₀` for each
> isotope. 3. Form the binding `B(𝔥)`. 4. Compare with the AME values
> `{2.224566, 8.481798, 7.71806}` MeV. A candidate rule closing all three to
> within `∼5 %` without per-atom retuning constitutes the empirical signature."*

**Step 3 is not defined.** The projection is dimensionless; the AME values are
in MeV; the conjecture never says how to get from one to the other. The sibling
session had to choose, and scored both — **M1** (read the tower as MeV) and
**M2** (`m_e` · tower). Every MeV comparison in the `k_λ` arc therefore
inherits an unstated convention chosen by the agent doing the scoring, **not by
the conjecture**.

**Why this is the more consequential of the two.** §Falsifiability is the
clause that makes the conjecture testable at all, and a falsifiability criterion
with an unspecified unit map is not a criterion. It also means the recorded
negatives in `qou-9f4h` — all seven pre-registered rules failing, best cell
26 % — are conditional on a choice the conjecture does not license. They are
honest negatives *for both conventions*, which is why they stand, but the
reason they had to be run twice is this gap.

**Under §NO FITTING there is a sharper worry:** an unspecified unit map is a
free choice sitting directly on the comparison boundary, which is exactly where
AGENTS.md locates the whole empirical content of the framework
(§"The paper is a MATHEMATICAL MODEL by default" — *"the comparison points carry
the full burden"*). Pinning it is not housekeeping.

## What is NOT claimed here

- Neither gap refutes the conjecture. **Scope (a)** at most, and really neither
  — they are defects in a statement, not negative results about a mechanism.
- The **`n⋆` claim** gets no support from the `k_λ` work, but it is not refuted
  either.
- The **Cauchy-limit claim is untouched** — not tested, not refuted.
- Nothing here is independently recomputed by me. The R2 analysis and the M1/M2
  split are relayed; the §Falsifiability quote is **verified verbatim** at the
  carrier.

## What would close this

Two owner decisions, neither an agent's to take:

1. **For gap 1** — either supply the extra choice that makes the cyclotomic
   projection well defined at generic eigenvalues, or restate the clause so it
   does not appeal to one. Note that doing this changes what R2 *means*, so the
   recorded R2 negative would need re-scoring against the new reading.
2. **For gap 2** — pin the dimensionless → MeV map in §Falsifiability. Once it
   is pinned, one of M1/M2 becomes the criterion and the other's column in the
   `k_λ` results becomes irrelevant.

## Status

**`todo`, and it stays `todo`** per §13a: the subject is an open conjecture, and
recording that its statement has gaps is not closing them. Only an owner
amendment to the carrier closes this. Sibling bean: `qou-9f4h` (the `k_λ`
selector itself).
