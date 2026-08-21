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
