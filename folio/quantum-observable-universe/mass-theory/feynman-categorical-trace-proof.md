**Proof.**
The argument proceeds in three steps.  By
([eigenbasis decomposition](#lem:feynman-eigenbasis-decomposition)),
the algebraic state space
$V_{\mathrm{phys}} = \varinjlim V^{\otimes n}$ decomposes into the
finite eigenbasis $\bigoplus_\lambda V_\lambda \otimes S_\lambda$ on
which the braid $\beta \in B_n$ acts.  By
([trace collapse](#lem:feynman-trace-collapse)),
the Feynman path integral on this eigenbasis collapses to a finite
weighted sum over the irreducible summands, with no regularisation
needed.  By
([Markov identification](#lem:feynman-markov-identification)),
this Markov-weighted sum equals the Jones--Markov trace
$\mathrm{tr}_M\bigl(\rho(\beta)\bigr)$ in $H_n(R, q)$, and the
Markov weights are
$w_\lambda = \dim_q(V_\lambda) / \dim_q(V^{\otimes n})$.

By the categorical mass as Markov trace
([categorical mass as Markov trace](#prop:categorical-mass-markov)),
the absolute value of this expression is the categorical mass at a
single brane level:
$\mathfrak{m}(\varrho)|_{\text{single level}}
= |\mathrm{tr}_M(\rho(\beta))|$.  $\square$
