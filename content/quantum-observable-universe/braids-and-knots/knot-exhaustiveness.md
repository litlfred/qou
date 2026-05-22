**Open question.**
The knot eigenbasis completeness theorem
([knot eigenbasis completeness](#prop:knot-eigenbasis-complete))
establishes that every irreducible summand of
$V^{\otimes n}$ is **detected** by some braid closure via
the Markov trace
([Jones–Markov trace](#thm:jones-markov-trace)).  This is
surjectivity of detection: no summand is invisible.

A stronger question: **do the knot types that appear in the
Archimedean universe exhaust the space of states?**

The generation completeness theorem shows that every knot
with Seifert genus $g(\mathfrak{K}) \leq 4$ appears in the
spectrum — the genus bound of Bring's surface captures all
embeddable knots in that range.  Knots with $g > 4$ are
excluded by the spectral filter.

But this does not address whether the **Jones polynomial
itself** is a faithful invariant: whether distinct knot
types always produce distinct polynomials.  The QOU uses
the Jones polynomial only for detection (non-degeneracy
on irreducibles), not for classification.  The classical
open question — does $J_K(q) = 1$ imply $K$ is the
unknot? — is never needed in our framework, because the
Markov trace non-degeneracy theorem is sufficient for the
knot eigenbasis.

This leaves three nested questions:

1. **(Detection.)** Does every irreducible summand get
   labelled by a knot?  **Yes** — proven by Alexander
   surjectivity + Markov non-degeneracy.

2. **(Generation.)** Does every knot with $g \leq 4$
   appear?  **Yes** — proven by generation completeness
   from the seven torus knot generators plus Skein
   crossing changes.

3. **(Faithfulness.)** Do distinct knots always produce
   distinct states?  **Open.**  If two distinct knots
   $\mathfrak{K} \neq \mathfrak{K}'$ have the same Jones
   polynomial $J_{\mathfrak{K}}(q) = J_{\mathfrak{K}'}(q)$,
   they would be physically indistinguishable in the
   Archimedean universe — they would represent the same
   particle.  Whether this occurs (and whether it has
   physical consequences) is an open question.

The first two questions are settled by existing theorems.
The third depends on progress in classical knot theory
and may already be answered by the full HOMFLY-PT
polynomial (which carries strictly more information than
the Jones specialisation).
