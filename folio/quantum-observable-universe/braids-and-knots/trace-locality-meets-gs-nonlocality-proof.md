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
[`rem:markov-axioms-primitive`](#rem:markov-axioms-primitive));
the negative stabilisation
$\mathrm{tr}_M(x \sigma_n^{-1}) = z_{-}\, \mathrm{tr}_M(x)$,
$z_{-} = z - (q - q^{-1})$, follows from the Hecke quadratic
relation.
The Markov property *is* the locality statement. $\square$ for (1).

**(2) GS non-locality.** Part (2) is a structural observation about
the Gröbner–Shirshov reduction algorithm on the Hecke algebra. The algorithm
applies three rewriting rules:

- *Hecke quadratic relation:*
  $\sigma_i^2 \to (q - q^{-1}) \sigma_i + 1$ (eliminates squared
  generators).
- *Braid relation:*
  $\sigma_i \sigma_{i+1} \sigma_i \to \sigma_{i+1} \sigma_i \sigma_{i+1}$
  (Yang–Baxter / commutation).
- *Far-commutativity:*
  $\sigma_i \sigma_j \to \sigma_j \sigma_i$ for $\lvert i - j \rvert
  \geq 2$.

The braid relation acts on a window of three consecutive generators,
and successive applications can propagate changes across the entire
braid word. Therefore the normal form depends non-locally on the
input — flipping a single generator in $\beta$ can require rewriting
many generators in $\mathrm{NF}_{\mathrm{GS}}(\beta)$. $\square$ for (2).

**Reconciliation.** Parts (1) and (2) concern different operations.
Part (1) is a property of the trace and part (2) a property of the
reduction to normal form, so they do not conflict: the composite
$\beta \mapsto \mathrm{tr}_M(\rho(\beta))$ passes through the
non-local map $\beta \mapsto \mathrm{NF}_{\mathrm{GS}}(\beta)$, and the
trace is then evaluated on the normal form. $\square$
