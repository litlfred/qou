---
# qou-dr8m
title: MFW lower bound for braid index from the corpus HOMFLY/Markov trace — settle 6_1 = 4 (flagged load-bearing by qou-xpgq)
status: todo
type: task
created_at: 2026-08-21T15:39:09Z
updated_at: 2026-08-21T15:39:09Z
---


## Framing (corrected after owner pushback — "there IS a filtration and jet")

My first answer — "there's no single algebra for GS to normalize in" — was
WRONG and is retracted. There is one, and this corpus already uses it:

  B_1 ⊂ B_2 ⊂ B_3 ⊂ …  →  B_∞ = colim B_n     (strand filtration)
  H_1 ⊂ H_2 ⊂ …        →  H_∞,  with the Ocneanu/Markov trace defined
                              COMPATIBLY across the tower

Stabilisation `β ↦ βσ_n^{±1}` is *internal* to B_∞, so Markov equivalence does
live inside a single filtered object. The corpus's Bratteli/Wedderburn tower is
exactly this.

**So the obstruction is not the absence of an algebra — it is the KIND of
question.** GS/normal forms answer *"is x = y in this algebra?"* — a canonical
representative of an ELEMENT. Braid index asks for

    min { n : the Markov class of L meets B_n }

i.e. the **minimal strand-filtration degree over an equivalence class**. That is
a minimisation over a class, not a normal form of an element; a confluent
rewriting system gives the latter and says nothing about the former.

**The sharp obstruction is non-monotonicity.** A greedy GS-style reduction would
compute the braid index IF Markov reduction were filtration-NON-INCREASING. It
is not: destabilising can require STABILISING first (going up a strand before
coming down). That is precisely why Birman–Menasco's "Markov Theorem Without
Stabilisation" is a theorem rather than an observation — and its price is a much
richer move set (exchange moves, flypes), not a finite confluent system.

**But the filtration DOES deliver the bound, and that is this bean.** The
Ocneanu trace is filtration-COMPATIBLE, which is exactly what makes HOMFLY
well-defined on the tower — and MFW then gives

    braid index ≥ ½·breadth_v HOMFLY + 1

So the corpus's own Hecke/Markov-trace machinery is the natural route to the
LOWER bound even though GS cannot reach the minimum itself. Task: compute HOMFLY
for 6₁ from the in-repo trace and settle the braid index = 4 that `qou-xpgq`
flagged as literature-recalled and load-bearing for its {5,10} arithmetic.

NOTE — do not conflate filtrations: the corpus's jet-order/Δ_λ filtration is
q-adic, a DIFFERENT filtration from the strand filtration above. MFW rides the
strand one.
CAVEAT: MFW is not always sharp; known counterexamples exist. A matching bound
settles it; a gap does not.

## The formulae, and what the trace bounds ABOVE as well as below

HOMFLY convention: `v⁻¹P(L₊) − v P(L₋) = z P(L₀)`, `P(unknot) = 1`.
For `β ∈ B_n` with exponent sum (writhe) `e` and closure `L`, MFW is a PAIR:

    (1)   e − n + 1  ≤  mindeg_v P_L
    (2)                 maxdeg_v P_L  ≤  e + n − 1

**Subtract → the LOWER bound on the Markov-class minimum (braid index).**
`e` cancels — which is the point, since `e` is not a link invariant:

    maxdeg_v P − mindeg_v P ≤ 2n − 2      ⟹    n ≥ ½·spread_v P + 1
    braid_index(L) = min{n} ≥ ½·spread_v P_L + 1

**Read (1) alone → an UPPER bound on a MAXIMUM.** The self-linking number of
the transverse representative is `sl(β) = e − n`, so (1) is exactly

    sl(β) ≤ mindeg_v P_L − 1        for EVERY β in the Markov class

i.e. the trace bounds the **maximal self-linking number** above — the
HOMFLY sharpening of Bennequin's `sl ≤ 2g(L) − 1`. So the same trace bounds a
min from below and a max from above; they are the two halves of one pair.

**Why there is no "maximum braid index".** The Markov class is unbounded above:
stabilise `β ↦ βσ_n^{±1}` and n grows without limit, closure unchanged. So
`max{n}` = ∞ trivially, and the MINIMUM is the only invariant of the two. That
asymmetry is structural, not an artifact.

**Adding (1)+(2) instead** bounds the writhe at fixed n:
    |mindeg_v P + maxdeg_v P − 2e| ≤ 2n − 2

## Lean: what is provable now vs. what is research-scale

- **MFW itself is research-scale.** Its proof needs HOMFLY well-definedness =
  Markov invariance of the Ocneanu trace on the H_n tower, then a degree
  argument. Not a session-scale formalisation.
- **The derivation FROM the pair is cheap and honest** — the §3b-cond
  conditional pattern: take (1) and (2) as explicit hypotheses on a generic
  ordered field / ℤ, conclude `n ≥ ½(maxdeg − mindeg) + 1` and
  `sl ≤ mindeg − 1`. Sorry-free, no axiom, and it states plainly that MFW is
  assumed, not proved. That is the correct first Lean rung here.
- Do NOT axiomatise MFW as a class and then present the bound as derived —
  §"Axiomatization is NOT a Proof".
