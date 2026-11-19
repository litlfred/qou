*Proof.*

**(1) Markov locality.** Part (1) of the proposition is the
definition of the Markov trace. By
[Jones–Markov trace](#thm:jones-markov-trace), the unique
$R$-linear trace
$\mathrm{tr}_M \colon \bigcup_n H_n(R, q) \to R\otimes\mathbb{Q}$
satisfying normalisation $\mathrm{tr}_M(1) = 1$, the trace property
$\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$, and the Markov property
$\mathrm{tr}_M(x \sigma_n) = z\, \mathrm{tr}_M(x)$
for all $x \in H_n(R, q)$, $n \geq 1$, $z = q^3/(q^2+1)$ (convention D — see
[Markov axioms](#rem:markov-axioms-primitive));
the negative stabilisation
$\mathrm{tr}_M(x \sigma_n^{-1}) = z_{-}\, \mathrm{tr}_M(x)$,
$z_{-} = z - (q - q^{-1})$, follows from the Hecke quadratic
relation.
The Markov property *is* the locality statement. $\square$
