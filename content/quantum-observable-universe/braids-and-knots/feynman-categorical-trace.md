Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
$\mathbf{C} = \mathbf{Rep}(\mathrm{SU}_q(2))$, $V$ the fundamental
representation, and $q$ not a root of unity.  Let
$\varrho \colon \mathbf{1} \to A$ be a closed cycle with braid
representative $\beta \in B_n$.

**Proposition.**
*The Feynman transition amplitude, evaluated on the knot-type
eigenbasis provided by the braided monoidal structure, equals the
Jones--Markov trace of the braid representation in the Hecke algebra:*

$$
  \langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}}
  =
  \sum_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}}
  w_\lambda \cdot \mathrm{tr}_{S_\lambda}\bigl(\rho_n(\beta)\bigr)
  =
  \mathrm{tr}_M\bigl(\rho(\beta)\bigr),
$$

*where the sum is over partitions $\lambda$ of $n$ with at most two
parts, $w_\lambda$ are the Markov weights determined by the Markov
property $\mathrm{tr}_M(x \sigma_n^{\pm 1}) = z^{\pm 1}\mathrm{tr}_M(x)$
([Jones--Markov trace](#thm:jones-markov-trace)),
$\mathrm{tr}_{S_\lambda}$ is the trace on the irreducible
$H_n(R, q)$-module $S_\lambda$, and the right-hand side is the
Jones--Markov trace on $H_n(R, q)$.  The Markov weights satisfy
$w_\lambda = \dim_q(V_\lambda) \cdot \dim(S_\lambda) / \dim_q(V^{\otimes n})$,
where $\dim_q(V_\lambda) = [2j+1]_q$ is the quantum dimension of the
$\mathrm{SU}_q(2)$-module of spin $j = (\lambda_1 - \lambda_2)/2$.*

*In particular, the transition amplitude is a finite sum over
$\lfloor n/2 \rfloor + 1$ terms --- one for each irreducible summand
of $V^{\otimes n}$ --- and its absolute value equals the categorical
mass at a single brane level
([categorical mass as Markov trace](#prop:categorical-mass-markov)):*

$$
  \mathfrak{m}(\varrho)\big|_{\text{single level}}
  =
  \bigl|\mathrm{tr}_M\bigl(\rho(\beta)\bigr)\bigr|
  =
  \bigl|
  \langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}}
  \bigr|.
$$
