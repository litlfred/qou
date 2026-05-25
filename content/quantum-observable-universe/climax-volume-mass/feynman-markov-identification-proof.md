**Proof.**
The Jones--Markov trace is the unique trace on $\bigcup_n H_n(R, q)$
satisfying the Markov property
$\mathrm{tr}_M(x \sigma_n^{\pm 1}) = z^{\pm 1}\mathrm{tr}_M(x)$
([Jones--Markov trace](#thm:jones-markov-trace)).
By the Wedderburn-Artin decomposition of the semisimple algebra $H_n(R, q)$,
every trace decomposes as a weighted sum of irreducible characters:

$$
  \mathrm{tr}_M\bigl(\rho(\beta)\bigr)
  =
  \sum_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}}
  w_\lambda \cdot \mathrm{tr}_{S_\lambda}\bigl(\rho_n(\beta)\bigr),
$$

where the Markov weights $w_\lambda$ are uniquely determined by the
Markov property and the normalisation $\mathrm{tr}_M(1) = 1$.  The
Markov weights encode the quantum dimensions:
$w_\lambda = \dim_q(V_\lambda) \cdot \dim(S_\lambda) / \dim_q(V^{\otimes n})$.

The transition amplitude on the eigenbasis, defined as the
Markov-weighted sum of partial traces, therefore equals the
Markov trace by construction:

$$
  \langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}}
  :=
  \sum_\lambda w_\lambda \cdot \mathrm{tr}_{S_\lambda}\bigl(\rho_n(\beta)\bigr)
  =
  \mathrm{tr}_M\bigl(\rho(\beta)\bigr).
$$

The content of this identification is not tautological: it says that
the unique measure on the finite eigenbasis that satisfies the Markov
property (and hence gives topological link invariants) is the one
that replaces the Feynman path measure.  $\square$
